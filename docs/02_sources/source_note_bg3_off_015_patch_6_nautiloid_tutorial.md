# Source Note

## Source ID

`BG3-OFF-015`

## Title

Patch 6 Now Live!

## Type

official update / patch notes

## Why this source matters

这条来源不是为了证明 `Nautiloid` 的剧情内容，而是为了证明：官方把开场 / 教程段视为一个带明确流程、任务物件、条件清理与后续状态交接的真实系统块，而不是纯过场前厅。

## Reliable facts

- 官方在 `Tutorial` 小节中单列修复了 nautiloid rune slates / tablets 的 narrator 触发问题。
- 官方在同一小节中修复了 `Shadowheart` 舱门流程：Arcana 检定只能像其他检定一样尝试一次，且 `Eldritch Rune` 会被高亮为 quest item。
- 官方还在 tutorial / opening 相关修复中调整了部分爆炸范围。
- 官方明确写到，开场 nautiloid 遭遇中获得的 harmful conditions 会在坠毁后被移除。
- 官方还修复了一个离开 nautiloid 时的崩溃问题：`Shadowheart` 被击倒且不在队伍中时，离开 nautiloid 可能触发 crash。
- 官方修复了“只剩 `Lae'zel` 存活结束 tutorial，会导致玩家在 Act I 无法存档”的问题。

## Useful inferences

- `推断`：`Nautiloid` 已经具备“任务物件 + 交互检定 + 状态清理 + 角色交接”的完整结构，不适合被简单写成纯教程。
- `推断`：开场阶段的许多规则并不是临时 UI 提示，而是会被补丁层长期维护的流程边界。

## Limits and bias

- 这条来源主要证明“官方在维护什么边界”，不能单独证明玩家一定感知到所有这些状态处理。
- 它更适合做 `Nautiloid` 区域包与实现验证入口，不适合单独承担宏观总论。

## Where to use

- `.agent/execplan_nautiloid_region_pack.md`
- `docs/02_sources/case_note_nautiloid_opening_state_and_multi_entry.md`
- `docs/03_analysis/01_macro_structure.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/04_combat_and_environment.md`
- `docs/03_analysis/05_implementation_validation.md`

## Follow-up questions

- `待验证问题`：哪些 nautiloid 阶段状态会继续回流到海滩 / Act I 地表，而不是在坠毁时被清理？
- `待验证问题`：哪些开场设计是强教程属性，哪些已是后续区域包的缩略版？
