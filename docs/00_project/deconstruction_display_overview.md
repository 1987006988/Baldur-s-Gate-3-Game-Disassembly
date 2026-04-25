# Deconstruction Display Overview

## 1. 总命题

这个项目不是要把《博德之门3》讲一遍，而是要解释：

> 为什么玩家会把 BG3 体验成“我想到的办法可以成立，而且世界真的会在后面接住它”。

所以，仓库真正要拆的是一条**反应性链条**：

`宏观结构与空间组织 → 局部行动与多解法 → 任务 / Journal 状态回流 → 同伴 / 营地 / 长休反馈折叠 → Act 收束与终局压力 → 实现验证`

这条链条才是 BG3 的总逻辑。按这个逻辑拆，项目负责人、读者、观众和后续 Codex 才能同时知道：

- 现在在拆什么
- 这一块为什么值得先拆
- 它和前后部分是什么关系
- 这一块完成后，应该回写到哪里

## 2. 为什么不能按剧情复述

按剧情复述有三个致命问题。

### 问题一：它会把“系统如何工作”冲淡成“剧情发生了什么”

BG3 的强项不是剧情事件多，而是**处理方式多、状态被记住、反馈会延迟折返**。如果只按剧情说，会自然把重点放在“谁跟谁说了什么”“哪一幕发生在 Act 几”，而不是“玩家怎样改写了推进结构”。

### 问题二：它会把本该互相解释的层拆开

BG3 里，任务、战斗、营地、同伴、区域结构不是并列栏目，而是同一条体验链的不同段落。按剧情顺序写，常见后果是：

- 战斗被写成局部遭遇
- 营地被写成休息插曲
- 同伴被写成人物志
- 任务被写成分支表

最后读者只能看到“内容很多”，看不到“为什么这些内容会连起来产生高反应性”。

### 问题三：它会制造“为什么突然拆营地”的观感

一旦项目先写了任务，再突然切到营地，读者很容易问：

> 为什么刚才还在讲任务回流，现在突然开始讲营地？

真正的问题不是营地不重要，而是如果前面没有先说清：

- 营地依赖前序任务 / 战斗 / 区域状态
- 营地承担延迟反馈与再解释
- 营地是反馈折叠层，不是生活附录

那么它看上去就像“平行插入的新模块”，而不是总链条的下游节点。

## 3. 参考范式与适配结果

### Reverse Design 适合 BG3 的地方

`BMK-002` 强调从已呈现的设计结果反向追问：设计者到底做了哪些决策、这些决策如何被作品自身证据支持，并尽量避免脱离作品乱猜。这对 BG3 很适合，因为 BG3 的强项恰恰不是某一条系统说明，而是大量“已经被玩家体验到、但需要反向解释”的现象。我们应借用它的核心做法：

- 先抓住高辨识度体验现象
- 再追问系统如何让它成立
- 最后用公开证据决定哪些判断能升级、哪些只能降级为推断或待验证问题

### Reverse Design 不适合直接照搬的地方

BG3 不是单一类型作品。它既有 CRPG 任务状态，又有电影化叙事包装，还有空间 / 战斗 / 环境解法。因此不能只做“单模块的逆向拆解长文”，否则会让跨模块回流关系散掉。

### Boss Keys 适合 BG3 的地方

`BMK-003` 把空间分析做成图论与依赖分析：入口、钥匙、门、关键道具、障碍、开关都能被画成一张结构图。BG3 很适合借用这套方法来处理：

- 高密度区域包
- 多入口推进
- 门槛、权限、绕行与折返
- 同一区域内任务 / 战斗 /探索的互相嵌套

### Boss Keys 不适合直接照搬的地方

BG3 不是纯 dungeon graph 游戏。它的关键不只在“空间如何通”，还在“状态如何被记住并在后面回流”。所以 Boss Keys 只能承担**空间骨架**，不能单独解释：

- 任务状态回流
- 长休与营地反馈
- 同伴关系推进
- Act 级别收束与终局压力

### BG3 应形成的自己的拆解逻辑

BG3 最适合形成的是一套“**区域证据带 + 反应性链条 + 实现验证层**”的逻辑：

- 区域证据带：研究时按区域包推进，避免只剩抽象模块跳转。
- 反应性链条：展示时按玩家体验链条呈现，避免只剩剧情复述。
- 实现验证层：用官方补丁、访谈、Journal / Osiris 文档和可观察结构校正结论，避免把强体验误写成技术实锤。

## 4. 最推荐的展示顺序

下面这条顺序，是面向人读的，不是面向内部收证据的。

### 第一部分：总命题与当前最强解释

作用：先告诉读者 BG3 到底为什么值得拆，不然所有局部模块都会像零件堆。

最适合形式：
- 长文总论
- 单页结构图
- 一张“反应性链条”总图

对应主文：
- `docs/03_analysis/00_core_thesis.md`

### 第二部分：宏观结构与区域包

作用：告诉读者 BG3 的自由感首先不是来自对白，而是来自高密度区域包、多入口推进和阶段性收束。

最适合形式：
- 结构图
- 区域包示意图
- Act / 区域关系图

对应主文：
- `docs/03_analysis/01_macro_structure.md`

### 第三部分：局部行动层——战斗 / 环境 / 多入口

作用：先把“我能这样试”的感觉解释出来。玩家先在局部场景里感到有办法，后面才会把任务与营地反馈理解成“世界接住了我”。

最适合形式：
- 案例长文
- 战术对照卡片
- 场景流程图

对应主文：
- `docs/03_analysis/04_combat_and_environment.md`

### 第四部分：任务 / Journal / 选择回流

作用：把第三部分产生的行动差异，写回任务状态与后续反馈。这里不是解释“有多少分支”，而是解释“系统怎么记住并重放你的行动”。

最适合形式：
- 选择点 → 状态变化 → 后续反馈链路图
- 案例卡片
- 区域包中的任务流示意图

对应主文：
- `docs/03_analysis/02_quests_and_choices.md`

### 第五部分：同伴 / 营地 / 长休反馈折叠

作用：这里不是突然换题，而是把前面分散的状态折叠到一个强感知节点里。营地之所以重要，不是因为它温馨，而是因为它是“延迟反馈集中可见”的地方。

最适合形式：
- 反馈折返图
- 长休循环流程图
- 强案例 + 候补案例卡片

对应主文：
- `docs/03_analysis/03_party_and_camp.md`

### 第六部分：Act 收束与终局压力

作用：说明前面累积的多入口、多状态、多反馈，在中后期如何被压缩、碰撞、结算。没有这一层，BG3 的总逻辑会停在“中前期很自由”。

最适合形式：
- 阶段性收束图
- 派系 / 终局组织关系图
- 压缩压力说明卡

对应主文：
- 以 `docs/03_analysis/01_macro_structure.md` 为骨架
- 与 `docs/03_analysis/02_quests_and_choices.md`、`03_party_and_camp.md` 联读

### 第七部分：实现验证层

作用：告诉读者哪些是稳结论、哪些是当前最强解释、哪些还得继续验证。没有这一层，整个项目很容易看起来像“漂亮但未经校验的拆解”。

最适合形式：
- 证据链图
- 来源类型矩阵
- 实现验证清单

对应主文：
- `docs/03_analysis/05_implementation_validation.md`

### 阶段 6 当前入口怎么读

阶段 5 的三条横向主干现在都已经被压成“`1` 条正式 spine + `1` 次 ceiling / supporting-bundle / handoff 收口”的同一种出口结构，所以阶段 6 的第一步不是再补其中某一条，而是把它们翻译成同一条展示链。

当前最稳的入口顺序应锁定为：

1. `docs/03_analysis/00_core_thesis.md`
2. `docs/03_analysis/01_macro_structure.md`
3. `docs/03_analysis/04_combat_and_environment.md`
4. `docs/03_analysis/02_quests_and_choices.md`
5. `docs/03_analysis/03_party_and_camp.md`
6. `docs/03_analysis/05_implementation_validation.md`

这样排的原因是：

- `00_core_thesis.md` 先回答“整条链在解释什么”。
- `01_macro_structure.md` 先把区域包、阶段压力与阅读梯排出来。
- `04_combat_and_environment.md` 先解释局部行动空间，避免任务回流失去上游动作来源。
- `02_quests_and_choices.md` 与 `03_party_and_camp.md` 再分别承担“状态被写回”和“状态被折叠读出”。
- `05_implementation_validation.md` 最后负责给前面整条链分级，而不是反过来替代展示入口。

### 阶段 6 第二子单元现在固定什么

在入口顺序已经锁定后，阶段 6 的第二步不再处理“先读谁”，而处理“每个模块在发布链里负责什么”：

- `00_core_thesis` 负责开场命题，不负责细节堆砌。
- `01_macro_structure` 负责导航骨架，不负责局部案例证明。
- `04_combat_and_environment` 负责第一组“局部 agency”证据，不负责任务百科。
- `02_quests_and_choices` 负责把前面的行动写回状态与后续读回。
- `03_party_and_camp` 负责把这些状态折成延迟反馈，不再单开人物志式入口。
- `05_implementation_validation` 负责最后分级与保边界，而不是提到最前面充当技术导论。

这一步的详细矩阵现在应以 `docs/01_methodology/presentation_forms.md` 与 `docs/00_project/repo_map.md` 为准；`deconstruction_display_overview.md` 只保留总逻辑与顺序解释，不重复承担全部发布细节。

### 阶段 6 第三子单元现在固定什么

在入口顺序与模块职责都已经锁定后，阶段 6 的第三步不再继续解释原则，而是把这条链压成一份**实际可发布的导览稿骨架**：

- 第一段先交代项目在解释什么、为什么不是剧情复述。
- 第二段把总命题与区域 / 压力骨架接起来，避免读者还没理解问题就先掉进案例堆。
- 第三段坚持“先局部行动、后状态回流”，防止任务模块失去上游动作来源。
- 第四段把营地固定成延迟反馈折叠层，而不是独立人物入口。
- 最后一段才进入实现验证，给前面整条链分级、保边界、留开放问题。

换句话说，仓库现在不只知道“先读谁”，还知道“导览稿该怎么一段一段往下讲”。这一步的执行细节应以 `docs/01_methodology/presentation_forms.md` 的 section skeleton 为准。

### 当前可直接复用的发布导览稿 / section skeleton

如果现在就要把仓库压成一份最小可讲、可发、可维护的导览稿，建议按下面这 5 段组织：

1. `开场：问题、边界与为什么不是剧情复述`
   - 依赖文件：`README.md`、`docs/00_project/deconstruction_display_overview.md`
   - 这段必须先回答：项目到底在解释哪条反应性链，为什么不按剧情讲，为什么营地不会再“突然出现”。
   - 默认 handoff：`docs/03_analysis/00_core_thesis.md`

2. `第一章：高反应性到底在解释什么，以及这条链如何被区域组织起来`
   - 依赖文件：`docs/03_analysis/00_core_thesis.md`、`docs/03_analysis/01_macro_structure.md`
   - 这段负责先锁命题，再把 `Act 1` 的入口 / 目标网 / 改道 / 门槛、`Act 2` 的压力 / 收束梯与 `Act 3` 的过滤 / 门槛 / 并行 / 组织压缩梯排出来。
   - 默认 handoff：`docs/03_analysis/04_combat_and_environment.md`

3. `第二章：玩家先在哪一层感到“我能这样试”，系统后来又怎样记住它`
   - 依赖文件：`docs/03_analysis/04_combat_and_environment.md`、`docs/03_analysis/02_quests_and_choices.md`
   - 这段必须坚持“先局部行动、后状态回流”的顺序：先解释 BG3 如何制造局部 `agency`，再解释任务 / Journal 如何把这些尝试写回后续状态。
   - 默认 handoff：`docs/03_analysis/03_party_and_camp.md`

4. `第三章：为什么营地 / 长休是反馈折叠层，而不是平行附录`
   - 依赖文件：`docs/03_analysis/03_party_and_camp.md`
   - 这段只负责把前面已经分散的状态折成延迟反馈与关系读回，不再单开人物志、恋爱总览或 camp scene 清单。
   - `Act 收束与终局压力` 也在这里与 `01_macro_structure.md`、`02_quests_and_choices.md` 联读进入，而不是另起独立终局章。
   - 默认 handoff：`docs/03_analysis/05_implementation_validation.md`

5. `收尾：哪些判断已经够稳，哪些仍只是当前最强解释`
   - 依赖文件：`docs/03_analysis/05_implementation_validation.md`
   - 这段负责把前面 4 段重新分级：哪些可写成事实、哪些仍是推断、哪些要继续保留为待验证问题。
   - 结束条件：读者能反向定位回前面各段对应的正文，而不是把实现验证误读成新的开场导论。

### 阶段 6 第四子单元现在固定什么

在 `section skeleton` 已经落成后，阶段 6 的第四步不再继续解释导览结构，而是固定**首轮发布包的最低配置**：

- 入口页至少要有：项目问题摘录、非剧情复述边界摘录、链条总图、边界卡。
- 第一段至少要有：高反应性命题摘录、区域 / 压力梯、说明为何下一段先看局部行动层的 handoff 卡。
- 第二段至少要有：一组“局部 `agency` -> 状态读回”的双联摘录，以及一张链路图。
- 第三段至少要有：一组 `camp fold / delayed feedback` 摘录、一张折返图，以及区分主 spine 与 supporting bundle 的卡片。
- 收尾段至少要有：事实 / 推断 / 待验证问题矩阵，以及一张开放问题卡。

换句话说，仓库现在不只知道“导览稿分几段”，还知道“每一段首轮最少要带什么才能算真的进入发布包”。

这一步的细节分工现在应以两个文件为准：

- `docs/01_methodology/presentation_forms.md`
  负责唯一的 excerpt queue / asset queue / card queue / traceback path 清单。
- `docs/03_analysis/05_implementation_validation.md`
  负责给这些发布单元提供当前最稳的公开证据入口与不可越级摘录的边界。

### 阶段 6 第五子单元现在固定什么

在最低配置已经锁定后，阶段 6 的第五步不再继续补 queue，而是先把最前面的两段落成第一批**实际发布单元**：

- `入口页` 现在已有一组真实的 `excerpt card / asset spec / traceback card`，用于说明项目问题、非剧情复述边界与反应性链条总图。
- `第一段：命题与导航` 现在已有一组真实的 `excerpt card / asset spec / traceback card`，用于说明高反应性命题、区域 / 压力梯，以及为什么下一段先看局部行动层。
- 这批单元的承载文件固定为 `docs/00_project/stage6_entry_first_section_release_units.md`；`presentation_forms.md` 继续负责规则与顺序，`05_implementation_validation.md` 继续负责证据边界。

换句话说，仓库现在不只知道“入口页和第一段最低该带什么”，还已经有了第一批可以直接拿去制作、审阅与继续扩写的发布样板。

### 阶段 6 第六子单元现在固定什么

在入口页与第一段已经有真实发布单元后，阶段 6 的第六步不再继续补规则，而是把**第二段：局部行动到状态回流**也落成第一组真实发布单元：

- 当前承载文件固定为 `docs/00_project/stage6_second_section_release_units.md`
- 这组单元固定包含：
  - `SECOND-EXCERPT-001`
  - `SECOND-ASSET-001`
  - `SECOND-TRACE-001`
- 这一步最重要的口径不是“再找一个更炫的案例”，而是把第二段明确压成一组**章节接力双联卡**：
  - 左侧只负责证明 `04_combat_and_environment.md` 中的局部 `agency` 已经成立
  - 右侧只负责证明 `02_quests_and_choices.md` 中的高可见 `readback` 已经成立
  - 中间必须明确写清：这是一组展示链中的接力关系，不是把 `Grymforge` 与 `Minthara -> Moonrise Towers` 误写成同一条具体因果链

换句话说，仓库现在不只知道“第二段最少要带什么”，也已经有了一组可以直接拿去制作、审阅与继续扩写的第二段样板。

### 阶段 6 第七子单元现在固定什么

在第二段已经有真实发布单元后，阶段 6 的第七步不再继续补营地原则，而是把**第三段：延迟反馈折叠**也落成第一组真实发布单元：

- 当前承载文件固定为 `docs/00_project/stage6_third_section_release_units.md`
- 这组单元固定包含：
  - `THIRD-EXCERPT-001`
  - `THIRD-ASSET-001`
  - `THIRD-TRACE-001`
- 这一步最重要的口径不是“再补几个 camp scene”，而是把第三段明确压成一组**折返层发布单元**：
  - 主卡只负责证明 `03_party_and_camp.md` 中的 `camp fold / delayed feedback` 已经成立
  - 边界条必须同时说明 `reflection / roster-state`、`dialogue accessibility maintenance` 与 `ending-feedback handoff` 仍然只属 supporting bundle / handoff
  - 图尾必须明确交接到 `05_implementation_validation.md`，而不是把证据分级提前吞掉

换句话说，仓库现在不只知道“第三段最少要带什么”，也已经有了一组可以直接拿去制作、审阅与继续扩写的第三段样板。

### 阶段 6 第八子单元现在固定什么

在第三段已经有真实发布单元后，阶段 6 的第八步不再继续补验证原则，而是把**收尾段：证据分级**也落成第一组真实发布单元：

- 当前承载文件固定为 `docs/00_project/stage6_final_section_release_units.md`
- 这组单元固定包含：
  - `FINAL-EXCERPT-001`
  - `FINAL-ASSET-001`
  - `FINAL-TRACE-001`
- 这一步最重要的口径不是“再补一份方法摘要”，而是把收尾段明确压成一组**证据分级发布单元**：
  - 主卡只负责证明前四段必须重新被分到 `事实 / 推断 / 待验证问题` 三层
  - 矩阵图必须同时保留“文档锚点 + Source ID 入口 + 开放问题条”，而不是把验证层画成只有事实没有空白的胜利图
  - `traceback card` 必须明确回链前四段 actual units 与 `05_implementation_validation.md`，而不是让收尾段反向吞掉前面已经落成的实际单元

换句话说，仓库现在不只知道“收尾段最少要带什么”，也已经有了一组可以直接拿去制作、审阅与继续扩写的收尾段样板；阶段 6 的五段首批实际发布单元也因此在当前计划下闭合。

### 阶段 6 第九子单元现在固定什么

在五段 actual units 已经闭合后，阶段 6 的第九步不再继续补新段落，而是把它们压成一份**首轮发布包总装配 / 审阅清单**：

- 当前承载文件固定为 `docs/00_project/stage6_release_package_assembly_review_sheet.md`
- 当前执行基准固定为 `.agent/execplan_stage6_release_package_assembly_review.md`，用于记录第九子单元的 origin / baseline
- 历史续轮 addendum 现在保留为维护记录链；截至 2026-04-26 的最近一次维护记录是 `.agent/execplan_stage6_release_package_assembly_review_round32.md`
- 当前默认维护入口已经进一步收口为 `stage6_release_package_assembly_review_sheet.md` 本身；只有确实命中新 trigger 时，才需要再读最近一次维护记录
- 当前默认维护动作已经进一步压成 `docs/01_methodology/stage6_freeze_maintenance_playbook.md`：后续会话应先按 playbook 做 trigger 判定与四步 maintenance pass，而不是直接重开新的 review round
- 这一步最重要的口径不是“再写一版导览稿”，而是把五段既有单元明确收成一份 assembly / review 层：
  - `assembly map` 只负责说明入口页、第一段、第二段、第三段、收尾段如何装成同一条发布链
  - `review checklist` 只负责核对顺序、handoff、证据强度与 traceback 是否一致
  - `writeback trigger` 只负责判断什么情况下才值得回写单段承载文件

换句话说，仓库现在不只知道“五段各自是什么”，也已经开始回答“这五段合起来时该怎样被装配、怎样被审阅、什么时候不该乱改”。在首轮一致性审阅已经完成、且第十轮补回 `入口页` benchmark traceback、并经 2026-04-26 的第三十二轮继续确认未再出现 actual-unit 级 trigger 后，阶段 6 的首批发布包已经闭合；后续会话默认应维持冻结维护态，而不是继续自动开 `round33`。默认顺序不再是“先想要不要开新 round”，而是“先读 review sheet + playbook 做 no-trigger 判定”；只有出现新的 writeback trigger、正文级改动、handoff 变化、traceback 回退、assembly map 改动，或项目负责人明确要求复核发布链时，才再调用最近一次维护记录。

## 5. 为什么营地 / 长休不应孤立出现

营地不应该作为“角色氛围页”单独出现，而应当出现在“任务 / 战斗 / 区域行动之后”。原因很简单：

### 它依赖上游状态

没有前面发生的任务推进、区域行动、人物关系变化、战斗结果，营地就没有东西可折叠。营地从来不是凭空产生意义，它是一个**读出点**。

### 它支撑下游理解

如果读者先理解了任务回流，再看营地，就会立刻明白：

- 为什么某些反应要延迟到长休出现
- 为什么营地对话可达性会成为补丁 / 热修对象
- 为什么同伴反应不只是 flavour text，而是反馈链的一部分

### 它在展示链中的最佳位置

营地最适合放在：

`局部行动层` 与 `任务回流层` 之后，`Act 收束` 之前。

换句话说，营地是**中游偏后**的反馈折叠层，而不是前言，也不是尾注。

## 6. 任务、战斗、宏观结构、营地应该如何穿插

最容易跑偏的写法，是把它们拆成四条平行栏目。更合适的写法是把它们视作同一条链条上的不同段落：

- 宏观结构决定“玩家此阶段能从哪里进入问题”。
- 战斗 / 环境决定“玩家在局部场景里能怎么尝试”。
- 任务 / Journal 决定“这些尝试如何被记录并回流”。
- 营地 / 长休决定“这些回流如何在后续被集中感知”。

因此，展示中应该穿插的是**链条关系**，不是栏目平均分配篇幅。

## 7. 研究顺序和展示顺序为什么不同

### 研究顺序

研究必须先按区域包推进。原因是证据天然按区域散落：

- 官方区域介绍会按区域写
- 玩家案例会按遭遇 / 任务节点写
- 战斗 / 环境问题要靠具体场景才能稳定判断
- 营地反馈也必须先知道它折叠了哪一段前史
- Journal / Osiris 文档适合作为横向验证，不适合一开始直接写结论

### 展示顺序

展示必须按玩家体验链条推进。原因是读者需要先知道“这条链到底在解释什么”，再去看区域包里的证据如何支撑它。

### 这两者的正确关系

- **研究顺序**负责收证据、压边界、避免空谈。
- **展示顺序**负责让人看懂为什么这一块现在出现、它如何为整体服务。

项目过去的问题，不是研究顺序错，而是没有把展示顺序单独写出来。

## 8. 读者阅读顺序建议

### 只想先看懂项目总逻辑

按这个顺序读：

1. `README.md`
2. `docs/00_project/deconstruction_display_overview.md`
3. `docs/03_analysis/00_core_thesis.md`
4. `docs/03_analysis/01_macro_structure.md`
5. `docs/03_analysis/04_combat_and_environment.md`
6. `docs/03_analysis/02_quests_and_choices.md`
7. `docs/03_analysis/03_party_and_camp.md`
8. `docs/03_analysis/05_implementation_validation.md`

其中 `Act 收束与终局压力` 当前不单列独立入口，而是通过 `01_macro_structure.md`、`02_quests_and_choices.md` 与 `03_party_and_camp.md` 的联读进入。

### 想直接推进项目执行

按这个顺序读：

1. `README.md`
2. `docs/00_project/deconstruction_master_execution_plan.md`
3. `docs/00_project/deconstruction_granular_codex_plan.md`
4. `docs/00_project/current_state.md`
5. `docs/00_project/next_step.md`
6. `docs/00_project/source_index.md`

## 9. 一句话回答“为什么不会再突然去拆营地”

因为现在仓库已经明确写清：

> 营地不是独立平行模块，而是前面区域行动、任务状态和关系变化的反馈折叠层；它只会在那条链条需要它时出现，不会再像从空中掉下来一样突然单开。
