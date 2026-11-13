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
- EN: Google Gemini (AI Studio) | aistudio.google.com/app/apikey
  Key: Register Google account -> AI Studio -> Get API key | Limits: Free tier: Gemini Flash/Flash-Lite, 5-15 RPM, some models have daily limits | Notes: Free tier data may be used for training; no credit card required
### Groq
- 官方接入：console.groq.com/keys
- 获取 Key：Groq 控制台 → Keys → 新建
- 限额/额度：免费层：30 RPM / 1000 次/日（gpt-oss-120b）
- 备注：速度最快（LPU）；免信用卡；商用可用
- EN: Groq | console.groq.com/keys
  Key: Groq Console -> Keys -> Create new | Limits: Free tier: 30 RPM / 1000 requests/day (gpt-oss-120b) | Notes: Fastest speed (LPU); no credit card required; commercial use allowed
### 智谱 Z.ai / GLM
- 官方接入：open.bigmodel.cn
- 获取 Key：注册 → 用户中心 → API keys
- 限额/额度：GLM-4.7-Flash 免费，1 并发；新用户 2000万 token 体验包
- 备注：国内可直连；chat API 免实名（Batch 需实名）；国际站 api.z.ai
- EN: Zhipu Z.ai / GLM | open.bigmodel.cn
  Key: Register -> User Center -> API keys | Limits: GLM-4.7-Flash free, 1 concurrency; new users get 20 million token trial pack | Notes: International site: api.z.ai
### 硅基流动 SiliconFlow
- 官方接入：cloud.siliconflow.cn
- 获取 Key：注册 → 账号 → API 密钥
- 限额/额度：新用户 2000万 token；部分开源模型永久免费
- 备注：国内可直连；免费模型需实名认证；响应快
- EN: SiliconFlow | cloud.siliconflow.cn
  Key: Register -> Account -> API Key | Limits: New users get 20 million tokens; some open-source models are free forever | Notes: Fast response
### 阿里百炼（通义）
- 官方接入：bailian.console.aliyun.com
- 获取 Key：开通百炼 → 授权 → 新建 API key
- 限额/额度：新用户每模型约 100万 token，90 天有效
- 备注：国内可直连；模型最全（Qwen + 第三方）
- EN: Alibaba Bailian (Tongyi) | bailian.console.aliyun.com
  Key: Activate Bailian -> Authorize -> Create API key | Limits: New users get approx. 1 million tokens per model, valid for 90 days | Notes: Largest model catalog (Qwen + third-party)
### OpenRouter（免费池）
- 官方接入：openrouter.ai/keys
- 获取 Key：注册 → Keys → 新建（单 key 多模型）
- 限额/额度：:free 模型 20 RPM / 50 次/日；充 10 美元后 1000 次/日
- 备注：免信用卡；自动路由多厂商；免费模型每日轮换（脚本实抓）
- EN: OpenRouter (Free Pool) | openrouter.ai/keys
  Key: Register -> Keys -> Create new (single key for multiple models) | Limits: :free models 20 RPM / 50 requests/day; 1000 requests/day after $10 deposit | Notes: No credit card required; automatic multi-vendor routing; free models rotate daily (verified via script)
### Mistral（La Plateforme）
- 官方接入：console.mistral.ai
- 获取 Key：注册 → API keys
- 限额/额度：免费模式（Experiment）：约 1B token/月，限流看后台
- 备注：API 数据不用于训练；免信用卡
- EN: Mistral (La Plateforme) | console.mistral.ai
  Key: Register -> API keys | Limits: Free mode (Experiment): approx. 1B tokens/month, rate limits visible in dashboard | Notes: API data not used for training; no credit card required
### Cerebras
- 官方接入：cloud.cerebras.ai
- 获取 Key：注册 → 加一次支付方式 → 免费 credit
- 限额/额度：$5 试用 credit，30 天过期；吞吐极高
- 备注：需加卡（仅试用）
- EN: Cerebras | cloud.cerebras.ai
  Key: Register -> Add payment method once -> Get free credit | Limits: $5 trial credit, expires in 30 days; extremely high throughput | Notes: Card required (for trial only)
### NVIDIA NIM
- 官方接入：build.nvidia.com
- 获取 Key：注册 NVIDIA Developer 计划 → 领 NIM key
- 限额/额度：100+ 开源模型，限流按模型动态（无公开表）
- 备注：原型/研究用；生产需 NVIDIA AI Enterprise 授权
- EN: NVIDIA NIM | build.nvidia.com
  Key: Register for NVIDIA Developer Program -> Get NIM key | Limits: 100+ open-source models, dynamic rate limits per model (no public table) | Notes: For prototyping/research; production requires NVIDIA AI Enterprise license
### Together AI
- 官方接入：api.together.ai
- 获取 Key：注册 → Settings → API keys
- 限额/额度：免费额度常变动（多为小额试用）
- 备注：开源模型托管便宜档
- EN: Together AI | api.together.ai
  Key: Register -> Settings -> API keys | Limits: Free quota varies frequently (usually small trial amounts) | Notes: Cost-effective hosting for open-source models
### AGNES AI Hub
- 官方接入：apihub.agnes-ai.com/v1
- 获取 Key：注册 agnes-ai.com → 领 API key
- 限额/额度：免费层含 agnes-flash 系列（具体免费模型/额度以官网为准）
- 备注：国内可直连；本日报的 EN 翻译引擎即 agnes-3.0-flash（同源）
- EN: AGNES AI Hub | apihub.agnes-ai.com/v1
  Key: Register at agnes-ai.com -> Get API key | Limits: Free tier includes agnes-flash series (check official site for specific free models/quotas) | Notes: 
### 科大讯飞星火
- 官方接入：open-platform.xfyun.cn
- 获取 Key：注册 → 控制台 → 申请 APIKey
- 限额/额度：每模型约 20万 token 免费
- 备注：国内可直连
- EN: iFLYTEK Spark | open-platform.xfyun.cn
  Key: Register -> Console -> Apply for APIKey | Limits: Approx. 200,000 free tokens per model | Notes: 
### Hugging Face Inference（免费层）
- 官方接入：huggingface.co/settings/tokens
- 获取 Key：注册 HF → Settings → Access tokens
- 限额/额度：免费推理额度（按模型、限额小；以官网为准）
- 备注：需代理；大量开源模型可在线推理；免信用卡
- EN: Hugging Face Inference (Free Tier) | huggingface.co/settings/tokens
  Key: Register HF -> Settings -> Access tokens | Limits: Free inference quota (per model, low limits; check official site) | Notes: Online inference for many open-source models; no credit card required
### SambaNova Cloud
- 官方接入：cloud.sambanova.ai
- 获取 Key：注册 → API keys
- 限额/额度：部分开源模型免费档（推理极快）；以官网为准
- 备注：需代理
- EN: SambaNova Cloud | cloud.sambanova.ai
  Key: Register -> API keys | Limits: Free tier for some open-source models (extremely fast inference); check official site | Notes: 
### xAI Grok
- 官方接入：console.x.ai
- 获取 Key：注册 xAI 控制台 → API key
- 限额/额度：免费层现状以官网为准（曾开放免费档）
- 备注：需代理
- EN: xAI Grok | console.x.ai
  Key: Register xAI Console -> API key | Limits: Current free tier status subject to official site (previously had free tier) | Notes: 
### DeepSeek
- 官方接入：platform.deepseek.com
- 获取 Key：注册 → API keys
- 限额/额度：极低价格；部分模型免费/赠送额度以官网为准
- 备注：国内可直连；便宜档主力
- EN: DeepSeek | platform.deepseek.com
  Key: Register -> API keys | Limits: Extremely low pricing; some models free/grant quotas subject to official site | Notes: Key budget option
### Cohere
- 官方接入：dashboard.cohere.com
- 获取 Key：注册 → API keys
- 限额/额度：免费试用额度（Chat/Rerank/Embed，以官网为准）
- 备注：需代理；长上下文强
- EN: Cohere | dashboard.cohere.com
  Key: Register -> API keys | Limits: Free trial quota (Chat/Rerank/Embed, subject to official site) | Notes: Strong for long context

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
- EN: Kuaishou Kling | app.klingai.com
  Key: Log in -> Developer Center -> API key | Limits: 66 free points/day (issued upon login); free 5s/720p with watermark | Notes: No commercial use in free tier; login requires phone number
### MiniMax Hailuo（海螺）
- 官方接入：hailuoai.video
- 获取 Key：注册 → 领免费额度 / 官方 API key
- 限额/额度：每日免费若干条；免费 720p
- 备注：国内可直连；免费带水印
- EN: MiniMax Hailuo | hailuoai.video
  Key: Register -> Get free quota / Official API key | Limits: Several free generations daily; free 720p | Notes: Free generations include watermark
### 字节 即梦 / Dreamina / Seedance
- 官方接入：jimeng.jianying.com
- 获取 Key：注册即梦 → 生成；API 走火山方舟
- 限额/额度：免费每日积分（地域差异，美区约 120/日）
- 备注：国内可直连；免费带水印；Seedance 走 API 付费
- EN: ByteDance Dreamina / Seedance | jimeng.jianying.com
  Key: Register Dreamina -> Generate; API via Volcano Ark | Limits: Daily free points (varies by region, approx. 120/day in US) | Notes: Free generations include watermark; Seedance API is paid
### 生数 Vidu
- 官方接入：platform.vidu.com
- 获取 Key：注册 → 免费额度 / API key
- 限额/额度：每日免费条数 + 闲时档；带水印
- 备注：国内可直连；按秒付费
- EN: Shengshu Vidu | platform.vidu.com
  Key: Register -> Free quota / API key | Limits: Daily free generations + off-peak tier; includes watermark | Notes: Pay-per-second pricing
### 阿里 通义万相 Wan
- 官方接入：create.wan.video
- 获取 Key：每日签到领 10 分；API 走百炼
- 限额/额度：约 1 条/日（720p/5s）；百炼新户免费秒数
- 备注：国内可直连；签到制
- EN: Alibaba Tongyi Wan | create.wan.video
  Key: Daily check-in for 10 points; API via Bailian | Limits: Approx. 1 generation/day (720p/5s); free seconds for new Bailian users | Notes: Check-in system
### Google Veo / Gemini Omni / Flow
- 官方接入：flow.google.com
- 获取 Key：注册 Google 账号 → Flow；API 走 ai.google.dev
- 限额/额度：免费 50 分/日（Veo 3.1 Lite）
- 备注：部分地区需代理；免费带水印
- EN: Google Veo / Gemini Omni / Flow | flow.google.com
  Key: Register Google account -> Flow; API via ai.google.dev | Limits: 50 free points/day (Veo 3.1 Lite) | Notes: Free generations include watermark
### Runway（Gen-4）
- 官方接入：runway.com
- 获取 Key：注册 → 一次性 125 分；API 需付费
- 限额/额度：一次性 125 分（非每日）
- 备注：需代理；专业向
- EN: Runway (Gen-4) | runway.com
  Key: Register -> One-time 125 credits; API requires paid plan | Limits: One-time 125 credits (not daily) | Notes: Professional orientation
### Luma AI（Ray）
- 官方接入：lumalabs.ai
- 获取 Key：登录 Luma → 每日免费积分
- 限额/额度：每日免费条数（以官网为准，带水印）
- 备注：需代理
- EN: Luma AI (Ray) | lumalabs.ai
  Key: Log in to Luma -> Daily free points | Limits: Daily free generations (subject to official site, with watermark) | Notes: 
### Pika
- 官方接入：pika.art
- 获取 Key：登录 Pika → 每日免费积分
- 限额/额度：每日免费条数（以官网为准，带水印）
- 备注：需代理
- EN: Pika | pika.art
  Key: Log in to Pika -> Daily free points | Limits: Daily free generations (subject to official site, with watermark) | Notes: 
### Pixverse
- 官方接入：pixverse.ai
- 获取 Key：登录 Pixverse → 每日免费积分
- 限额/额度：每日免费条数（以官网为准，带水印）
- 备注：需代理
- EN: Pixverse | pixverse.ai
  Key: Log in to Pixverse -> Daily free points | Limits: Daily free generations (subject to official site, with watermark) | Notes: 
### Haiper
- 官方接入：haiper.ai
- 获取 Key：登录 Haiper → 每日免费积分
- 限额/额度：每日免费条数（以官网为准，带水印）
- 备注：需代理
- EN: Haiper | haiper.ai
  Key: Log in to Haiper -> Daily free points | Limits: Daily free generations (subject to official site, with watermark) | Notes: 

## 免费生图 / Free Image Generation

### Stability AI
- 官方接入：platform.stability.ai
- 获取 Key：注册（建议 Google 登录才到账）→ 25 分
- 限额/额度：注册 25 分（约 3–10 张），无持续免费额度
- 备注：需代理；之后按量付费
- EN: Stability AI | platform.stability.ai
  Key: Register (Google login recommended for credit) -> 25 credits | Limits: 25 credits upon registration (approx. 3-10 images), no recurring free quota | Notes: Pay-per-use after trial
### FLUX（Black Forest Labs）
- 官方接入：fal.ai/models/black-forest-labs
- 获取 Key：经 fal.ai / Hugging Face Spaces 免费调用 schnell
- 限额/额度：FLUX.1 schnell 常免费（每日额度，需排队）
- 备注：需代理；开源权重可本地
- EN: FLUX (Black Forest Labs) | fal.ai/models/black-forest-labs
  Key: Call schnell via fal.ai / Hugging Face Spaces for free | Limits: FLUX.1 schnell often free (daily quota, queue required) | Notes: Open-source weights available for local use
### Google Imagen / Nano Banana
- 官方接入：ai.google.dev
- 获取 Key：AI Studio → Get API key
- 限额/额度：免费层可调用图像生成（限额小）
- 备注：部分需代理
- EN: Google Imagen / Nano Banana | ai.google.dev
  Key: AI Studio -> Get API key | Limits: Image generation available in free tier (low limits) | Notes: 
### Meta AI（Muse Image）
- 官方接入：meta.ai
- 获取 Key：登录 Meta 账号即可
- 限额/额度：每日免费额度（不公布具体数）
- 备注：移动端为主
- EN: Meta AI (Muse Image) | meta.ai
  Key: Log in with Meta account | Limits: Daily free quota (specific numbers not public) | Notes: Mobile-centric
### Leonardo
- 官方接入：app.leonardo.ai
- 获取 Key：登录 Leonardo → 每日免费 token
- 限额/额度：每日免费额度（以官网为准，需刷新）
- 备注：需代理；免费档够用
- EN: Leonardo | app.leonardo.ai
  Key: Log in to Leonardo -> Daily free tokens | Limits: Daily free quota (subject to official site, requires refresh) | Notes: Free tier is sufficient
### Ideogram
- 官方接入：ideogram.ai
- 获取 Key：登录 Ideogram → 每日免费额度
- 限额/额度：每日免费张数（以官网为准，带水印）
- 备注：需代理；文字渲染强
- EN: Ideogram | ideogram.ai
  Key: Log in to Ideogram -> Daily free quota | Limits: Daily free images (subject to official site, with watermark) | Notes: Strong text rendering
### Krea
- 官方接入：krea.ai
- 获取 Key：登录 Krea → 每日免费积分
- 限额/额度：每日免费积分（以官网为准）
- 备注：需代理
- EN: Krea | krea.ai
  Key: Log in to Krea -> Daily free points | Limits: Daily free points (subject to official site) | Notes: 
### Playground
- 官方接入：playground.com
- 获取 Key：登录 Playground → 免费额度
- 限额/额度：免费生成额度（以官网为准，可商用免费档）
- 备注：需代理
- EN: Playground | playground.com
  Key: Log in to Playground -> Free quota | Limits: Free generation quota (subject to official site, free commercial tier available) | Notes: 
### Microsoft Designer（Bing Image）
- 官方接入：designer.microsoft.com
- 获取 Key：登录 Microsoft 账号
- 限额/额度：每日免费额度（以官网为准）
- 备注：需代理；免注册门槛低
- EN: Microsoft Designer (Bing Image) | designer.microsoft.com
  Key: Log in with Microsoft account | Limits: Daily free quota (subject to official site) | Notes: Low barrier to entry
### LiblibAI（哩布哩布）
- 官方接入：liblib.art
- 获取 Key：登录 → 每日免费算力
- 限额/额度：每日免费算力（生图，以官网为准）
- 备注：国内可直连；国内模型社区
- EN: LiblibAI | liblib.art
  Key: Log in -> Daily free compute | Limits: Daily free compute for image generation (subject to official site) | Notes: Domestic model community

## 高性价比生视频 / Cost-Effective Video

### 字节 Seedance 2.x（火山）
- 官方接入：volcengine.com/ark
- 获取 Key：开通火山方舟 → API key
- 限额/额度：按秒付费（实抓价见下方·官网）
- 备注：国内可直连；性价比看分辨率/时长
- EN: ByteDance Seedance 2.x (Volcano) | volcengine.com/ark
  Key: Activate Volcano Ark -> API key | Limits: Pay-per-second (see official site for current pricing) | Notes: Cost-effectiveness depends on resolution/duration
- 单条价：⚠️ unverified（https://www.volcengine.com/product/ark 实抓未命中）
### 阿里 万相 Wan 3.0（百炼）
- 官方接入：bailian.console.aliyun.com
- 获取 Key：百炼 API key
- 限额/额度：分分辨率按量；新户免费秒数
- 备注：国内可直连
- EN: Alibaba Wan 3.0 (Bailian) | bailian.console.aliyun.com
  Key: Bailian API key | Limits: Pay-per-use by resolution; free seconds for new users | Notes: 
- 单条价：⚠️ unverified（https://help.aliyun.com/zh/model-studio/billing-of-model-studio 实抓未命中）
### 快手 Kling（分分辨率价）
- 官方接入：app.klingai.com 开发者定价
- 获取 Key：开发者中心 API key
- 限额/额度：分分辨率按量（实抓价见下方·官网）
- 备注：国内可直连
- EN: Kuaishou Kling (By Resolution) | app.klingai.com developer pricing
  Key: Developer Center API key | Limits: Pay-per-use by resolution (see official site for current pricing) | Notes: 
- 实抓价目（节选，最低档起）：$1、$2（https://klingai.com/app/pricing，as of 2026-11-13）

## 高性价比生图 / Cost-Effective Image

### xAI Grok Imagine
- 官方接入：console.x.ai
- 获取 Key：xAI 控制台 → API key
- 限额/额度：按张付费（便宜档）
- 备注：需代理
- EN: xAI Grok Imagine | console.x.ai
  Key: xAI Console -> API key | Limits: Pay-per-image (low-cost tier) | Notes: 
- 实抓价目（节选，最低档起）：$0.02、$0.08、$0.1、$0.2（https://docs.x.ai/，as of 2026-11-13）
### fal.ai（开源图/视频托管）
- 官方接入：fal.ai
- 获取 Key：注册 → API key；有试用额度
- 限额/额度：开源模型按量极便宜（实抓价见下方）
- 备注：需代理；开源模型最便宜档
- EN: fal.ai (Open-source Image/Video Hosting) | fal.ai
  Key: Register -> API key; has trial credit | Limits: Open-source models are very cheap pay-per-use (see below for current pricing) | Notes: Cheapest tier for open-source models
- 实抓价目（节选，最低档起）：$0.0002、$0.002、$0.003、$0.005（https://fal.ai/pricing，as of 2026-11-13）
### Together / Novita（便宜推理）
- 官方接入：api.together.ai · novita.ai
- 获取 Key：注册 → API key
- 限额/额度：开源模型按量，极便宜
- 备注：需代理
- EN: Together / Novita (Cheap Inference) | api.together.ai, novita.ai
  Key: Register -> API key | Limits: Open-source models pay-per-use, very cheap | Notes: 
- 实抓价目（节选，最低档起）：$0、$0.0015、$0.0017、$0.0019（https://www.together.ai/pricing，as of 2026-11-13）
### 硅基流动（国产便宜档）
- 官方接入：api.siliconflow.cn
- 获取 Key：注册 → API 密钥
- 限额/额度：开源模型按量；部分免费
- 备注：国内可直连
- EN: SiliconFlow (Domestic Budget Tier) | api.siliconflow.cn
  Key: Register -> API Key | Limits: Open-source models pay-per-use; some free | Notes: 
- 实抓价目（节选，最低档起）：$6、$7、$11（https://cloud.siliconflow.cn/pricing，as of 2026-11-13）
### Replicate（便宜推理）
- 官方接入：replicate.com
- 获取 Key：注册 → API tokens
- 限额/额度：按量计费（开源模型极便宜；以官网为准）
- 备注：需代理；托管大量开源图/视频模型
- EN: Replicate (Cheap Inference) | replicate.com
  Key: Register -> API tokens | Limits: Pay-per-use (open-source models very cheap; subject to official site) | Notes: Hosts many open-source image/video models