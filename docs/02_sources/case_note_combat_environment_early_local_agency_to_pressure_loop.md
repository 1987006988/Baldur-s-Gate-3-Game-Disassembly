# Case Note

## Case name

Combat / Environment 跨阶段主干：early local agency -> regional pressure loop

## Related module

`docs/03_analysis/04_combat_and_environment.md`

次级回流模块：
- `docs/03_analysis/05_implementation_validation.md`

## Question

在当前公开来源下，`Nautiloid -> Act 1 地表主区 -> Grymforge -> Shadow-Cursed Lands` 能否被稳定压成阶段 5 / `Combat / Environment` 的第一条跨阶段主干，说明 BG3 的战斗 / 环境能动性会从“开场局部问题重写”逐步升级成“中盘区域压力循环”，而不是只靠单个 `Grymforge` 区域包支撑整个模块？

## Research boundary

- 本 note 只处理首条环境主干，不延伸到 `Last Light / Moonrise / Gauntlet`、`Act 3` 城市子包或终局组织。
- 本 note 不罗列具体 encounter / 机关 / cheese 清单，只回答每个区域包在这条主干里承担什么层级职责。
- 本 note 不把任何单条具体打法提前升级成 `objective / step` 事实链；更细路径判断仍留在后续实现验证与区域包补强。

## First-pass source set

- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-006`
- `BG3-OFF-015`
- `BG3-PLY-004`

## Cross-stage compression matrix

| 链段 | 当前最稳职责 | 当前可升级到的层级 | 不能越级写成什么 |
| --- | --- | --- | --- |
| `Nautiloid` | 开场压缩样本：把移动、交互、战斗风险、关键物件与 quest close 压进第一块空间 | `compressed local-agency sample` | 不能把某条 tutorial 打法直接写成成熟主案例 |
| `Act 1 地表主区` | 把局部能动性从开场样本扩成 route choice 常态；战斗开始成为顺序与接近方式的一部分 | `route-agency normalization layer` | 不能把单条 early-surface 遭遇写成这条主干的第二个成熟强案例 |
| `Grymforge` | 第一块成熟 `encounter bundle / combat-agency compression pack`；玩家能正式把复杂遭遇读成环境重写问题 | `mature region-pack anchor` | 不能把具体熔炉 / 落体 / 远程拉杆路径写成稳定 objective 链 |
| `Shadow-Cursed Lands` | 把战术 agency 从单场遭遇推进到整段区域穿行：风险、绕行、接近与持续推进被重新绑紧 | `regional pressure loop` | 不能把这块直接写成收束点组或 late-game 第二条环境 spine |

## What can be written as facts

- `BG3-OFF-003` 直接提供了 `Swiss cheese` 设计语言：BG3 会用多入口与非常规 problem-solving 组织场景 / 路径，而不是只给一条标准解。
- `BG3-OFF-015` 直接暴露 `Nautiloid` 并非无状态前厅：它有 narrator 触发物、受限检定、关键 quest item、harmful condition 清理与 crash 边界。
- `BG3-OFF-002` 继续暴露 `Nautiloid` 的 quest close、tutorial 结束后的 buff / equipment handoff，以及 `Act II` 的 `writing and flow` / `scripting` 维护边界。
- `BG3-OFF-006` 直接把 `Grymforge` 定义成包含 `choices` 与 `complex combat encounters` 的区域，并公开暴露 `Underdark -> Grymforge` 的 setup。
- `BG3-PLY-004` 只能作为玩家案例入口，说明玩家确实会把 `Grymforge / Grym` 读成高差、机关、落体与战前布置共同组成的环境重写型遭遇。

## What can only be written as inferences

- `推断`：把这四段连起来后，当前最稳的阶段 5 / `Combat / Environment` 口径不是“BG3 到处都有名场面打法”，而是“BG3 会先在开场建立局部问题重写习惯，再把这种习惯常态化、压缩化，最后推到区域级压力循环”。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-015`
- `推断`：`Act 1 地表主区` 在这条 spine 里的价值，不是提供另一个成熟主案例，而是证明 `Nautiloid` 里的局部 agency 不是教程例外，而会在 crash 后变成 route choice 的常态。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-015`
- `推断`：`Grymforge` 仍然是当前最成熟的环境主案例，但它不应继续孤立存在；更稳的写法是把它当成“前两段样本 / 常态化之后的成熟压缩包”。基于 `BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004`
- `推断`：`Shadow-Cursed Lands` 让 combat agency 进入另一种口径：玩家不再只是在眼前一场遭遇里重写条件，而是在持续风险中判断如何移动、绕行、接近与继续推进。基于 `BG3-OFF-002`, `BG3-OFF-003`

## What must remain open questions

- `待验证问题`：当前公开来源是否足以把 `Shadow-Cursed Lands` 之后的 late `Act 2` / `Act 3` 区域包再压成第二条 cross-stage combat spine，还是必须明确停在 region-pack / supporting bundle 层？
- `待验证问题`：`Act 1 地表主区` 中是否存在一个比现在更稳的非教程、非 `Grymforge` 具体环境案例，能在后续补强里进入正文？
- `待验证问题`：`Shadow-Cursed Lands` 中哪些风险变量还能继续被公开来源压细，而哪些必须长期停在“区域级压力循环”的判断上？

## Notes

- 当前最稳的仓库口径应是：阶段 5 / `Combat / Environment` 的第一条环境主干先停在 `Shadow-Cursed Lands`，不要急着把收束点组、城市子包或终局组织拉进来凑第二条 spine。
- 这条主干最适合反向支撑两个判断：
  - `04_combat_and_environment.md`：BG3 的战斗 / 环境自由感如何从局部问题重写升级成区域级压力循环
  - `05_implementation_validation.md`：哪些区域已经足以进入横向主干，哪些仍只能停在 region-pack / supporting bundle 层
