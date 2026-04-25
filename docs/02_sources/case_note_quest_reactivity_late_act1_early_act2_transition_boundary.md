# Case Note

## Case name

Quest Reactivity：`Mountain Pass / Creche -> Shadow-Cursed Lands -> Last Light / Moonrise / Gauntlet` 的 late `Act 1` / early `Act 2` 交接边界

## Related module

`docs/03_analysis/02_quests_and_choices.md`

次级回流模块：
- `docs/03_analysis/05_implementation_validation.md`
- `docs/03_analysis/01_macro_structure.md`

## Question

在已完成的“上游前置链”和“跨 Act readback spine”之间，是否已经存在一组足够稳的公开交接边界，可以把 `Mountain Pass / Creche`、`Shadow-Cursed Lands` 与 `Last Light / Moonrise / Gauntlet` 压成同一条 `gate -> pressure filter -> convergence pack` 的中盘接缝？

## Research boundary

- 本 note 只处理 late `Act 1` 到 early `Act 2` 的交接边界，不重写 `Act 2` 总框架，也不把三个节点扩成地点目录。
- 本 note 不把 `Mountain Pass / Creche` 写成 `Lae'zel` 单人剧情专章；这里只保留它对进入中盘前门槛感的结构职责。
- 本 note 不把 `Shadow-Cursed Lands` 写成影咒 lore 摘要；这里只保留它如何把多入口推进重新过滤进高压条件。
- 本 note 不把 `Last Light / Moonrise / Gauntlet` 写成三份平行地点包；这里只保留它们如何把前面被过滤过的问题束压向较少读回节点。
- 本 note 只写到公开可验证的层级，不反推私有 objective / step 编排。

## First-pass source set

- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-016`

## Transition-boundary matrix

| 链段 | 当前能写成事实的部分 | 当前最稳推断 | 仍待验证 |
| --- | --- | --- | --- |
| `Mountain Pass / Creche` | `Patch #3` 直接暴露对话门槛、局部敌意、即时伙伴反应与 `camp night` 后果读取边界。来源：`BG3-OFF-016` | 这块当前最稳的职责不是再展开新问题网，而是把 late `Act 1` 压成进入中盘前的高压 gate：你如何通过门槛、如何处理局部权威、以及这些处理如何立刻或延迟被读取。基于 `BG3-OFF-003`, `BG3-OFF-016` | 还不能把这块与 `Act 2` 切换之间的具体警告、规则和完整 objective 映射写成事实表。 |
| `Shadow-Cursed Lands` | `Patch 7` 直接暴露 `Act II` 的 `writing and flow`、`scripting`、角色反应与营地场景维护；`Swiss cheese` 语言说明高压不等于单入口。来源：`BG3-OFF-002`, `BG3-OFF-003` | 这块当前最稳的职责不是“收束”，而是 `pressure filter`：玩家仍可从不同路径接近目标，但每条推进都必须在更持续的风险和更密的前史读回条件下继续成立。基于 `BG3-OFF-002`, `BG3-OFF-003` | 还不能把区域内部哪些风险变量已接近 `objective / step`、哪些仍只是 `flow / reaction` 维护边界写成事实表。 |
| `Last Light / Moonrise / Gauntlet` | `Patch 7` 直接写到 `Moonrise Towers` 会重读 `Act I` 的 Minthara 处理；Journal 文档继续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 结构语言。来源：`BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 这组节点当前最稳的职责不是平行地点包，而是 `convergence pack`：前面已经被过滤过的状态差异、角色反应与任务推进，在这里开始被压向较少的读回节点并逼近后续结算。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把 `Last Light`、`Moonrise`、`Gauntlet` 三者内部的精细分工或完整 objective / step 映射写成事实表。 |

## What can be written as facts

- `事实`：`Patch #3` 直接暴露 `Mountain Pass / Creche` 的多重维护边界：拒绝 `Vlaakith` 后的多余检定、`Voss` 敌意变化、即时伙伴反应与 `camp night` 后果读取都需要被单独修复。来源：`BG3-OFF-016`
- `事实`：`Patch 7` 在 `Act II`、`Writing and Flow` 与 `Scripting` 条目中集中暴露中盘任务流、角色反应、营地夜晚场景与对话优先级的维护边界。来源：`BG3-OFF-002`
- `事实`：`Patch 7` 明确写到被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对 `Act I` 的处理作出反应。来源：`BG3-OFF-002`
- `事实`：Adam Smith 用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构，说明进入高压阶段并不自动意味着多入口失效。来源：`BG3-OFF-003`
- `事实`：官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为公开更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## What can only be written as inferences

- `推断`：这组交接边界当前最稳的写法，不是 “`Act 1` 结束，`Act 2` 开始” 这种章节名义切换，而是功能切换：`Mountain Pass / Creche` 先把前史压成高压 gate，`Shadow-Cursed Lands` 再把多入口推进过滤进持续风险条件，`Last Light / Moonrise / Gauntlet` 最后把这些已被过滤的差异压向较少的读回节点。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-016`
- `推断`：因此这组交接是现有主干的下一层，而不是另一份 `Act 1` / `Act 2` 目录；它解释的是“反应性如何跨过阶段接缝继续成立”，不是“这几个地点各自有什么内容”。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `推断`：从公开证据强度看，`Mountain Pass / Creche` 的若干局部门槛已接近 `objective / step` 邻近层，但 `Shadow-Cursed Lands` 仍更稳地停留在 `pressure / flow bundle`，`Last Light / Moonrise / Gauntlet` 则更稳地停留在 `convergence pack / reread bundle`。基于 `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`

## What must remain open questions

- `待验证问题`：除 `Minthara -> Moonrise Towers -> Act II reaction` 外，是否还能找到第二条同级别的公开中盘读回链，来减轻这段交接对单一高可见路径的依赖？
- `待验证问题`：`Mountain Pass / Creche` 中哪些门槛与敌意变化已经足以继续压到 `objective / step` 邻近层，哪些仍只能停留在补丁边界摘要？
- `待验证问题`：`Shadow-Cursed Lands` 内部哪些压力变量与推进分工能继续稳定压到 Journal 层，哪些目前仍更适合停留在 `flow / reaction / camp` 维护边界？
- `待验证问题`：`Last Light / Moonrise / Gauntlet` 三者中，哪些读回与压缩职责可以继续分层，哪些目前仍只能作为同一块 `convergence pack` 被公开描述？

## Source IDs

- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-016`

## Notes

- 当前最稳的仓库口径应是：late `Act 1` / early `Act 2` 的关键，不在于“有没有阶段切换”，而在于“状态回流在切换处被怎样重新过滤、加压与压缩”。
- 这份 note 的作用不是替代 `Act 2` 区域包或收束点 note，而是把既有两块成果之间的接缝压成一条可复述、可继续验证的横向子单元。
