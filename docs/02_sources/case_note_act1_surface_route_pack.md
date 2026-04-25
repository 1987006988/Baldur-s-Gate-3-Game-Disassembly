# Case Note

## Case name

Act 1 地表主区：坠毁后问题网与前史密度

## Related module

`docs/03_analysis/01_macro_structure.md`

次级回流模块：

- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/04_combat_and_environment.md`
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/05_implementation_validation.md`

## Question

`Act 1 地表主区` 能否作为 `Nautiloid` 之后的第一块稳定区域包，说明 BG3 在坠毁之后并没有把玩家送进一条单线新手路，而是立即把招募、探索、前置遭遇与后续区域入口铺成一张可改写顺序的问题网？

## Research boundary

- 本 note 只处理 crash 后到 `Grove / Goblin` 状态矩阵真正展开之前的地表主区网络。
- 本 note 不把 `Grove / Goblin` 冲突本身写成这里的子章节；它只作为地表 route pack 的下游指向。
- 本 note 不把地表写成景点清单，也不把招募线写成人物目录。

## First-pass source set

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-015`

## Working route sketch

以下只是本轮研究用的分析压缩，不是要写进正文的“官方路线图”：

1. `坠毁点 -> 开场残余状态清理 -> 第一批同伴回收`
2. `坠毁点 -> 可选探索 / 绕路空间 -> 早期战斗与资源压力`
3. `地表前场 -> Grove / Goblin / Camp / 后续区域入口的前史网络`

本轮只需要证明这三条压力线是并行铺开的，而不需要穷举所有具体路线顺序。

## What can be written as facts

- `BG3-OFF-003` 直接说明，Larian 用 `Swiss cheese` 描述 BG3 的场景 / 路径组织方式：同一目标存在多个洞口与进入方法。
- `BG3-OFF-001` 说明官方对 BG3 的产品表达，是把区域跨度、选择后果、队伍协作与回合制互动并列呈现，而不是把“开场 -> 主线 -> 结局”做成单一路径承诺。
- `BG3-OFF-015` 说明 nautiloid 阶段获得的 harmful conditions 会在坠毁后被移除，表明开场到地表之间存在明确的状态清理边界。
- `BG3-OFF-002` 说明 tutorial 结束后的 buff 与装备交接会影响后续招募，例如如果玩家带走了 `Shadowheart / Lae'zel` 的装备，她们在地表被招募时应获得新的装备。
- `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 共同说明：公开可见的任务结构至少可被理解为 `Category → Quest → Objective → Step` 与对应的 trigger updates，因此 crash 后的“继续回收同伴、继续承接 opening state”不适合被写成无结构的自由漫游空窗。

## What can only be written as inferences

- `推断`：`Act 1 地表主区` 最稳的写法，不是“景点串联”也不是“招募清单”，而是 BG3 第一块真正稳定展开的问题网：玩家在这里第一次同时面对 opening 残余状态、同伴回收、可选探索、早期遭遇与下游区域入口。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-015`
- `推断`：与 `Nautiloid` 相比，地表主区的关键增量不是“内容更多”，而是“顺序可改写”。它把原本压缩在开场里的空间、目标、同伴与战斗压力展开成更稳定的前场网络。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-015`
- `推断`：玩家在地表产生的自由感，很大一部分来自“可以先兑现哪一段 opening 前史”的选择，而不是来自没有结构。系统并不是不设目标，而是允许多个目标压力并行挂起。基于 `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这也是为什么地表主区应被视为 `Grove / Goblin`、`Camp` 与后续区域包的共同上游：它先把同伴、方向、风险与未解决目标堆出密度，后面各模块才有东西可折返、可收束。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`

## What must remain open questions

- `待验证问题`：哪些 opening 状态会在地表继续被读取为招募、对话或任务前置，哪些只是在坠毁时被清理后重新开始？
- `待验证问题`：地表主区中哪些早期路线差异会稳定回流到 `Camp` 或 `Grove / Goblin`，哪些只是玩家体验到的顺序差异？
- `待验证问题`：是否需要在后续补 1 条更聚焦 `recruitment_and_discovery` 的 case note，来承接地表主区与营地前史之间的关系？
- `待验证问题`：是否需要补一条更直接谈 Act 1 early-game structure 的官方来源，来把“route pack”从高层推断继续升级？

## Notes

- 当前最稳的仓库口径应是：`Act 1 地表主区` 先承担“第一个稳定问题网”的证明职责，不承担 `Grove / Goblin` 之后的大型状态矩阵职责。
- 它最适合反向支撑五个方向：
  - 宏观结构：`Nautiloid` 之后，BG3 立刻展开为可改写顺序的前场网络
  - 任务回流：opening state 没有消失，而是以新的目标压力继续挂起
  - 战斗 / 环境：战斗开始从教学样本变成 route choice 的组成部分
  - 营地 / 长休：第一批营地前史并不是凭空出现，而是由地表顺序密度生成
  - 实现验证：补丁与 Journal 文档足以让“哪些状态被清理、哪些被续接”成为公开可验证问题
