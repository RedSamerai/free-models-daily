# free-models-daily · 设计说明

公开 GitHub 仓库，每日自动 commit 一份 **ZH/EN 双语**日报，覆盖六板块：
**免费 LLM API / 免费生视频 / 免费生图 / 高性价比生视频 / 高性价比生图 / 开源可本地**；
同时维护一份常驻 registry。核心铁律：**只收「活抓信号」，禁止用 LLM 凭记忆写新闻 / 并购 / 参数**。

---

## 1. 仓库结构

```
free-models-daily/
├─ README.md            # 说明 + 「Latest digest」直达链接 + registry 入口
├─ SPEC.md              # 本文档
├─ sources.md           # 数据源清单（采集范围 + 策展 org 清单）
├─ run_daily.py         # 每日 pipeline（采集 → diff → 渲染 → QA → commit）
├─ vendors.json         # 策展厂商条目（ZH 内容 + 分层，EN 由 pipeline 现场翻译）
├─ config.json          # 端点 / 策展 org 清单 / 代理 / commit 身份
├─ registry/
│  └─ models.md         # 常驻活索引：六板块 + 实抓免费模型池 / 开源新模型
├─ daily/
│  └─ YYYY-MM-DD.md     # 每日 changelog（当天新增/变化，双语）
├─ state/
│  └─ last_signals.json  # 上期各信号快照（diff 基线）
└─ .env.example         # AGNES key 等占位（.env 不进仓）
```

**README 顶部**固定指向最新一期 daily；只有真有变更、且 commit 后，才更新到最新一期；无变更则保持不动。

---

## 2. 单条 entry 模板（六要素）

每条固定 6 字段，**ZH 块 + EN 块**：

| 字段 | ZH | EN |
|---|---|---|
| 名称 | 厂商 / 模型名 | 翻译 |
| 官方接入 / 接入方式 | 官网 / API 地址 | 同 |
| 获取 Key（含申请链接） | 步骤 | 步骤 |
| 限额 / 额度 | 免费额度 / RPM / 每日上限 / 单条价 | 同 |
| 备注 | 手机验证 / 中国直连 / 支付方式 / 商用边界 等 | 省略 CN 专属项（见 §5） |

硬规则：
- 每个数值（价格 / 额度 / RPM）必须带**可点来源 URL** + `as of <YYYY-MM-DD>`。
- 抓不到的数值 → 标 `⚠️ unverified`，不写死数字。
- 实抓不到的官网（JS 重）用策展数据（vendors.json）+ ⚠️ 标注；实抓能到的（OpenRouter 免费池 / HF 开源新模型 / 策展 org release）走机器信号。

---

## 3. 六板块定义

| 板块 | 收录什么 | 字段侧重 |
|---|---|---|
| 免费 LLM | 无需信用卡 / 长期或大额免费额度的文本 LLM API | 免费额度 / RPM / 是否禁商用 |
| 免费生视频 | 有真免费层的视频生成 API（含每日积分 / 闲时） | 免费条数 / 分辨率 / 水印 / 商用 |
| 免费生图 | 有真免费层的生图 API | 同上 |
| 高性价比生视频 | 非免费但便宜的生视频 API/聚合（直接列，不做「顶配90%」标注） | 单条价格 / 免卡 / 支付方式 |
| 高性价比生图 | 非免费但便宜的生图 API（如 fal/聚合按量） | 同上 |
| 开源可本地 | 开源权重本地/自托管，零 API 成本 | 权重链接 / License / 显存 / 可商用 |

---

## 4. 信任模型（核心）

**只认活抓信号，禁止 LLM 回忆。** 硬规则：
1. **信号源**：
   - OpenRouter 免费池 = `GET https://openrouter.ai/api/v1/models` 过滤 `:free` / `price==0`（实时，不照抄第三方口径）。
   - Hugging Face = 官方 API：新模型（按 `text-to-video` / `text-to-image` 标签 + 时间窗）。
   - GitHub = 策展 org 清单（`config.json` 的 `curation_orgs`，见 sources.md §C）的 releases API（真实 release 对象 + 真实日期），喂「开源可本地」板块。
   - 厂商价格 / 额度 / 停服 = 抓 sources.md 里列的官网价格页 / changelog / 官方博客。
2. **禁 LLM 记忆**：任何「并购 / 停服 / 新发布 / 参数规模」条目，必须来自**当天实际抓到的**官方 changelog / blog / press release，否则不进报告。
3. **事实必挂 URL**：验活失败 → 标 `⚠️ unverified`，不当断言。
4. **免费 ≠ 可商用**：商用边界在备注注明（Apache-2.0 自托管 = 可商用；官方免费层常禁商用 / 带水印）。

---

## 5. 双语规则

- 每条 entry = ZH 块 + EN 块。
- **EN 块省略 CN 专属备注**：「需代理 / 需科学上网 / 国内直连 / 需实名 / 手机号验证」等只出现在 ZH 块；EN 保留模型 / 接入 / Key 步骤 / 限额 / 来源。
- EN 由 AGNES 现场翻译，不是机翻堆砌；pipeline 内置去 CN token 的 QA。

---

## 6. 每日 pipeline 与定时

`run_daily.py` 单次运行（纯 stdlib，免依赖）：
1. **实抓**：OpenRouter :free 池 / HF 最新开源文生视频·文生图（likes≥3）/ 策展 GitHub org releases。
2. **diff** 上期 `state/last_signals.json` → 分类新增（🆕）。
3. **渲染**：`registry/models.md`（六板块 + 实抓池）+ `daily/YYYY-MM-DD.md`（当天新增，双语）。
4. **翻译**：AGNES（`agnes-3.0-flash`）把 vendors.json 的 ZH 条目现场译成 EN 块；EN 块自动剔除漏入的 CN 专属 token（QA 门）。
5. **提交**：**有新增才 commit + push `main`；无新增则跳过、不空 commit 堆天数。** 本地 git 身份固定，直接提交到 main。

定时（Hermes cron，非 Windows 计划任务）：
- `0 3 * * *`（UTC+8，即北京 03:00）主任务；`0 4 * * *` 备份任务（失败补跑）。
- 通过 `D:\HermesData\scripts\free_models_daily.py` wrapper 调 `run_daily.py`；无 agent、静默运行（commit 即产出）。
- 失败顺延：主任务异常时由 04:00 备份补跑，digest 窗口自动变 24–48h。

---

## 7. 维护

- **新厂商**：OpenRouter :free 池 / HF trending / 官方 changelog 命中「带免费层的新厂商」→ 追加 `sources.md` §B/§C + `vendors.json`，当天日报标 🆕。
- **策展 org 失效**：org 改名 / 迁移时，pipeline 做存在校验、失效自动跳过并记 log，不静默丢；需人工更新 `config.json` 的 `curation_orgs`。
- **验收线**：每条 entry 有来源 URL 且验活通过（否则 `⚠️ unverified`）；数值带 `as of <date>`；EN 块无 CN 备注泄漏；`git log` 只有真实变更的 commit。
