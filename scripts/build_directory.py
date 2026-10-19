#!/usr/bin/env python3
"""Render the bilingual Markdown directory from reviewed local data. No network calls."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data/communities.json').read_text())
TYPES = {'technical-demos': ('Technical demos', '技术 Demo'), 'learning-building': ('Learning & building', '学习与实践'), 'networking': ('Networking & project exchange', '交流与项目分享'), 'applied-ai': ('Applied AI & community', 'AI 应用与社区')}

def country_path(country, lang):
    return country['slug'] + ('.md' if lang == 'en' else '.zh.md')

def type_label(record, lang):
    return TYPES[record['type']][lang == 'zh']

def ordered(records):
    return sorted(records, key=lambda r: r['name']['en'].lower())

def entry(record, lang):
    en = lang == 'en'
    affiliation = ('Maintainer-affiliated' if en else '维护者关联社区') if record['affiliation'] == 'maintainer' else ('Independent' if en else '独立社区')
    status = ('Coming soon' if en else '筹备中') if record['status'] == 'coming-soon' else ('Listed' if en else '已收录')
    method = ('Official search-index evidence; scripted access blocked' if en else '官方页面搜索索引证据；脚本访问受限') if record['review_method'] == 'official-search-index' else ('Official page reviewed' if en else '已查看官方页面')
    sources = ' · '.join(f'[{"Source" if en else "来源"} {i+1}]({u})' for i,u in enumerate(record['sources']))
    return f"- [**{record['name'][lang]}**]({record['url']}) — {record['description'][lang]}\n  - {type_label(record,lang)} · {status} · {affiliation}.\n  - {sources} · {record['reviewed_on']} · {method}.\n"

def render_country(country, lang):
    en = lang == 'en'
    title = f"AI Communities in {country['name'][lang]}" if en else f"{country['name'][lang]} AI 社区目录"
    root = '../README.md' if en else '../README.zh.md'
    other = country_path(country, 'zh' if en else 'en')
    cities = [c for c in DATA['cities'] if c['country'] == country['slug']]
    lines = [f'# {title}\n',f'[{"All countries" if en else "所有国家"}]({root}) · [{"简体中文" if en else "English"}]({other})\n',
        ('Choose a city, then a format. Technical-demo groups suit builders who want implementation discussion; learning groups suit people trying tools together. Check each organiser’s current event page for language, cost, eligibility and venue.\n' if en else '先选城市，再按活动形式选择：技术 Demo 社区适合讨论实现细节，学习型社区适合结伴实践工具。语言、费用、参与条件和地点请以组织者当前活动页为准。\n'),
        f'{"Reviewed" if en else "核验日期"}: {DATA["reviewed_on"]}. '+('Listed means a community entry is supported by official evidence, not that registration is open today. Coming-soon entries are not active-event recommendations.\n' if en else '“已收录”表示有官方依据支持该社区入口，不表示今天有活动或开放报名。“筹备中”不作为已开展活动推荐。\n'),
        (' | '.join(f"[{c['name'][lang]}](#{c['slug']})" for c in cities))+'\n']
    for city in cities:
        records = [r for r in DATA['communities'] if r['city'] == city['slug']]
        listed = ordered([r for r in records if r['status'] == 'listed'])
        future = ordered([r for r in records if r['status'] == 'coming-soon'])
        lines += [f'<a id="{city["slug"]}"></a>\n',f'## {city["name"][lang]}\n',f'{"Local time zone" if en else "当地时区"}: `{city["timezone"]}`.\n']
        if listed:
            lines += [('### Community options\n' if en else '### 社区选择\n')]
            lines += [entry(r,lang) for r in listed]
        else:
            lines += [('No independently reviewed live community option in this starter directory yet. Suggest one with an official source.\n' if en else '本版尚未收录已核验的现有社区入口，欢迎附官方来源补充。\n')]
        if future:
            lines += [('### Coming soon — not an active chapter\n' if en else '### 筹备中 — 不作为已开放分站推荐\n')]
            lines += [entry(r,lang) for r in future]
        if len(listed) == 1:
            lines += [('Coverage note: one listed option is a starting point, not a claim that this is the city’s only or best community.\n' if en else '覆盖说明：仅收录一个入口代表本版覆盖有限，不代表它是该城市唯一或最好的社区。\n')]
        if any(r['type'] == 'technical-demos' for r in listed):
            lines += [('Before joining a demo night, check the organiser’s builder or submission requirements and bring a project or technical question.\n' if en else '参加 Demo 活动前，先查看组织者对开发经历或演示投稿的要求，准备一个项目或技术问题。\n')]
    lines += [f'[{"Suggest an addition or correction" if en else "补充社区或纠错"}](../CONTRIBUTING.md) · [{"Evidence and access notes" if en else "核验与访问说明"}](../docs/REVIEW.md)\n']
    return '\n'.join(lines)

def render_home(lang):
    en = lang == 'en'
    listed = [r for r in DATA['communities'] if r['status'] == 'listed']
    upcoming = [r for r in DATA['communities'] if r['status'] == 'coming-soon']
    intro = ('Find AI meetups, builder demo nights, learning groups and local networking communities by **country and city**. Start with a city below and open the organiser’s own page.\n' if en else '按**国家与城市**寻找 AI Meetup、开发者 Demo Night、学习实践社群和本地交流活动。先选城市，再打开组织者官方入口。\n')
    lines = ['# Awesome AI Communities\n',('[English](README.md) · [简体中文](README.zh.md)\n'),intro,
        (f'**{len(DATA["countries"])} countries · {len(DATA["cities"])} cities · {len(listed)} listed community/city entries · {len(upcoming)} coming-soon entries.** Reviewed {DATA["reviewed_on"]}. Counts refer to chapter listings, not unique global organisations.\n' if en else f'**{len(DATA["countries"])} 个国家 · {len(DATA["cities"])} 座城市 · {len(listed)} 条已收录社区／城市记录 · {len(upcoming)} 条筹备记录。** 核验日期：{DATA["reviewed_on"]}。按分站记录计数，不是全球组织数量。\n'),
        ('Maintained by [Lightman Wang](https://github.com/hades217), founder of [JR Academy](https://jracademy.ai/). **Disclosure:** JR Academy AI Circle is maintainer-affiliated. Other listed communities are independently operated; inclusion does not imply partnership, endorsement or ranking.\n' if en else '由 [Lightman Wang](https://github.com/hades217)（[JR Academy 匠人学院](https://jracademy.ai/)创始人）维护。**关联披露：**匠人 AI圈是维护者关联社区，其他社区独立运营；收录不代表合作、背书或排名。\n'),
        ('## Find your city\n' if en else '## 按国家与城市查找\n'),
        ('Listed = official evidence supports the entry; check the current calendar yourself. Chapter access may require an application, membership or payment. No event dates, attendance figures or prices are inferred.\n' if en else '已收录 = 官方依据支持该入口，请自行查看最新日历。活动可能需申请、会员或付费；本目录不推测场次、人数或价格。\n'),
        ('| Country | City guide | Listed community links |\n|---|---|---|' if en else '| 国家 | 城市详情 | 已收录社区入口 |\n|---|---|---|')]
    for country in DATA['countries']:
        for city in [c for c in DATA['cities'] if c['country'] == country['slug']]:
            records = ordered([r for r in listed if r['city'] == city['slug']])
            links = ' · '.join(f"[{r['name'][lang]}]({r['url']})" for r in records) or ('Suggest a community' if en else '欢迎补充')
            lines += [f"| {country['name'][lang]} | [{city['name'][lang]}](countries/{country_path(country,lang)}#{city['slug']}) | {links} |"]
    lines += ['\n'+('## Coming soon\n' if en else '## 筹备中的分站\n'),
        ('The following AI Circle city pages explicitly say Coming Soon. They are included for transparency, not as currently operating meetup recommendations.\n' if en else '以下 AI圈城市页面明确标注 Coming Soon。保留入口供关注筹备动态，不当作已开展的 Meetup 推荐。\n')]
    lines += [f"- [{r['name'][lang]}]({r['url']}) — Coming Soon." for r in upcoming]
    lines += ['\n'+('## Choose a community format\n' if en else '## 按活动形式选择\n'),
        ('- **Technical demos:** show working code and discuss implementation. See AI Tinkerers and Builders After Dark; the latter also covers non-AI projects.\n- **Learning & building:** try tools or build with peers. See Build Club, Malaysian AI, AI After Hours and Vibe Coding Collective.\n- **Networking & project exchange:** meet practitioners and share projects. See the listed AI Circle city chapters.\n- **Applied AI:** broader education and discussion. See AI LA.\n' if en else '- **技术 Demo：**展示代码、讨论实现。可查看 AI Tinkerers、Builders After Dark，后者也涵盖非 AI 项目。\n- **学习与实践：**结伴尝试工具与构建项目。可查看 Build Club、Malaysian AI、AI After Hours、Vibe Coding Collective。\n- **交流与项目分享：**认识本地从业者、交流项目。可查看已收录的 AI圈城市页。\n- **AI 应用与社区：**更广泛的教育与讨论，可查看 AI LA。\n'),
        ('## Scope and evidence\n' if en else '## 范围与证据\n'),
        ('This is a curated starter directory, not an exhaustive global database or a live event feed. Country guides include source links, review methods, dates and affiliation labels. Some official sites block scripted access; search-index evidence is labelled separately from a direct page read. We do not publish private chat invitations or contact lists.\n' if en else '这是经过筛选的初版目录，不是全球穷尽数据库或实时活动流。国家详情页附来源、核验方式、日期及关联标识。部分官方站点限制脚本访问，搜索索引依据与直接查看页面分别标注。不公开私人群邀请或联系人名单。\n'),
        ('[Review notes](docs/REVIEW.md) · [Contributing](CONTRIBUTING.md) · [Machine-readable data](data/communities.json)\n' if en else '[核验记录](docs/REVIEW.md) · [贡献指南](CONTRIBUTING.md) · [结构化数据](data/communities.json)\n'),
        ('## Related directories\n' if en else '## 相关资源目录\n'),
        ('- [Awesome AI](https://github.com/hades217/awesome-ai) — the broader AI resource list, including models, coding tools, courses and communities.\n' if en else '- [Awesome AI 中文版](https://github.com/hades217/awesome-ai/blob/master/README.zh.md) — 更广泛的 AI 资源清单，涵盖大模型、编程工具、课程与社区。\n'),
        ('## Contribute\n' if en else '## 参与维护\n'),
        ('Suggest a community or correction through an issue or pull request. Include the city, official organiser page and what makes it useful. Maintainer affiliation must be disclosed. No paid placement, referral links or copied city pages.\n' if en else '欢迎通过 Issue 或 Pull Request 补充社区与纠错，请附城市、组织者官方页面与具体价值。有维护者关联需披露，不接受付费排名、推广返佣链接或仅更换地名的重复内容。\n'),
        'MIT License · [LICENSE](LICENSE)\n']
    return '\n'.join(lines)

if __name__ == '__main__':
    for language in ('en','zh'):
        (ROOT / ('README.md' if language == 'en' else 'README.zh.md')).write_text(render_home(language))
        for country in DATA['countries']:
            (ROOT / 'countries' / country_path(country,language)).write_text(render_country(country,language))
    print('Rendered 2 READMEs and 12 country guides from local data.')
