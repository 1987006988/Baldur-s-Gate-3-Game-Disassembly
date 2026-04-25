# Case Note

## Case name

Last Light / Moonrise / Gauntlet：中盘收束点组

## Related module

`docs/03_analysis/02_quests_and_choices.md`

次级回流模块：
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/01_macro_structure.md`
- `docs/03_analysis/05_implementation_validation.md`

## Question

`Last Light / Moonrise / Gauntlet / 相关收束点` 能否被写成 `Act 2` 的同一块“中盘收束点组”，即：它们的核心价值不在于分别提供三个地点高潮，而在于把前面累积的路径差异、区域压力、任务推进与营地前史压缩到较少的读取节点里？

## Research boundary

- 本 note 只处理这组节点如何共同承担中盘收束，不展开 `Act 3` 后续结算，也不把每个地点拆成攻略。
- 本 note 不写 `Shadow-Cursed Lands` 的重复导览；它只把那块当作上游压力前场。
- 本 note 不把 `Journal / objective / step` 的完整映射写死；更细的组织方式继续留在实现验证层。

## First-pass source set

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Convergence frame

| 维度 | 当前能写成事实的部分 | 当前最稳推断 | 仍待验证 |
| --- | --- | --- | --- |
| 收束点组的公开边界 | `Patch 7` 的 `Writing and Flow`、`Scripting`、`Act II` 条目集中修复中盘任务流、角色反应、营地夜晚场景与对话优先级；同一补丁还明确写到被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对 `Act I` 的处理作出反应。来源：`BG3-OFF-002` | 当前最稳的公开读法不是“某个地点更重要”，而是 `Act 2` 在这里开始把前置路径差异集中读回到较少的节点里。 | 公开来源仍不足以逐点列出 `Last Light`、`Moonrise`、`Gauntlet` 各自承担的全部收束职能。 |
| 多路径为什么没有消失 | Adam Smith 用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构，强调同一目标依然允许多个进入方式。来源：`BG3-OFF-003` | 因此 `Act 2` 收束不应被写成“自由被取消”，而应被写成“多路径被压向更少、更密的读取与承接节点”。 | 还不能把这条高层结构语言直接外推成每个收束点内部的具体私有规则。 |
| 任务为什么更适合按“组”而不是按“地点”写 | 官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 视作更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 这意味着本轮更稳的写法是“objective / step 在这里被压缩与重读”，而不是把 `Last Light`、`Moonrise`、`Gauntlet` 各写成互不解释的地点篇章。 | 仍缺能把具体 objective / step 分工逐条压实到公开材料的直接锚点。 |
| 上游压力如何在这里变成收束 | `Act 2` 的上位框架与 `Shadow-Cursed Lands` 已经说明：中盘关键不是单纯更黑更难，而是前史、风险与推进方式被重组。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003` | 与 `Shadow-Cursed Lands` 的“组织压力”不同，这组节点更像“读取压力 + 压缩压力”的共同落点：前面被拉长的路径差异开始需要在这里被重新回答。 | 还需要下轮更直接的官方条目，去区分哪些压力先在现场读取，哪些主要通过营地 / 后续阶段延迟读出。 |

## What can be written as facts

- `事实`：官方 About 页把 `shadow-cursed forests` 作为 BG3 差异化区域之一直接点名，说明 `Act 2` 不是无结构中转带。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 的 `Writing and Flow`、`Scripting`、`Act II` 条目集中暴露中盘任务流、角色反应、营地夜晚场景与对话优先级的维护边界。来源：`BG3-OFF-002`
- `事实`：`Patch 7` 明确写到：`Knocked Out Minthara will now always flee to Moonrise Towers.` 来源：`BG3-OFF-002`
- `事实`：`Patch 7` 还明确写到：`In Act II, Minthara will now react to you having knocked her out in Act I.` 来源：`BG3-OFF-002`
- `事实`：Adam Smith 用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构，强调同一目标存在多个进入方式。来源：`BG3-OFF-003`
- `事实`：官方 Journal 文档把任务公开表述为 `Category -> Quest -> Objective -> Step`，并将 `trigger updates` 作为更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## What can only be written as inferences

- `推断`：`Last Light / Moonrise / Gauntlet / 相关收束点` 当前最稳的写法不是三个平行地点，而是 `Act 2` 的收束点组：前面被分散保存的路径差异、角色反应与推进压力，在这里被压到较少的读取节点上。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：与 `Shadow-Cursed Lands` 的“区域级压力循环”相比，这组节点更像“中盘压缩器”：它们不再主要组织玩家怎么穿行，而开始组织前史如何被回答、如何逼近后续结算。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`
- `推断`：这也是为什么本轮应优先回写 `02_quests_and_choices.md` 与 `03_party_and_camp.md`，而不是继续扩写地点景观或局部战斗：当前最稳的增量是“路径差异如何被重读”，不是“地点本身多壮观”。基于 `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## What must remain open questions

- `待验证问题`：`Last Light`、`Moonrise`、`Gauntlet` 各自更偏向承担哪一类收束任务，目前还缺直接点名这些节点分工的官方来源。
- `待验证问题`：除 `Minthara -> Moonrise Towers -> Act II reaction` 外，还有哪些前史读回链足以公开支撑“中盘收束点组”这一判断，而不只是个别高可见路径？
- `待验证问题`：这组节点中的哪些收束已经足以压到 `objective / step` 层，哪些目前只能保留在 flow / reaction / camp 的维护边界？

## Source IDs

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Notes

- 当前最稳的仓库口径应是：`Act 2` 先证明“压力如何重组推进”，再证明“这些推进差异会在收束点组里被集中读取”；不要把 `Last Light`、`Moonrise`、`Gauntlet` 直接拆成彼此平行的地点章节。
- 这份 note 的作用不是取代未来更细的地点级补强，而是先把 `Act 2` 尾段压成一块可复述的结构单元，给 `Act 3 总框架` 提供干净的上游边界。
