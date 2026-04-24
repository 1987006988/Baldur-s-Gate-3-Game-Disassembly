# Source Note

## Source ID

`BG3-OFF-013`

## Title

Journal Structure Overview

## Type

official modding / journal doc

## Why this source matters

这条来源把 BG3 Journal 的层级结构说得最简洁、最适合拿来当验证骨架。它能帮助仓库把“任务回流”写成结构判断，而不是模糊的剧情印象。

## Reliable facts

- 文档明确给出 Journal 层级：Category → Quest → Objective → Steps，并且可以有 Subquest → Subquest Objective → Subquest Steps。
- 文档说明游戏内 Journal 左侧是 categories 与 quests，右侧是 objectives 与 steps，按最近到最早的顺序显示。

## Useful inferences

- `推断`：后续如果要把某条反应链升级为更稳的实现层判断，应优先看它更像 category / quest 级变化，还是 objective / step 级变化。
- `推断`：这条来源特别适合作为“为什么不能把 BG3 任务只写成剧情目录”的反证材料。

## Limits and bias

- 这是结构总览，不涉及具体 quest 的个案数据。
- 它只能帮助我们划清结构层级，不能单独证明某条任务具体如何触发。

## Where to use

- `docs/00_project/deconstruction_master_execution_plan.md`
- `docs/00_project/deconstruction_granular_codex_plan.md`

## Follow-up questions

- `待验证问题`：当前最强的 quest reactivity 案例，分别落在哪一层级最合理？
- `待验证问题`：哪些营地反馈其实更像 step 可见层的后续读出？
