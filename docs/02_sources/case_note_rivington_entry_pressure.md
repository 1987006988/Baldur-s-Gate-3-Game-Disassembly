# Case Note

## Case name

Rivington：入口过滤与外环承压

## Related module

`docs/03_analysis/01_macro_structure.md`

次级回流模块：
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/05_implementation_validation.md`

## Question

`Rivington` 能否被写成 `Act 3` 的第一层“入口过滤 + 外环承压”区域包，即：它的核心价值不在于提供一个进城前缓冲段，而在于把已在 `Act 3 总框架` 中成立的高密度并行线、前史读回与结算负载，先在这里第一次分束、过滤并重排阅读顺序？

## Research boundary

- 本 note 只处理 `Rivington` 作为 `Act 3` 第一个城市子块的结构职责，不展开 `Wyrm's Crossing`、`Lower City` 或终局组织的地点级子包。
- 本 note 不写地点导览、支线列表、派系百科，也不把 `Rivington` 直接升级成高密度结算区。
- 本 note 只写到公开可验证的层级：城市节点定位、选择驱动的 ending feedback、开发者对多入口与更高密度状态排列的表述，以及 Journal 的公开结构语言。

## First-pass source set

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Entry-filter frame

| 维度 | 当前能写成事实的部分 | 当前最稳推断 | 仍待验证 |
| --- | --- | --- | --- |
| 城市阶段入口 | 官方 About 页把 `the sprawling city of Baldur's Gate` 与 `shadow-cursed forests`、`Underdark` 并列呈现，说明 `Act 3` 是公开可验证的差异化阶段节点。来源：`BG3-OFF-001` | 既然 `Act 3` 被公开表述为一整个差异化城市阶段，那么它的第一层子块当前最稳的写法，就不是“进城前剩余内容”，而是高密度城市的第一道阅读入口。 | 公开来源仍不足以直接点名 `Rivington` 内部各条并行线的具体分工。 |
| 后期读回负载 | `Patch 7` 明确加入新的 evil ending cinematics，并把它们写成会 `depending on the choices you make` 出现；同一补丁继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界。来源：`BG3-OFF-002` | 这说明 `Act 3` 的问题不是“有没有后果”，而是“后果读回负载已经变密”；因此 `Rivington` 更适合作为第一次承压与分束点，而不是独立结算区。 | 目前仍缺能把 `Rivington` 内部哪些读回发生在现场、哪些延迟到后续子块的公开条目。 |
| 多入口为何仍要先过滤 | Adam Smith 继续用 `Swiss cheese` 描述 BG3 的多入口结构，并明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003` | `Rivington` 当前最稳的价值不是取消多入口，而是让高密度城市里的多入口第一次被“先碰哪一束问题”所过滤；入口依然很多，但玩家必须开始更早承担阅读顺序选择。 | 还不能把这条高层设计语言直接外推成 `Rivington` 内某一条固定路径规则。 |
| 任务层公开边界 | 官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为公开更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 因此本轮对 `Rivington` 最稳的任务层写法，是“后期并行 quest bundle 在这里第一次被过滤与重排”，而不是假装已经掌握内部 objective / step 结构。 | 仍缺能够把 `Rivington` 的具体 bundle 继续压到 `objective / step` 层的直接公开材料。 |

## What can be written as facts

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 差异化区域之一直接点名。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 明确加入新的 evil ending cinematics，并把它们表述为会 `depending on the choices you make` 出现。来源：`BG3-OFF-002`
- `事实`：`Patch 7` 同时继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界。来源：`BG3-OFF-002`
- `事实`：Adam Smith 继续用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构，并明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003`
- `事实`：官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为公开更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## What can only be written as inferences

- `推断`：`Rivington` 当前最稳的写法，不是“终于接近大城市前的前厅”，而是 `Act 3` 的第一层入口过滤包：它先把后期同时升高的并行线密度与结算负载，压成“先碰哪一束问题、先承接哪一组读回”的阅读顺序选择。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：与 `Last Light / Moonrise / Gauntlet` 的“中盘收束点组”不同，`Rivington` 并不主要承担把前史直接压到较少节点上；它更像后期高密度第一次落地时的分束区：先过滤、再重排，而不是立刻结算。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：与后续更靠近城市核心的子块相比，`Rivington` 更适合被写成“外环承压”而不是“高密度结算区”：它先让玩家感到后期密度已经开始压上来，但又还没有被压到只剩终局读取。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`

## What must remain open questions

- `待验证问题`：`Rivington` 内哪些并行线最适合继续被压成“入口过滤 bundle”，哪些其实已经更接近 `Wyrm's Crossing` 或 `Lower City` 的第二层重排与结算负载？
- `待验证问题`：哪些 `Rivington` 级别的阅读顺序变化，能继续稳定压到 `objective / step` 层，哪些目前仍只能停留在“quest bundle 被过滤”这一公开边界？
- `待验证问题`：除 `Patch 7` 的 ending feedback 与 flow / scripting 边界外，还有哪些同级别官方条目足以更直接支撑“`Rivington` 负责第一层过滤”这一判断？

## Source IDs

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Notes

- 当前最稳的仓库口径应是：`Act 3` 先证明“后期为什么会同时更密、更近结算”，`Rivington` 再证明“这层高密度如何第一次被过滤成可进入的阅读顺序”，而不是把 `Rivington` 写成城市前厅导览。
- 这份 note 的作用不是替代后续 `Wyrm's Crossing`、`Lower City`，而是先给它们提供干净的上游边界：第一层过滤已经发生，后面的子块不需要再重复扮演“入口前厅”。
