# Case Note

## Case name

Act 3：高密度与高收束压力

## Related module

`docs/03_analysis/01_macro_structure.md`

次级回流模块：
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/05_implementation_validation.md`

## Question

`Act 3` 能否被写成 BG3 的“高密度城市 + 高收束压力”框架包，即：它的核心价值不在于把博德之门城市拆成更多地点，而在于说明为什么前面累积的多条任务线、派系线与角色后果，会在同一阶段同时变得更密、更忙、也更接近结算？

## Research boundary

- 本 note 只处理 `Act 3` 的上位框架，不展开 `Rivington`、`Wyrm's Crossing`、`Lower City` 的地点级子包。
- 本 note 把 `Act 2 总框架`、`Shadow-Cursed Lands` 与 `Last Light / Moonrise / Gauntlet` 收束点组当作上游前史，不重写其中细节。
- 本 note 只写到公开可验证的层级：城市节点定位、选择驱动的 ending feedback、开发者对多入口与高密度状态覆盖的表述、以及 Journal 的公开结构语言。

## First-pass source set

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Framework table

| 维度 | 当前可写成事实的部分 | 当前最稳推断 | 仍待验证 |
| --- | --- | --- | --- |
| 城市化高密度 | 官方 About 页把 `the sprawling city of Baldur's Gate` 与 `shadow-cursed forests`、`Underdark` 并列呈现，说明后期在官方表述里本就是差异化阶段节点。来源：`BG3-OFF-001` | `Act 3` 当前最稳的入口不是“终局前剩余内容”，而是“城市化高密度阶段”：空间、派系与可进入问题同时变多。 | 公开来源仍不足以直接区分 `Rivington`、`Wyrm's Crossing`、`Lower City` 各自承担的密度功能。 |
| 高收束压力 | `Patch 7` 明确加入新的 evil ending cinematics，并把它们表述为 `depending on the choices you make` 的结果。来源：`BG3-OFF-002` | 这说明后期压力不只是“快到结局”，而是前史选择开始更集中地要求被读回、被结算、被可视化。 | 仍缺更直接点名各条 `Act 3` 前史读回链的官方条目。 |
| 密度为什么不是单纯堆内容 | Adam Smith 用 `Swiss cheese` 描述 BG3 的多入口结构，并明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003` | 因此 `Act 3` 不应被写成“内容太多所以显得乱”，而应被写成“多入口结构在后期要同时承载更多并行线与更多结算读回”。 | 公开来源还不足以把这层设计语言直接外推到每个具体城市子块。 |
| 任务结构的公开边界 | Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为公开更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 这意味着本轮最稳的写法是“后期并行 quest bundle 在同一阶段拥挤并压向结算”，而不是声称已经掌握内部 objective 编排。 | 仍缺能把 `Act 3` 的具体派系 / 城市子块稳定压到 objective / step 层的直接公开材料。 |

## What can be written as facts

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 差异化区域之一直接点名。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 明确写到新增 evil ending cinematics 会根据玩家做出的选择出现。来源：`BG3-OFF-002`
- `事实`：Adam Smith 用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构。来源：`BG3-OFF-003`
- `事实`：Adam Smith 还明确说团队上线后继续补了大量额外 dialogue / cinematics，以覆盖更高密度的结局与状态排列。来源：`BG3-OFF-003`
- `事实`：官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## What can only be written as inferences

- `推断`：`Act 3` 当前最稳的写法不是“城市地点更多”的后期内容堆积，而是 BG3 的反应性承压测试：更多并行线、更多前史读回与更多结算反馈被压进同一阶段。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`
- `推断`：与 `Act 2` 的收束点组不同，`Act 3` 的关键变化不是继续把路径压到更少节点，而是让高密度城市同时承载“并行推进”与“接近结算”两种压力，所以玩家才会同时感觉忙碌与逼近终局。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`
- `推断`：`Swiss cheese` 式多入口在 `Act 3` 并没有自动失效；它更像在高密度城市里继续存在，只是每个入口都更容易连到派系、任务与结局的高负载读回。基于 `BG3-OFF-002`, `BG3-OFF-003`
- `推断`：因此本轮更适合先回写 `01_macro_structure.md` 与 `02_quests_and_choices.md`，而不是直接拆城市区块或终局剧情，因为当前最稳的增量是“结构如何承压”，不是“某个地点发生了什么”。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## What must remain open questions

- `待验证问题`：`Rivington`、`Wyrm's Crossing`、`Lower City` 各自更多承担“入口过滤”“中段并行枢纽”还是“高密度结算区”的哪一层职责？
- `待验证问题`：除 evil ending cinematics 外，还有哪些同级别的官方条目能更直接支撑“后期前史读回密度更高”这一判断？
- `待验证问题`：`Act 3` 的哪些并行线可以稳定压到 `objective / step` 层，哪些目前仍更适合停留在“quest bundle / ending feedback”这一公开边界？

## Source IDs

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Notes

- 当前最稳的仓库口径应是：`Act 2` 先把中盘压力压成“收束点组”，`Act 3` 再把后期写成“高密度城市中的结算负载”；不要把 `Act 3` 回退成城市百科。
- 这份 note 的作用不是取代后续城市子块，而是先给 `Rivington`、`Wyrm's Crossing`、`Lower City` 提供干净的上位边界。
