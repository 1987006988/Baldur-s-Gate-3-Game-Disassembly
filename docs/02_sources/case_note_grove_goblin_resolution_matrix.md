# Case Note

## Case name

Grove / Goblin 冲突：处理方式与延迟回流矩阵

## Related module

`docs/03_analysis/02_quests_and_choices.md`

次级回流模块：
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/05_implementation_validation.md`

## Question

`Grove / Goblin 冲突` 能否作为 `Act 1` 第一块真正证明“任务不是派系二选一，而是处理方式、时序与后续读出会一起组成状态回流网”的区域包？

## Research boundary

- 本 note 只处理 `Act 1 地表主区` 下游的 `Grove / Goblin` 冲突，不扩成 Grove 政治综述或 Goblin Camp 剧情目录。
- 本 note 只记录目前有公开来源支撑的“处理方式 / 即时结果 / 延迟结果 / 营地折返”节点，不写全量路线表。
- 本 note 允许写到 `Moonrise` 与营地，但只把它们当作延迟反馈落点，不展开后续章节内容。

## First-pass source set

- `BG3-OFF-002`
- `BG3-OFF-004`
- `BG3-OFF-008`
- `BG3-PLY-003`

## Resolution matrix

| 处理节点 | 当前能写成事实的部分 | 即时结果 | 延迟结果 / 落点 | 当前最稳判断 | 仍待验证 |
| --- | --- | --- | --- | --- | --- |
| 击倒而非击杀 Minthara | `Hotfix #20` 明确区分 `knocked out` 与 `killed`，并说明 `journal wording` 会据此区分。来源：`BG3-OFF-004` | 冲突处理方式不是单一“是否击败首领”，而是至少存在不同状态写法。 | 该差异不会停留在现场文案，后续还会继续被读取。来源：`BG3-OFF-002`, `BG3-OFF-004` | `Grove / Goblin` 当前最稳的强证据不是“选哪一边”，而是“同一首领可被不同方式处理并被系统区分”。 | 这条路径从一开始就是正式支持路线，还是后续被正规化的高可见特例？ |
| 击倒 Minthara -> 长休 -> 再处理其他首领 | `Hotfix #20` 直接修复了这一时序下游戏曾错误判断 Minthara 是否已在 Act I 被击败的问题。来源：`BG3-OFF-004` | 长休不是中性暂停；它会改变后续状态判定与读取顺序。 | 该路径的失效点本身说明冲突状态会跨长休继续结算，而非现场一次性关账。来源：`BG3-OFF-004` | 这块最该写成“resolution timing matrix”，而不是平面分支树。 | 除 Minthara 外，其他首领或顺序差异哪些也有同级别的公开证据？ |
| 被击倒的 Minthara 的后续落点 | `Patch 7` 明确写到 `Knocked Out Minthara will now always flee to Moonrise Towers.`，并会在 Act II 对 Act I 的击倒作出反应。来源：`BG3-OFF-002` | Act I 的非常规处理不会在离开区域时消失。 | 反馈会延迟到后续区域与后续章节才被重新读出。来源：`BG3-OFF-002` | 这块已经足以证明 BG3 的冲突处理会被重新调用，而不只是留下任务完成/失败标签。 | 这类跨区域后果在 `Grove / Goblin` 里是个别高可见路径，还是更普遍的设计方向？ |
| 营地中的 Minthara 对话与 `companion reaction` | `Hotfix #5` 直接修复了 Minthara 的营地对话可达性、`companion reaction`，以及营地外解散后回营地无法对话的问题。来源：`BG3-OFF-008` | 营地不是和冲突分开的“角色空间”；它会读取并展示冲突后果。 | 冲突后果的一部分会以营地可达性与同伴反应形式折返。来源：`BG3-OFF-008` | `Grove / Goblin` 的下游不止是区域后果，也包含营地读出层。 | 除 Minthara 外，哪些 `Grove / Goblin` 后果也会以同样稳定的营地折返方式出现？ |

## What can be written as facts

- `事实`：`Grove / Goblin` 冲突至少在 Minthara 路径上明确区分 `knocked out` 与 `killed`，并且这种区分会影响 `journal wording`。来源：`BG3-OFF-004`
- `事实`：`Grove / Goblin` 的部分状态会跨长休继续被读取，否则不会出现“击倒 -> 长休 -> 再处理其他首领”的专门修复条目。来源：`BG3-OFF-004`
- `事实`：被击倒的 Minthara 会逃往 `Moonrise Towers`，并在 `Act II` 对玩家曾在 `Act I` 击倒她作出反应。来源：`BG3-OFF-002`
- `事实`：Minthara 的营地对话可达性与 `companion reaction` 属于需要单独维护的公开边界。来源：`BG3-OFF-008`

## What can only be written as inferences

- `推断`：`Grove / Goblin` 当前最稳的区域包写法不是“谁是好人 / 坏人”，而是“处理方式 / 时序 / 延迟结果 / 营地折返”的状态回流矩阵。基于 `BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-008`
- `推断`：相较于 `Act 1 地表主区` 的“目标网”，`Grove / Goblin` 是 `Act 1` 第一块更明显把“怎么处理一个冲突对象”写成后续状态差异的区域包。基于 `BG3-OFF-002`, `BG3-OFF-004`
- `推断`：营地在这块里不是突然插入的新模块，而是冲突后果的一个下游读出点。基于 `BG3-OFF-002`, `BG3-OFF-008`

## What must remain open questions

- `待验证问题`：除 Minthara 外，`Grove / Goblin` 里还有哪些首领顺序或处理差异拥有同级别的官方公开证据？
- `待验证问题`：哪些后果主要写回 `Journal / objective wording`，哪些会先折返到营地可达性与 `companion reaction`？
- `待验证问题`：`BG3-PLY-003` 所呈现的玩家体验中，哪些部分是稳定支持路径，哪些只是历史 bug 或边缘状态的残留印象？

## Source IDs

- `BG3-OFF-002`
- `BG3-OFF-004`
- `BG3-OFF-008`
- `BG3-PLY-003`

## Notes

- 这份 note 的作用不是替代 `case_note_minthara_knockout_path.md` 或 `case_note_minthara_camp_reaction_chain.md`，而是把两条既有 note 收束成同一个区域包矩阵。
- 当前最稳的口径应是：`Grove / Goblin` 证明了“处理方式 + 时序 + 营地折返”会一起决定后果可见性，但还不足以写成完整派系结局大全。
