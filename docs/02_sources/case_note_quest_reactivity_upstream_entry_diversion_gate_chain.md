# Case Note

## Case name

Quest Reactivity：`Nautiloid -> Act 1 地表主区 -> Underdark -> Mountain Pass / Creche` 的上游前置链

## Related module

`docs/03_analysis/02_quests_and_choices.md`

次级回流模块：
- `docs/03_analysis/05_implementation_validation.md`
- `docs/03_analysis/01_macro_structure.md`

## Question

当前已完成的 `Act 1` 区域包里，是否已经存在一条足够稳的“入口 / 目标网 / 改道 / 门槛”前置链，可以直接服务阶段 5 现有的 `Quest Reactivity` readback spine，而不必把 `Act 1` 重新写成总表？

## Research boundary

- 本 note 只处理 `Nautiloid`、`Act 1 地表主区`、`Underdark`、`Mountain Pass / Creche` 四段如何共同服务当前 `readback spine`。
- 本 note 不重写 `Grove / Goblin` 的 `resolution matrix`，只解释它为什么可以作为第一块高可见读回点出现。
- 本 note 不扩成 `Act 1` 全路线表，也不把 `Underdark` 或 `Mountain Pass / Creche` 写成地点 / 剧情摘要。

## First-pass source set

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-006`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-015`
- `BG3-OFF-016`

## Lead-in chain

| 链段 | 当前能写成事实的部分 | 如何服务现有 readback spine | 仍待验证 |
| --- | --- | --- | --- |
| `Nautiloid`：入口埋点 | `Patch 6` 与 `Patch 7` 直接暴露 narrator 触发物、关键 quest item、受限检定、`Escape the Nautiloid` 的 quest close，以及坠毁时的状态清理 / 装备交接边界。来源：`BG3-OFF-002`, `BG3-OFF-015` | 这说明 `Quest Reactivity` 的前史不是从 `Grove / Goblin` 才开始，而是从开场就已经在埋 objective / state。 | 哪些开场状态会继续稳定回流到海滩后的招募、对话或任务判断，当前公开锚点还不够细。 |
| `Act 1 地表主区`：目标网 | `Patch 7` 继续暴露地表招募时的装备交接边界；公开 Journal 文档持续给出 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 结构语言。来源：`BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-015` | 这说明 `Nautiloid` 埋下的状态并没有在坠毁后消失，而是被展开成多个同时挂起的 objective pressure，给后续 `Grove / Goblin` 提供前史密度。 | 哪些早期路线差异已足以压到 objective / step，哪些仍只是玩家体感上的顺序改写？ |
| `Underdark`：改道 / 重构 | 官方 About 页直接点名 `Underdark`；`Swiss cheese` 设计语言与 `Underdark -> Grymforge` 的公开 setup 共同暴露“同一阶段可切到另一套推进框架”。来源：`BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-006` | 这说明 `Quest Reactivity` 的上游不只包含“先做哪个目标”，还包含“先兑现哪一套空间 / 任务框架”的改道选择。 | 哪些地下入口与过渡已经足以稳定映射到 objective / step，哪些仍只能停留在 `entry / diversion bundle`？ |
| `Mountain Pass / Creche`：late `Act 1` 门槛 / 张力 | `Patch #3` 直接暴露 `Vlaakith` 对话门槛、`Rosymorn Monastery gate` 倒计时、`Voss` 敌意变化、`Lae'zel` 即时反应与 `camp night` 延迟读取边界。来源：`BG3-OFF-016` | 这说明在进入 `Act 2` 前，BG3 会把前面的路线自由进一步压成“你怎样跨门槛、怎样处理阵营权威、同伴怎样立即与延迟回应”的高压入口。 | 哪些边界已足以继续压到 `Mountain Pass / Creche -> Act 2` 的 objective / step 交接，哪些仍只能停留在 `gate-and-tension pack`？ |

## What can be written as facts

- `事实`：`BG3-OFF-002` 与 `BG3-OFF-015` 直接暴露了 `Nautiloid` 的 quest close、状态清理与地表招募交接边界。
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 持续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，因此“入口埋点 / 目标续接”可以被写成结构判断，而不是纯体验印象。
- `事实`：`BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-006` 共同暴露了 `Underdark` 的差异化区域定位、多入口设计语言与 `Underdark -> Grymforge` 的公开 setup。
- `事实`：`BG3-OFF-016` 直接暴露了 `Mountain Pass / Creche` 的门槛、敌意、即时伙伴反应与 `camp night` 后果读取边界。

## What can only be written as inferences

- `推断`：阶段 5 当前最稳的上游口径，不是“`Act 1` 前半到后半的完整任务表”，而是“入口埋点 -> 目标网 -> 改道 / 重构 -> 门槛 / 张力”的四段前置链。
- `推断`：这条前置链说明 `Grove / Goblin` 之所以能成为第一块高可见 `resolution matrix`，不是因为前面没有任务反应性，而是因为前四段已经把 objective 压力、路线改写与高压门槛准备好了。
- `推断`：从这一层看，BG3 的 `Quest Reactivity` 既来自处理方式会被读回，也来自玩家是在怎样的入口、怎样的改道与怎样的门槛条件下进入第一个高可见状态矩阵。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-016`

## What must remain open questions

- `待验证问题`：`Nautiloid` 与地表主区之间，哪些状态续接已经足以稳定压到 `objective / step`，哪些仍更适合停留在 `opening-state carryover` 边界？
- `待验证问题`：`Underdark` 的改道 / 重构结论，哪些能继续压到 Journal / objective / step，哪些仍只能留在 `entry / diversion bundle`？
- `待验证问题`：`Mountain Pass / Creche` 与 `Act 2` 的交接里，哪些已足以被写成 objective / step 邻近边界，哪些仍只能停留在 `gate / tension / camp readout` 这一组公开边界？

## Source IDs

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-006`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-015`
- `BG3-OFF-016`

## Notes

- 这份 note 不替代四个已有区域包 note；它的作用是把它们压成阶段 5 的第二条横向产出，即 readback spine 的上游前置链。
- 当前最稳的仓库口径应是：`Quest Reactivity` 现在已经同时拥有“前置链”和“读回链”两段，但前者目前仍以 `entry / diversion / gate` 层最稳，后者则从 `Grove / Goblin` 开始进入更高可见的 `resolution matrix`。
