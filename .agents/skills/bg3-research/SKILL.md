# BG3 Research Skill

## 用途

这是一个 instruction-only skill，用于在本仓库内执行高频研究动作时复用固定流程，减少会话漂移并确保状态与来源同步。

## 什么时候用

当任务包含以下任一动作时使用:

- 新增资料来源
- 把来源写入 `docs/00_project/source_index.md`
- 生成来源笔记
- 从来源笔记提炼到分析模块
- 更新 `docs/00_project/current_state.md` 与 `docs/00_project/next_step.md`

## 什么时候不要用

- 纯粹修正排版、错字或链接
- 仅调整脚本、Makefile、配置文件而不涉及研究内容
- 仓库级结构重构且尚未明确研究目标时

## 固定流程

1. 先读 `README.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/source_index.md`
2. 判断本次任务属于新增来源、补来源笔记、回写分析、还是更新状态
3. 若有新来源，先分配 Source ID 并登记到 `source_index.md`
4. 用 `templates/source_note.md` 或等价结构记录来源摘要、可信度、可用事实、限制
5. 把提炼结果写入对应分析模块，并显式区分“事实 / 推断 / 待验证问题”
6. 若结论、范围或方法发生变化，追加更新 `docs/00_project/decision_log.md`
7. 收尾时同步 `current_state.md` 和 `next_step.md`

## 标准输出

一次合格的研究任务通常应产生以下至少两类产物:

- 一个或多个已登记的来源条目
- 一个来源笔记或结构化来源摘要
- 一个被更新的分析模块
- 一次状态同步

## 最少必须更新的文件

完成一次研究任务后，最少要更新:

- `docs/00_project/current_state.md`
- `docs/00_project/next_step.md`

若引入新来源，还必须更新:

- `docs/00_project/source_index.md`

若结论或结构发生变化，还必须更新:

- `docs/00_project/decision_log.md`
