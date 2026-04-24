# Source Note

## Source ID

`BG3-OFF-012`

## Title

Journal Editor Overview

## Type

official modding / journal doc

## Why this source matters

这条来源给了仓库一个非常直接的公开入口：BG3 的任务 Journal 在编辑器里被怎样展示与编辑。它有助于我们避免把“任务”只理解成一串剧情文本，而忽视其公开可见的层级与属性结构。

## Reliable facts

- 文档明确说 Journal Editor 的 Project Browser 会列出 mods 及其 quests。
- 文档明确说 Quest Browser 以 categories、quests、subquests、objectives 和 steps 的层级来展示 journal data。
- 文档明确列出 Quest Properties、Objective Properties 和 Quest State Properties 等编辑面板。

## Useful inferences

- `推断`：BG3 的任务回流研究应默认把“Category / Quest / Objective / Step”视作公开可验证结构，而不是只把 quest 当成剧情名字。
- `推断`：区域包执行时，如果某条判断已经需要下探到 objective / step 层，就应提前标记为“需要 Journal 验证”。

## Limits and bias

- 这是编辑器总览，不直接证明 shipped content 里某条 quest 的具体数据长相。
- 它适合建立验证语言，不适合单独证明某条具体后果链。

## Where to use

- `docs/00_project/deconstruction_master_execution_plan.md`
- `docs/00_project/deconstruction_granular_codex_plan.md`

## Follow-up questions

- `待验证问题`：哪些现有 case 最值得进一步映射到 objective / step 级别？
- `待验证问题`：哪些“任务回流”判断实际上更像 Journal 可见层，而不是更深脚本层？
