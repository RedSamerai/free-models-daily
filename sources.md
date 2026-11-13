# 数据源清单（sources.md · 全量 v2，待你审）

> 作用：pipeline 只在本清单范围内采集，不做全网乱搜。发现新厂商才增量追加。
> 信任原则：只认活抓信号（API/页面/Releases/changelog 实抓），禁止 LLM 凭记忆写新闻。
> 标记：✅ = 本会话已实抓可达；◻ = 待 OpenCode 配好时统一验活，验不过不进 registry。
> 国内站多直连可达；海外站部分需代理（HF 实测走 7897 通）。被 403/CF 挡多=数据中心 IP 被反爬，本地/代理能开，不算死。
> 双语规则：需代理/科学上网 备注只写进 ZH 块，EN 块省略。

---

## A. 活抓 backbone（机器主源，"现在有什么"的事实来源）

| 源 | 端点 | 类型 | 状态 | 抓什么 |
|---|---|---|---|---|
| OpenRouter 免费池 | GET https://openrouter.ai/api/v1/models <br>过滤 :free / price=0 | API | ✅ | 免费 LLM 最实时；新 :free=当天信号 |
| Hugging Face | GET https://huggingface.co/api/models?sort=created <br>或 ?sort=trending / collections | API | ✅ | 开源模型上新 + 每日推理额度 |
| GitHub API | GET https://api.github.com/repos/{org}/{repo}/releases <br>+ search | RELEASE | ✅ | 策展 org 的模型/权重发布 |
| 官方 changelog | 各厂商 CHANGELOG/Blog/RSS（§B 标注） | CHANGELOG | ◻ | 停服/涨价/新发布的唯一新闻来源 |

**没有更新就不 commit 判定**：A 段信号 diff 空 且 B 段 changelog 无新增 → 不 commit。
**backbone 抓不到（429/超时）→ 该板块本期跳过并记 log，不用 LLM 记忆补。**

---

## B. 厂商官网源（按六板块归类）

### 免费 LLM（llm-free）
| 厂商 | 源 URL | 抓什么 | 状态 |
|---|---|---|---|
| AGNES AI（自留） | platform.agnes-ai.cn <br>apihub.agnes-ai.com | 免费模态、RPM、每日积分 | ✅ |
| 智谱 Z.ai / GLM | open.bigmodel.cn <br>国际 api.z.ai | 免费模型、0 元项、RPM | ✅ |
| 硅基流动 SiliconFlow | cloud.siliconflow.cn <br>siliconflow.cn/pricing | 零价模型、赠金、实名要求 | ✅ |
| 阿里百炼 | bailian.console.aliyun.com <br>价格/免费额度页 | 每模型 100万 token、90天有效 | ✅ |
| NVIDIA NIM | build.nvidia.com <br>integrate.api.nvidia.com | 试用 credits、RPM、模型数 | ✅ |
| Google Gemini | ai.google.dev（定价/限额）<br>aistudio.google.com/app/apikey | 免费层模型、RPM/RPD、训练政策 | ✅ |
| Groq | console.groq.com <br>groq.com/pricing | 免费层 RPD | ✅ |
| Mistral | console.mistral.ai <br>docs.mistral.ai 定价 | 免费模式额度 | ◻ |
| Cerebras | cloud.cerebras.ai | 免费额度 + $5 试用 | ✅ |
| Cohere | dashboard.cohere.com/api-keys | 试用 key（非商用） | ◻ |
| xAI（Grok） | console.x.ai <br>docs.x.ai | 免费/额度 | ◻ |
| Cloudflare Workers AI | dash.cloudflare.com <br>定价 | 1万 neurons/日，含 SDXL/FLUX | ◻ |
| OpenRouter 文档 | openrouter.ai/docs | 免费池 RPD/RPM、$10 规则 | ✅ |
| GitHub Models | github.com/marketplace/models | GPT/Phi/Llama 免费额度 | ◻ |
| Hugging Face Inference | huggingface.co/settings/tokens | 免费层额度（小） | ✅ |
| SambaNova | developer.sambanovai.com | 需卡 + $5 试用 | ◻ |
| Together AI | api.together.ai | 免费额度（常变动） | ✅ |
| Aion Labs | aionlabs.ai | 免费 15 RPM | ◻ |
| 讯飞星火 | open-platform.xfyun.cn | 每模型 20万 token；国内直连 | ✅ |
| 火山方舟（豆包） | volcengine.com/ark | 每模型 50万 token 免费 | ◻ |
| 百度千帆 | cloud.baidu.com/qianfan | 新用户 100万/模型；国内直连 | ◻ |
| 腾讯混元 / TokenHub | cloud.tencent.com | 免费额度；国内直连 | ◻ |
| Kimi（月之暗面） | moonshot.cn | 免费额度；国内直连 | ◻ |
| 摩尔线程 / 七牛 | 各自官网 | 部分免费层 | ◻ |

### 免费生视频（video-free）
| 厂商/模型 | 源 URL | 抓什么 | 状态 |
|---|---|---|---|
| 快手 Kling（可灵） | app.klingai.com <br>开发者文档 | 免费 66 分/日、登录发放；国内直连 | ✅ |
| MiniMax Hailuo（海螺） | hailuoai.video <br>官方 API | 免费每日额度；国内直连 | ✅ |
| 字节 即梦/Dreamina/Seedance | jimeng.jianying.com <br>官方 API | 免费每日积分（地域差异）；国内直连 | ◻ |
| 生数 Vidu | platform.vidu.com 定价 | 免费条数、闲时、水印 | ✅ |
| 爱诗 PixVerse | pixverse.ai 定价 | 免费 30 分/日 | ◻ |
| 阿里 万相 Wan | create.wan.video <br>百炼 | 每日签到 10 分≈1条/日；国内直连 | ◻ |
| Google Veo / Gemini Omni / Flow | flow.google.com <br>ai.google.dev | 免费 50 分/日；部分需代理 | ◻ |
| Luma | lumalabs.ai 定价 | 约 30 渲染/月；需代理 | ◻ |
| Runway（Gen-4） | runway.com 定价 | 一次性 125 分；需代理 | ◻ |
| Pika | pika.art 定价 | 免费 80 分/月；需代理 | ◻ |
| Adobe Firefly | firefly.adobe.com | 免费每日生成 | ◻ |
| Higgsfield | 官方 API | 免费生视频 | ✅ |

### 免费生图（image-free）
| 厂商/模型 | 源 URL | 抓什么 | 状态 |
|---|---|---|---|
| 智谱 CogView | bigmodel.cn 免费目录 | 0 元生图 | ◻ |
| 百炼 通义万相 | bailian.console.aliyun.com | 免费额度 | ◻ |
| Google Nano Banana / Gemini 图像 | ai.google.dev | 免费层 | ✅ |
| fal FLUX | fal.ai | 免登录每日额度 | ✅ |
| 即梦（图） | jimeng.jianying.com | 积分 | ◻ |
| Stability AI | platform.stability.ai | 注册 25 分；需代理 | ◻ |
| Meta AI（Muse Image） | meta.ai | 每日免费额度 | ◻ |
| FLUX（Black Forest Labs） | 官方 API | FLUX.1 schnell 常免费；需代理 | ◻ |
| GPT Image / DALL-E | OpenAI 官方 API | 免费额度小 | ◻ |
| Leonardo / Ideogram / Krea / Recraft | 各自官网 | 免费每日额度；需代理 | ◻ |

### 高性价比生视频（video-value）
> 直接列模型 + 记录单秒/单片价供排序，不做"≈顶配 90%"对比标注。
| 厂商 | 源 URL | 抓什么 | 状态 |
|---|---|---|---|
| 即梦/Seedance（火山） | jimeng.jianying.com <br>火山方舟 | 单秒价 | ◻ |
| 百炼 Wan 3.0 | bailian.console.aliyun.com | 分分辨率价 | ◻ |
| 快手 Kling | app.klingai.com 开发者定价 | 分分辨率单秒价 | ✅ |
| MiniMax Hailuo | hailuo.ai <br>fal.ai | 单条价 | ◻ |
| Vidu Q3/Q4 | platform.vidu.com | 单秒价、错峰 | ✅ |
| xAI Grok Imagine | docs.x.ai | 单条价 | ✅ |
| LTX（Lightricks 云） | ltx.studio | 云端价 | ◻ |
| Runway | runway.com 开发者定价 | 单秒价 | ◻ |
| Google Gemini Omni / Veo | ai.google.dev | 单秒价 | ✅ |

### 高性价比生图（image-value）
| 厂商 | 源 URL | 抓什么 | 状态 |
|---|---|---|---|
| fal FLUX/Stable | fal.ai/pricing | 每张价 | ✅ |
| 百炼 通义万相 | bailian.console.aliyun.com | 每张价 | ◻ |
| Google Gemini 图像 | ai.google.dev | 每张价 | ✅ |
| Replicate | 各模型页 | 每张/每次价（开源托管极便宜） | ◻ |
| Together / Novita | api.together.ai <br>novita.ai | 便宜推理价 | ✅ |
| 硅基流动 | api.siliconflow.cn | 国产便宜档，国内直连 | ✅ |
| Stability / Luma | 各定价页 | 每张价 | ◻ |

### 开源可本地（oss-local）
| 源 | 抓什么 | 状态 |
|---|---|---|
| §C 策展 org 的 GitHub Release | 新模型、权重链接、License、显存 | ◻ |
| Hugging Face（§A） | 新开源模型、权重、license | ✅ |

---

## C. 策展 GitHub / HF org 清单（每天扫 release，喂「开源可本地」）

> 每个 org 拉 releases + HF 对应 org 新模型。当日有 release = 可进当天"开源可本地"层。
> org 会改名/迁移 → pipeline 做存在校验，失效自动标 ◻ 提醒你换，不静默丢。

| 类别 | org（GitHub / HF） | 说明 |
|---|---|---|
| LLM | deepseek-ai<br>Qwen<br>google（Gemma）<br>Meta-Llama<br>Mistral-AI<br>nvidia（Nemotron）<br>microsoft（Phi）<br>openai（gpt-oss） | 主流开源权重 |
| LLM（国产+嵌入） | 01-ai（Yi）<br>THUDM（ChatGLM）<br>ibm（Granite）<br>baai（BGE）<br>baichuan-inc<br>openbmb（MiniCPM/MOSS）<br>iFlow-OS（心流） | 国产 + 嵌入 |
| 视频 | Lightricks（LTX）<br>Tencent-Hunyuan（HunyuanVideo）<br>THUDM（CogVideo）<br>alibaba（Wan/通义）<br>MiniMax-AI<br>KwaiVGI / Genmo（Mochi）<br>Open-Sora<br>LumaAI<br>Haiper<br>stabilityai（SVD） | 开源视频生成 |
| 生图 | stabilityai（SD）<br>black-forest-labs（FLUX）<br>compvis（SD）<br>ByteDance（Seedream）<br>Tencent（混元）<br>Meta（EMU） | 开源图像生成 |
| 运行时·生态 | ollama/ollama<br>vllm-project/vllm<br>ggerganov/llama.cpp<br>Comfy-Org/ComfyUI<br>mudler/localai<br>softwaremill/LM-Studio<br>oobabooya/text-generation-webui<br>open-webui | 本地推理/工具链 |
| 量化·优化 | Kijai<br>city96<br>TheBloke | 视频/LLM 量化 |

> 说明：运行时·生态 类（ollama / vLLM / llama.cpp 等）不出模型，出的是"能本地跑"的能力，纳入是为了让"开源可本地"层带上"用什么工具跑、多少显存"的信号；当日它们有重大 release 也可进日报。

---

## D. 新厂商发现（每天扫"有没有新出带免费层的厂商"）

1. OpenRouter 免费池新 :free 模型（§A）→ 若属新厂商 → 追加 §B。
2. mnfst/awesome-free-llm-apis 仓库 diff（外部维护的活清单，交叉验证）。
3. HF 当日 trending 新模型 → 判所属厂商/开源 org。
4. 官方 changelog 命中"停服/涨价/新免费" → daily 新闻块。
5. web_search 兜底（默认每周 1 次：free LLM API free tier 当月 / free AI video generation API 当月）→ 命中先活抓官网确认才进 registry。
6. 命中 → 追加到 §B/§C + 当天日报标 新。

---

## 待你定（审这份 source list）
1. 厂商名单对不对：尤其 §B 性价比层，你不用管，我按活抓价排序列成品。
2. §C 策展 org 清单补全后够不够（含 ollama/vLLM 等运行时）。
3. §D web 兜底频率：默认每周 1 次，要更勤说一声。
4. 有没有明确不想收的厂商（水/中转太多的）。
