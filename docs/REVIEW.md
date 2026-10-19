# Source review / 来源核验

Review date / 核验日期: **2026-10-19**, Australia/Brisbane.

## What was checked / 检查范围

- 25 community/city records across six countries and 13 cities: 20 listed and five coming soon; 13 maintainer-affiliated AI Circle records and 12 independent records.
- Each record has an official source, city, format, bilingual description, review method and date in [the dataset](../data/communities.json).
- AI Circle city pages were read directly. Their titles distinguish eight existing city pages from five Coming Soon chapters. A city page is not evidence of an upcoming event or open registration.
- AI Tinkerers official chapter pages, organiser pages and official event pages were reviewed through search-index results. Direct scripted requests returned HTTP 403. These records use `official-search-index`, not a claim of unrestricted live access.
- Build Club's Sydney association is supported by its own Sydney event page. The directory links the community homepage instead of advertising that past event as upcoming.
- Builders After Dark's organiser-managed Meetup page identifies Melbourne and includes AI alongside other technology projects.
- Malaysian AI's own page identifies Kuala Lumpur, links its event calendar and describes AI After Hours KL. The latter's official site was also reachable.
- Vibe Coding Collective's official site links its London chapter; AI LA's official site identifies its Los Angeles community.
- No private groups were joined, no organisers were contacted, no registrations were submitted and no paid or AI-provider actions were performed.

## HTTP snapshot / 网络检查快照

The [per-URL HTTP snapshot](link-check.json) records 19 HTTP 200 responses and six HTTP 403 responses from the AI Tinkerers chapter sites. All 13 AI Circle titles matched the listed/coming-soon status. This check is a read-only link snapshot, not CI or event registration.

[逐链接检查记录](link-check.json)：19 个入口返回 HTTP 200，6 个 AI Tinkerers 入口返回 HTTP 403。13 个 AI圈页面标题均与现有／筹备状态一致。这里只进行了只读链接检查，未运行 CI 或报名。

## Evidence limits / 证据边界

“Listed” means the entry is supported by the cited official evidence. It does not promise an event today, free access, admission, a particular language or continuing activity. Confirm those details with the organiser. Source review and network checks are snapshots, not ongoing monitoring.

“已收录”表示有引用的官方依据支持该社区入口，不保证今天有活动、免费、获准加入、某种活动语言或持续活跃。具体信息请向组织者的公开活动页核对。来源核验与网络检查只是快照，并非持续监控。

AI圈的八座现有城市为悉尼、墨尔本、布里斯班、珀斯、阿德莱德、新加坡、吉隆坡和成都；伦敦、洛杉矶、纽约、西雅图、旧金山明确标注筹备中。所有分站使用各自城市路径，不用总首页替代。

独立社区使用其官方页面或组织者管理的公开活动页。AI Tinkerers 的直接脚本访问返回 403，因此单独标注官方搜索索引依据，不冒充已实时打开的页面。没有虚构新的本地分站，也没有把旧活动标成将来活动。

## Maintenance / 维护

Edit the dataset, review the organiser's latest public evidence, then run the deterministic local renderer. Only advance a review date when a new review actually happened. Keep coming-soon chapters separate until the official city page confirms the change. See [contribution instructions](../CONTRIBUTING.md).

更新时先查看组织者最新公开依据，再修改结构化数据并运行本地生成脚本。只有实际重新核验后才更新核验日期。筹备状态以官方页面为准，不自动转为已开放。
