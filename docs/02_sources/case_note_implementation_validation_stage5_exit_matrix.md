# Case Note

## Case name

Implementation Validation：阶段 5 统一 exit matrix

## Related module

`docs/03_analysis/05_implementation_validation.md`

次级回流模块：
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/04_combat_and_environment.md`

## Question

当 `Quest Reactivity`、`Combat / Environment`、`Companion / Camp / Long Rest` 三条横向主干都已经各自完成“1 条 spine + 1 次 ceiling / boundary 收口”之后，阶段 5 的统一出口到底应如何写？哪些判断已经可以保守写成事实或当前最强解释，哪些仍必须停在 bundle / handoff 层？

## Research boundary

- 本 note 不新增新来源，不重开任何单条主干，也不回跳已完成区域包。
- 本 note 只统一整理三条横向主干已经完成的 spine / ceiling / bundle / handoff 结论。
- 本 note 不把任何 bundle 误升为第二条对称 spine，也不把少数 objective-adjacent fragment 误写成 objective 总表。

## First-pass source set

- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-004`
- `BG3-OFF-006`
- `BG3-OFF-007`
- `BG3-OFF-008`
- `BG3-OFF-010`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-015`
- `BG3-OFF-016`

## Exit matrix

| 横向主干 | 已成立的正式 spine | 已锁定的 ceiling / boundary | 当前可保守写成的结论 | 当前必须停留的层级 | 阶段出口结论 |
| --- | --- | --- | --- | --- | --- |
| `Quest Reactivity` | `Grove / Goblin -> Act 2 convergence -> Act 3 readback / ending feedback` 的单显式 readback spine，且已有 `Nautiloid -> Act 1 地表主区 -> Underdark -> Mountain Pass / Creche` 前置链与 late `Act 1` / early `Act 2` 接缝。 | 只剩少数 objective-adjacent fragment 可继续逼近 `objective / step`：`Minthara` 的局部 resolution-state fragment，以及 `Vlaakith / Voss / Lae'zel` 的局部 gate fragment。第二条公开跨阶段主链已被 ceiling 锁死。 | BG3 的任务反应性当前最稳地体现为：少数局部 state / gate fragment 可以逼近 objective-adjacent 层，而更大范围的反应性则表现为跨长休、跨区域、跨 Act 的 readback / bundle 结构。 | `camp fold`、late-game `filter / gate / parallel resolution / ending feedback`、以及除少数 fragment 外的 objective 总表。 | 在当前公开来源下，`Quest Reactivity` 已完成收口；后续不再扩第二条公开主链，只在出现更强官方来源时才重开局部窄化。 |
| `Combat / Environment` | `Nautiloid -> Act 1 地表主区 -> Grymforge -> Shadow-Cursed Lands` 的 “early local agency -> regional pressure loop” spine。 | `Shadow-Cursed Lands` 之后的 late `Act 2` / `Act 3` 锚点已经被锁定为 `convergence`、`entry filter`、`bridge / gate`、`parallel resolution` 与 `organization / ending feedback` supporting bundles，第二条对称环境 spine 不成立。 | BG3 的战斗 / 环境能动性已可被保守写成一条跨阶段主干：它先在开场建立局部重写习惯，再在地表常态化，在 `Grymforge` 压成成熟 encounter bundle，最终在 `Shadow-Cursed Lands` 升成区域级压力循环。 | late-game 第二条环境 spine、`Act 3` encounter / 机关 / cheese 列表、以及任何未经更强官方来源支撑的 late-game 环境锚点升级。 | 在当前公开来源下，`Combat / Environment` 已完成“首条正式 spine + second-spine ceiling”闭合；下一步不应继续回跳 late-game 子包。 |
| `Companion / Camp / Long Rest` | `Act 1 地表主区 -> Dark Urge bard / Grove / Goblin -> Mountain Pass / Creche -> Last Light / Moonrise / Gauntlet -> 终局组织与收束压力` 的单 public `camp fold / delayed feedback` spine。 | `BG3-OFF-007` 只稳定支撑 `reflection / roster-state supporting bundle`，`BG3-OFF-010` 只稳定支撑 `dialogue accessibility maintenance bundle`，late-game 只稳定支撑 `ending-feedback handoff`；第二条公开 camp spine 不成立。 | 营地 / 长休当前最稳的系统判断是：它是被持续维护的反馈折叠层，负责把前序任务、关系与状态变化重新集中读出，而不是人物志附录。 | 第二条对称 camp spine、camp scene 清单、以及把 `reflection` / `accessibility maintenance` / `ending feedback` 反写成新的 camp-centered 主链。 | 在当前公开来源下，`Companion / Camp / Long Rest` 已完成“1 条 public spine + supporting bundles + handoff boundary”闭合。 |

## What can be written as facts

- `事实`：阶段 5 的三条横向主干现在都已经至少完成 `1` 条正式 spine 与 `1` 次 ceiling / boundary 收口，而不再停留在只有单个案例或单个区域包支撑的状态。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-004`, `BG3-OFF-006`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-015`, `BG3-OFF-016`
- `事实`：`Quest Reactivity` 当前只剩少数局部 fragment 还能继续逼近 `objective / step`，而 `Combat / Environment` 与 `Companion / Camp / Long Rest` 也都已经明确锁定“不再继续追第二条对称 spine”的边界。来源：`BG3-OFF-004`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-016`

## What can only be written as inferences

- `推断`：阶段 5 当前已经完成真正的阶段出口，因为三条主干都不再需要新的“同级 spine”，只剩“哪些 bundle 若未来出现更强官方来源，可能再上升”这一类局部开放问题。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-004`, `BG3-OFF-006`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-015`, `BG3-OFF-016`
- `推断`：因此阶段 5 的下一动作不应再是重开任一横向主干，而应切到阶段 6 / 展示收束，把这三条主干的出口矩阵转译成对外展示与阅读入口。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## What must remain open questions

- `待验证问题`：未来若出现更强官方来源，哪一个 bundle 最可能先被重新升级？
- `待验证问题`：阶段 6 应如何把“1 条 spine + ceiling / bundle / handoff 边界”转译成读者可直接理解的展示入口，而不把研究边界抹平？

## Source IDs

- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-004`
- `BG3-OFF-006`
- `BG3-OFF-007`
- `BG3-OFF-008`
- `BG3-OFF-010`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-015`
- `BG3-OFF-016`
