# Case Note

## Case name

Quest Reactivity：第二条公开跨阶段链的证据上限与降级口径

## Related module

`docs/03_analysis/02_quests_and_choices.md`

次级回流模块：
- `docs/03_analysis/05_implementation_validation.md`

## Question

在已完成的 `readback spine`、上游前置链与 late `Act 1` / early `Act 2` 中盘接缝之外，现有公开来源里是否还能压出第二条不依赖 `Minthara -> Moonrise Towers -> Act II reaction` 的同级别跨阶段链？

## Research boundary

- 本 note 不新增区域包，不重写 `Act 1`、`Act 2`、`Act 3` 已完成子包。
- 本 note 不重新搜索新来源；只评估仓库里已蒸馏的官方 source note 与已完成的区域包结论。
- 本 note 不把 `party_and_camp` 的锚点硬抬成 `Quest Reactivity` 主干；这里只判断它们是否足以构成同级别公开跨阶段链。
- 本 note 只写到公开可验证层级，不反推私有 objective / step 编排。

## First-pass source set

- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-007`
- `BG3-OFF-010`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-016`

## Candidate-ceiling matrix

| 候选锚点 | 当前能写成事实的部分 | 为什么还不是第二条同级别跨阶段链 | 当前更稳的落点 |
| --- | --- | --- | --- |
| `Mountain Pass / Creche -> Voss / camp night` | `Patch #3` 直接暴露 `Vlaakith` 对话门槛、`Voss` 敌意变化、`Lae'zel` 即时反应与 `camp night` 对 `crèche` 后果的读取时机。来源：`BG3-OFF-016` | 它只直接点名了 late `Act 1` 的 gate 与局部 / 营地读出边界，没有继续点名某个 `Act II` 节点会如何重读这条处理方式，也没有形成明确的 `Act I -> Act II` 反应句。 | `gate / tension / camp readout bundle` |
| `Karlach` 跨 Act 反思 + 非 `Minthara` 营地可达性修复 | `Patch #2` 直接点名 `Karlach` 在 `Acts 1 and 2` 之间的反思时刻；`Hotfix #3` 直接修复 `Astarion`、`Mizora`、`Wyll`、`Voss` 的营地 scene / dialogue accessibility。来源：`BG3-OFF-007`, `BG3-OFF-010` | 这些条目证明了营地 / 长休中的跨阶段反馈与可达性维护不是 `Minthara` 孤例，但它们来自不同 quest / 角色线，缺少同一条“上游处理方式 -> 指定后续节点 -> 指定跨 Act 反应”的闭合链。 | `camp fold / dialogue accessibility bundle` |
| late-game `evil ending cinematics` / `writing and flow` / `scripting` | `Patch 7` 直接写到新的 evil ending cinematics 会 `depending on the choices you make` 出现，并持续集中维护 late-game `writing and flow`、`scripting`、角色反应与营地边界；`Swiss cheese` 与 Journal 文档继续提供结构语言。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 这组条目足以证明后期存在更高密度的前史读回与 ending feedback，但没有明确点名某个更早阶段的特定处理会在某个指定后期节点被怎样重读，因此还不足以构成第二条显式 readback spine。 | `ending feedback / organization bundle` |

## What can be written as facts

- `事实`：`BG3-OFF-016` 已足以确认 `Mountain Pass / Creche` 的门槛、局部敌意、即时伙伴反应与 `camp night` 读取时机，会被作为同一块边界单独维护。
- `事实`：`BG3-OFF-007` 已足以确认 `Karlach` 的跨 Act 反思时刻，以及营地作为队伍状态处理入口的公开边界。
- `事实`：`BG3-OFF-010` 已足以确认非 `Minthara` 的营地 scene / dialogue accessibility 也会被单独维护，包括 `Astarion`、`Mizora`、`Wyll` 与 `Voss`。
- `事实`：`BG3-OFF-002` 已足以确认 late-game `ending feedback`、`writing and flow` / `scripting`、角色反应与营地边界会继续被集中维护，且 evil ending cinematics 会根据玩家选择出现。
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 仍只提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的结构语言，不直接补出任何第二条 shipped quest 个案链。

## What can only be written as inferences

- `推断`：现有公开来源里，确实存在多组不依赖 `Minthara` 的跨阶段读出锚点，但它们分散落在 `gate / camp fold / ending feedback` 三种不同层级，尚不能被安全压成与 `Minthara -> Moonrise Towers -> Act II reaction` 同级别的显式链。
- `推断`：因此阶段 5 当前最稳的口径不是“仓库已经有两条同级别的公开跨阶段链”，而是“仓库已有一条显式 readback spine，外加数条较弱的 supporting anchors，足以防止把 `Quest Reactivity` 误写成全局 objective 表”。
- `推断`：`party_and_camp` 与 late-game `ending feedback` 的公开锚点，对阶段 5 的价值更像“约束不能越级写死”，而不是提供第二条可复述主干。

## What must remain open questions

- `待验证问题`：如果后续官方来源能直接点名 `Voss`、`Lae'zel`、`Karlach`、`Wyll` 或某条 late-game 处理会在指定后续节点被重读，这一结论是否可以重新升级？
- `待验证问题`：目前最稳的下一步，不是继续空找第二条链，而是继续压实现有主干中哪些链段已逼近 `objective / step`，哪些必须停在 `gate / camp fold / ending feedback bundle`。
- `待验证问题`：若未来没有更强公开锚点，阶段 5 / `Quest Reactivity` 是否应在完成这次降级后停止扩链，转入其余横向主干？

## Source IDs

- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-007`
- `BG3-OFF-010`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-016`

## Notes

- 这份 note 不取代既有 `readback spine`、前置链或中盘接缝 note；它的作用是给阶段 5 增加一个“证据上限判断”子单元，明确仓库现在为什么不能再无代价地继续抬高 `Quest Reactivity` 的实现层口径。
- 当前最稳的仓库口径应是：`Quest Reactivity` 现在已经有一条显式主干，但其余官方锚点仍更适合被写成 supporting bundles，而不是被误写成第二条对等主干。
