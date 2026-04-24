# Source Note

## Source ID

`BG3-OFF-011`

## Title

Scripting: Introduction to Osiris

## Type

official modding / scripting doc

## Why this source matters

这条来源为仓库的 Implementation Validation 提供了公开结构入口。它不是为了证明某条 shipped quest 的具体私有脚本，而是为了告诉我们：官方公开给 mod 作者的脚本层概念，到底用什么词来组织事件、调用、数据库与规则。

## Reliable facts

- 文档明确说 Osiris 覆盖 goals、events、queries、calls、sections、databases 和 rules 等基础概念。
- 文档明确说 Osiris 中的操作通常是“必须发生”的，因此会带有 failsafes；示例中，若角色移动路径被阻挡，角色会被传送过去。

## Useful inferences

- `推断`：以后凡是带有“任务状态在后续节点被重新结算”的判断，都更适合通过 Osiris / Journal / patch 三角交叉验证，而不是只靠玩家感受。
- `推断`：Osiris 文档更适合定义“我们可以合理猜到什么层级”，不适合直接证明某条私有剧情脚本的细枝末节。

## Limits and bias

- 这是官方公开文档，不等于 shipped content 的内部开发文档。
- 它适合做验证框架，不适合直接做单案例实锤。

## Where to use

- `docs/00_project/deconstruction_master_execution_plan.md`
- `docs/00_project/deconstruction_granular_codex_plan.md`

## Follow-up questions

- `待验证问题`：哪些现有模块的判断最需要 Osiris 作为验证入口？
- `待验证问题`：哪些判断更应该优先去看 Journal 结构，而不是 Osiris？
