# Source Note

## Source ID

`BG3-OFF-016`

## Title

Patch #3: Mac Support, Magic Mirror & More!

## Type

official update / patch notes

## Why this source matters

这是当前第一条能直接压到 `Mountain Pass / Creche` 的官方来源。它不是泛泛而谈的设计表述，而是补丁层直接暴露这一区域被维护的边界：`Vlaakith` 对话门槛、`Voss` 相关敌意状态、`Lae'zel` 的即时反应，以及 `camp night` 对 `crèche` 后果的读取时机。对仓库来说，这让 `Mountain Pass / Creche` 可以被写成“结构门槛 + 伙伴张力”叠层包，而不必退回剧情摘要。

## Reliable facts

- `Patch #3` 修复了一个会挡住后续对话的多余检定：当玩家拒绝 `Vlaakith` 的提议后，原本不该存在的 skill check 可能阻塞后续对话启动。
- 同一补丁修复了 `Lae'zel` 在 `Crèche Y'llek` 遇到 `Dream Visitor` 后的反应时机，使其会在对话结束后立即触发。
- 同一补丁修复了 `Rosymorn Monastery gate` 的爆炸倒计时，使其在玩家进入 `Astral Plane` 后会被正确取消。
- 同一补丁明确写到：如果 `Lae'zel` 在与 `Voss` 的互动中成功通过 `Deception` 检定，`githyanki` 不应继续保持敌对。
- 同一补丁还修复了 `Avatar Lae'zel` 在 `camp night` 里过早反思 `crèche` 后果的问题；在真正访问 `zaith'isk` 之前，这段反思不应提前发生。

## Useful inferences

- `推断`：这条来源说明 `Mountain Pass / Creche` 不是单一同伴支线容器，而是一块把对话门槛、局部敌意、即时伙伴反应与营地后续读取绑在一起维护的区域包。
- `推断`：对当前仓库而言，这块最稳的落点应先放在 `01_macro_structure.md` 与 `03_party_and_camp.md`，因为补丁直接暴露的是“门槛 + 反应 + 后续读取”边界，而不是完整任务表。

## Limits and bias

- 补丁说明暴露的是维护边界，不等于完整设计文档；它不能单独还原整块区域的全部流程。
- 这些条目多数是修复摘要，适合支撑“哪些地方被系统显性维护”，不适合直接外推全部剧情与状态路径。
- 它还不足以单独证明 `Act 2` 切换的完整规则，因此与阶段切换有关的技术判断仍要降级处理。

## Where to use

- `.agent/execplan_mountain_pass_creche_region_pack.md`
- `docs/02_sources/case_note_mountain_pass_creche_gate_and_party_tension.md`
- `docs/03_analysis/01_macro_structure.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/05_implementation_validation.md`

## Follow-up questions

- `待验证问题`：`Mountain Pass / Creche` 的哪些门槛变化能继续稳定映射到 `Journal / objective / step` 层，而不是只停在补丁边界？
- `待验证问题`：`Lae'zel` 的即时反应与 `camp night` 反思，哪些属于局部角色特例，哪些代表更普遍的区域后果折返模式？
