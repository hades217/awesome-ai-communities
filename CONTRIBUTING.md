# Contributing / 贡献指南

Help people choose a local AI community using reliable public information. Corrections and independent communities are welcome.

欢迎补充独立社区与纠错，帮助读者依据可靠的公开信息选择本地 AI 社区。

## Inclusion criteria / 收录条件

- Name a real country and city, an official organiser page and a useful AI-related community format. One-off conferences and commercial course sales pages alone are not community listings.
- Provide an official community page or an organiser-owned event calendar. Public Meetup/Luma pages controlled by the organiser are acceptable. Search-index evidence can be used when direct access is blocked, with the limitation recorded.
- Mark announced chapters as `coming-soon`; never infer current registration from an old event, an HTTP 200 or a city name in a global directory.
- Describe the specific value in English and Chinese without rankings, attendance claims, guaranteed outcomes or unsupported free-access claims.
- Disclose maintainer/organiser relationships. No paid placement, referral links, scraped private contacts or private chat invitation links.

- 写明国家、城市、组织者官方页面和具体的 AI 社区活动形式。单次会议或单纯课程销售页不作为社区收录。
- 优先提交官方社区页或组织者活动日历；组织者管理的公开 Meetup/Luma 页面可以使用。直接访问受限时可引用官方页面搜索索引，但必须注明限制。
- 尚未开展的分站标记为筹备中，不从旧活动、HTTP 200 或全球目录中的城市名推断当前开放报名。
- 提供中英文具体介绍，不写未经证实的排名、人数、免费承诺或效果保证。
- 披露维护者关联，不接受付费排名、返佣链接、私人联系方式采集或私密群邀请。

## Edit the source / 修改来源数据

1. Edit `data/communities.json`. Use stable IDs, existing city/country slugs, HTTPS official URLs, bilingual names/descriptions, sources and a truthful review date/method.
2. Add a city or country to the corresponding array only when you have a genuine community to list there. Preserve existing slugs and IDs.
3. Render locally with `python3 scripts/build_directory.py`. This only writes Markdown from local data; it does not access the network or call a model.
4. Read both READMEs and the affected country guides. Confirm local links and anchors, city placement, affiliation and coming-soon status.
5. Open a pull request with the evidence and explain what changed. Do not add workflows or automatic deployment.

1. 编辑 `data/communities.json`，填写稳定 ID、正确城市、HTTPS 官方入口、中英文介绍、来源和真实核验方式及日期。
2. 有真实社区可收录时再增加城市或国家，保留既有 slug 与 ID。
3. 运行 `python3 scripts/build_directory.py` 生成 Markdown。脚本只处理本地数据，不联网、不调用模型。
4. 阅读两份 README 与相关国家详情页，检查链接、锚点、城市归属、关联披露和筹备状态。
5. 提交附来源的 Pull Request，不添加 workflow 或自动部署。

## CI policy / CI 规则

This repository intentionally has no workflows, and GitHub Actions is disabled at repository creation. Do not enable CI or add workflows without the owner's explicit authorisation. Use `[skip ci]` in commits. Skipping checks does not permit bypassing branch protection or required checks if they are introduced later.

本仓库有意不配置 workflow，创建时关闭 GitHub Actions。未经 owner 明确授权，不启用 CI 或添加 workflow；提交信息使用 `[skip ci]`。后续若有分支保护或必需检查，不得以跳过 CI 为由绕过。
