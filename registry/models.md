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
  Key: Register Google Account → AI Studio → Get API key | Limits: Free tier: Gemini Flash/Flash-Lite, RPM 5–15, daily limits for some models | Notes: Free tier data may be used for training; no credit card required
### Groq
- 官方接入：console.groq.com/keys
- 获取 Key：Groq 控制台 → Keys → 新建
- 限额/额度：免费层：30 RPM / 1000 次/日（gpt-oss-120b）
- 备注：速度最快（LPU）；免信用卡；商用可用
- EN: Groq | console.groq.com/keys
  Key: Groq Console → Keys → Create New | Limits: Free tier: 30 RPM / 1000 requests/day (gpt-oss-120b) | Notes: Fastest speed (LPU); no credit card required; commercial use allowed
### 智谱 Z.ai / GLM
- 官方接入：open.bigmodel.cn
- 获取 Key：注册 → 用户中心 → API keys
- 限额/额度：GLM-4.7-Flash 免费，1 并发；新用户 2000万 token 体验包
- 备注：国内可直连；chat API 免实名（Batch 需实名）；国际站 api.z.ai
- EN: Zhipu Z.ai / GLM | open.bigmodel.cn
  Key: Register → User Center → API Keys | Limits: GLM-4.7-Flash free, 1 concurrent request; 20M token trial pack for new users | Notes: International site: api.z.ai
### 硅基流动 SiliconFlow
- 官方接入：cloud.siliconflow.cn
- 获取 Key：注册 → 账号 → API 密钥
- 限额/额度：新用户 2000万 token；部分开源模型永久免费
- 备注：国内可直连；免费模型需实名认证；响应快
- EN: SiliconFlow | cloud.siliconflow.cn
  Key: Register → Account → API Keys | Limits: 20M tokens for new users; some open-source models are permanently free | Notes: Fast response times
### 阿里百炼（通义）
- 官方接入：bailian.console.aliyun.com
- 获取 Key：开通百炼 → 授权 → 新建 API key
- 限额/额度：新用户每模型约 100万 token，90 天有效
- 备注：国内可直连；模型最全（Qwen + 第三方）
- EN: Alibaba Bailian (Tongyi) | bailian.console.aliyun.com
  Key: Activate Bailian → Authorization → Create API key | Limits: Approx. 1M tokens per model for new users, valid for 90 days | Notes: Most comprehensive model catalog (Qwen + third-party)
### OpenRouter（免费池）
- 官方接入：openrouter.ai/keys
- 获取 Key：注册 → Keys → 新建（单 key 多模型）
- 限额/额度：:free 模型 20 RPM / 50 次/日；充 10 美元后 1000 次/日
- 备注：免信用卡；自动路由多厂商；免费模型每日轮换（脚本实抓）
- EN: OpenRouter (Free Pool) | openrouter.ai/keys
  Key: Register → Keys → Create New (single key for multiple models) | Limits: :free models: 20 RPM / 50 requests/day; 1000 requests/day after $10 deposit | Notes: No credit card required; automatic routing across multiple vendors; free models rotate daily
### Mistral（La Plateforme）
- 官方接入：console.mistral.ai
- 获取 Key：注册 → API keys
- 限额/额度：免费模式（Experiment）：约 1B token/月，限流看后台
- 备注：API 数据不用于训练；免信用卡
- EN: Mistral (La Plateforme) | console.mistral.ai
  Key: Register → API Keys | Limits: Free Mode (Experiment): ~1B tokens/month, rate limits via dashboard | Notes: API data not used for training; no credit card required
### Cerebras
- 官方接入：cloud.cerebras.ai
- 获取 Key：注册 → 加一次支付方式 → 免费 credit
- 限额/额度：$5 试用 credit，30 天过期；吞吐极高
- 备注：需加卡（仅试用）
- EN: Cerebras | cloud.cerebras.ai
  Key: Register → Add Payment Method → Free Credit | Limits: $5 trial credit, expires in 30 days; very high throughput | Notes: Credit card required (for trial only)
### NVIDIA NIM
- 官方接入：build.nvidia.com
- 获取 Key：注册 NVIDIA Developer 计划 → 领 NIM key
- 限额/额度：100+ 开源模型，限流按模型动态（无公开表）
- 备注：原型/研究用；生产需 NVIDIA AI Enterprise 授权
- EN: NVIDIA NIM | build.nvidia.com
  Key: Register for NVIDIA Developer Program → Claim NIM key | Limits: 100+ open-source models, dynamic rate limits per model (no public table) | Notes: For prototyping/research; production use requires NVIDIA AI Enterprise license
### Together AI
- 官方接入：api.together.ai
- 获取 Key：注册 → Settings → API keys
- 限额/额度：免费额度常变动（多为小额试用）
- 备注：开源模型托管便宜档
- EN: Together AI | api.together.ai
  Key: Register → Settings → API Keys | Limits: Free credits vary frequently (usually small trial amounts) | Notes: Affordable hosting for open-source models
### 科大讯飞星火
- 官方接入：open-platform.xfyun.cn
- 获取 Key：注册 → 控制台 → 申请 APIKey
- 限额/额度：每模型约 20万 token 免费
- 备注：国内可直连
- EN: iFlytek Spark | open-platform.xfyun.cn
  Key: Register → Console → Apply for APIKey | Limits: Approx. 200k tokens free per model | Notes: 

## 免费生视频 / Free Video Generation

### 实抓：Hugging Face 最新文生视频模型

- `netprojects/Cosmos3-Edge-Omni-mlx-bf16` (0 👍) [2026-11-07]
- `netprojects/Cosmos3-Edge-Omni-mlx-8bit` (0 👍) [2026-11-07]
- `Lilgarca/my-model-v02` (0 👍) [2026-11-07]
- `nemoyu/nlp-chapter6-nextgpt-models` (0 👍) [2026-11-06]
- `Lilgarca/my-model-v01` (2 👍) [2026-11-06]
- `Wenwu2000/ReSeed` (0 👍) [2026-11-02]
- `AtlasAI-official/Quasar` (1 👍) [2026-10-21]
- `shreshthsaini/Rectified-CFGpp` (0 👍) [2026-10-13]
- `AhmadRH/PACT` (1 👍) [2026-10-12]
- `muhammad-taqi512/LYRA-ANY` (0 👍) [2026-10-04]
- `bomehika/oelala-loras` (1 👍) [2026-10-01]
- `SOLRICKS/Mila` (1 👍) [2026-08-10]
- `lightx2v/LightLingBot-Video` (13 👍) [2026-07-28]
- `MLXCreator/MLX-Creator` (0 👍) [2026-06-26]
- `CCSSNE/CyberNeurova-Lance-3B-abliterated` (0 👍) [2026-06-23]
- `BasinShapers/Cosmos3-Nano-MLX` (1 👍) [2026-06-19]
- `SceneWorks/bernini-mlx` (0 👍) [2026-06-14]
- `prometheusAIR/Cosmos3-Super-NVFP4` (0 👍) [2026-06-10]
- `prometheusAIR/Cosmos3-Super-FP8` (2 👍) [2026-06-10]
- `SanDiegoDude/Cosmos3-Super-nf4` (4 👍) [2026-06-02]

### 快手 Kling（可灵）
- 官方接入：app.klingai.com
- 获取 Key：登录 → 开发者中心 → API key
- 限额/额度：免费 66 分/日（登录发放）；免费 5s/720p 带水印
- 备注：国内可直连；免费层禁商用；登录需手机号
- EN: Kuaishou Kling | app.klingai.com
  Key: Login → Developer Center → API key | Limits: 66 credits/day free (awarded upon login); free 5s/720p with watermark | Notes: Commercial use prohibited on free tier
### MiniMax Hailuo（海螺）
- 官方接入：hailuoai.video
- 获取 Key：注册 → 领免费额度 / 官方 API key
- 限额/额度：每日免费若干条；免费 720p
- 备注：国内可直连；免费带水印
- EN: MiniMax Hailuo | hailuoai.video
  Key: Register → Claim free credits / Official API key | Limits: Several free clips daily; free 720p | Notes: Free tier includes watermarks
### 字节 即梦 / Dreamina / Seedance
- 官方接入：jimeng.jianying.com
- 获取 Key：注册即梦 → 生成；API 走火山方舟
- 限额/额度：免费每日积分（地域差异，美区约 120/日）
- 备注：国内可直连；免费带水印；Seedance 走 API 付费
- EN: ByteDance Jimeng / Dreamina / Seedance | jimeng.jianying.com
  Key: Register for Jimeng → Generate; API via Volcano Ark | Limits: Free daily credits (varies by region, ~120/day in US) | Notes: Free tier includes watermarks; Seedance API is paid
### 生数 Vidu
- 官方接入：platform.vidu.com
- 获取 Key：注册 → 免费额度 / API key
- 限额/额度：每日免费条数 + 闲时档；带水印
- 备注：国内可直连；按秒付费
- EN: Shengshu Vidu | platform.vidu.com
  Key: Register → Free credits / API key | Limits: Daily free clips + off-peak tier; includes watermark | Notes: Pay-per-second
### 阿里 通义万相 Wan
- 官方接入：create.wan.video
- 获取 Key：每日签到领 10 分；API 走百炼
- 限额/额度：约 1 条/日（720p/5s）；百炼新户免费秒数
- 备注：国内可直连；签到制
- EN: Alibaba Tongyi Wan | create.wan.video
  Key: Daily check-in for 10 credits; API via Bailian | Limits: Approx. 1 clip/day (720p/5s); free seconds for new Bailian users | Notes: Check-in system
### Google Veo / Gemini Omni / Flow
- 官方接入：flow.google.com
- 获取 Key：注册 Google 账号 → Flow；API 走 ai.google.dev
- 限额/额度：免费 50 分/日（Veo 3.1 Lite）
- 备注：部分地区需代理；免费带水印
- EN: Google Veo / Gemini Omni / Flow | flow.google.com
  Key: Register Google Account → Flow; API via ai.google.dev | Limits: 50 credits/day free (Veo 3.1 Lite) | Notes: Free tier includes watermarks
### Runway（Gen-4）
- 官方接入：runway.com
- 获取 Key：注册 → 一次性 125 分；API 需付费
- 限额/额度：一次性 125 分（非每日）
- 备注：需代理；专业向
- EN: Runway (Gen-4) | runway.com
  Key: Register → One-time 125 credits; API requires payment | Limits: One-time 125 credits (not daily) | Notes: Professional focus

## 免费生图 / Free Image Generation

### Stability AI
- 官方接入：platform.stability.ai
- 获取 Key：注册（建议 Google 登录才到账）→ 25 分
- 限额/额度：注册 25 分（约 3–10 张），无持续免费额度
- 备注：需代理；之后按量付费
- EN: Stability AI | platform.stability.ai
  Key: Register (Google login recommended) → 25 credits | Limits: 25 credits on registration (~3–10 images), no recurring free credits | Notes: Pay-per-use after registration
### FLUX（Black Forest Labs）
- 官方接入：fal.ai/models/black-forest-labs
- 获取 Key：经 fal.ai / Hugging Face Spaces 免费调用 schnell
- 限额/额度：FLUX.1 schnell 常免费（每日额度，需排队）
- 备注：需代理；开源权重可本地
- EN: FLUX (Black Forest Labs) | fal.ai/models/black-forest-labs
  Key: Call schnell free via fal.ai / Hugging Face Spaces | Limits: FLUX.1 schnell often free (daily quota, queue required) | Notes: Open-source weights available for local use
### Google Imagen / Nano Banana
- 官方接入：ai.google.dev
- 获取 Key：AI Studio → Get API key
- 限额/额度：免费层可调用图像生成（限额小）
- 备注：部分需代理
- EN: Google Imagen / Nano Banana | ai.google.dev
  Key: AI Studio → Get API key | Limits: Free tier allows image generation (low limits) | Notes: 
### Meta AI（Muse Image）
- 官方接入：meta.ai
- 获取 Key：登录 Meta 账号即可
- 限额/额度：每日免费额度（不公布具体数）
- 备注：移动端为主
- EN: Meta AI (Muse Image) | meta.ai
  Key: Login with Meta Account | Limits: Daily free quota (exact number not disclosed) | Notes: Mobile-focused

## 高性价比生视频 / Cost-Effective Video

### 字节 Seedance 2.x（火山）
- 官方接入：volcengine.com/ark
- 获取 Key：开通火山方舟 → API key
- 限额/额度：按秒付费（约 $0.3/s 档）；质量高
- 备注：国内可直连；性价比看分辨率/时长
- EN: ByteDance Seedance 2.x (Volcano) | volcengine.com/ark
  Key: Activate Volcano Ark → API key | Limits: Pay-per-second (~$0.3/s tier); high quality | Notes: Cost-effectiveness depends on resolution/duration
### 阿里 万相 Wan 3.0（百炼）
- 官方接入：bailian.console.aliyun.com
- 获取 Key：百炼 API key
- 限额/额度：分分辨率按量；新户免费秒数
- 备注：国内可直连
- EN: Alibaba Wan 3.0 (Bailian) | bailian.console.aliyun.com
  Key: Bailian API key | Limits: Pay-per-use by resolution; free seconds for new users | Notes: 
### 快手 Kling（分分辨率价）
- 官方接入：app.klingai.com 开发者定价
- 获取 Key：开发者中心 API key
- 限额/额度：约 $0.10/s（标准），更高档更贵
- 备注：国内可直连
- EN: Kuaishou Kling (Resolution-based pricing) | app.klingai.com developer pricing
  Key: Developer Center API key | Limits: ~$0.10/s (standard), higher tiers cost more | Notes: 

## 高性价比生图 / Cost-Effective Image

### xAI Grok Imagine
- 官方接入：console.x.ai
- 获取 Key：xAI 控制台 → API key
- 限额/额度：按张付费（便宜档）
- 备注：需代理
- EN: xAI Grok Imagine | console.x.ai
  Key: xAI Console → API key | Limits: Pay-per-image (budget tier) | Notes: 
### fal.ai（开源图/视频托管）
- 官方接入：fal.ai/pricing
- 获取 Key：注册 → API key；有试用额度
- 限额/额度：FLUX/Stable 等约 $0.001–0.01/张；视频按秒
- 备注：需代理；开源模型最便宜档
- EN: fal.ai (Open-source Image/Video Hosting) | fal.ai/pricing
  Key: Register → API key; trial credits available | Limits: FLUX/Stable etc. ~$0.001–0.01/image; video pay-per-second | Notes: Most affordable tier for open-source models
### Together / Novita（便宜推理）
- 官方接入：api.together.ai · novita.ai
- 获取 Key：注册 → API key
- 限额/额度：开源模型按量，极便宜
- 备注：需代理
- EN: Together / Novita (Budget Inference) | api.together.ai · novita.ai
  Key: Register → API key | Limits: Pay-per-use for open-source models, very cheap | Notes: 
### 硅基流动（国产便宜档）
- 官方接入：api.siliconflow.cn
- 获取 Key：注册 → API 密钥
- 限额/额度：开源模型按量；部分免费
- 备注：国内可直连
- EN: SiliconFlow (Budget Tier) | api.siliconflow.cn
  Key: Register → API Key | Limits: Pay-per-use for open-source models; some free | Notes: 