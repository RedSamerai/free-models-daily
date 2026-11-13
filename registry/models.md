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
  Key: Register Google account → AI Studio → Get API key | Limits: Free tier: Gemini Flash/Flash-Lite, 5-15 RPM, some models have daily limits | Notes: Free tier data may be used for training; No credit card required
### Groq
- 官方接入：console.groq.com/keys
- 获取 Key：Groq 控制台 → Keys → 新建
- 限额/额度：免费层：30 RPM / 1000 次/日（gpt-oss-120b）
- 备注：速度最快（LPU）；免信用卡；商用可用
- EN: Groq | console.groq.com/keys
  Key: Groq Console → Keys → Create new | Limits: Free tier: 30 RPM / 1000 requests/day (gpt-oss-120b) | Notes: Fastest speed (LPU); No credit card required; Commercial use allowed
### 智谱 Z.ai / GLM
- 官方接入：open.bigmodel.cn
- 获取 Key：注册 → 用户中心 → API keys
- 限额/额度：GLM-4.7-Flash 免费，1 并发；新用户 2000万 token 体验包
- 备注：国内可直连；chat API 免实名（Batch 需实名）；国际站 api.z.ai
- EN: Zhipu Z.ai / GLM | open.bigmodel.cn
  Key: Register → User Center → API Keys | Limits: GLM-4.7-Flash is free, 1 concurrent request; 20M token trial for new users | Notes: International site: api.z.ai
### 硅基流动 SiliconFlow
- 官方接入：cloud.siliconflow.cn
- 获取 Key：注册 → 账号 → API 密钥
- 限额/额度：新用户 2000万 token；部分开源模型永久免费
- 备注：国内可直连；免费模型需实名认证；响应快
- EN: SiliconFlow | cloud.siliconflow.cn
  Key: Register → Account → API Keys | Limits: 20M tokens for new users; Some open-source models are permanently free | Notes: Fast response
### 阿里百炼（通义）
- 官方接入：bailian.console.aliyun.com
- 获取 Key：开通百炼 → 授权 → 新建 API key
- 限额/额度：新用户每模型约 100万 token，90 天有效
- 备注：国内可直连；模型最全（Qwen + 第三方）
- EN: Alibaba Bailian (Tongyi) | bailian.console.aliyun.com
  Key: Activate Bailian → Authorization → Create new API key | Limits: New users get ~1M tokens per model, valid for 90 days | Notes: Widest model catalog (Qwen + Third-party)
### OpenRouter（免费池）
- 官方接入：openrouter.ai/keys
- 获取 Key：注册 → Keys → 新建（单 key 多模型）
- 限额/额度：:free 模型 20 RPM / 50 次/日；充 10 美元后 1000 次/日
- 备注：免信用卡；自动路由多厂商；免费模型每日轮换（脚本实抓）
- EN: OpenRouter (Free Pool) | openrouter.ai/keys
  Key: Register → Keys → Create (Single key for multiple models) | Limits: :free models 20 RPM / 50 requests/day; 1000 requests/day after $10 top-up | Notes: No credit card required; Automatic multi-provider routing; Free models rotate daily (based on real-time data)
### Mistral（La Plateforme）
- 官方接入：console.mistral.ai
- 获取 Key：注册 → API keys
- 限额/额度：免费模式（Experiment）：约 1B token/月，限流看后台
- 备注：API 数据不用于训练；免信用卡
- EN: Mistral (La Plateforme) | console.mistral.ai
  Key: Register → API Keys | Limits: Free mode (Experiment): ~1B tokens/month, rate limits depend on dashboard | Notes: API data not used for training; No credit card required
### Cerebras
- 官方接入：cloud.cerebras.ai
- 获取 Key：注册 → 加一次支付方式 → 免费 credit
- 限额/额度：$5 试用 credit，30 天过期；吞吐极高
- 备注：需加卡（仅试用）
- EN: Cerebras | cloud.cerebras.ai
  Key: Register → Add payment method once → Free credit | Limits: $5 trial credit, expires in 30 days; Extremely high throughput | Notes: Requires adding a card (for trial only)
### NVIDIA NIM
- 官方接入：build.nvidia.com
- 获取 Key：注册 NVIDIA Developer 计划 → 领 NIM key
- 限额/额度：100+ 开源模型，限流按模型动态（无公开表）
- 备注：原型/研究用；生产需 NVIDIA AI Enterprise 授权
- EN: NVIDIA NIM | build.nvidia.com
  Key: Register for NVIDIA Developer Program → Get NIM key | Limits: 100+ open-source models, rate limits dynamic per model (no public table) | Notes: For prototyping/research; Production use requires NVIDIA AI Enterprise license
### Together AI
- 官方接入：api.together.ai
- 获取 Key：注册 → Settings → API keys
- 限额/额度：免费额度常变动（多为小额试用）
- 备注：开源模型托管便宜档
- EN: Together AI | api.together.ai
  Key: Register → Settings → API Keys | Limits: Free credits vary frequently (mostly small trial amounts) | Notes: Budget tier for open-source model hosting
### AGNES AI Hub
- 官方接入：apihub.agnes-ai.com/v1
- 获取 Key：注册 agnes-ai.com → 领 API key
- 限额/额度：免费层含 agnes-flash 系列（具体免费模型/额度以官网为准）
- 备注：国内可直连；本日报的 EN 翻译引擎即 agnes-3.0-flash（同源）
- EN: AGNES AI Hub | apihub.agnes-ai.com/v1
  Key: Register at agnes-ai.com → Get API key | Limits: Free tier includes agnes-flash series (Specific free models/limits subject to official website) | Notes: The EN translation engine for this report is agnes-3.0-flash (same source)
### 科大讯飞星火
- 官方接入：open-platform.xfyun.cn
- 获取 Key：注册 → 控制台 → 申请 APIKey
- 限额/额度：每模型约 20万 token 免费
- 备注：国内可直连
- EN: iFlytek Spark | open-platform.xfyun.cn
  Key: Register → Console → Apply for API Key | Limits: ~200k tokens free per model | Notes: 

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
  Key: Login → Developer Center → API Key | Limits: Free 66 credits/day (issued on login); Free 5s/720p with watermark | Notes: Commercial use prohibited on free tier; Login requires phone number
### MiniMax Hailuo（海螺）
- 官方接入：hailuoai.video
- 获取 Key：注册 → 领免费额度 / 官方 API key
- 限额/额度：每日免费若干条；免费 720p
- 备注：国内可直连；免费带水印
- EN: MiniMax Hailuo | hailuoai.video
  Key: Register → Get free credits / Official API key | Limits: Daily free generations limited; Free 720p | Notes: Free tier includes watermark
### 字节 即梦 / Dreamina / Seedance
- 官方接入：jimeng.jianying.com
- 获取 Key：注册即梦 → 生成；API 走火山方舟
- 限额/额度：免费每日积分（地域差异，美区约 120/日）
- 备注：国内可直连；免费带水印；Seedance 走 API 付费
- EN: ByteDance Jimeng / Dreamina / Seedance | jimeng.jianying.com
  Key: Register Jimeng → Generate; API via Volcano Ark | Limits: Daily free credits (varies by region, ~120/day for US region) | Notes: Free tier includes watermark; Seedance API is paid
### 生数 Vidu
- 官方接入：platform.vidu.com
- 获取 Key：注册 → 免费额度 / API key
- 限额/额度：每日免费条数 + 闲时档；带水印
- 备注：国内可直连；按秒付费
- EN: Shengshu Vidu | platform.vidu.com
  Key: Register → Free credits / API key | Limits: Daily free generations + off-peak tier; Includes watermark | Notes: Pay-per-second
### 阿里 通义万相 Wan
- 官方接入：create.wan.video
- 获取 Key：每日签到领 10 分；API 走百炼
- 限额/额度：约 1 条/日（720p/5s）；百炼新户免费秒数
- 备注：国内可直连；签到制
- EN: Alibaba Tongyi Wanxiang | create.wan.video
  Key: Daily check-in for 10 credits; API via Bailian | Limits: ~1 generation/day (720p/5s); Free seconds for new Bailian users | Notes: Check-in system
### Google Veo / Gemini Omni / Flow
- 官方接入：flow.google.com
- 获取 Key：注册 Google 账号 → Flow；API 走 ai.google.dev
- 限额/额度：免费 50 分/日（Veo 3.1 Lite）
- 备注：部分地区需代理；免费带水印
- EN: Google Veo / Gemini Omni / Flow | flow.google.com
  Key: Register Google account → Flow; API via ai.google.dev | Limits: Free 50 credits/day (Veo 3.1 Lite) | Notes: Free tier includes watermark
### Runway（Gen-4）
- 官方接入：runway.com
- 获取 Key：注册 → 一次性 125 分；API 需付费
- 限额/额度：一次性 125 分（非每日）
- 备注：需代理；专业向
- EN: Runway (Gen-4) | runway.com
  Key: Register → One-time 125 credits; API is paid | Limits: One-time 125 credits (not daily) | Notes: Professional-oriented

## 免费生图 / Free Image Generation

### Stability AI
- 官方接入：platform.stability.ai
- 获取 Key：注册（建议 Google 登录才到账）→ 25 分
- 限额/额度：注册 25 分（约 3–10 张），无持续免费额度
- 备注：需代理；之后按量付费
- EN: Stability AI | platform.stability.ai
  Key: Register (Google login recommended for credit allocation) → 25 credits | Limits: 25 credits on registration (~3–10 images), no ongoing free tier | Notes: Pay-per-use after initial credit
### FLUX（Black Forest Labs）
- 官方接入：fal.ai/models/black-forest-labs
- 获取 Key：经 fal.ai / Hugging Face Spaces 免费调用 schnell
- 限额/额度：FLUX.1 schnell 常免费（每日额度，需排队）
- 备注：需代理；开源权重可本地
- EN: FLUX (Black Forest Labs) | fal.ai/models/black-forest-labs
  Key: Free access to 'schnell' via fal.ai / Hugging Face Spaces | Limits: FLUX.1 schnell often free (daily limit, queuing required) | Notes: Open-source weights available for local use
### Google Imagen / Nano Banana
- 官方接入：ai.google.dev
- 获取 Key：AI Studio → Get API key
- 限额/额度：免费层可调用图像生成（限额小）
- 备注：部分需代理
- EN: Google Imagen / Nano Banana | ai.google.dev
  Key: AI Studio → Get API key | Limits: Free tier allows image generation (small limits) | Notes: 
### Meta AI（Muse Image）
- 官方接入：meta.ai
- 获取 Key：登录 Meta 账号即可
- 限额/额度：每日免费额度（不公布具体数）
- 备注：移动端为主
- EN: Meta AI (Muse Image) | meta.ai
  Key: Login with Meta account | Limits: Daily free quota (specific numbers not published) | Notes: Mobile-first

## 高性价比生视频 / Cost-Effective Video

### 字节 Seedance 2.x（火山）
- 官方接入：volcengine.com/ark
- 获取 Key：开通火山方舟 → API key
- 限额/额度：按秒付费（实抓价见下方·官网）
- 备注：国内可直连；性价比看分辨率/时长
- EN: ByteDance Seedance 2.x (Volcano) | volcengine.com/ark
  Key: Activate Volcano Ark → API key | Limits: Pay-per-second (Real-time prices subject to official website) | Notes: Cost-effectiveness depends on resolution/duration
- 单条价：⚠️ unverified（https://www.volcengine.com/product/ark 实抓未命中）
### 阿里 万相 Wan 3.0（百炼）
- 官方接入：bailian.console.aliyun.com
- 获取 Key：百炼 API key
- 限额/额度：分分辨率按量；新户免费秒数
- 备注：国内可直连
- EN: Alibaba Wanxiang 3.0 (Bailian) | bailian.console.aliyun.com
  Key: Bailian API key | Limits: Pay-per-use by resolution; Free seconds for new users | Notes: 
- 单条价：⚠️ unverified（https://help.aliyun.com/zh/model-studio/billing-of-model-studio 实抓未命中）
### 快手 Kling（分分辨率价）
- 官方接入：app.klingai.com 开发者定价
- 获取 Key：开发者中心 API key
- 限额/额度：分分辨率按量（实抓价见下方·官网）
- 备注：国内可直连
- EN: Kuaishou Kling (Resolution-based pricing) | app.klingai.com Developer Pricing
  Key: Developer Center API key | Limits: Pay-per-use by resolution (Real-time prices subject to official website) | Notes: 
- 实抓价目（节选，最低档起）：$1、$2（https://klingai.com/app/pricing，as of 2026-11-13）

## 高性价比生图 / Cost-Effective Image

### xAI Grok Imagine
- 官方接入：console.x.ai
- 获取 Key：xAI 控制台 → API key
- 限额/额度：按张付费（便宜档）
- 备注：需代理
- EN: xAI Grok Imagine | console.x.ai
  Key: xAI Console → API key | Limits: Pay-per-image (Budget tier) | Notes: 
- 实抓价目（节选，最低档起）：$0.02、$0.08、$0.1、$0.2（https://docs.x.ai/，as of 2026-11-13）
### fal.ai（开源图/视频托管）
- 官方接入：fal.ai
- 获取 Key：注册 → API key；有试用额度
- 限额/额度：开源模型按量极便宜（实抓价见下方）
- 备注：需代理；开源模型最便宜档
- EN: fal.ai (Open-source Image/Video Hosting) | fal.ai
  Key: Register → API key; Has trial credit | Limits: Open-source models are extremely cheap pay-per-use (Real-time prices subject to website) | Notes: Cheapest tier for open-source models
- 实抓价目（节选，最低档起）：$0.0002、$0.002、$0.003、$0.005（https://fal.ai/pricing，as of 2026-11-13）
### Together / Novita（便宜推理）
- 官方接入：api.together.ai · novita.ai
- 获取 Key：注册 → API key
- 限额/额度：开源模型按量，极便宜
- 备注：需代理
- EN: Together / Novita (Cheap Inference) | api.together.ai · novita.ai
  Key: Register → API key | Limits: Open-source models pay-per-use, extremely cheap | Notes: 
- 实抓价目（节选，最低档起）：$0、$0.0015、$0.0017、$0.0019（https://www.together.ai/pricing，as of 2026-11-13）
### 硅基流动（国产便宜档）
- 官方接入：api.siliconflow.cn
- 获取 Key：注册 → API 密钥
- 限额/额度：开源模型按量；部分免费
- 备注：国内可直连
- EN: SiliconFlow (Domestic Budget Tier) | api.siliconflow.cn
  Key: Register → API Keys | Limits: Open-source models pay-per-use; Some free | Notes: 
- 实抓价目（节选，最低档起）：$6、$7、$11（https://cloud.siliconflow.cn/pricing，as of 2026-11-13）