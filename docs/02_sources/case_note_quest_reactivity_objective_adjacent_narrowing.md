# Case Note

## Case name

Quest Reactivity：objective-adjacent 窄化验证

## Related module

`docs/03_analysis/02_quests_and_choices.md`

次级回流模块：
- `docs/03_analysis/05_implementation_validation.md`

## Question

在“前置链 + 中盘接缝 + readback spine + 证据上限 + 层级锁定”都已完成之后，`Grove / Goblin` 与 `Mountain Pass / Creche` 这两个仍最接近 `objective / step` 的局部锚点，究竟还能再压哪一层？哪些部分又必须明确停手，不能再被误写成 objective 总表？

## Research boundary

- 本 note 不新增新区域，不重写既有区域包，也不再寻找第二条跨阶段主链。
- 本 note 只处理两组局部锚点：
  - `Grove / Goblin`
  - `Mountain Pass / Creche`
- 本 note 只使用现有官方 patch / hotfix 与 Journal 结构文档，不引入新的社区案例。
- 本 note 只回答“哪些局部 fragment 接近 `objective / step`”，不反推私有 shipped quest 的完整 objective / step 排布。

## First-pass source set

- `BG3-OFF-004`
- `BG3-OFF-008`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-016`

## Narrowing matrix

| 锚点 | 当前可继续压细的 fragment | 为什么可继续压细 | 必须停手的部分 | 为什么必须停手 |
| --- | --- | --- | --- | --- |
| `Grove / Goblin` | `Minthara` 的 `knocked out / killed` 差异、`journal wording`、以及“击倒 -> 长休 -> 再处理其他首领”的时序判定 | `BG3-OFF-004` 直接点名状态差异、journal wording 与长休时序；`BG3-OFF-012` / `013` / `014` 允许我们把这类条目公开写到 `quest / objective / step` 邻近层，而不是只写成模糊体验。 | 营地中的对话可达性与 `companion reaction` | `BG3-OFF-008` 证明它们是真实边界，但这组条目暴露的是 delayed camp readout，而不是新的 objective fragment。 |
| `Mountain Pass / Creche` | `Vlaakith` 拒绝后的对话阻塞、`Voss` 相关敌意变化、`Lae'zel` 即时反应时机 | `BG3-OFF-016` 直接点名局部门槛、敌意变化与即时反应；配合 `BG3-OFF-012` / `013` / `014`，可以把它们公开压到 objective-adjacent 的 local gate fragment。 | `camp night` 中对 `crèche` 后果的延迟反思，以及整块区域与 `Act 2` 的完整切换规则 | `BG3-OFF-016` 只暴露 delayed readout 时机与局部门槛边界，没有给出与 `Moonrise Towers` 同级的 downstream 命名落点，因此不能把整块区域写成 `Act 2` objective map。 |

## What can be written as facts

- `事实`：`BG3-OFF-004` 直接区分了 `Minthara` 的 `knocked out` 与 `killed`，并点名 `journal wording` 会随之变化。
- `事实`：同一来源还直接暴露了“击倒 `Minthara` -> 长休 -> 再处理其他首领”这组时序会影响后续判定。
- `事实`：`BG3-OFF-008` 直接暴露了 `Minthara` 在营地中的对话可达性与 `companion reaction` 需要单独修复。
- `事实`：`BG3-OFF-016` 直接暴露了 `Mountain Pass / Creche` 的局部门槛、局部敌意变化、即时反应与 `camp night` 后果读取时机。
- `事实`：`BG3-OFF-012`、`BG3-OFF-013`、`BG3-OFF-014` 只提供公开的 `Category / Quest / Objective / Step` 与 `trigger update` 结构语言，不直接给 shipped quest 的私有排布。

## What can only be written as inferences

- `推断`：`Grove / Goblin` 当前能再压一层的，不是整块 resolution matrix，而只是 `Minthara` 的局部 resolution-state fragment：它足以逼近 objective-adjacent 层，但还不足以外推全量首领顺序与处理差异。基于 `BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：`Mountain Pass / Creche` 当前能再压一层的，不是整块 late `Act 1` gate-and-tension pack，而只是 `Vlaakith / Voss / Lae'zel` 这组局部门槛 / 敌意 / 即时反应 fragment；`camp night` 依旧更稳地停在 delayed readout。基于 `BG3-OFF-016`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此 objective-adjacent narrowing 的真实结果，不是仓库又得到一张更细的 objective 表，而是更清楚地区分了“局部 state / gate fragment”与“下游读出层”之间的边界。基于 `BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-016`

## What must remain open questions

- `待验证问题`：除 `Minthara` 外，`Grove / Goblin` 里是否还有同级别、能被官方来源直接点名的局部 resolution fragment？
- `待验证问题`：`Mountain Pass / Creche` 是否还能找到更直接点名 `Act 2` 进入警告、切换文本或 objective 邻近结构的官方来源？
- `待验证问题`：如果没有更强官方来源，`Quest Reactivity` 是否应在完成这次窄化后停止扩链，并切到其他横向主干？

## Source IDs

- `BG3-OFF-004`
- `BG3-OFF-008`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-016`

## Notes

- 这份 note 的作用不是替代 `case_note_grove_goblin_resolution_matrix.md` 或 `case_note_mountain_pass_creche_gate_and_party_tension.md`，而是给它们补一层“哪些局部 fragment 已足够 objective-adjacent，哪些部分必须停在 delayed readout”的细分纪律。
- 当前最稳的仓库口径应是：`Quest Reactivity` 在现有公开来源下已经收口，继续推进的正确方式不是扩链，而是只在出现更强官方来源时重开局部窄化。
