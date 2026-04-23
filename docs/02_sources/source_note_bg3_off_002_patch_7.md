# Source Note

## Source ID

`BG3-OFF-002`

## Title

Patch 7 Now Live!

## Type

official update / patch notes

## Why this source matters

这是当前“任务与选择回流”模块最直接的官方证据之一。它不是抽象宣传，而是补丁层面对任务、营地、对话流和角色反应的持续修正，能证明 BG3 的“反应性”不是一次性文案，而是被长期维护的系统目标。

## Reliable facts

- 官方在 Patch 7 中明确加入了更多与选择结果相关的结局反馈，例如新的 evil ending cinematics，并说明这些会“depending on the choices you make”出现。
- Patch 7 的 `Writing and Flow`、`Scripting`、`Act II` 等部分包含大量与任务流、营地夜晚场景、角色反应、对话优先级相关的修复。
- 补丁说明明确写到：`In Act II, Minthara will now react to you having knocked her out in Act I.`
- 补丁说明还写到：`Knocked Out Minthara will now always flee to Moonrise Towers.`
- 补丁还修复了多个营地长休、错误对话触发、任务流软锁和角色后续反应问题，说明这些反馈链条由具体脚本和流程条件支撑。

## Useful inferences

- `推断`：Larian 将“选择之后还能被世界重新解释和回应”视为需要持续维护的核心体验，不然不会在发布后继续修正这么多 flow / scripting / reactivity 问题。
- `推断`：Minthara 的 knock-out 路径被正式纳入后续状态流，说明任务系统并非只记录单次击杀/放过二元结果，而是存在更细的状态分支。

## Limits and bias

- 补丁说明能证明“系统在维护什么”，但不能单独证明玩家在游玩时一定感知到这些变化。
- 补丁条目多为修复摘要，无法单独还原完整任务脚本逻辑。
- 部分条目针对边缘情况，不能自动外推为全局设计原则。

## Where to use

- `.agent/execplan_quests_and_choices.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/05_implementation_validation.md`

## Follow-up questions

- `待验证问题`：哪些 Patch 7 条目最能串成“选择点 - 状态变化 - 后续反馈”的完整案例链？
- `待验证问题`：Minthara knock-out 路径在设计上是核心支持路径，还是后续被逐步正规化的特殊路径？
