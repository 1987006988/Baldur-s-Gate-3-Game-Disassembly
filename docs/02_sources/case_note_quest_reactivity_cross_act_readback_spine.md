# Case Note

## Case name

Quest Reactivity：从 `Grove / Goblin` 到终局组织的跨阶段状态回流主干

## Related module

`docs/03_analysis/02_quests_and_choices.md`

次级回流模块：
- `docs/03_analysis/05_implementation_validation.md`
- `docs/03_analysis/01_macro_structure.md`

## Question

当前已完成的区域包里，是否已经存在一条足够稳的 `Act 1 -> Act 2 -> Act 3` 状态回流主干，可以直接把阶段 5 / `Quest Reactivity` 从区域包复述压成横向主干？

## Research boundary

- 本 note 只处理当前最强的一条跨阶段链：`Grove / Goblin` 的处理矩阵如何在 `Act 2` 的收束点组被重新读取，并在 `Act 3` 的 `Rivington -> Wyrm's Crossing -> Lower City -> 终局组织与收束压力` 阶梯里继续被过滤、重排、并逼向 ending feedback。
- 本 note 不扩成全任务表，不补无关 `Act 1` 支线，也不重写 `Rivington`、`Wyrm's Crossing`、`Lower City` 或终局组织内部的地点级细节。
- 本 note 只写到公开可验证的层级：`处理方式 / 时序 / 营地可达性 / flow / ending feedback / objective-step 结构语言`；不假装掌握私有 objective 编排。

## First-pass source set

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-004`
- `BG3-OFF-008`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Readback spine

| 链段 | 当前能写成事实的部分 | 当前最稳推断 | 仍待验证 |
| --- | --- | --- | --- |
| `Act 1`：`Grove / Goblin` 处理矩阵 | `Hotfix #20` 直接区分 `knocked out` 与 `killed`，并暴露长休时序与 `journal wording` 边界；`Hotfix #5` 继续暴露营地对话可达性与 `companion reaction` 边界。来源：`BG3-OFF-004`, `BG3-OFF-008` | 这块当前最稳的价值不是“站哪边”，而是“处理方式 + 长休时序 + 营地折返”已经被系统写成可再读的状态矩阵。 | 除 `Minthara` 外，还有哪些 `Grove / Goblin` 处理差异拥有同级别公开锚点？ |
| `Act 2`：`Last Light / Moonrise / Gauntlet` 收束点组 | `Patch 7` 明确写到被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对 `Act I` 的处理作出反应；同一补丁继续集中修 `Act II` 的 `writing and flow`、`scripting`、角色反应与营地边界。来源：`BG3-OFF-002` | 因此 `Act 2` 当前最稳的功能，不是再开一批平行地点，而是把前一阶段的处理差异压向较少的收束点，并在这里开始重读。 | `Last Light`、`Moonrise`、`Gauntlet` 三者内部各自承担了哪些收束分工，目前仍缺直接公开锚点。 |
| `Act 3` 第一层：`Rivington` 入口过滤 | 官方 About 页与 `Swiss cheese` 设计语言继续支撑“多入口没有失效”；公开 Journal 文档继续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 语言。来源：`BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | `Rivington` 当前最稳的职责，是把已经接近 late-game 的并行问题束先过滤成初始阅读顺序，而不是直接结算。 | 哪些读回已经在 `Rivington` 现场发生，哪些仍只是入口层分束，公开锚点还不够细。 |
| `Act 3` 第二至四层：`Wyrm's Crossing -> Lower City -> 终局组织与收束压力` | `Patch 7` 的 ending feedback、后期 `writing and flow` / `scripting` 维护，与开发者对更高密度 dialogue / cinematics 的补写，共同暴露 late-game 不只是“剩余支线很多”，而是高负载读回区。来源：`BG3-OFF-002`, `BG3-OFF-003` | 当前最稳的压法是：`Wyrm's Crossing` 负责第二层门槛化重排，`Lower City` 负责更高密度并排承接与局部结算，`终局组织与收束压力` 再把这些并排问题束压向更少、更硬的终局组织位与 ending feedback。 | 这条 late-game 压缩梯里，哪些已经足以压到 `objective / step`，哪些仍只能停留在 `bundle / flow / ending feedback`，还需要在实现验证层继续分层。 |

## What can be written as facts

- `事实`：`BG3-OFF-004` 直接区分了 `Grove / Goblin` 中 `knocked out` 与 `killed` 的状态差异，并暴露长休时序会影响后续判定。
- `事实`：`BG3-OFF-008` 直接暴露了 `Grove / Goblin` 冲突下游的营地对话可达性与 `companion reaction` 维护边界。
- `事实`：`BG3-OFF-002` 明确写到被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对 `Act I` 的处理作出反应。
- `事实`：`BG3-OFF-002` 还继续集中暴露 `Act II` 与 late-game 的 `writing and flow`、`scripting`、角色反应、长休 / 营地边界与 ending feedback。
- `事实`：`BG3-OFF-001`, `BG3-OFF-003` 把后期城市节点与多入口设计语言公开化；`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 则给出了 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言。

## What can only be written as inferences

- `推断`：阶段 5 当前最稳的 `Quest Reactivity` 主干，不是“某条任务从头到尾的私有 objective 表”，而是“处理矩阵 -> 收束点组 -> 过滤 / 门槛 / 并排承接 -> 组织级压缩”的跨阶段读回梯。
- `推断`：这条链说明 BG3 的任务反应性不只来自分支数量，而来自同一处理方式会在跨长休、跨区域、跨 Act 的多个节点被重新读取。
- `推断`：`Act 3` 的作用不是简单把 `Act 2` 的收束继续压到更少节点，而是在更高密度的城市阶段里先重新分束、再门槛化、再并排承接，最后再压向组织级终局读取。

## What must remain open questions

- `待验证问题`：当前最强链仍然高度依赖 `Minthara -> Moonrise Towers -> Act II reaction` 这一条公开实锚；阶段 5 还需要第二条同级别的跨阶段链，避免横向主干过度依赖单一路径。
- `待验证问题`：`Rivington`、`Wyrm's Crossing`、`Lower City` 与 `终局组织与收束压力` 之间，哪些读回已足以压到 `objective / step`，哪些仍只能停留在 `bundle / flow / ending feedback` 边界？
- `待验证问题`：在不重写总逻辑的前提下，还需要哪些上游 `Act 1` / late `Act 1` 区域包，来给这条主干补“入口 / 改道 / 门槛”层的前史，而不是继续扩写同一条 readback spine？

## Source IDs

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-004`
- `BG3-OFF-008`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Notes

- 这份 note 不替代 `case_note_grove_goblin_resolution_matrix.md`、`case_note_last_light_moonrise_gauntlet_convergence.md` 或各个 `Act 3` 子包；它的作用是把这些既有区域包的稳定结论压成阶段 5 的第一条横向主干。
- 当前最稳的仓库口径应是：`Quest Reactivity` 首先证明“处理方式会被反复读回”，然后再继续追问“哪些读回已经足以压到 objective / step，哪些仍只能停留在 bundle / flow / ending feedback”。
