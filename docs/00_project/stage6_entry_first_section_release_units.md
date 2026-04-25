# Stage 6 Entry + First Section Release Units

## Scope

本文件只承载阶段 6 第五个子单元的首批实际发布单元：

- `入口页`
- `第一段：命题与导航`

这里不重写最低配置，也不替代 `presentation_forms.md`。它只回答一件事：

> 入口页与第一段，当前已经能实际拿去制作的第一批 `excerpt card / asset spec / traceback card` 到底是什么？

## 入口页

### Excerpt Card | `ENTRY-EXCERPT-001` | 项目问题与非剧情复述边界

- 卡片目标：先回答“这项目究竟在解释什么”，并立刻切断“剧情复述”阅读预期。
- 展示文案：
  - “这个项目不是要把《博德之门3》讲一遍，而是要解释：为什么玩家会把 BG3 体验成‘我想到的办法可以成立，而且世界真的会在后面接住它’。”
  - “按剧情复述会把‘系统如何工作’冲淡成‘剧情发生了什么’，也会把任务、战斗、营地、同伴和区域结构拆成互不解释的并列栏目。”
- 直接锚点：
  - `README.md`
  - `docs/00_project/deconstruction_display_overview.md`
- 使用边界：
  - 只能立“项目问题 + 非剧情复述边界”
  - 不能提前展开具体区域包、任务主链或实现判断

### Asset Spec | `ENTRY-ASSET-001` | 反应性链条总图

- 图的职责：把“项目在解释什么”压成一张开场链条图，而不是角色 / Act / 任务百科封面。
- 必须出现的节点：
  - `宏观结构与空间组织`
  - `局部行动与多解法`
  - `任务 / Journal 状态回流`
  - `同伴 / 营地 / 长休反馈折叠`
  - `Act 收束与终局压力`
  - `实现验证`
- 必须出现的边界说明：
  - 研究顺序按区域包 / Act 包推进
  - 展示顺序按反应性链条进入
- 视觉禁区：
  - 不把 `Quest`、`Combat`、`Camp` 画成三条并列主入口
  - 不把 `Act 1/2/3` 画成剧情目录时间轴
  - 不把 benchmark 方法画成具体区域的技术实锤

### Traceback Card | `ENTRY-TRACE-001` | 项目边界回链

- 读者可见主张：本项目解释的是 BG3 的反应性链条，而不是剧情摘要。
- 文档回链：
  - `README.md`
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/03_analysis/05_implementation_validation.md`
- Source ID 回链：
  - `BMK-002`
  - `BMK-003`
  - `BG3-OFF-001`
  - `BG3-OFF-003`
- 当前安全层级：
  - 可以安全回链到“为何用反应性链条而不是剧情复述”这一层
- 不可越级之处：
  - 不可把官方高层表述写成任何单一区域的实现实锤
  - 不可把 benchmark 方法写成 BG3 已被完整验证的内部设计图

## 第一段：命题与导航

### Excerpt Card | `OPENING-EXCERPT-001` | 高反应性命题与区域 / 压力梯

- 卡片目标：把“高反应性命题是什么”与“这条链如何被区域 / 压力结构组织起来”压进同一组开场文案。
- 展示文案：
  - “BG3 的高反应性不是单靠分支数量堆出来的，而是把多入口空间、规则驱动的解法、任务与营地中的状态回流，以及电影化反馈包装缝合到同一条体验链里。”
  - “BG3 的宏观结构不是纯开放世界，也不是严格线性章节，而是由多个高密度区域、多个进入方式、交叠目标与阶段性收束构成。”
- 默认 handoff：
  - 先交给 `docs/03_analysis/04_combat_and_environment.md`
  - 再进入 `docs/03_analysis/02_quests_and_choices.md`
- 直接锚点：
  - `docs/03_analysis/00_core_thesis.md`
  - `docs/03_analysis/01_macro_structure.md`
- 使用边界：
  - 只能解释“命题 + 导航骨架”
  - 不能把 `Act` 梯写成剧情提要
  - 不能把 Journal 结构语言越级写成 shipped content 的私有 quest 编排

### Asset Spec | `OPENING-ASSET-001` | 区域 / 压力梯与 handoff 图

- 图的职责：把“区域包如何组织这条链”与“为什么下一段先看局部行动层”画成同一张导航图。
- 必须出现的结构：
  - `Act 1`：`入口 / 目标网 / 改道 / 门槛`
  - `Act 2`：`压力过滤 -> 收束点组`
  - `Act 3`：`入口过滤 -> 门槛重排 -> 并行承接 -> 组织级压缩`
- 必须出现的 handoff：
  - 图尾必须标出“下一段先看局部行动层，而不是先看任务列表”
- 视觉禁区：
  - 不做地图景点导览
  - 不把 `Act 2` 与 `Act 3` 压成纯剧情高潮梯
  - 不把 `04_combat_and_environment`、`02_quests_and_choices`、`03_party_and_camp` 画成平级导论

### Traceback Card | `OPENING-TRACE-001` | 命题与导航回链

- 读者可见主张：高反应性来自“区域组织 + 局部行动 + 状态回流 + 反馈折叠 + 验证边界”的同一条链，而第一段只负责先锁命题与导航。
- 文档回链：
  - `docs/03_analysis/00_core_thesis.md`
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/05_implementation_validation.md`
- Source ID 回链：
  - `BG3-OFF-001`
  - `BG3-OFF-003`
  - `BG3-OFF-012`
  - `BG3-OFF-013`
  - `BG3-OFF-014`
- 当前安全层级：
  - 可以安全回链到“高反应性命题 + 区域 / 压力梯 + handoff 到局部行动层”
- 不可越级之处：
  - 不可把公开 Journal / modding 结构语言写成私有内容编排表
  - 不可把任何单一 `Act` 写成剧情梗概

## 当前完成定义

- `入口页` 已有首个可复用的 `excerpt card / asset spec / traceback card`
- `第一段：命题与导航` 已有首个可复用的 `excerpt card / asset spec / traceback card`
- 这两组单元都能回链到正文与 `Source ID`
- 下一步应切到“第二段：局部行动到状态回流”的首批实际发布单元，而不是回头重写最低配置
