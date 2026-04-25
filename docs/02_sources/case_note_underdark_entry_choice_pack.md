# Case Note

## Case name

Underdark：入口选择与阶段重构包

## Related module

`docs/03_analysis/01_macro_structure.md`

次级回流模块：
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/05_implementation_validation.md`

## Question

`Underdark` 能否被写成 `Act 1` 内部的“问题框架重构包”：进入它本身就会改写阅读顺序，并把玩家从地表问题网与 `Grove / Goblin` 状态回流网推向另一套以地下穿行与下游 `Grymforge` 为中心的推进结构？

## Research boundary

- 本 note 只处理 `Underdark` 的入口选择、阶段重构作用与对 `Grymforge` 的推送关系，不扩成地下景观导览或支线总表。
- 本 note 不把 `Grymforge` 本身重写一遍；它只把 `Grymforge` 当作 `Underdark` 的下游读出点。
- 本 note 允许写到“进入地下会改变什么”，但不把所有内部路线顺序写成事实矩阵。

## First-pass source set

- `BG3-OFF-001`
- `BG3-OFF-003`
- `BG3-OFF-006`

## Entry / progression pack

| 维度 | 当前能写成事实的部分 | 当前最稳判断 | 仍待验证 |
| --- | --- | --- | --- |
| 区域定位 | 官方 About 页把 `Underdark` 与影咒森林、博德之门等差异化区域并列呈现。来源：`BG3-OFF-001` | `Underdark` 不是可有可无的隐藏角落，而是官方产品叙述中的阶段级区域。 | 这是否足以把 `Underdark` 在 `Act 1` 内部的优先级继续压实到更细入口层？ |
| 进入与阅读顺序 | Adam Smith 用 `Swiss cheese` 描述 BG3 的场景 / 路径组织，强调同一目标存在多个洞口与进入方式。来源：`BG3-OFF-003` | 进入 `Underdark` 的价值，当前更稳的写法是“同一阶段内改写阅读顺序”，而不只是“换一张地图继续走”。 | 哪些具体入口差异会稳定映射到 objective / step 变化，哪些只是玩家体感上的顺序差异？ |
| 下游推送 | `Community Update 14` 的 patch notes 直接写到 `Added setup for several Grymforge quests in the Underdark.`，同时把 `Grymforge` 定义为包含 `new questlines, choices, cinematics, complex combat encounters` 的区域。来源：`BG3-OFF-006` | `Underdark` 不是封闭支路，而是会把玩家直接推向下一块高密度区域包。 | `Underdark -> Grymforge` 的哪些过渡节点最适合在后续做更细的任务 / 实现验证映射？ |

## What can be written as facts

- `事实`：官方 About 页把 `Underdark` 作为 BG3 多个差异化可探索区域之一，与影咒森林和博德之门等区域并列。来源：`BG3-OFF-001`
- `事实`：Adam Smith 在 Xbox Podcast 中把 BG3 的场景 / 路径结构比作 `Swiss cheese`，强调同一目标存在多个进入方式。来源：`BG3-OFF-003`
- `事实`：`Community Update 14` 的 patch notes 直接写到 `Added setup for several Grymforge quests in the Underdark.`。来源：`BG3-OFF-006`
- `事实`：同一更新把 `Grymforge` 描述为包含 `new questlines, choices, cinematics, complex combat encounters` 的区域。来源：`BG3-OFF-006`

## What can only be written as inferences

- `推断`：就 `Act 1` 而言，`Underdark` 当前最稳的写法不是“新增地下地图”，而是第一块明确把玩家从地表问题网和 `Grove / Goblin` 处理矩阵中抽离出来、重写为另一套空间 / 风险 / 下游推进框架的区域包。基于 `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-006`
- `推断`：进入 `Underdark` 的选择，说明 BG3 的自由推进不只体现在“同一冲突怎么处理”，也体现在“同一阶段先兑现哪一套空间与任务框架”。基于 `BG3-OFF-003`, `BG3-OFF-006`
- `推断`：`Underdark` 在 `Act 1` 里的角色，当前更适合被写成“并行路径 + 功能性转场”的复合块：它允许阅读顺序改写，同时又稳定把玩家推向 `Grymforge`。基于 `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-006`

## What must remain open questions

- `待验证问题`：`Underdark` 的哪些具体入口 / 过渡最值得在后续映射到 `Journal / objective / step` 层，而不是只停留在结构判断？
- `待验证问题`：`Underdark` 的哪些后果主要表现为下游 `Grymforge` 推进，哪些会折返到营地或更广义的 `Act 1` 状态读出？
- `待验证问题`：是否需要在后续单独补 1 份 `underdark_to_grymforge_progression` note，来承接这次只做到高层结构的边界？

## Source IDs

- `BG3-OFF-001`
- `BG3-OFF-003`
- `BG3-OFF-006`

## Notes

- 这份 note 的作用不是替代 `case_note_grymforge_environment_resolution.md`，而是解释为什么 `Grymforge` 现在应该被读成 `Underdark` 的下游高密度区域，而不是独立漂浮的战斗案例。
- 当前最稳的仓库口径应是：`Underdark` 在 `Act 1` 内部主要承担“阶段重构 / 入口选择包”的职责，不承担地下全区导览职责。
