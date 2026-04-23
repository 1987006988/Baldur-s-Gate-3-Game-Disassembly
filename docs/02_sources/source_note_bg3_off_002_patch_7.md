# Source Note

## Source ID

`BG3-OFF-002`

## Title

Patch 7 Now Live!

## Type

official update / patch notes

## Why this source matters

这是当前“任务与选择回流”与“营地 / 长休反馈”模块都很关键的官方证据之一。它不是抽象宣传，而是补丁层面对任务、营地、对话流和角色反应的持续修正，能证明 BG3 的“反应性”不是一次性文案，而是被长期维护的系统目标；同时它还直接回指并补强了 `Dark Urge bard` 事件的官方 framing。

## Reliable facts

- 官方在 Patch 7 中明确加入了更多与选择结果相关的结局反馈，例如新的 evil ending cinematics，并说明这些会“depending on the choices you make”出现。
- Patch 7 单独用一个小节再次回指 `Community Update #28`，重申当玩家扮演 `Dark Urge` 时，某位 bard 会在营地以可控制角色身份暂时加入队伍。
- Patch 7 在同一小节中明确强调：这不是“新同伴”路线，而是一个短暂且带后果的事件。
- Patch 7 还明确写到：如果玩家邀请她，`Alfira` 会真正以可控制角色身份暂时加入队伍；她没有蝌蚪、可以升级、也不能使用 Magic Mirror。
- Patch 7 的 `Writing and Flow`、`Scripting`、`Act II` 等部分包含大量与任务流、营地夜晚场景、角色反应、对话优先级相关的修复。
- 补丁说明明确写到：`In Act II, Minthara will now react to you having knocked her out in Act I.`
- 补丁说明还写到：`Knocked Out Minthara will now always flee to Moonrise Towers.`
- 补丁还修复了多个营地长休、错误对话触发、任务流软锁和角色后续反应问题，说明这些反馈链条由具体脚本和流程条件支撑。

## Useful inferences

- `推断`：Larian 将“选择之后还能被世界重新解释和回应”视为需要持续维护的核心体验，不然不会在发布后继续修正这么多 flow / scripting / reactivity 问题。
- `推断`：就 `Dark Urge bard` 事件而言，Patch 7 已经把它从“剧透式 tease”进一步压实成“短暂营地状态变化，而非稳定招募路线”的官方定位。
- `推断`：Minthara 的 knock-out 路径被正式纳入后续状态流，说明任务系统并非只记录单次击杀/放过二元结果，而是存在更细的状态分支。

## Limits and bias

- 补丁说明能证明“系统在维护什么”，但不能单独证明玩家在游玩时一定感知到这些变化。
- 补丁条目多为修复摘要，无法单独还原完整任务脚本逻辑。
- 部分条目针对边缘情况，不能自动外推为全局设计原则。

## Where to use

- `.agent/execplan_quests_and_choices.md`
- `.agent/execplan_party_and_camp.md`
- `docs/02_sources/case_note_dark_urge_bard_event.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/05_implementation_validation.md`

## Follow-up questions

- `待验证问题`：`Dark Urge bard` 事件在 Patch 7 已明确到“Alfira 暂时入队”的情况下，还缺哪些后续反馈条目，才能进一步闭合完整链路？
- `待验证问题`：Minthara knock-out 路径在设计上是核心支持路径，还是后续被逐步正规化的特殊路径？
