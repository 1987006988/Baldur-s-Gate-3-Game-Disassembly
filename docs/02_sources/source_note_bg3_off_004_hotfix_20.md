# Source Note

## Source ID

`BG3-OFF-004`

## Title

Hotfix #20 Now Live!

## Type

official hotfix

## Why this source matters

这条来源价值很高，因为它不是泛泛地说“我们很 reactive”，而是直接暴露了一个可追踪的状态问题：Minthara 被击倒、长休、再击败其他首领后，游戏如何判断她在 Act I 的状态，以及这个状态如何影响后续区域和任务流。

## Reliable facts

- Hotfix #20 明确修复了：如果玩家在击倒 Minthara 后先长休，再去处理其余地精首领，游戏有时不会正确认定她在 Act I 已被击败。
- 同一热修还修复了与击倒 Minthara 后跨区域状态相关的 `Enemy of Justice` 异常判定。
- 热修继续处理了 Minthara 在 Act II / Act III 跟随与离队上的状态问题，说明这条路径涉及跨 Act 状态传递。
- 热修还写到 journal wording 会调整为能区分“knocked out”与“killed”的情况。

## Useful inferences

- `推断`：至少在这条支线上，游戏确实区分“击杀”和“击倒”这两类状态，而不是简单视作同一个结果。
- `推断`：任务与选择回流的一部分复杂度来自跨区域、跨长休、跨 Act 的状态一致性维护。

## Limits and bias

- 这条来源围绕特定角色与特定路径，代表性有限。
- 热修说明的是修复点，不直接等于底层状态结构全貌。
- Minthara 路径可能兼具设计支持与后期玩家反馈驱动优化，不能直接外推到所有任务。

## Where to use

- `.agent/execplan_quests_and_choices.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/05_implementation_validation.md`

## Follow-up questions

- `待验证问题`：Minthara 路径能否作为首批“选择点 - 状态变化 - 后续反馈”案例之一？
- `待验证问题`：这条路径更像核心任务分支，还是一个被逐步正规化的特殊例外？
