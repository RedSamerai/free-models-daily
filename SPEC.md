# free-models-daily · 设计 spec（v1，待你过目）

> 状态：讨论已收敛，此文件是实现前的设计稿。你审完、说"按这个做"，我才开始动手（写 pipeline / 建仓 / 配 cron）。

## 0. 一句话
公开 GitHub 仓，每日自动 commit 一份 **ZH/EN 双语**日报，覆盖六板块：**免费 LLM API / 免费生视频 / 免费生图 / 高性价比生视频 / 高性价比生图 / 开源可本地**；同时维护一份**常驻 registry**。核心铁律：**只收"活抓信号"，禁止 LLM 回忆新闻/并购/参数**。

---

## 1. 仓库结构
```
free-models-daily/
├─ README.md            # EN 主 README：说明 + 「Latest digest」直达链接 + registry 六入口
├─ README.zh.md         # ZH 主 README（同上，中文）
├─ sources.md           # 数据源清单（厂商 changelog / 官网价格页 / GitHub 策展 org / HF 检索条件）
│                        #   agent 只在此清单内采集；发现新厂商增量追加
├─ registry/
│  ├─ llm-free.md        # 常驻：免费 LLM API
│  ├─ video-free.md      # 常驻：免费生视频
│  ├─ image-free.md      # 常驻：免费生图
│  ├─ video-value.md     # 常驻：高性价比生视频
│  ├─ image-value.md     # 常驻：高性价比生图
│  └─ oss-local.md       # 常驻：开源可本地部署
├─ daily/
│  └─ 2026-11-14.md      # 每日 changelog（只记「当天变了什么」：🆕 新增 / 🔄 变化 / ⛔ 停服）
├─ .pipeline/
│  ├─ pipeline.py        # 采集→diff→验链→渲染→commit（OpenCode 实现）
│  ├─ config.json        # 源清单引用 / AGNES key 占位 / 验活超时 / commit 身份
│  └─ state.json         # 上次各信号快照 + 页面 hash（.gitignore，不进仓）
└─ .gitignore
```
**README 顶部**固定一行，指向最新一期：
```
> Latest digest: [2026-11-14](daily/2026-11-14.md)
```
每天只有真有变更、且 commit 后，才更新到最新一期；无变更则保持不动。

---

## 2. 单条 entry 模板（六要素）
每条固定 6 字段，**ZH 块 + EN 块**（示意，以真实数据为准）：

````
### 3. Zhipu GLM-4.7-Flash  智谱 GLM-4.7-Flash

**ZH**
- 模型：智谱 GLM-4.7-Flash（1M 上下文，长期免费）
- 官方API/接入：https://bigmodel.cn → OpenAI 兼容 `/api/paas/v4`
- Key获取：bigmodel.cn 实名注册 → API 管理 → 创建（免费模型页 https://docs.bigmodel.cn/cn/guide/models/free/glm-4.7-flash）
- 限额/额度：GLM-4.7-Flash 输入/输出 0 元（as of 2026-11-13）
- 备注：需实名；⚠️ 官方页未标截止日
- 来源：https://docs.bigmodel.cn/cn/guide/models/free/glm-4.7-flash

**EN**
- Model: Zhipu GLM-4.7-Flash (1M ctx, free long-term)
- API: https://bigmodel.cn → OpenAI-compatible `/api/paas/v4`
- Get Key: register (real-name) → API management → create key
- Quota: CNY 0 input/output (as of 2026-11-13)
- Source: https://docs.bigmodel.cn/cn/guide/models/free/glm-4.7-flash
````

**硬规则**
- 每个数值（价格 / 额度 / RPM）必须带**可点来源 URL** + `as of <YYYY-MM-DD>`。
- 抓不到的数值 → 该字段写 `⚠️ unverified`，**不写死数字**。
- **EN 块省略 CN 特有备注**（需代理 / 需科学上网 / 国内直连 / 需实名 等一律只出现在 ZH 块）；EN 保留：模型 / 接入 / Key 步骤 / 限额 / 来源。
- 第三方中转（CheaperGen / WaveSpeed / fal 等）可列，但备注标注「第三方中转，自行评估数据合规与稳定性」。

---

## 3. 六板块定义
| 板块 | 文件 | 收录什么 | 字段侧重 |
|---|---|---|---|
| 免费 LLM | llm-free | 无需信用卡/长期或大额免费额度的文本 LLM API | 免费额度 / RPM / 是否禁商用 |
| 免费生视频 | video-free | 有真免费层的视频生成 API（含每日积分/闲时） | 免费条数 / 分辨率 / 水印 / 商用 |
| 免费生图 | image-free | 有真免费层的生图 API | 同上 |
| 高性价比生视频 | video-value | 非免费但便宜的生视频 API/聚合（直接列，不做"顶配90%"标注） | 单条价格 / 免卡 / 支付方式 |
| 高性价比生图 | image-value | 非免费但便宜的生图 API（如 fal/聚合按量） | 同上 |
| 开源可本地 | oss-local | 开源权重本地/自托管，零 API 成本 | 权重链接 / License / 显存 / 可商用 |

---

## 4. 信任模型（核心，治旧 40% 不真实）
**只认可活抓信号，禁止 LLM 回忆。** 硬规则：
1. **信号源**：
   - OpenRouter 免费池 = `GET https://openrouter.ai/api/v1/models` 过滤 `pricing.prompt=="0" && pricing.completion=="0"`（实时，不照抄第三方"16/18 个"口径）
   - Hugging Face = 官方 API：新建 / trending 模型（按 `text-to-video` / `text-to-image` / `text-generation` 标签 + 时间窗）
   - GitHub = 「策展 org 清单」的 releases API（真实 release 对象 + 真实日期）。策展 org 清单 = 我挑定的固定一批开源模型 org（视频/图像/LLM，如 Lightricks、Tencent、THUDM、Wan-Video、MiniMax-AI、stabilityai、Luma 等），写在 sources.md，你审源清单时定稿；目的是每天扫这批 org 的新 release，喂「开源可本地」板块
   - 厂商价格/额度/停服 = 抓 `sources.md` 里列的**官网价格页 / changelog / 官方博客**
2. **禁 LLM 记忆**：任何「并购 / 停服 / 新发布 / 参数规模」条目，必须来自**当天实际抓到的**官方 changelog / blog / press release，否则**不进报告**。
   （旧报告"NVIDIA 收购 HF / Stripe 收购 OpenRouter"就是这类 LLM 编造，直接杜绝。）
3. **事实必挂 URL**：验活失败 → 标 `⚠️ unverified`，不当断言。
4. **免费 ≠ 可商用**：涉及商用边界在备注注明（Apache-2.0 自托管 = 可商用；官方免费层常禁商用/带水印）。

---

## 5. 初版 registry 种子（冷启动，一次性）
1. 取 workbuddy 报告**可信部分**做底稿（额度 / 直连 / Key 步骤 这类能对得上官网的）。
2. 我**另行全网搜索**（官网 / 官方 changelog / GitHub / HF / 各家价格页）。
3. 两者整合，**每条重新活抓官网验证**；验不过 / 对不上的**直接丢弃**。
4. 产出：初版 registry 六文件 + 一期 `daily/`（顶部标注「初版 seed」）。
5. 你**审一遍初版 registry**，确认后转正式每日运行。

---

## 6. 每日 cron 流程（03:00 北京 = UTC 前一日 19:00）
```
03:00 触发（**Hermes 定时任务**跑 `python .pipeline\pipeline.py`；用户 Hermes 基本不关，不用 Windows 任务计划）
 1. 活抓：OpenRouter :free / HF 新建+trending(video·image·llm 标签) /
    GitHub「策展 org 清单」releases / sources.md 内官网 changelog·价格页
 2. diff state.json → 分类 🆕 新增 / 🔄 变化(价格·额度·停服·换域名) / ⛔ 停服
 3. 逐条验活 URL（HEAD → GET 回退）
 4. 渲染 daily/YYYY-MM-DD.md（ZH/EN）+ 更新 registry 对应文件
 5. 检测新厂商（带免费层、不在 sources.md）→ 追加 sources.md + 日报标 🆕
 6. 有变化 → **自动生成 draft（auto-commit 到 `draft` 分支，不碰 main）**；无变化 → 不生成、不打扰
 7. 更新 state.json
 8. **Hermes QA 门**（我审，你 3am 不用醒）：draft 生成后我**独立复核**——重跑验活 URL / 剔除无来源的 LLM 回忆条目 / 查 EN 无 CN 备注泄漏 / 查 as-of 日期与格式 → 过则 **auto commit + push `main`**；不过则不 commit、记 log。`draft` 分支留原始生成版，供你晨间审计

失败重试：
 - 采集/验链失败 → 原地重试 1 次
 - 仍失败 → **04:00 Hermes cron 补跑**（digest 窗口自动变 24–48h）
 - 只有 draft 生成或 QA 不过才补；**main 只收 QA 通过的内容（=我复核过）**
```

---

## 7. 双语规则（重申）
- 每条 entry = ZH 块 + EN 块。
- **EN 块不含**「需代理 / 需科学上网 / 国内直连 / 需实名」等 CN 备注（你定）；ZH 保留。
- EN 是**认真翻译**（AGNES 生成 + 可人工修），不是机翻堆砌。

---

## 8. 验收标准（一期日报 / 初版 registry 合格线）
- [ ] 每条 entry 有来源 URL，且验活通过（否则标 `⚠️ unverified`）
- [ ] 每个数值带 `as of <date>`
- [ ] EN 块无 CN 备注泄漏（grep 检查「代理 / 直连 / 实名」）
- [ ] 停服 / 到期项进 ⛔ 或「到期倒计时」区
- [ ] 无 LLM 回忆类新闻（并购/参数），全部可溯源到当天抓取
- [ ] `git log` 只有真实变更的 commit，**不空 commit 堆天数**
- [ ] README「Latest digest」指向最新一期

---

## 9. 交付分工
- **Hermes**：设计 / 拆 OpenCode 指令块 / 全网搜索补料 / 配 Hermes cron / **每期独立 QA 复核 → 过则自动 commit main** + 验收初版 registry
- **OpenCode**：写 `.pipeline/pipeline.py`（采集 / diff / 验链 / 渲染 / 生成 `draft`；**不 push main**）
- **你**：审 spec、审初版 registry、定 `sources.md` 源清单；**日常日报不用管**（我 3am 自动 QA+发布），`draft` 分支留着给你晨间抽查

---

## 10. 已定（本轮收敛）
1. 触发 = **Hermes 定时任务**（不用 Windows 任务计划）；03:00 自动生成 → **我 QA 复核** → 过则自动 commit main（你 3am 不用醒，见 §6 QA 门）。
2. 性价比层**不设价格软筛，全列**便宜档，按「单条 5s / 每张图」排序供读者挑。
3. **策展 org 清单**：见 §4 定义；初版我提一批主流开源 org，你审 `sources.md` 时定稿。
4. EN 由 AGNES 生成，**每期我 QA 复核一遍再 commit main**（与 §6 QA 门同一道）。
