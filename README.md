# 📡 free-models-daily

**免费 · 高性价比 AI 模型 API 与开源模型 —— 双语活索引（ZH / EN）**
*Free & cost-effective AI model APIs and open-source models — a bilingual, auto-maintained digest.*

---

## 这是什么 / What this is

一份**持续自动更新**的「免费层 · 高性价比 · 开源可本地」AI 模型清单，中英双语。
A continuously auto-refreshed, bilingual digest of **free-tier, cost-effective, and open-source / local** AI models.

- 每条都带**可点来源 + 数据日期（as-of）**；验活失败即标 ⚠️，绝不臆造。
- 没有更新的当天**不产生提交**，历史只保留真实变更。
- 性价比层的**单价实时抓自官方定价页**，抓不到就标 ⚠️，不写死数字。

- Every entry carries a **clickable source + as-of date**; anything unverifiable is marked ⚠️, never invented.
- Days with no change produce **no commit** — history stays clean.
- Cost-effective unit prices are **live-scraped from official pricing pages**; unscrapable values show ⚠️, never hard-coded.

## 内容板块 / Sections

| 板块 | 收录 | Layer |
|---|---|---|
| 免费 LLM | 无需信用卡 / 大额长期免费额度 | Free LLM APIs |
| 免费生视频 | 真免费层（每日积分 / 闲时） | Free video generation |
| 免费生图 | 真免费层生图 API | Free image generation |
| 高性价比生视频 / 生图 | 便宜档，**单价实抓官方定价页** | Cost-effective video / image |
| 开源可本地 | 开源权重（Hugging Face 实抓 + GitHub 策展 release） | Open-source / self-host |

Six layers, all bilingual. The two cost-effective layers carry **live unit prices** scraped from official pricing pages.

## 怎么读 / Where to start

1. **全量活索引** → [`registry/models.md`](registry/models.md)（最新、最全、双语）
2. **逐日变更** → `daily/`（每篇只列当天新增，作 changelog）
3. **数据来源** → [`sources.md`](sources.md)

1. **Full living index** → [`registry/models.md`](registry/models.md) (newest, most complete, bilingual)
2. **Daily changelog** → `daily/` (each file lists only that day's additions)
3. **Data sources** → [`sources.md`](sources.md)

<!-- LATEST_DAILY -->
> 📄 最近更新 / Latest changelog：[`daily/2026-11-13.md`](daily/2026-11-13.md)
<!-- /LATEST_DAILY -->

## 更新节奏 / Update cadence

- **每日**（北京时间 03:00）自动实抓 → diff → 渲染 → 提交；无变更则跳过。
- **每周**（周一 03:30）web 兜底搜**新厂商**，官网活验通过后才录入。

- **Daily** (03:00 UTC+8): auto-scrape → diff → render → commit; skips no-change days.
- **Weekly** (Mon 03:30): a web sweep discovers new vendors, added only after liveness-verification.

## 信任模型 / Trust model

**只认活抓信号，禁止 LLM 回忆** —— 并购 / 停服 / 参数规模，必须来自当天**实际抓到**的官方 changelog / blog / API，否则不进清单。
*Live-scraped signals only — no LLM-recalled facts. M&A / shutdowns / model parameters must come from same-day, actually-fetched official changelogs / blogs / APIs, or they don't make the list.*

---

<p align="center"><sub>由纯 Python 标准库 pipeline + 定时任务自动维护 · 双语正文中 EN 部分由模型现场翻译，并自动剔除仅面向中国读者的备注。<br/>Auto-maintained by a stdlib-Python pipeline and cron jobs; English is translated on the fly and stripped of China-only notes.</sub></p>
