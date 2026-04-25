# Presentation Forms

## 当前有效版本

以下内容为阶段 6 当前有效的展示口径；如果与旧文本冲突，以下述新口径为准。

### 作用

本文件定义“研究文档如何被压成展示产物”的当前执行口径。

- 阶段 6 之前，它主要是轻量原则页。
- 阶段 6 第二个子单元完成后，它承担“模块职责 / 推荐展示形态 / 发布导览矩阵”。
- 阶段 6 第三个子单元完成后，它还要继续承担一份可直接执行的发布导览稿 / section skeleton。

### 研究文档与展示产物的关系

- 研究文档是 `source of truth`。
- 展示产物只能压缩、重组、转译研究结论，不能替代研究文档本身。
- 如果展示内容与研究文档冲突，以研究文档为准，并回到研究文档修正。
- 没有研究文档支撑的展示结论，不应进入对外或对内展示层。

### 阶段 6 当前前提

- 当前正式阅读顺序已锁定为：
  `00_core_thesis -> 01_macro_structure -> 04_combat_and_environment -> 02_quests_and_choices -> 03_party_and_camp -> 05_implementation_validation`
- `Act 收束与终局压力` 继续通过 `01_macro_structure.md`、`02_quests_and_choices.md` 与 `03_party_and_camp.md` 联读进入，不单开新的发布入口文件。
- 本文件当前只负责把这条阅读链压成展示职责、导览骨架与发布最低配置，不新增研究模块，也不改写阶段 5 已锁定的证据边界。

### 模块职责 / 推荐展示形态 / 发布导览矩阵

| 阅读位序 | 模块 | 当前展示职责 | 推荐展示形态 | 在发布导览中的使用方式 | 默认交接 |
| --- | --- | --- | --- | --- | --- |
| 1 | `00_core_thesis` | 先回答“BG3 的高反应性到底在解释什么”，锁定整条链的命题边界。 | opening brief、总论摘要、链条总图 | 作为第一段正文，不承担案例堆砌。 | `01_macro_structure` |
| 2 | `01_macro_structure` | 给出 `Act` / 区域 / 压力梯与阅读导航。 | 结构图、区域梯、阶段压力示意图 | 作为导航骨架，解释为什么下一步先看局部行动层。 | `04_combat_and_environment` |
| 3 | `04_combat_and_environment` | 先证明玩家为什么会感到“我能这样试”。 | 场景流程图、多解法对照卡、局部战术页 | 作为第一组证据段，优先呈现局部 `agency`。 | `02_quests_and_choices` |
| 4 | `02_quests_and_choices` | 把局部行动写回状态变化与后续读回。 | 选择点 -> 状态变化 -> 后续反馈链路图、案例卡、读回矩阵 | 作为第二组证据段，必须承接 `04`。 | `03_party_and_camp` |
| 5 | `03_party_and_camp` | 把分散状态折叠到营地 / 长休反馈。 | 延迟反馈折返图、长休循环图、少量强案例卡 | 作为第三组证据段，只能晚于 `02` 出现。 | `05_implementation_validation` |
| 6 | `05_implementation_validation` | 给整条链分级、保边界、留开放问题。 | 证据矩阵、来源类型图、验证入口清单 | 作为收尾章或附录，不反向替代开场导论。 | 结束 |

### 当前可直接执行的发布导览稿 / section skeleton

| 发布段落 | 必须回答的问题 | 直接依赖文件 | 推荐压缩产物 | 默认交接 |
| --- | --- | --- | --- | --- |
| 入口页 | 这项目在解释什么、为什么不是剧情复述、为什么当前按这条链读。 | `README.md`、`docs/00_project/deconstruction_display_overview.md` | 边界说明、总逻辑短页、读者导言 | `00_core_thesis` |
| 第一段：命题与导航 | 高反应性命题是什么，这条链怎样被区域包与阶段压力组织起来。 | `docs/03_analysis/00_core_thesis.md`、`docs/03_analysis/01_macro_structure.md` | opening brief、总图、区域梯 | `04_combat_and_environment` |
| 第二段：局部行动到状态回流 | 玩家先在哪一层感到自由，系统后来怎样把它写回状态。 | `docs/03_analysis/04_combat_and_environment.md`、`docs/03_analysis/02_quests_and_choices.md` | 局部 `agency` 案例卡、读回链路图 | `03_party_and_camp` |
| 第三段：延迟反馈折叠 | 为什么营地 / 长休是反馈折叠层，而不是人物附录。 | `docs/03_analysis/03_party_and_camp.md` | 折返图、循环图、少量强案例 | `05_implementation_validation` |
| 收尾段：证据分级 | 哪些判断已经够稳，哪些仍是当前最强解释。 | `docs/03_analysis/05_implementation_validation.md` | 证据矩阵、验证入口清单、开放问题卡 | 结束 |

### 首轮发布最低配置

如果只做第一版最小可发布导览，至少应准备这 6 项：

1. 一页开场说明：项目问题、非目标、为什么不是剧情复述。
2. 一张链条总图：`总命题 -> 宏观结构 -> 局部行动 -> 状态回流 -> 营地折叠 -> 实现验证`。
3. 一张区域 / 压力梯：解释 `Act 1 -> Act 2 -> Act 3` 如何重组反应性。
4. 一组“局部行动 -> 状态回流”样例：至少能同时指向 `04_combat_and_environment.md` 与 `02_quests_and_choices.md`。
5. 一张“任务结果 -> 营地 / 长休 -> 延迟反馈”折返图。
6. 一张证据矩阵：明确哪些判断是事实、推断、待验证问题。

### 阶段 6 第四子单元：首轮发布包最低配置 / excerpt queue / asset queue

到这一步为止，阶段 6 不再讨论“先读谁”或“谁负责什么”，而只回答一件事：

> 如果现在就要做第一版最小可发布导览，每一段最少必须带哪些摘录、图、卡片与回溯路径？

| 发布段落 | 最低 excerpt queue | 最低 asset queue | 最低 card queue | 最低 traceback path |
| --- | --- | --- | --- | --- |
| 入口页 | 1 条项目问题摘录 + 1 条“为什么不是剧情复述”摘录。 | 1 张反应性链条总图。 | 1 张边界卡：写清非目标与阅读方式。 | `README.md` -> `docs/00_project/deconstruction_display_overview.md` -> `BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003` |
| 第一段：命题与导航 | 1 条高反应性命题摘录 + 1 条 `Act / 区域 / 压力梯` 摘录。 | 1 张区域 / 压力梯图。 | 1 张 handoff 卡：说明为什么下一段先看局部行动层。 | `docs/03_analysis/00_core_thesis.md` -> `docs/03_analysis/01_macro_structure.md` -> `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` |
| 第二段：局部行动到状态回流 | 1 条局部 `agency` 摘录 + 1 条状态读回摘录。 | 1 张 `local agency -> readback` 链路图。 | 1 张双联卡：左侧放局部解法，右侧放后续状态读回。 | `docs/03_analysis/04_combat_and_environment.md` -> `docs/03_analysis/02_quests_and_choices.md` -> `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` |
| 第三段：延迟反馈折叠 | 1 条 `camp fold / delayed feedback` 摘录 + 1 条营地边界摘录。 | 1 张“任务结果 -> 营地 / 长休 -> reread”折返图。 | 1 张强案例卡 + 1 张边界卡，分别对应 `camp fold` 与 `supporting bundle`。 | `docs/03_analysis/03_party_and_camp.md` -> `docs/03_analysis/05_implementation_validation.md` -> `BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`, `BG3-OFF-016` |
| 收尾段：证据分级 | 1 条“事实 / 推断 / 待验证问题”摘录 + 1 条阶段出口边界摘录。 | 1 张证据矩阵。 | 1 张开放问题卡：只保留仍值得继续验证的问题。 | `docs/03_analysis/05_implementation_validation.md` -> `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016` |

### 首轮发布包的执行约束

- 每一段首轮只做 `1` 组最小单元：`1` 组摘录、`1` 张核心图、`1` 组卡片，不做平行备选版本。
- 每一段都必须保留 traceback path；缺 traceback 的内容即使写得漂亮，也不算发布包完成。
- `Quest`、`Combat`、`Camp` 之间如果出现竞争同一张图的情况，优先保留链条图，不额外拆成并列模块图。
- 入口页与收尾段都不能吞掉中间三段：前者只负责立边界，后者只负责分级与保边界。

### 当前推荐的实际制作顺序

如果下一轮要继续推进发布包，应按下面顺序做最小落地，而不是五段一起铺开：

1. 入口页：先做边界摘录、链条总图与边界卡。
2. 第一段：再做命题摘录、区域 / 压力梯与 handoff 卡。
3. 第二段：随后补第一组 “局部行动 -> 状态回流” 双联卡。
4. 第三段：再补营地折返图与边界卡。
5. 收尾段：最后补证据矩阵与开放问题卡。

### 阶段 6 第五子单元：入口页与第一段的首批实际发布单元

到这一步为止，阶段 6 不再只是维护 queue，而是先把最前面的两段落成第一批真的可复用发布物：

- 承载文件：`docs/00_project/stage6_entry_first_section_release_units.md`
- 已落成单元：
  - `ENTRY-EXCERPT-001`
  - `ENTRY-ASSET-001`
  - `ENTRY-TRACE-001`
  - `OPENING-EXCERPT-001`
  - `OPENING-ASSET-001`
  - `OPENING-TRACE-001`
- 这一步的完成标准不是“又新增了一份表”，而是：
  - 入口页已经能直接拿去制作边界卡与链条总图
  - 第一段已经能直接拿去制作命题摘录、区域 / 压力梯与 handoff 卡
  - 两段都能回链到正文与 `Source ID`

完成第五子单元后，下一唯一主任务应切到：

1. `第二段：局部行动到状态回流`
2. 再进 `第三段：延迟反馈折叠`
3. 最后才回到 `收尾段：证据分级`

### 阶段 6 第六子单元：第二段的首批实际发布单元

到这一步为止，阶段 6 不再只说“第二段最少要带什么”，而是先把第二段真正落成第一组可复用发布物：

- 承载文件：`docs/00_project/stage6_second_section_release_units.md`
- 已落成单元：
  - `SECOND-EXCERPT-001`
  - `SECOND-ASSET-001`
  - `SECOND-TRACE-001`
- 这一步的完成标准不是“又补了一份 queue”，而是：
  - 第二段已经能直接拿去制作“局部 agency + 状态读回”的双联摘录
  - 第二段已经有一张明确声明“章节接力，而非单一案例因果链”的 `local agency -> readback` 接力图
  - 第二段已经能同时回链到 `04_combat_and_environment.md`、`02_quests_and_choices.md` 与 `Source ID`

完成第六子单元后，下一唯一主任务应切到：

1. `第三段：延迟反馈折叠`
2. 再进 `收尾段：证据分级`

### 阶段 6 第七子单元：第三段的首批实际发布单元

到这一步为止，阶段 6 不再只说“第三段最少要带什么”，而是先把第三段真正落成第一组可复用发布物：

- 承载文件：`docs/00_project/stage6_third_section_release_units.md`
- 已落成单元：
  - `THIRD-EXCERPT-001`
  - `THIRD-ASSET-001`
  - `THIRD-TRACE-001`
- 这一步的完成标准不是“又补了一份营地说明”，而是：
  - 第三段已经能直接拿去制作“`camp fold / delayed feedback` 折返层”主卡
  - 第三段已经有一张明确声明“supporting bundle / handoff 不等于第二条对称营地主干”的 `task result -> camp fold -> reread` 折返图
  - 第三段已经能同时回链到 `03_party_and_camp.md`、`05_implementation_validation.md` 与 `Source ID`

完成第七子单元后，下一唯一主任务应切到：

1. `收尾段：证据分级`

### 第三段首批实际单元的特别约束

- 第三段只能把“前序状态如何在营地 / 长休重新可见”压实，不能重写成 camp scene 清单、同伴人物志或恋爱系统导览。
- 第三段的主卡必须同时携带 supporting-bundle 边界；否则会把 `reflection / roster-state`、`dialogue accessibility maintenance` 与 `ending-feedback handoff` 误读成第二条公开营地主干。
- 第三段仍必须保留 handoff 到 `05_implementation_validation.md`；否则就会把证据分级职责提前吞掉。

### 阶段 6 第八子单元：收尾段的首批实际发布单元

到这一步为止，阶段 6 不再只说“收尾段最少要带什么”，而是先把收尾段真正落成第一组可复用发布物：

- 承载文件：`docs/00_project/stage6_final_section_release_units.md`
- 已落成单元：
  - `FINAL-EXCERPT-001`
  - `FINAL-ASSET-001`
  - `FINAL-TRACE-001`
- 这一步的完成标准不是“又补了一份方法说明”，而是：
  - 收尾段已经能直接拿去制作“`facts / inferences / open questions` 证据分级主卡”
  - 收尾段已经有一张明确声明“前四段 actual units 证据强度并不相同、且必须保留开放问题”的 `claim tier -> document anchor -> source entry` 证据矩阵
  - 收尾段已经能同时回链到 `05_implementation_validation.md`、前四段 actual units 与 `Source ID`

完成第八子单元后，阶段 6 的五段首批实际发布单元可视为在当前计划下闭合。
如果下一次会话继续推进，不应回头重写任一段 queue；应先整理首轮发布包总装配 / 审阅清单，再决定是否需要新的发布层动作。

### 阶段 6 第九子单元：首轮发布包总装配 / 审阅清单

到这一步为止，阶段 6 不再新增第六段 actual units，也不再补新的 queue，而是把五段既有实际单元压成一份统一的 assembly / review 层：

- 承载文件：`docs/00_project/stage6_release_package_assembly_review_sheet.md`
- 执行计划：`.agent/execplan_stage6_release_package_assembly_review.md`
- 这一步的完成标准不是“再写一段导览文案”，而是：
  - 已有一份 `assembly map`，明确入口页、第一段、第二段、第三段、收尾段如何装成同一条发布链
  - 已有一份 `review checklist`，明确顺序、handoff、证据强度与 traceback 该怎么统一审阅
  - 已有一份 `writeback trigger`，明确什么情况下才允许回写单段承载文件

完成第九子单元后，下一唯一主任务不应回到 queue 或阶段 5；应执行这份 review sheet 的受控一致性审阅。当前首轮审阅已完成并修正 `FINAL-ASSET-001` 的独立 `入口页` 行；后续若没有新的 trigger，就先按 `docs/01_methodology/stage6_freeze_maintenance_playbook.md` 做 no-trigger 判定，再只更新审阅结论与状态同步，不再扩写单段文件。

### 第九子单元的特别约束

- 总装配 / 审阅清单只能汇总、核对、标记触发条件，不能替代五段 actual units 原文件。
- 这一步不能新增第六段发布单元、第二版 release card，或把已有段落重新复制成另一份长文。
- 这一步不能把“审阅”当成重开阶段 5 的借口；supporting bundle、modding / Journal 文档与开放问题边界继续维持原级别。

### 收尾段首批实际单元的特别约束

- 收尾段只能负责重分级与回链，不能反向取代前四段的正文、excerpt 或 asset 职责。
- 收尾段的证据矩阵必须把 `入口页`、第一段、第二段、第三段显式保留为四行；不能把 `入口页` 并入第一段，否则会破坏五段装配链的 traceback。
- 收尾段的证据矩阵必须同时保留 `事实`、`推断` 与 `待验证问题` 三列；否则就会把当前最强解释误写成已经证实的实现结论。
- 收尾段必须把 `BG3-OFF-011` 到 `BG3-OFF-014` 固定在“公开验证语言 / 结构边界”层，而不能把它们越级写成 shipped content 的私有脚本实锤。

### 第二段首批实际单元的特别约束

- 第二段只能把 `04` 的局部 agency 锚点与 `02` 的高可见 readback 锚点并排压实，不能伪造“一条具体微观案例从左一路流到右”的假因果链。
- 第二段的图与卡必须明确保留 handoff 到 `03_party_and_camp.md`；否则就会把营地折返层提前吞掉。
- 第二段仍不能借“局部行动到状态回流”之名重开第二条对称 spine、objective 总表或 late-game encounter 清单。

### 不应再出现的发布错误

- 不要把 `Quest`、`Combat`、`Camp` 当成三份并列导论。
- 不要让 `03_party_and_camp.md` 早于 `02_quests_and_choices.md` 出现。
- 不要把 `05_implementation_validation.md` 提前当成开场技术导论。
- 不要把 `Act 收束与终局压力` 重新拆成独立入口，打断已锁定的 6 模块主链。

### “研究完成”和“展示完成”的区别

- 研究完成：相关模块已有可追溯结论，区分了事实、推断、待验证问题，并已同步状态文件。
- 展示完成：已有一份面向阅读效率的压缩表达，且不抹平研究文档中的边界、证据等级和未决问题。

研究完成先于展示完成；展示完成不代表研究已经充分完成。

### 追溯要求

- 每个展示产物都必须能回溯到对应研究文档路径。
- 每个关键判断都必须能回溯到至少一个 `Source ID`。
- 如果展示中做了压缩合并，仍要保留“来自哪个模块、依赖哪些来源”的说明。
- 若无法清楚回溯到研究文档或 `Source ID`，该展示产物视为未完成。

### 使用边界

- 本文件只提供展示原则、模块矩阵与当前导览骨架，不引入新目录、新模板或新检查流程。
- 只有当研究文档已足够稳定时，才考虑制作展示产物。
- 如果时间有限，优先补研究文档，不优先做展示层整理。
