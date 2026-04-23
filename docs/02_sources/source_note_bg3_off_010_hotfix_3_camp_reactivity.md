# Source Note

## Source ID

`BG3-OFF-010`

## Title

Hotfix #3 Now Live!

## Type

official hotfix

## Why this source matters

这条来源的价值不在于提供新的正文主案例，而在于补出一组明确的“非 `Minthara` 营地 reaction / 对话可达性”官方锚点。它能帮助我们把 `party_and_camp` 中的一个关键待验证问题收窄：营地中的 scene / dialogue accessibility 并不只在 `Minthara` 个案上被维护。

## Reliable facts

- 官方明确修复了：如果玩家通过别的方式发现 Astarion 的秘密，仍然应该在营地触发他的 bite scene。
- 官方明确修复了：如果玩家还没见过 Lorroakan，不应在营地对话里提前出现关于他的台词。
- 官方明确修复了：Mizora 在 Iron Throne 相关事件后应回到营地，而不是直接消失。
- 官方明确修复了：如果 Wyll 的父亲已被救下，Wyll 不应继续像父亲不在场那样说话。
- 官方明确修复了：玩家应能在营地获得一段与 Voss 的特定对话。

## Useful inferences

- `推断`：营地中的 scene accessibility、角色识别正确性、后续在场状态与对话可达性，在多个非 `Minthara` 角色/事件上都是被官方单独维护的边界。
- `推断`：这条热修更适合用来证明“营地反馈链不是 `Minthara` 孤例”，而不适合单独承担一个完整剧情折返案例。

## Limits and bias

- 这条来源覆盖的是一串修复条目，而不是一条可独立复述的完整剧情链。
- 这些条目分散在不同角色与不同阶段，能证明边界存在，但不能单独证明统一底层机制。
- 它更适合收窄待验证问题，而不是直接把“营地反馈已被完全证明为系统规律”升级成事实。

## Where to use

- `.agent/execplan_party_and_camp.md`
- `docs/00_project/source_index.md`
- `docs/03_analysis/03_party_and_camp.md`

## Follow-up questions

- `待验证问题`：这些非 `Minthara` 条目与 `BG3-OFF-008` 结合后，是否足以支撑“营地反馈链被系统性维护”的更高层判断？
- `待验证问题`：这组条目中，哪一条最适合在后续继续发展成正文中的平行补强案例？
