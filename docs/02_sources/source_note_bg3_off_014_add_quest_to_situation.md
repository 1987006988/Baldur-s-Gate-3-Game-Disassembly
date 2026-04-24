# Source Note

## Source ID

`BG3-OFF-014`

## Title

Journal: Adding a Quest to a Situation

## Type

official modding / journal tutorial

## Why this source matters

这条来源最有价值的地方不在于给具体 BG3 shipped quest 提供细节，而在于它把“叙事 brief → Journal 设计 → 编辑器实现 → scripting trigger updates”串成了一条公开流程，对仓库理解“任务不是纯文本，而是被系统组织起来的结构”很有帮助。

## Reliable facts

- 文档明确说，该教程会展示如何设计 quest、在 Journal 中实现它，并设置 scripting 来触发更新。
- 文档明确建议先读 Journal Structure Overview，再进入本教程。
- 文档在 Journal Editor Implementation 部分明确要求先打开 Journal Editor，再进行后续实现步骤。

## Useful inferences

- `推断`：对 BG3 的任务回流研究，最稳的实现验证姿势不是猜内部脚本，而是先问“这条判断更像 Journal 设计、还是 script trigger update 的问题”。
- `推断`：这条来源说明 Journal 和 scripting 在官方公开流程里本来就是连着看的，因此仓库后续也应把两者并列作为验证入口。

## Limits and bias

- 这是面向 mod 作者的教学流程，不是 shipped content 个案解剖。
- 它适合帮助仓库理解“实现层怎么分层看”，不适合直接证明单个剧情案例的实现。

## Where to use

- `docs/00_project/deconstruction_master_execution_plan.md`
- `docs/00_project/deconstruction_granular_codex_plan.md`

## Follow-up questions

- `待验证问题`：哪些现有高价值案例最值得按“brief → journal → trigger”去重新审视？
- `待验证问题`：哪些任务分歧更适合先看 Journal 结构，哪些更适合先看补丁 / 热修条目？
