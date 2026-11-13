#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""free-models-daily 每日 pipeline
流程：机器实抓(OpenRouter/HF/GitHub) → diff 上期 → 生成 registry + daily(双语) → QA → commit+push
纯 stdlib（urllib），HF 走代理。EN 块由 AGNES 现场翻译（规则：EN 省略 CN-only 备注）。
用法：python run_daily.py [--dry-run]
"""
import json, os, re, sys, ssl, datetime, urllib.request, urllib.parse, subprocess, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG = json.load(open(os.path.join(ROOT, "config.json"), encoding="utf-8"))
VENDORS = json.load(open(os.path.join(ROOT, "vendors.json"), encoding="utf-8"))

def load_env():
    env = {}
    p = os.path.join(ROOT, ".env")
    for line in open(p, encoding="utf-8"):
        line = line.strip()
        if line and "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1); env[k] = v
    return env
ENV = load_env()
AGNES_KEY = ENV.get("AGNES_API_KEY", ""); AGNES_BASE = ENV.get("AGNES_BASE_URL", "").rstrip("/"); AGNES_MODEL = ENV.get("agnes-3.0-flash") or ENV.get("AGNES_MODEL", "agnes-3.0-flash")
PROXY_HF = CONFIG.get("proxy", {}).get("huggingface")

CN_ONLY_TOKENS = ["需代理", "科学上网", "国内直连", "国内可直连", "手机号", "实名", "国内", "需翻墙"]

def http_get_json(url, proxy=None, timeout=30):
    import time
    handler = urllib.request.ProxyHandler({"http": proxy, "https": proxy}) if proxy else urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(handler)
    last = None
    for a in range(3):
        req = urllib.request.Request(url, headers={"User-Agent": "free-models-daily/1.0", "Accept": "application/json"})
        try:
            with opener.open(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e
            if a < 2:
                time.sleep(3 * (a + 1))
    raise last

def http_get_text(url, proxy=None, timeout=30):
    import time
    handler = urllib.request.ProxyHandler({"http": proxy, "https": proxy}) if proxy else urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(handler)
    last = None
    for a in range(3):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (free-models-daily)"})
        try:
            with opener.open(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            last = e
            if a < 2:
                time.sleep(3 * (a + 1))
    raise last

def http_head_ok(url, proxy=None, timeout=15):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    handler = urllib.request.ProxyHandler({"http": proxy, "https": proxy}) if proxy else urllib.request.ProxyHandler({})
    try:
        with urllib.request.build_opener(handler).open(req, timeout=timeout) as r:
            return r.status < 400
    except Exception:
        return False

# ---------- AGNES ----------
def agnes(prompt, max_tokens=4000, system="你是严谨的技术翻译，只输出 JSON，不加解释。"):
    if not AGNES_KEY:
        raise SystemExit("AGNES_API_KEY missing in .env")
    body = json.dumps({"model": AGNES_MODEL,
                       "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
                       "max_tokens": max_tokens, "temperature": 0.2}).encode()
    import time
    last = None
    for a in range(3):
        req = urllib.request.Request(AGNES_BASE + "/chat/completions", data=body,
                                    headers={"Authorization": "Bearer " + AGNES_KEY, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=120, context=ssl.create_default_context()) as r:
                data = json.loads(r.read().decode())
            txt = data["choices"][0]["message"]["content"].strip()
            m = re.search(r"\{.*\}", txt, re.DOTALL)
            return json.loads(m.group(0)) if m else json.loads(txt)
        except Exception as e:
            last = e
            if a < 2:
                time.sleep(150)
    print(f"    AGNES 翻译重试后仍失败，本次 EN 降级为缺省: {last}")
    return {}

# ---------- 机器实抓 ----------
def fetch_openrouter_free():
    try:
        models = http_get_json(CONFIG["endpoints"]["openrouter_models"])
        free = []
        for m in models.get("data", []):
            p = m.get("pricing", {})
            if m.get("id","").endswith(":free") or (p.get("prompt")=="0" and p.get("completion")=="0"):
                free.append({"id": m.get("id"), "ctx": m.get("context_length"), "created": m.get("created_at")})
        return {"ok": True, "items": free, "count": len(free)}
    except Exception as e:
        return {"ok": False, "err": str(e), "items": []}

def fetch_hf_new():
    sc = CONFIG.get("hf_scan", {})
    tags = ",".join(sc.get("tags", [])); lim = sc.get("limit", 60); min_likes = sc.get("min_likes", 3)
    url = f"{CONFIG['endpoints']['hf_models']}?filter={tags}&sort=createdAt&direction=-1&limit={lim}"
    try:
        rows = http_get_json(url, proxy=PROXY_HF)
        items = [{"id": r.get("id"), "likes": r.get("likes", 0), "created": r.get("createdAt"),
                  "tags": [t for t in (r.get("tags") or []) if t in ("text-to-video","text-to-image")]}
                 for r in rows if (r.get("likes") or 0) >= min_likes]
        return {"ok": True, "items": items[:sc.get("keep", 30)], "count": len(items)}
    except Exception as e:
        return {"ok": False, "err": str(e), "items": []}

def fetch_gh_releases():
    out = []
    for org_repo in CONFIG.get("curation_orgs", []):
        url = CONFIG["endpoints"]["github_releases"].format(org=org_repo.split("/")[0], repo=org_repo.split("/")[1])
        try:
            rels = http_get_json(url)
            for r in rels[:3]:
                out.append({"org_repo": org_repo, "tag": r.get("tag_name"), "name": r.get("name"),
                           "date": r.get("published_at"), "url": r.get("html_url")})
        except Exception:
            pass  # 404/不存在 → 跳过（org 改名场景，log 到 state）
    return {"ok": True, "items": out, "count": len(out)}

# ---------- diff 状态 ----------
def fetch_value_pricing():
    """性价比层官方定价实抓：能抓到服务端价格就落活价(min–max)，抓不到标 ⚠️，不写死数字。"""
    out = {}
    for p in CONFIG.get("value_pricing", []):
        vid = p["vendor"]; url = p.get("url", "")
        proxy = PROXY_HF if p.get("proxy") in ("hf", True) else None
        try:
            html = http_get_text(url, proxy=proxy)
            toks = re.findall(r"\$\d+(?:\.\d+)?", html)
            nums = sorted({float(t[1:]) for t in toks})
            if nums:
                sample = "、".join(f"${n:g}" for n in nums[:4])
                out[vid] = {"ok": True, "price": sample, "url": url}
            else:
                out[vid] = {"ok": False, "price": None, "url": url}
        except Exception as e:
            out[vid] = {"ok": False, "price": None, "url": url, "err": str(e)[:50]}
    return out

def sig_hash(items):
    return hashlib.md5(json.dumps(items, sort_keys=True).encode()).hexdigest()

def load_state():
    p = os.path.join(ROOT, "state", "last_signals.json")
    if os.path.exists(p):
        d = json.load(open(p, encoding="utf-8"))
        return {
            "openrouter": set(d.get("openrouter", [])),
            "hf": set(d.get("hf", [])),
            "gh": {tuple(x) for x in d.get("gh", [])},
            "vendor_ids": set(d.get("vendor_ids", [])),
            "value_pricing": d.get("value_pricing", ""),
        }
    return {"openrouter": set(), "hf": set(), "gh": set(), "vendor_ids": set(), "value_pricing": ""}

def save_state(st):
    out = {
        "openrouter": sorted(st["openrouter"]),
        "hf": sorted(st["hf"]),
        "gh": [list(t) for t in sorted(st["gh"])],
        "vendor_ids": sorted(st["vendor_ids"]),
        "value_pricing": st.get("value_pricing", ""),
    }
    os.makedirs(os.path.join(ROOT, "state"), exist_ok=True)
    json.dump(out, open(os.path.join(ROOT, "state", "last_signals.json"), "w", encoding="utf-8"))

# ---------- 翻译（AGNES）----------
def translate_vendors():
    zh = {v["id"]: v for v in VENDORS}
    payload = []
    for vid, v in zh.items():
        payload.append({"id": vid, "name": v["name"], "api": v.get("api",""), "key": v.get("key",""),
                        "limits": v.get("limits",""), "notes": v.get("notes","")})
    if not payload:
        return {}
    prompt = ("把这些中文 AI 模型厂商条目翻译成英文 JSON。输出 {id: {en_name,en_api,en_key,en_limits,en_notes}}。"
              "规则：EN 版必须省略任何中国专属备注（如 需代理/科学上网/国内直连/手机号/实名），只保留通用信息；"
              "忠实翻译，不要新增信息，不要机翻腔。只输出 JSON。")
    data = agnes(prompt + "\n\n" + json.dumps(payload, ensure_ascii=False), max_tokens=8000) or {}
    en = {}
    for vid, e in data.items():
        # QA: 从 EN 字段里清掉漏进来的 CN-only token
        clean = {}
        for fk, fv in e.items():
            if isinstance(fv, str):
                for t in CN_ONLY_TOKENS:
                    fv = re.sub(r"[^,。.;；]*" + re.escape(t) + r"[^,。.;；]*[，。；;]?", " ", fv)
                fv = re.sub(r"\s{2,}", " ", fv).strip(" ;，。")
            clean[fk] = fv
        en[vid] = clean
    return en

def vendor_block(v, en, verified_note=True):
    e = en.get(v["id"], {})
    mark = "" if v.get("verified", True) else "  ⚠️未实验"
    lines = []
    lines.append(f"### {v['name']}{mark}")
    lines.append(f"- 官方接入：{v.get('api','')}")
    lines.append(f"- 获取 Key：{v.get('key','')}")
    lines.append(f"- 限额/额度：{v.get('limits','')}")
    lines.append(f"- 备注：{v.get('notes','')}")
    if e:
        lines.append(f"- EN: {e.get('en_name','')} | {e.get('en_api','')}\n"
                     f"  Key: {e.get('en_key','')} | Limits: {e.get('en_limits','')} | Notes: {e.get('en_notes','')}")
    return "\n".join(lines)

# ---------- registry ----------
LAYER_TITLE = {
  "llm_free": ("免费 LLM API", "Free LLM API"),
  "video_free": ("免费生视频", "Free Video Generation"),
  "image_free": ("免费生图", "Free Image Generation"),
  "video_value": ("高性价比生视频", "Cost-Effective Video"),
  "image_value": ("高性价比生图", "Cost-Effective Image"),
  "audio_free": ("免费 TTS 语音", "Free TTS / Voice"),
}
def build_registry(vendors, en, machine_or, vp=None):
    vp = vp or {}
    by = {}
    for v in vendors:
        by.setdefault(v["layer"], []).append(v)
    parts = ["# 模型 API 注册表（living index）\n",
             f"_as-of: {datetime.date.today().isoformat()} · 每 5 字段：名称 / 官方接入 / 获取Key / 限额 / 备注_\n"]
    for layer, (zh_t, en_t) in LAYER_TITLE.items():
        parts.append(f"\n## {zh_t} / {en_t}\n")
        if layer == "llm_free" and machine_or.get("ok"):
            parts.append(f"### 实抓免费模型池（OpenRouter，{machine_or['count']} 个）\n")
            for m in machine_or["items"][:40]:
                parts.append(f"- `{m['id']}`" + (f" · {m['ctx']} ctx" if m.get("ctx") else ""))
            parts.append("\n")
        if layer == "video_free" and fetch_hf_result.get("ok"):
            vf = [h for h in fetch_hf_result["items"] if "text-to-video" in h["tags"]]
            if vf:
                parts.append("### 实抓：Hugging Face 最新文生视频模型\n")
                for h in vf[:20]:
                    parts.append(f"- `{h['id']}` ({h.get('likes',0)} 👍) [{h.get('created','')[:10]}]")
                parts.append("")
        for v in by.get(layer, []):
            block = vendor_block(v, en)
            if layer in ("video_value", "image_value") and v["id"] in vp:
                pr = vp[v["id"]]
                if pr.get("ok"):
                    block += f"\n- 实抓价目（节选，最低档起）：{pr['price']}（{pr['url']}，as of {datetime.date.today().isoformat()}）"
                else:
                    block += f"\n- 单条价：⚠️ unverified（{pr.get('url','官网定价页')} 实抓未命中）"
            parts.append(block)
    open(os.path.join(ROOT, "registry", "models.md"), "w", encoding="utf-8").write("\n".join(parts))

# ---------- daily ----------
def build_daily(new_or, new_hf, new_gh, vendors_added, today):
    has_update = bool(new_or or new_hf or new_gh or vendors_added)
    p = [f"# 每日更新 {today}", "", f"> 本期新增 {len(new_or)+len(new_hf)+len(new_gh)+len(vendors_added)} 条；"
         f"若无新增则本日不 commit（自动跳过）。", ""]
    if not has_update:
        p.append("✅ 今日无更新（机器实抓 diff 为空，且无新增厂商）。")
    if new_or:
        p.append("## 免费 LLM · OpenRouter 新增 :free 模型\n")
        for m in new_or:
            p.append(f"- `{m['id']}`" + (f"（{m['ctx']} ctx）" if m.get("ctx") else ""))
        p.append("\n*EN: New free (`:free`) models added to the OpenRouter pool above.*\n")
    if new_gh:
        p.append("## 开源可本地 · 策展 org 新 Release\n")
        for r in new_gh:
            p.append(f"- **{r['org_repo']}** {r.get('tag','')} — {r.get('name','')} （{str(r.get('date',''))[:10]}） [release]({r.get('url','')})")
        p.append("")
    if new_hf:
        p.append("## Hugging Face · 最新开源文生图/视频模型\n")
        for h in new_hf:
            p.append(f"- `{h['id']}`（{h.get('likes',0)} likes）")
        p.append("")
    if vendors_added:
        p.append("## 新增策展厂商\n")
        for vid in vendors_added:
            p.append(f"- {vid}")
        p.append("")
    os.makedirs(os.path.join(ROOT, "daily"), exist_ok=True)
    open(os.path.join(ROOT, "daily", today + ".md"), "w", encoding="utf-8").write("\n".join(p))
    return has_update

# ---------- README 指向最新 daily ----------
def update_readme(today, has_update):
    """只更新 README 里的 LATEST_DAILY 锚点块（指向最新一篇 daily/），不动其余正文。"""
    d = os.path.join(ROOT, "daily")
    files = sorted(f for f in os.listdir(d) if f.endswith(".md")) if os.path.isdir(d) else []
    latest = files[-1] if files else None
    if latest:
        line = f"> 📄 最近更新 / Latest changelog：[`daily/{latest}`](daily/{latest})"
    else:
        line = "> 📄 全量活索引 / Full index：[`registry/models.md`](registry/models.md)"
    p = os.path.join(ROOT, "README.md")
    if not os.path.exists(p):
        open(p, "w", encoding="utf-8").write(f"# free-models-daily\n\n{line}\n")
        return
    txt = open(p, encoding="utf-8").read()
    if "<!-- LATEST_DAILY -->" in txt and "<!-- /LATEST_DAILY -->" in txt:
        new = re.sub(r"(?s)<!-- LATEST_DAILY -->.*<!-- /LATEST_DAILY -->",
                     f"<!-- LATEST_DAILY -->\n{line}\n<!-- /LATEST_DAILY -->", txt)
        if new != txt:  # 只在链接确实变化时写，避免无谓 CRLF / 变更
            open(p, "w", encoding="utf-8").write(new)
    # 无锚点则不改动，避免覆盖富版 README

# ---------- git ----------
def git(*args, check=True):
    r = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed:\n{r.stderr}")
    return r

def ensure_remote():
    remotes = subprocess.run(["git","remote"], cwd=ROOT, capture_output=True, text=True).stdout
    if "origin" not in remotes:
        git("remote", "add", "origin", CONFIG["git_remote"], check=False)
        print("  remote origin:", CONFIG["git_remote"])

def commit_push(today, has_update):
    git("add", "-A")
    ensure_remote()
    git("-c", f"user.name={CONFIG['commit_author']['name']}",
        "-c", f"user.email={CONFIG['commit_author']['email']}",
        "commit", "-m", f"daily {today}: {('updated' if has_update else 'seed')} free-models index")
    try:
        git("push", "-u", "origin", CONFIG.get("branch","main"), check=False)
    except SystemExit:
        pass
    # push 可能因无远端仓失败 → 提示
    r = subprocess.run(["git","push","-u","origin",CONFIG.get("branch","main")], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        print("  ⚠️ push 未成功（远端仓可能还不存在）：", r.stderr.strip().splitlines()[-1] if r.stderr else "")

# ================= MAIN =================
if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    today = datetime.date.today().isoformat()
    print(f"[{today}] free-models-daily pipeline {'(dry-run)' if dry else ''}")
    os.makedirs(os.path.join(ROOT, "registry"), exist_ok=True)

    print("  fetch: OpenRouter / HF / GitHub ...")
    machine_or = fetch_openrouter_free()
    global fetch_hf_result
    fetch_hf_result = fetch_hf_new()
    gh = fetch_gh_releases()
    print(f"    openrouter free: {machine_or.get('count',0)} ok={machine_or.get('ok')}")
    print(f"    hf new: {fetch_hf_result.get('count',0)} ok={fetch_hf_result.get('ok')}")
    print(f"    gh releases: {gh.get('count',0)}")
    vp = fetch_value_pricing()
    print(f"    value pricing: {sum(1 for x in vp.values() if x.get('ok'))}/{len(vp)} live")

    st = load_state()
    or_ids = {m["id"] for m in machine_or["items"]}
    hf_ids = {h["id"] for h in fetch_hf_result["items"]}
    gh_keys = {(r["org_repo"], r.get("tag")) for r in gh["items"]}
    v_ids = {v["id"] for v in VENDORS}

    new_or_ids = or_ids - st["openrouter"]
    new_hf = hf_ids - st["hf"]
    new_gh = gh_keys - st["gh"]
    vend_added = v_ids - st["vendor_ids"]
    print(f"  diff: +{len(new_or_ids)} openrouter, +{len(new_hf)} hf, +{len(new_gh)} gh-release, +{len(vend_added)} vendor")

    print("  AGNES: 翻译厂商条目为 EN ...")
    en = translate_vendors() if not dry else {}

    vp_sig = hashlib.md5(json.dumps(vp, sort_keys=True).encode()).hexdigest()
    build_registry(VENDORS, en, machine_or, vp)
    has_update = build_daily([m for m in machine_or["items"] if m["id"] in new_or_ids],
                             [i for i in fetch_hf_result["items"] if i["id"] in new_hf],
                             [r for r in gh["items"] if (r["org_repo"], r.get("tag")) in new_gh],
                             sorted(vend_added), today) or (vp_sig != st.get("value_pricing", ""))
    update_readme(today, has_update)

    print(f"  has_update={has_update}")
    save_state({"openrouter": or_ids, "hf": hf_ids, "gh": gh_keys, "vendor_ids": v_ids, "value_pricing": vp_sig})

    if dry:
        print("  dry-run：不 commit。registry/daily 已生成，可检查。")
    else:
        if has_update or not os.path.exists(os.path.join(ROOT, "state","last_signals.json.baseline")):
            commit_push(today, has_update)
            open(os.path.join(ROOT, "state", "last_signals.json.baseline"), "w").close()
            print("  committed" + (" (seed)" if not has_update else ""))
        else:
            print("  无更新 → 跳过 commit（本期不提交）。")
    print("done.")
