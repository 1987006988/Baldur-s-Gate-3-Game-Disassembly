# Party and Camp

## Question

同伴、营地与长休，如何把前序选择、关系推进和延迟反馈缝合成一种“世界仍在回应玩家”的体验？

## 总判断

营地 / 长休在 BG3 里不是单纯的“休整容器”，而是一个把分散在任务推进、角色状态与关系互动中的变化集中回收、再呈现给玩家的折返点：它既承担叙事节奏上的“停顿与再解释”，也承担系统节奏上的“状态汇流与可达性维护”。对玩家来说，这会表现为“我刚才做的事在营地被重新接住”；对系统来说，这意味着任务状态、角色状态、对话可达性与 `companion reaction` 会在营地节点重新汇流并被显性维护。

这一判断的首轮支撑不来自“同伴剧情总整理”，而来自三类更可验证的入口：1 条强案例（`Dark Urge` 的营地 bard 事件）、1 条候补案例（`Minthara` 的营地反应链）、以及一组系统型补丁锚点（补丁/热修明确暴露营地反馈边界与维护对象）。本轮补强后，还加入了 1 条非 `Minthara` 的官方平行锚点，用来验证营地 reaction / 对话可达性并非孤例。来源：`BG3-OFF-002`, `BG3-OFF-005`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`, `BG3-PLY-002`

当前可写为事实的部分：
- `事实`：官方明确确认 `Dark Urge` 流程中“某位 bard 会在营地以可控制角色身份暂时加入队伍”，且强调是 `TEMPORARILY`，不是稳定的新同伴路线。来源：`BG3-OFF-005`
- `事实`：Patch 7 又把这条事件进一步压实到 `Alfira`、`temporarily` 和“不是新同伴路线”的官方 framing 上。来源：`BG3-OFF-002`
- `事实`：官方热修明确把 Minthara 的营地对话可达性与 `companion reaction` 当作需要修复的对象，包含“营地外解散后回营地无法对话”等边界问题。来源：`BG3-OFF-008`
- `事实`：官方热修也在非 `Minthara` 条目中明确修复了营地 scene / dialogue accessibility 与角色识别问题，例如 Astarion 的 camp scene、Voss 的 camp 对话、Mizora 的回营地与 Wyll 的后续识别。来源：`BG3-OFF-010`
- `事实`：官方补丁条目持续暴露并修复 `camp night`、`character reaction`、`writing / flow` 等与营地/长休直接相关的反馈链边界；且营地同时承载队伍状态处理与跨 Act 的叙事反思时刻。来源：`BG3-OFF-002`, `BG3-OFF-007`

当前只能写为推断的部分：
- `推断`：BG3 的一部分高反应性来自“延迟反馈被放到营地 / 长休节点重新呈现”，而不只来自任务现场的即时结算。
- `推断`：营地最重要的系统价值之一，不是单独提供对白，而是把分散在任务、关系和角色状态中的结果重组为玩家可感知的二次反馈。

当前必须保留为待验证问题的部分：
- `待验证问题`：`Dark Urge bard` 事件有哪些稳定后续分支、哪些后续差异跨版本成立？现有官方来源不足以逐条对应这些细节。
- `待验证问题`：`Minthara` 案例更像角色特例修补，还是能外推为更普遍的营地反馈调度规律？
- `待验证问题`：长休触发顺序、营地事件优先级与任务状态回流之间，是否存在更稳定的公开可验证模式？

## 玩家层

玩家视角下，“营地”之所以重要，不是因为它提供了更多对白，而是因为它把“我刚才做的事”重新转译为可被同伴、关系与世界状态回应的内容：同伴评论、关系推进、可对话/不可对话、临时入队/离队等信号，都会让玩家把后果理解为仍在发生的过程，而不是任务现场的一次性结算。

在证据层面，本模块首轮不会把玩家感受直接升级为系统事实；我们只把社区讨论当作“玩家如何感知反馈”的案例线索，并让它去对齐官方可验证锚点：
- `案例线索`：社区把 `Dark Urge` 的 bard 事件讨论为“长休触发 -> 营地状态变化 -> 后续差异”的高辨识度节点，但它只能说明玩家如何叙述与感知，不足以说明系统细节与全局规律。来源：`BG3-PLY-002`
- `事实锚点`：官方确实确认该事件至少包含“营地临时入队”这一可见状态变化，从而使“玩家把反馈理解为营地折返”具备最小可验证落点。来源：`BG3-OFF-005`
- `事实锚点`：Patch 7 又把它进一步写到 `Alfira` 的具体临时状态上，因此“这只是社区误读或模糊剧透”的风险已明显下降。来源：`BG3-OFF-002`
- `事实锚点`：官方也确实把“营地中的对话可达性/同伴反应缺失”当作需要修复的边界，因此玩家对“后果没被接住”的不适并非纯主观，而对应到公开维护对象。来源：`BG3-OFF-008`

## 系统层

把营地 / 长休理解为“反馈汇流点”，核心不是把它神秘化，而是把它当作一个节奏切换器：把前序事件产生的分散状态，迁移到一个低压、可集中触发的空间中再呈现。用最小关系链描述就是：

1) 前置触发：任务推进/区域推进/战斗结局/关系互动造成状态变化。  
2) 节奏切换：长休或回营地把这些状态带入可集中触发的节点。  
3) 反馈落点：营地通过对话、`companion reaction`、临时队伍状态变化、可达性开放/关闭、以及跨章节“反思时刻”等形式回收状态。  
4) 体验生成：玩家把这种延迟且重组后的反馈理解成“同伴活着”与“世界还记得我做了什么”。

这条链路中，首轮可以被公开来源直接支撑的边界主要在第 3 步：营地的“反馈落点”不是自然发生，而是被明确维护与修复的系统对象：
- `事实`：官方将营地夜晚、角色反应与 `writing / flow` 的触发与顺序问题列为持续修复对象。来源：`BG3-OFF-002`
- `事实`：官方将营地对话可达性与 `companion reaction` 的缺失列为需要热修的边界。来源：`BG3-OFF-008`
- `事实`：官方也在多个非 `Minthara` 条目上修复营地 scene / dialogue 的可达性、识别正确性与角色在场状态。来源：`BG3-OFF-010`
- `事实`：官方同时把营地当作队伍状态处理入口（合作模式队伍成员去留）与跨 Act 的叙事反馈节点（反思时刻）。来源：`BG3-OFF-007`

因此，本模块首轮的系统判断会刻意收束为两句可被证据约束的说法，而不外推成“所有营地对白都按统一规律组织”：
- `推断`：营地 / 长休是“把状态汇流成反馈”的稳定设计意图方向（因为其边界在补丁/热修中反复被暴露与维护）。
- `推断`：营地反馈链的关键系统问题是“可达性与调度”，而不是“内容总量”。

补充前序入口：
- `事实`：`Patch 7` 说明 nautiloid 结束后的装备交接会在地表招募阶段继续被读取，例如 `Shadowheart / Lae'zel` 在后续被招募时需要获得新的装备。来源：`BG3-OFF-002`
- `推断`：这意味着第一批营地前史并不是从营地节点凭空开始，而是由 `Act 1 地表主区` 的招募顺序、opening state 续接与早期问题网密度先行生成。对营地模块而言，地表不是背景板，而是反馈折叠层的真正上游。来源：`BG3-OFF-002`
- `待验证问题`：哪些地表主区的早期顺序差异会稳定影响第一批营地事件调度，当前还缺更直接的公开来源。

补充下游入口：
- `事实`：`Hotfix #5` 直接修复了 Minthara 的营地对话可达性、`companion reaction`，以及营地外解散后回营地无法对话的问题；这说明 `Grove / Goblin` 冲突的后果会在营地层被重新读取。来源：`BG3-OFF-008`
- `事实`：`Patch 7` 又把同一冲突的另一部分延迟结果压实到后续区域与章节：被击倒的 Minthara 会逃往 `Moonrise Towers`，并在 `Act II` 对玩家的处理作出反应。来源：`BG3-OFF-002`
- `推断`：因此 `Grove / Goblin` 是 `Act 1` 第一块能把“冲突处理方式”与“营地反馈可达性”写进同一条链路的区域包；营地在这里不是独立角色页，而是冲突后果的一个下游读出点。来源：`BG3-OFF-002`, `BG3-OFF-008`
- `待验证问题`：除 Minthara 外，哪些 `Grove / Goblin` 处理结果也会以同样稳定的方式折返到第一批营地反馈？

补充高压门槛入口：
- `事实`：`Patch #3` 直接修复了 `Lae'zel` 在 `Crèche Y'llek` 遇到 `Dream Visitor` 后的反应时机，使其会在对话结束后立即触发。来源：`BG3-OFF-016`
- `事实`：同一补丁还修复了 `Avatar Lae'zel` 在 `camp night` 中过早反思 `crèche` 后果的问题；在真正访问 `zaith'isk` 之前，这段反思不应提前发生。来源：`BG3-OFF-016`
- `事实`：同一补丁同时暴露了这块区域与门槛 / 敌意处理的耦合边界：`Vlaakith` 相关对话可能被错误检定挡住，`Voss` 相关 `Deception` 结果会影响 `githyanki` 是否敌对。来源：`BG3-OFF-016`
- `推断`：这说明 `Mountain Pass / Creche` 不应被当作营地模块外部的纯剧情插曲；它更像 `camp night` 张力的又一块上游压力包，局部权威冲突与伙伴反应会在区域现场和营地后续之间连续读出。来源：`BG3-OFF-016`
- `待验证问题`：这块的哪些后果会稳定折返到第一批 `camp night`，哪些只停留在局部对话或敌意变化层，目前还缺更直接的公开来源。

补充中盘入口：
- `事实`：`Patch 7` 明确写到，被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对玩家曾在 `Act I` 击倒她作出反应。来源：`BG3-OFF-002`
- `事实`：同一补丁的 `Writing and Flow`、`Scripting`、`Act II` 条目包含大量与任务流、营地夜晚场景、角色反应、对话优先级相关的修复。来源：`BG3-OFF-002`
- `推断`：这说明进入 `Act 2` 后，营地 / 同伴反馈不再只是接住某个局部区域的余波；它开始更紧地参与“前史如何被重新读取”这一中盘结构过程。来源：`BG3-OFF-002`
- `推断`：因此 `Act 2` 对营地模块的首轮价值，不是再补一批零散 companion 条目，而是先把它写成“高压条件下的反馈折叠层”：前一阶段处理差异会更靠近收束点与中盘推进被重新显性化。来源：`BG3-OFF-002`
- `待验证问题`：`Act 2` 中哪些后果会稳定折返到 `camp night` 或营地对话，哪些更主要停留在地区现场或收束点附近被读取，目前仍缺更直接的公开来源。

补充中盘收束点组：
- `事实`：`Patch 7` 的 `Writing and Flow`、`Scripting`、`Act II` 条目持续把营地夜晚场景、角色反应、对话优先级与任务流一起暴露为需要维护的同一批边界。来源：`BG3-OFF-002`
- `事实`：同一补丁还明确写到，被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对玩家曾在 `Act I` 的处理作出反应。来源：`BG3-OFF-002`
- `事实`：官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此 `Last Light / Moonrise / Gauntlet` 对营地模块当前最稳的价值，不是再补三个地点的同伴对话摘录，而是把它们写成“反馈折叠更靠近收束节点”的中盘读出层：前面分散保存的关系与处理差异，开始更密地在这组节点附近被重新显性化。来源：`BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：与 `Shadow-Cursed Lands` 的前场压力相比，这组节点更像把营地 / 同伴反馈从“持续陪跑”推向“集中读回”：营地不该在这里被写成独立插曲，而应被理解成收束点组的下游折返层。来源：`BG3-OFF-002`
- `待验证问题`：这组节点中的哪些后果会稳定折返到 `camp night` 或营地对话，哪些仍主要停留在现场任务流与角色反应层，目前仍缺更直接的公开来源。

## 阶段 5 / 首条跨区域 camp fold 主干

本轮不再把营地模块停留在“强案例 + 候补案例 + 补丁锚点”的并列结构，而是把既有入口压成第一条跨区域 `camp fold / delayed feedback` spine：

| 链段 | 当前可稳定写到的层级 | 这段在主干里承担什么职责 | 当前不能升级的部分 |
| --- | --- | --- | --- |
| `Act 1 地表主区` | `upstream state-density layer` | 生成第一批营地折叠会读取的前史密度。来源：`BG3-OFF-002` | 还不能把具体早期顺序差异写成 camp scene 调度事实表。 |
| `Dark Urge bard` | `local camp-state-shift sample` | 证明某些前序触发会在营地被重新读成角色存在状态变化。来源：`BG3-OFF-005`, `BG3-OFF-002`, `BG3-PLY-002` | 还不能把完整后续分支与后续差异写成全局规律。 |
| `Grove / Goblin` | `first delayed camp readout bundle` | 证明冲突处理方式会在营地对话可达性与 `companion reaction` 层被重新读取。来源：`BG3-OFF-008`, `BG3-OFF-002` | 还不能把除 `Minthara` 外的全部后果升级成同级 camp fold 链。 |
| `Mountain Pass / Creche` | `gate / tension -> camp-night delayed reread bundle` | 证明局部门槛、敌意变化与伙伴张力会在 `camp night` 被延迟读回。来源：`BG3-OFF-016` | 还不能把整块 late `Act 1` / early `Act 2` 过渡误写成新的显式任务主链。 |
| `Last Light / Moonrise / Gauntlet` | `convergence-adjacent reread bundle` | 说明中盘收束点组会把营地读回推向更靠近收束节点的位置。来源：`BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把具体哪些 `Act II` 后果稳定折返到 camp scene 列表写成事实表。 |
| `终局组织与收束压力` | `ending-feedback handoff bundle` | 说明 late-game 的读回压力开始从 camp fold 移交给终局组织位与结算反馈层。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把 late-game `ending feedback` 写成第二条对称的 camp spine。 |

- `推断`：因此阶段 5 / `Companion / Camp / Long Rest` 当前已经拥有第一条可复述的横向主干，但它不是第二条 `Quest Reactivity`；它的结构更接近“前史密度生成 -> 局部 camp-state shift -> delayed camp readout -> camp-night reread -> convergence-adjacent reread -> ending-feedback handoff”。
- `推断`：真正进入这条主干中心的，只能是被公开来源直接点名为会在营地被重新读取、重新排序或被持续维护的状态边界；`Karlach` 的跨 `Act` 反思时刻与非 `Minthara` camp fix 当前仍更稳地停在 `reflection / dialogue accessibility supporting bundle` 层。来源：`BG3-OFF-007`, `BG3-OFF-010`
- `推断`：这也意味着营地模块当前最需要守住的边界，不是“再找更多 camp scene”，而是避免把 `Act II` 收束点组与 late-game `ending feedback` 误写成新的 objective 主链或人物志目录。

## 阶段 5 / second public camp spine ceiling / late-game boundary

本轮不再继续追“第二条公开营地主干”，而是把最可能被误升的锚点压成证据上限矩阵：

| 候选锚点 | 公开锚点 | 当前最多可升级到的层级 | 为什么不足以升成第二条公开 spine |
| --- | --- | --- | --- |
| `BG3-OFF-007`：`Withers' Wardrobe` + `Karlach` 跨 `Act` 反思 | `Patch #2` 直接把营地写成队伍状态处理入口，并补入 `Karlach` 的跨 `Act` 反思时刻。来源：`BG3-OFF-007` | `reflection / roster-state supporting bundle` | 这组条目证明营地是 roster 管理与反思落点，但还没有把多个区域前史重新压成单一 camp-centered readback chain。 |
| `BG3-OFF-010`：非 `Minthara` camp scene / dialogue fixes | `Hotfix #3` 直接修复 Astarion、Voss、Mizora、Wyll 等多个非 `Minthara` 的 camp scene / dialogue accessibility 问题。来源：`BG3-OFF-010` | `dialogue accessibility maintenance bundle` | 这些修复分散、局部且跨角色，能证明维护广度，却不足以组成同一条可复述的跨区域 spine。 |
| `Last Light / Moonrise / Gauntlet` 的中盘读回 | 既有第一条营地主干已把这组节点压成 `convergence-adjacent reread bundle`。 | `convergence-adjacent reread bundle` | 这组节点当前更稳地承担“营地读回更靠近收束点被重读”的职责，而不是第二条 camp-centered 主链的中段。 |
| late-game `ending feedback` / 终局组织读回 | 既有第一条营地主干与终局 organization note 已把这层压成 `ending-feedback handoff bundle`。 | `ending-feedback handoff bundle` | 晚期读回压力已开始从 camp fold 让渡给终局组织位与结算反馈层，不能再反向写成第二条对称营地主链。 |

- `事实`：`BG3-OFF-007` 直接确认营地承担合作模式队伍成员去留处理，并补入 `Karlach` 在 `Acts 1/2` 间的反思时刻。来源：`BG3-OFF-007`
- `事实`：`BG3-OFF-010` 直接确认多个非 `Minthara` 的 camp scene / dialogue accessibility / 在场识别问题会被单独修复。来源：`BG3-OFF-010`
- `推断`：因此 `BG3-OFF-007` 与 `BG3-OFF-010` 当前最重要的价值，不是生成第二条公开营地主干，而是把营地反馈链的维护范围从 `Dark Urge bard` 与 `Minthara` 两个高辨识度锚点扩展到 roster 管理、跨 `Act` 反思与分散的非 `Minthara` 可达性维护。
- `推断`：在当前公开来源下，阶段 5 / `Companion / Camp / Long Rest` 的最稳结构已经收束为“1 条 public camp fold spine + 2 类 supporting bundles + 1 个 late-game handoff boundary”，而不是“2 条对称营地主干”。
- `推断`：因此营地模块当前应视为在现有来源下完成收口；除非出现更强、能稳定串起多区域前史与营地读回的官方来源，否则不要继续追第二条 public camp spine，也不要回到 camp scene 清单或同伴人物志写法。

## 实现验证层

本模块的实现验证目标不是反向工程出营地系统全貌，而是用公开材料确认：营地反馈不是偶然演出，而是被持续维护的系统边界；并把首轮能验证的内容限制在“官方明确写到/修到”的层级上。

本轮采用的验证策略是“三段式”：
- 用补丁/热修/社区更新锁定维护对象与边界（营地夜晚、角色反应、对话可达性、临时入队等）。
- 用强/候补案例把这些边界落到一条可复述的最小链路上。
- 把无法公开验证的部分统一降级为 `推断` 或 `待验证问题`，避免用社区讨论填补系统细节空缺。

## 强案例：Dark Urge 营地 bard 事件

这条案例之所以被选为首轮强案例，不是因为证据最完备，而是因为它最容易闭合“前置触发 -> 营地节点 -> 状态变化 -> 玩家可感知差异”的最小链路，并且至少有 1 条官方来源可以把链路钉在可验证的事实锚点上。

最小链路（首轮只写到证据允许的层级）：
- 前置触发（保守表述）：玩家以 `Dark Urge` 身份推进到相关夜间事件语境。  
  - `事实`：官方把这一变化明确放在 `Dark Urge` 相关改动语境中。来源：`BG3-OFF-005`
- 营地节点：该变化发生在营地，并表现为“可控制角色在营地暂时加入队伍”。  
  - `事实`：官方明确确认 `a certain bard` 会在营地以可控制角色身份暂时入队，并强调 `TEMPORARILY`。来源：`BG3-OFF-005`
- 事件 framing：后续官方补丁又再次回指这条事件，并把它压实到 `Alfira` 的具体临时状态上，同时强调这不是“新同伴”路线。  
  - `事实`：Patch 7 直接重申这是一条短暂营地事件，并补足 `Alfira` 可升级、无蝌蚪、不能用 Magic Mirror 等状态边界。来源：`BG3-OFF-002`
- 后续差异（暂不升级）：社区把它讨论为会引出后续差异的节点，但现阶段不足以把“具体后续差异分布”写成事实。  
  - `案例线索`：社区讨论可用于观察玩家如何叙述“长休触发 -> 角色替换/保留 -> 后续差异”，但不能承担系统细节。来源：`BG3-PLY-002`
  - `待验证问题`：哪些后续反馈稳定存在、是否跨版本成立、以及它们更像任务脚本回流还是营地事件调度，目前缺乏与之逐条对应的官方来源。

在正文论证中的使用边界：
- `推断`：该案例可支撑“营地能承接前序触发并产生可见状态变化”的判断，但不支撑“所有营地反馈都按同一机制闭环”的泛化结论。
- `推断`：该案例更适合作为“任务与选择回流”与“营地/长休反馈汇流”之间的耦合点，而不是独立证明营地系统全貌。来源：`BG3-OFF-005`, `BG3-OFF-002`

## 候补案例：Minthara 营地反应链

这条案例更像“系统边界暴露点”：它强于证明“营地反馈链被官方单独维护”，弱于构成一条完整的剧情折返闭环。因此它被放在候补位置，用来校正强案例的特例风险，而不是取代强案例承担主论证。

首轮可验证的关键边界：
- `事实`：官方热修明确修复 Minthara 的营地对话可达性问题，并包含 `companion reaction` 与关系反馈相关条目。来源：`BG3-OFF-008`
- `事实`：官方热修明确把“营地外解散后回营地无法对话”当作需要修复的问题。来源：`BG3-OFF-008`
- `事实`：官方补丁为营地夜晚、角色反应与 `writing / flow` 的触发与顺序问题提供更高层的“持续维护对象”背景。来源：`BG3-OFF-002`
- `事实`：非 `Minthara` 的官方热修条目也已存在，例如 Astarion 的 camp scene、Voss 的营地对话、Mizora 的回营地与 Wyll 的后续识别修复。来源：`BG3-OFF-010`

可写为推断但必须收束的结论：
- `推断`：营地中的 `companion reaction` 与关系反馈不只是装饰性文本，而是玩家判断“后果是否被接住”的主要交互面之一。
- `推断`：把这条案例放回 `Grove / Goblin` 区域包看，它的价值不在于补一个角色特例，而在于证明“冲突处理方式会在营地被重新读出”。来源：`BG3-OFF-002`, `BG3-OFF-008`
- `待验证问题`：在已有 `Minthara` 与非 `Minthara` 平行条目后，剩余问题不再是“是否存在非 `Minthara` 官方条目”，而是这些条目是否足以支撑“营地反馈链被系统性维护”的更高层判断。

## 系统型补丁锚点

系统型补丁锚点的作用，是把“营地反馈”从单一剧情事件拉回到公开可见的维护对象：团队在补丁与热修中反复修的不是“多写两段对白”，而是营地反馈链的边界条件（触发、顺序、可达性、反应与队伍状态处理）。

首轮锚点（只写到可验证粒度）：
- `事实`：`BG3-OFF-002` 以补丁条目形式持续暴露并修复 `camp night`、`character reaction`、`writing / flow`、以及与任务后续反应相关的问题。来源：`BG3-OFF-002`
- `事实`：`BG3-OFF-007` 同时暴露营地作为队伍状态处理入口与跨 Act 叙事反馈节点（反思时刻）的双重角色。来源：`BG3-OFF-007`
- `事实`：`BG3-OFF-008` 直接暴露营地对话可达性与 `companion reaction` 会被单独热修。来源：`BG3-OFF-008`
- `事实`：`BG3-OFF-010` 说明这种维护不只出现在 `Minthara` 个案，也出现在 Astarion、Voss、Mizora、Wyll 等非 `Minthara` 条目上。来源：`BG3-OFF-010`

可写为推断的系统结论（收束版）：
- `推断`：这些补丁/热修条目共同说明，营地 / 长休是一个被长期维护的反馈层，而不是个别剧情特例的落点。
- `推断`：营地反馈链的关键工程风险点在“状态回流与可达性”，这也是为何它会以补丁条目的形式不断被显性修复。来源：`BG3-OFF-002`, `BG3-OFF-008`

## 阶段 5 / Companion / Camp / Long Rest 当前出口

- `推断`：本模块当前的正式阶段出口已经清楚：`1` 条 public `camp fold / delayed feedback` spine，外加 `reflection / roster-state`、`dialogue accessibility maintenance` 与 `ending-feedback handoff` 三类已锁定的 supporting bundle / handoff 边界。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`
- `推断`：在没有更强官方来源前，`Karlach` 反思、非 `Minthara` camp fix 与 late-game `ending feedback` 都不应再被重写成第二条对称营地主干。来源：`BG3-OFF-007`, `BG3-OFF-010`
- `推断`：因此阶段 5 对营地模块的正确收口，不是继续追 camp scene，而是把“营地是反馈折叠层”沉到统一 exit matrix，并把下一步切到阶段 6 / 展示收束。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`

## Stage 6 Display Role

- `推断`：在当前展示链里，本模块必须晚于 `02_quests_and_choices.md` 出现；它负责把前面已经建立的状态回流折成营地 / 长休的延迟反馈，而不是单独承担“同伴内容入口”。来源：`BG3-OFF-002`, `BG3-OFF-008`, `BG3-OFF-010`
- `推断`：因此本模块最适合被压成“任务结果 -> 营地 / 长休 -> 关系反馈”的折返图、循环图与少量强案例卡，而不适合再被写成人物志、恋爱总览或 camp scene 清单。来源：`BG3-OFF-005`, `BG3-OFF-007`, `BG3-OFF-010`
- `推断`：本模块的默认 handoff 应该是 `05_implementation_validation.md`：营地反馈的价值在展示链里是把状态折回来，再由实现验证层说明哪些折返已经够稳、哪些仍只是当前最强解释。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`

## Stage 6 Release Anchor

- `THIRD-EXCERPT-001` 可安全摘录本文件中的“营地 / 长休不是休整容器，而是反馈折返点”总判断，以及阶段 5 首条 `camp fold / delayed feedback` 主干里的高层结构：`Act 1 地表主区` 负责前史密度，`Dark Urge bard` 负责局部 `camp-state shift`，`Grove / Goblin` 负责第一批 delayed camp readout，`Mountain Pass / Creche` 负责 `camp night` reread。来源：`BG3-OFF-002`, `BG3-OFF-005`, `BG3-OFF-008`, `BG3-OFF-016`, `BG3-PLY-002`
- `THIRD-ASSET-001` 在本文件中应被压成“`task result -> camp / long rest -> reread` 折返图”的主体：左侧只保留前史密度与高辨识度折返入口，中心只保留 `camp fold / delayed feedback`，右侧只保留必须交接到验证层的 supporting-bundle / handoff 边界。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`, `BG3-OFF-016`
- `THIRD-TRACE-001` 在本文件中的默认职责只证明第三段主卡的正文锚点已经成立；它不能把 `Dark Urge bard`、`Minthara`、`Lae'zel` 与 `Karlach` 硬写成同一条具体因果链，也不能把 `reflection / roster-state`、`dialogue accessibility maintenance` 与 late-game `ending-feedback handoff` 误写成第二条公开营地主干。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`, `BG3-OFF-016`

## Source IDs

- `BG3-OFF-002`
- `BG3-OFF-005`
- `BG3-OFF-007`
- `BG3-OFF-008`
- `BG3-OFF-010`
- `BG3-OFF-016`
- `BG3-PLY-002`

## Open questions

- `第三案例候选（不升级为正文案例）`：是否需要在后续补强一个非 `Dark Urge`、非 `Minthara` 的营地反馈案例（当前候选为“救出 Halsin 后的营地同伴对话恢复”），以降低首轮论证对高辨识度特例的依赖？来源：`BG3-OFF-009`
- 长休触发顺序、营地事件优先级与任务状态回流之间，是否存在可公开验证的更稳定模式？
- `Dark Urge bard` 在已被 `BG3-OFF-002` 与 `BG3-OFF-005` 双重锚定后，剩余缺口主要集中在哪些“后续反馈”条目上，才能进一步闭合完整链路？
- `Act 1 地表主区` 的哪些早期顺序差异最值得继续追踪到第一批营地折返，以证明“前史密度 -> 营地折叠”不是纯口头解释？
- `Mountain Pass / Creche` 中哪些门槛 / 对话 / 局部敌意变化会稳定沉到营地后续，而不是只在区域现场被读取？
- 如果未来要重新打开第二条公开营地主干，至少需要什么级别的官方来源，才能让 `BG3-OFF-007` 或 `BG3-OFF-010` 这类 supporting bundle 升级为 spine anchor？

## Revision notes

- 2026-04-25：补入阶段 6 的第三段 release anchor，明确 `THIRD-EXCERPT-001`、`THIRD-ASSET-001` 与 `THIRD-TRACE-001` 只能把本模块压成 `camp fold / delayed feedback` 折返层，而不能误升 supporting bundle / handoff 为第二条公开营地主干。
- 2026-04-25：新增阶段 5 / `Companion / Camp / Long Rest` 当前出口小节，明确本模块在当前公开来源下已形成“1 条 public spine + supporting bundles + handoff boundary”的统一收口。

- 2026-04-25：新增阶段 5 / `Companion / Camp / Long Rest` 的 second public camp spine ceiling / late-game boundary 结论，明确 `BG3-OFF-007` 当前只稳定支撑 `reflection / roster-state supporting bundle`，`BG3-OFF-010` 当前只稳定支撑 `dialogue accessibility maintenance bundle`，而 late-game `ending feedback` 继续停在 `ending-feedback handoff`，不足以组成第二条对称营地主干。
- 2026-04-22：建立同伴与营地模块骨架。
- 2026-04-22：根据 `02_quests_and_choices` 的首轮回写做最小同步，补入“营地作为任务反馈折返点”的当前判断。
- 2026-04-23：把 `03_party_and_camp` 从“首轮回写框架”推进为“首轮完整正文”，并保持“强案例 + 候补案例 + 系统型补丁锚点”结构与事实/推断/待验证问题分离。
- 2026-04-23：完成一次小范围证据补强迭代：用 `BG3-OFF-002` 进一步压实 `Dark Urge bard` 的官方 framing，并补入 `BG3-OFF-010` 作为非 `Minthara` 的营地 reaction / 对话可达性平行锚点。
- 2026-04-24：补入 `Act 1 地表主区` 作为营地前史生成层的最小必要入口，明确营地折叠依赖地表阶段先生成的招募与状态密度。
- 2026-04-24：补入 `Grove / Goblin` 作为地表之后的第一块冲突下游，明确 Minthara 营地反馈链应被视为区域包后果读出，而不是孤立角色补丁。
- 2026-04-24：补入 `Mountain Pass / Creche` 作为营地张力的高压前史入口，明确 `Lae'zel` 的即时反应与 `camp night` 后果读取应被理解为区域门槛的下游读出。
- 2026-04-24：补入 `Act 2` 作为中盘反馈折叠入口，明确这阶段应先被写成“前史状态在高压条件下被重新读取”，而不是补零散 companion 气氛条目。
- 2026-04-24：补入 `Last Light / Moonrise / Gauntlet` 作为 `Act 2` 的中盘收束点组，明确营地 / 同伴反馈在这里更适合被理解成“收束节点附近的集中读回”，而不是地点附带对白集合。
- 2026-04-25：新增阶段 5 的第一条跨区域 `camp fold / delayed feedback` 主干，把 `Act 1 地表主区 -> Dark Urge bard / Grove / Goblin -> Mountain Pass / Creche -> Last Light / Moonrise / Gauntlet -> 终局组织与收束压力` 压成同一条营地 spine，并明确晚期 `Act 2` / `Act 3` 读回当前只能写成 `convergence-adjacent reread` 与 `ending-feedback handoff`，不能误升为第二条 objective 主链。
- 2026-04-25：补入阶段 6 的模块导览职责，明确本模块在展示链中承担“延迟反馈折叠层”而不是独立人物入口，并默认 handoff 到 `05_implementation_validation.md`。
