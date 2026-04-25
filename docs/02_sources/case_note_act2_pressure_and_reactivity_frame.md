# Case Note

## Case name

Act 2：中盘压力与反应性重组框架

## Related module

`docs/03_analysis/01_macro_structure.md`

次级回流模块：
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/05_implementation_validation.md`

## Question

`Act 2` 能否被写成 BG3 的“中盘压力 / 反应性重组框架”，即：它不是单纯把气氛变暗，而是把前史状态、任务推进、营地反馈与阶段收束更紧地绑在一起？

## Research boundary

- 本 note 只处理 `Act 2` 的上位框架，不展开 `Shadow-Cursed Lands`、`Last Light`、`Moonrise`、`Gauntlet` 的地点级细节。
- 本 note 不写影咒 lore 摘要，也不把 `Act 2` 退化成“中盘剧情概要”。
- 本 note 不提前写死 `Act 2` 的具体切换规则、影咒机制或完整 `Journal / objective / step` 映射；这些技术化判断继续留在实现验证层。

## First-pass source set

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Pressure / reactivity frame

| 维度 | 当前能写成事实的部分 | 当前最稳判断 | 仍待验证 |
| --- | --- | --- | --- |
| 阶段定位 | 官方 About 页把 `shadow-cursed forests` 与 `Underdark`、博德之门城市并列呈现。来源：`BG3-OFF-001` | `Act 2` 从一开始就被官方写成差异化阶段节点，而不是 `Act 1` 与城市段之间的过道。 | 官方产品页还不足以单独压实 `Act 2` 内部各收束点的功能分工。 |
| 前史重读 | `Patch 7` 明确写到：被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对玩家在 `Act I` 击倒她作出反应。来源：`BG3-OFF-002` | `Act 2` 的一个关键功能是重新读取前一阶段留下的处理差异，而不是把 `Act 1` 状态全部归零。 | 目前公开来源还不足以列出更多同级别的 `Act 1 -> Act 2` 稳定读回链。 |
| 流程与反馈边界 | `Patch 7` 的 `Writing and Flow`、`Scripting`、`Act II` 条目包含大量与任务流、营地夜晚场景、角色反应、对话优先级相关的修复。来源：`BG3-OFF-002` | 中盘压力不只体现在气氛，而体现在任务推进、角色反应与营地反馈被更密集地维护和纠错。 | 哪些压力判断能继续压到“objective / step 的更紧组织”，目前还缺更直接的公开材料。 |
| 结构语言 | Adam Smith 用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构；Journal 文档把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 视为更新入口。来源：`BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | `Act 2` 更稳的写法不是“更压迫所以更线性”，而是“多入口逻辑仍在，但被放进更高压、更紧的状态读取与反馈组织里”。 | 还不能把这种高层结构语言直接外推为某一条影咒或收束节点的私有实现规则。 |

## What can be written as facts

- `事实`：官方 About 页用“from the shadow-cursed forests to the magical caverns of the Underdark, and all the way to the sprawling city of Baldur's Gate”来表达 BG3 的空间跨度。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 明确写到：`Knocked Out Minthara will now always flee to Moonrise Towers.` 来源：`BG3-OFF-002`
- `事实`：`Patch 7` 明确写到：`In Act II, Minthara will now react to you having knocked her out in Act I.` 来源：`BG3-OFF-002`
- `事实`：`Patch 7` 的 `Writing and Flow`、`Scripting`、`Act II` 部分包含大量与任务流、营地夜晚场景、角色反应、对话优先级相关的修复。来源：`BG3-OFF-002`
- `事实`：Adam Smith 把 BG3 的场景 / 路径结构比作 `Swiss cheese`，强调同一目标存在多个进入方式。来源：`BG3-OFF-003`
- `事实`：官方 Journal 文档把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为 Journal 更新的公开入口语言。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## What can only be written as inferences

- `推断`：`Act 2` 当前最稳的写法不是“阴影气氛更强的区域组”，而是 BG3 把反应性改写成“高压条件下的选择与承接”的阶段框架。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`
- `推断`：与 late `Act 1` 的“高压门槛 + 伙伴张力”相比，`Act 2` 的关键变化不在于完全取消多入口，而在于让前史状态更早、更密地在任务流、营地反馈和收束点附近被重新读取。基于 `BG3-OFF-002`, `BG3-OFF-003`
- `推断`：这也是为什么本轮应先回写 `01_macro_structure.md`、并给 `03_party_and_camp.md` 与 `05_implementation_validation.md` 准备中盘入口，而不是急着写单一地点摘要。基于 `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## What must remain open questions

- `待验证问题`：除 Minthara 外，还有哪些 `Act 1 -> Act 2` 的公开前史读回链，足以支撑“中盘是系统性重读前史”而不是个别高可见路径？
- `待验证问题`：`Act 2` 的哪些压力变量能继续稳定压到 `Journal / objective / step` 层，哪些只能先停留在 flow / reaction / camp 的维护边界？
- `待验证问题`：`Shadow-Cursed Lands`、`Last Light / Moonrise / Gauntlet` 各自如何分担这个中盘框架，目前还需要下个子块继续压实。

## Source IDs

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Notes

- 当前最稳的仓库口径应是：`Act 2` 先证明“中盘压力是结构变化”，再拆具体子块；不要一上来把影咒、Moonrise 或收束点拆成彼此平行的地点章节。
- 这份 note 的作用不是替代未来的 `Shadow-Cursed Lands` 或 `Last Light / Moonrise / Gauntlet` case note；它只负责给这些子块提供共同的上位问题。
