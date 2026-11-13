# 模型 API 注册表（living index）

_as-of: 2026-11-13 · 每 5 字段：名称 / 官方接入 / 获取Key / 限额 / 备注_


## 免费 LLM API / Free LLM API

### 实抓免费模型池（OpenRouter，16 个）

- `baidu/ernie-5.5-flash-preview:free` · 1024000 ctx
- `thinkingmachines/inkling-2-small:free` · 1048576 ctx
- `liquid/lfm-3-1.7b:free` · 262144 ctx
- `particle-ai/particle-1:free` · 1048576 ctx
- `recursive/flint-v1.0:free` · 262144 ctx
- `nvidia/nemotron-3.5-super-vl:free` · 1000000 ctx
- `dots-studio/dots-3-note-preview:free` · 512000 ctx
- `nvidia/nemotron-3.5-lightning:free` · 1000000 ctx
- `cohere/north-mini-code:free` · 256000 ctx
- `nvidia/nemotron-3-ultra-550b-a55b:free` · 1000000 ctx
- `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` · 256000 ctx
- `google/gemma-4-26b-a4b-it:free` · 262144 ctx
- `google/gemma-4-31b-it:free` · 262144 ctx
- `google/lyria-3-pro-preview` · 1048576 ctx
- `google/lyria-3-clip-preview` · 1048576 ctx
- `openrouter/free` · 200000 ctx


### Google Gemini（AI Studio）
- 官方接入：aistudio.google.com/app/apikey
- 获取 Key：注册 Google 账号 → AI Studio → Get API key
- 限额/额度：免费层：Gemini Flash/Flash-Lite，RPM 5–15，部分模型每日上限
- 备注：免费层数据可用于训练；部分地区需代理；免信用卡
### Groq
- 官方接入：console.groq.com/keys
- 获取 Key：Groq 控制台 → Keys → 新建
- 限额/额度：免费层：30 RPM / 1000 次/日（gpt-oss-120b）
- 备注：速度最快（LPU）；免信用卡；商用可用
### 智谱 Z.ai / GLM
- 官方接入：open.bigmodel.cn
- 获取 Key：注册 → 用户中心 → API keys
- 限额/额度：GLM-4.7-Flash 免费，1 并发；新用户 2000万 token 体验包
- 备注：国内可直连；chat API 免实名（Batch 需实名）；国际站 api.z.ai
### 硅基流动 SiliconFlow
- 官方接入：cloud.siliconflow.cn
- 获取 Key：注册 → 账号 → API 密钥
- 限额/额度：新用户 2000万 token；部分开源模型永久免费
- 备注：国内可直连；免费模型需实名认证；响应快
### 阿里百炼（通义）
- 官方接入：bailian.console.aliyun.com
- 获取 Key：开通百炼 → 授权 → 新建 API key
- 限额/额度：新用户每模型约 100万 token，90 天有效
- 备注：国内可直连；模型最全（Qwen + 第三方）
### OpenRouter（免费池）
- 官方接入：openrouter.ai/keys
- 获取 Key：注册 → Keys → 新建（单 key 多模型）
- 限额/额度：:free 模型 20 RPM / 50 次/日；充 10 美元后 1000 次/日
- 备注：免信用卡；自动路由多厂商；免费模型每日轮换（脚本实抓）
### Mistral（La Plateforme）
- 官方接入：console.mistral.ai
- 获取 Key：注册 → API keys
- 限额/额度：免费模式（Experiment）：约 1B token/月，限流看后台
- 备注：API 数据不用于训练；免信用卡
### Cerebras
- 官方接入：cloud.cerebras.ai
- 获取 Key：注册 → 加一次支付方式 → 免费 credit
- 限额/额度：$5 试用 credit，30 天过期；吞吐极高
- 备注：需加卡（仅试用）
### NVIDIA NIM
- 官方接入：build.nvidia.com
- 获取 Key：注册 NVIDIA Developer 计划 → 领 NIM key
- 限额/额度：100+ 开源模型，限流按模型动态（无公开表）
- 备注：原型/研究用；生产需 NVIDIA AI Enterprise 授权
### Together AI
- 官方接入：api.together.ai
- 获取 Key：注册 → Settings → API keys
- 限额/额度：免费额度常变动（多为小额试用）
- 备注：开源模型托管便宜档
### AGNES AI Hub
- 官方接入：apihub.agnes-ai.com/v1
- 获取 Key：注册 agnes-ai.com → 领 API key
- 限额/额度：免费层含 agnes-flash 系列（具体免费模型/额度以官网为准）
- 备注：国内可直连；本日报的 EN 翻译引擎即 agnes-3.0-flash（同源）
### 科大讯飞星火
- 官方接入：open-platform.xfyun.cn
- 获取 Key：注册 → 控制台 → 申请 APIKey
- 限额/额度：每模型约 20万 token 免费
- 备注：国内可直连
### Hugging Face Inference（免费层）
- 官方接入：huggingface.co/settings/tokens
- 获取 Key：注册 HF → Settings → Access tokens
- 限额/额度：免费推理额度（按模型、限额小；以官网为准）
- 备注：需代理；大量开源模型可在线推理；免信用卡
### SambaNova Cloud
- 官方接入：cloud.sambanova.ai
- 获取 Key：注册 → API keys
- 限额/额度：部分开源模型免费档（推理极快）；以官网为准
- 备注：需代理
### xAI Grok
- 官方接入：console.x.ai
- 获取 Key：注册 xAI 控制台 → API key
- 限额/额度：免费层现状以官网为准（曾开放免费档）
- 备注：需代理
### DeepSeek
- 官方接入：platform.deepseek.com
- 获取 Key：注册 → API keys
- 限额/额度：极低价格；部分模型免费/赠送额度以官网为准
- 备注：国内可直连；便宜档主力
### Cohere
- 官方接入：dashboard.cohere.com
- 获取 Key：注册 → API keys
- 限额/额度：免费试用额度（Chat/Rerank/Embed，以官网为准）
- 备注：需代理；长上下文强
### Unorouter（开源 LLM 聚合）
- 官方接入：api.unorouter.com/v1
- 获取 Key：注册 unorouter.com → API key
- 限额/额度：160+ 个 :free 模型；免费 1 req/min/模型；以官网为准
- 备注：北京可直连；OpenAI 兼容、单 key 路由多上游；全栈开源可审计
### Cloudflare Workers AI / AI Gateway
- 官方接入：dash.cloudflare.com
- 获取 Key：Cloudflare 账号 → API token
- 限额/额度：免费层含额度（限流以官网为准）
- 备注：需代理；免信用卡；边缘推理
### GitHub Models
- 官方接入：models.github.ai
- 获取 Key：GitHub 账号 → 免费 token
- 限额/额度：开源模型免费调用（限额/并发以官网为准）
- 备注：需代理；免信用卡
### Requesty
- 官方接入：requesty.ai
- 获取 Key：注册 → API key
- 限额/额度：免费模型约 200 req/日（以官网为准）
- 备注：需代理；免信用卡；多模型路由
### Kilo Code（kilo-auto/free）
- 官方接入：kilo.ai
- 获取 Key：注册（部分免 key）
- 限额/额度：free 池自动路由（限额以官网为准）
- 备注：需代理；免信用卡
### LLM7.io
- 官方接入：token.llm7.io
- 获取 Key：注册 → 领 token
- 限额/额度：API 网关免费层（以官网为准）
- 备注：需代理
### OVHcloud AI Endpoints
- 官方接入：ovhcloud.com
- 获取 Key：匿名即可（部分模型免 key）
- 限额/额度：免费匿名档 2 RPM/IP/模型（以官网为准）
- 备注：需代理；EU 托管开源模型；免注册

## 免费生视频 / Free Video Generation

### 实抓：Hugging Face 最新文生视频模型

- `lightx2v/LightLingBot-Video` (13 👍) [2026-07-28]
- `SanDiegoDude/Cosmos3-Super-nf4` (4 👍) [2026-06-02]
- `SanDiegoDude/Cosmos3-Nano-nf4` (4 👍) [2026-06-02]
- `cyberneurova/CyberNeurova-Lance-3B-abliterated` (8 👍) [2026-05-20]
- `OmerHagage/ltx2-greenscreen-avatar-ic-lora-vertical-v1` (23 👍) [2026-05-13]
- `realrebelai/LOW_VRAM_Workflows` (61 👍) [2026-03-20]
- `atMrMattV/Visione` (6 👍) [2026-03-10]
- `Backup-bdg/Xoron-Dev-MultiMoe` (10 👍) [2026-01-23]
- `artificialguybr/FollowCam-Redmond-WAN2-T2V-14B` (3 👍) [2025-10-23]
- `deadman44/Wan2.2_Workflow_for_myxx_series_LoRA` (26 👍) [2025-08-04]
- `deadman44/Wan2.2_T2i_T2v_LoRA` (28 👍) [2025-07-27]
- `artificialguybr/Wan-Bloom-Redmond-Wan2.1-T2V-14B` (3 👍) [2025-07-21]

### 快手 Kling（可灵）
- 官方接入：app.klingai.com
- 获取 Key：登录 → 开发者中心 → API key
- 限额/额度：免费 66 分/日（登录发放）；免费 5s/720p 带水印
- 备注：国内可直连；免费层禁商用；登录需手机号
### MiniMax Hailuo（海螺）
- 官方接入：hailuoai.video
- 获取 Key：注册 → 领免费额度 / 官方 API key
- 限额/额度：每日免费若干条；免费 720p
- 备注：国内可直连；免费带水印
### 字节 即梦 / Dreamina / Seedance
- 官方接入：jimeng.jianying.com
- 获取 Key：注册即梦 → 生成；API 走火山方舟
- 限额/额度：免费每日积分（地域差异，美区约 120/日）
- 备注：国内可直连；免费带水印；Seedance 走 API 付费
### 生数 Vidu
- 官方接入：platform.vidu.com
- 获取 Key：注册 → 免费额度 / API key
- 限额/额度：每日免费条数 + 闲时档；带水印
- 备注：国内可直连；按秒付费
### 阿里 通义万相 Wan
- 官方接入：create.wan.video
- 获取 Key：每日签到领 10 分；API 走百炼
- 限额/额度：约 1 条/日（720p/5s）；百炼新户免费秒数
- 备注：国内可直连；签到制
### Google Veo / Gemini Omni / Flow
- 官方接入：flow.google.com
- 获取 Key：注册 Google 账号 → Flow；API 走 ai.google.dev
- 限额/额度：免费 50 分/日（Veo 3.1 Lite）
- 备注：部分地区需代理；免费带水印
### Runway（Gen-4）
- 官方接入：runway.com
- 获取 Key：注册 → 一次性 125 分；API 需付费
- 限额/额度：一次性 125 分（非每日）
- 备注：需代理；专业向
### Luma AI（Ray）
- 官方接入：lumalabs.ai
- 获取 Key：登录 Luma → 每日免费积分
- 限额/额度：每日免费条数（以官网为准，带水印）
- 备注：需代理
### Pika
- 官方接入：pika.art
- 获取 Key：登录 Pika → 每日免费积分
- 限额/额度：每日免费条数（以官网为准，带水印）
- 备注：需代理
### Pixverse
- 官方接入：pixverse.ai
- 获取 Key：登录 Pixverse → 每日免费积分
- 限额/额度：每日免费条数（以官网为准，带水印）
- 备注：需代理
### Haiper
- 官方接入：haiper.ai
- 获取 Key：登录 Haiper → 每日免费积分
- 限额/额度：每日免费条数（以官网为准，带水印）
- 备注：需代理
### ZSky AI
- 官方接入：zsky.ai
- 获取 Key：注册 ZSky → API key
- 限额/额度：免费 REST 生成 1080p 视频（额度以官网为准）
- 备注：需代理；免费层现状以官网为准

## 免费生图 / Free Image Generation

### Stability AI
- 官方接入：platform.stability.ai
- 获取 Key：注册（建议 Google 登录才到账）→ 25 分
- 限额/额度：注册 25 分（约 3–10 张），无持续免费额度
- 备注：需代理；之后按量付费
### FLUX（Black Forest Labs）
- 官方接入：fal.ai/models/black-forest-labs
- 获取 Key：经 fal.ai / Hugging Face Spaces 免费调用 schnell
- 限额/额度：FLUX.1 schnell 常免费（每日额度，需排队）
- 备注：需代理；开源权重可本地
### Google Imagen / Nano Banana
- 官方接入：ai.google.dev
- 获取 Key：AI Studio → Get API key
- 限额/额度：免费层可调用图像生成（限额小）
- 备注：部分需代理
### Meta AI（Muse Image）
- 官方接入：meta.ai
- 获取 Key：登录 Meta 账号即可
- 限额/额度：每日免费额度（不公布具体数）
- 备注：移动端为主
### Leonardo
- 官方接入：app.leonardo.ai
- 获取 Key：登录 Leonardo → 每日免费 token
- 限额/额度：每日免费额度（以官网为准，需刷新）
- 备注：需代理；免费档够用
### Ideogram
- 官方接入：ideogram.ai
- 获取 Key：登录 Ideogram → 每日免费额度
- 限额/额度：每日免费张数（以官网为准，带水印）
- 备注：需代理；文字渲染强
### Krea
- 官方接入：krea.ai
- 获取 Key：登录 Krea → 每日免费积分
- 限额/额度：每日免费积分（以官网为准）
- 备注：需代理
### Playground
- 官方接入：playground.com
- 获取 Key：登录 Playground → 免费额度
- 限额/额度：免费生成额度（以官网为准，可商用免费档）
- 备注：需代理
### Microsoft Designer（Bing Image）
- 官方接入：designer.microsoft.com
- 获取 Key：登录 Microsoft 账号
- 限额/额度：每日免费额度（以官网为准）
- 备注：需代理；免注册门槛低
### LiblibAI（哩布哩布）
- 官方接入：liblib.art
- 获取 Key：登录 → 每日免费算力
- 限额/额度：每日免费算力（生图，以官网为准）
- 备注：国内可直连；国内模型社区
### hiapi.ai
- 官方接入：api.hiapi.ai
- 获取 Key：注册 → API key
- 限额/额度：免费额度（含 GPT 图像）；以官网为准
- 备注：需代理
### ModelScope（阿里 魔搭）
- 官方接入：modelscope.cn
- 获取 Key：注册 → API key
- 限额/额度：Qwen-Image 等免费调用（非商用，以官网为准）
- 备注：国内可直连；开源模型社区

## 高性价比生视频 / Cost-Effective Video

### 字节 Seedance 2.x（火山）
- 官方接入：volcengine.com/ark
- 获取 Key：开通火山方舟 → API key
- 限额/额度：按秒付费（实抓价见下方·官网）
- 备注：国内可直连；性价比看分辨率/时长
- 单条价：⚠️ unverified（https://www.volcengine.com/product/ark 实抓未命中）
### 阿里 万相 Wan 3.0（百炼）
- 官方接入：bailian.console.aliyun.com
- 获取 Key：百炼 API key
- 限额/额度：分分辨率按量；新户免费秒数
- 备注：国内可直连
- 单条价：⚠️ unverified（https://help.aliyun.com/zh/model-studio/billing-of-model-studio 实抓未命中）
### 快手 Kling（分分辨率价）
- 官方接入：app.klingai.com 开发者定价
- 获取 Key：开发者中心 API key
- 限额/额度：分分辨率按量（实抓价见下方·官网）
- 备注：国内可直连
- 实抓价目（节选，最低档起）：$1、$2（https://klingai.com/app/pricing，as of 2026-11-13）

## 高性价比生图 / Cost-Effective Image

### xAI Grok Imagine
- 官方接入：console.x.ai
- 获取 Key：xAI 控制台 → API key
- 限额/额度：按张付费（便宜档）
- 备注：需代理
- 实抓价目（节选，最低档起）：$0.02、$0.08、$0.1、$0.2（https://docs.x.ai/，as of 2026-11-13）
### fal.ai（开源图/视频托管）
- 官方接入：fal.ai
- 获取 Key：注册 → API key；有试用额度
- 限额/额度：开源模型按量极便宜（实抓价见下方）
- 备注：需代理；开源模型最便宜档
- 实抓价目（节选，最低档起）：$0.0002、$0.002、$0.003、$0.005（https://fal.ai/pricing，as of 2026-11-13）
### Together / Novita（便宜推理）
- 官方接入：api.together.ai · novita.ai
- 获取 Key：注册 → API key
- 限额/额度：开源模型按量，极便宜
- 备注：需代理
- 实抓价目（节选，最低档起）：$0、$0.0015、$0.0017、$0.0019（https://www.together.ai/pricing，as of 2026-11-13）
### 硅基流动（国产便宜档）
- 官方接入：api.siliconflow.cn
- 获取 Key：注册 → API 密钥
- 限额/额度：开源模型按量；部分免费
- 备注：国内可直连
- 实抓价目（节选，最低档起）：$6、$7、$11（https://cloud.siliconflow.cn/pricing，as of 2026-11-13）
### Replicate（便宜推理）
- 官方接入：replicate.com
- 获取 Key：注册 → API tokens
- 限额/额度：按量计费（开源模型极便宜；以官网为准）
- 备注：需代理；托管大量开源图/视频模型

## 免费 TTS 语音 / Free TTS / Voice

### ElevenLabs
- 官方接入：elevenlabs.io
- 获取 Key：注册 → API key
- 限额/额度：免费约 1 万字符/月（不可商用；以官网为准）
- 备注：需代理；音质顶尖
### Google Cloud TTS
- 官方接入：cloud.google.com/text-to-speech
- 获取 Key：GCP 项目 → API key
- 限额/额度：WaveNet 每月 100 万字符免费（以官网为准）
- 备注：需代理
### Azure Neural TTS
- 官方接入：learn.microsoft.com/azure/ai-services/speech-service
- 获取 Key：Azure 账号 → Speech key
- 限额/额度：神经语音每月 50 万字符免费（以官网为准）
- 备注：需代理
### Amazon Polly
- 官方接入：aws.amazon.com/polly
- 获取 Key：AWS 账号（免费层前一年）
- 限额/额度：标准语音每月 500 万字符（前一年免费，以官网为准）
- 备注：需代理
### Inworld
- 官方接入：platform.inworld.ai
- 获取 Key：注册 → API key
- 限额/额度：免费 70 分钟 TTS + 100 自定义音色（以官网为准）
- 备注：需代理；实时语音智能体
### Fish Audio
- 官方接入：fish.audio
- 获取 Key：注册 → API key
- 限额/额度：免费层（个人使用，以官网为准）
- 备注：需代理；中英音色多