# Case Note

## Case name

Shadow-Cursed Lands：区域压力循环

## Related module

`docs/03_analysis/04_combat_and_environment.md`

次级回流模块：
- `docs/03_analysis/01_macro_structure.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/05_implementation_validation.md`

## Question

`Shadow-Cursed Lands` 能否被写成 `Act 2` 的第一个具体压力组织器，即：它的核心价值不在于影咒气氛本身，而在于如何把区域风险、路径选择、遭遇判断与推进方向重新绑成一条中盘压力循环？

## Research boundary

- 本 note 只处理 `Shadow-Cursed Lands` 作为区域包的功能，不展开 `Last Light`、`Moonrise`、`Gauntlet` 的收束点细节。
- 本 note 不写影咒 lore 摘要，也不把具体区域机制、判定规则或完整 objective / step 映射提前写死。
- 本 note 只回答“压力如何组织区域推进”，不回答中盘所有后续结算如何完成；后者留给下一块收束点组。

## First-pass source set

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`

## Pressure-loop frame

| 维度 | 当前能写成事实的部分 | 当前最稳推断 | 仍待验证 |
| --- | --- | --- | --- |
| 区域定位 | 官方 About 页把 `shadow-cursed forests` 与 `Underdark`、博德之门城市并列呈现。来源：`BG3-OFF-001` | `Shadow-Cursed Lands` 不是 `Act 2` 的背景板，而是官方直接点名的阶段级区域节点。 | 官方产品页仍不足以单独说明这块内部如何分工。 |
| 压力公开边界 | `Patch 7` 的 `Writing and Flow`、`Scripting`、`Act II` 条目包含大量任务流、角色反应、营地夜晚场景与对话优先级修复；同一补丁还明确写到被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 重读 `Act I` 前史。来源：`BG3-OFF-002` | `Act 2` 的第一个具体区域从一开始就承担“在压力下重读前史与推进 flow”的职责，而不是等到收束点才突然开始。 | 目前还缺能把这块内部压力继续压到更细 objective / step 层的公开材料。 |
| 路径语言 | Adam Smith 用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构。来源：`BG3-OFF-003` | `Shadow-Cursed Lands` 的压力不应被理解成取消多入口，而应被理解成“多入口仍在，但每条推进都要通过更高风险来判断”。 | 还不能把这条高层设计语言直接外推为某个具体区域机制或固定路线规则。 |
| 区域功能 | 上游 `Act 2` 框架已经说明中盘关键不是“更黑更难”，而是“高压条件下的选择与承接”。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003` | `Shadow-Cursed Lands` 是这套框架的第一层实体化：它把探索从 `Act 1` 的展开式问题网，改写为“在持续风险下推进、绕行、接近后续收束点”的区域循环。 | 它与 `Last Light / Moonrise / Gauntlet` 之间的具体收束分工，还要靠下一块继续压实。 |

## What can be written as facts

- `事实`：官方 About 页用 `shadow-cursed forests` 指认 BG3 的一块差异化区域，并把它与 `Underdark`、博德之门城市并列呈现。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 的 `Writing and Flow`、`Scripting`、`Act II` 条目包含大量与任务流、角色反应、营地夜晚场景、对话优先级相关的修复。来源：`BG3-OFF-002`
- `事实`：`Patch 7` 还明确写到，被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对玩家在 `Act I` 的处理作出反应。来源：`BG3-OFF-002`
- `事实`：Adam Smith 用 `Swiss cheese` 描述 BG3 的场景 / 路径组织，强调同一目标可通过多个洞口与方式接近。来源：`BG3-OFF-003`

## What can only be written as inferences

- `推断`：`Shadow-Cursed Lands` 当前最稳的写法不是“影咒地区总览”，而是 `Act 2` 的第一个具体压力组织器：风险不再只是情绪包装，而开始直接重组玩家如何移动、遭遇和继续推进。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`
- `推断`：与 `Mountain Pass / Creche` 的“门槛 + 伙伴张力”不同，这块区域把压力外扩到整段穿行本身；与后续收束点相比，它更像“组织压力”而不是“结算压力”。基于 `BG3-OFF-002`, `BG3-OFF-003`
- `推断`：因此这块区域对仓库的价值，不是提供一串更难的遭遇，而是说明中盘自由感开始从“我能去哪里”转成“我如何在风险条件下继续保持多种推进方式”。基于 `BG3-OFF-001`, `BG3-OFF-003`

## What must remain open questions

- `待验证问题`：`Shadow-Cursed Lands` 中哪些压力变量能继续稳定压到 `Journal / objective / step` 层，哪些目前只能停留在 flow / reaction / camp 维护边界？
- `待验证问题`：这块区域内部哪些前史读回会在区域现场发生，哪些更主要会延迟到 `Last Light / Moonrise / Gauntlet` 或营地层？
- `待验证问题`：哪些更细的公开来源足以继续压实“风险如何重组推进方式”，而不是把这块长期停留在高层框架判断？

## Source IDs

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`

## Notes

- 当前更稳的仓库口径应是：`Shadow-Cursed Lands` 先证明“中盘压力如何落到区域推进上”，再去拆具体收束点；不要提前把它写成收束点合集的前言或影咒设定摘要。
