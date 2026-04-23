# ExecPlan 使用规范

ExecPlan 是本仓库处理长期复杂任务的自包含活文档。一个新会话如果只读某份 ExecPlan，也应知道目标、上下文、证据、当前进度和下一步动作。

## 何时必须使用

- 新增大型模块
- 调整整体方法论
- 批量重构资料结构
- 大规模补充资料并重写结论

## 核心原则

- 自包含：不要把关键背景留在聊天记录里
- 活文档：执行中持续更新，不是事后总结
- 可接力：中断后换一个会话也能继续推进
- 有验证：每个阶段都说明如何判断是否完成

## 推荐结构

- `Goal`
- `Why it matters`
- `Repository context`
- `Inputs and evidence`
- `Milestones`
- `Validation`
- `Progress`
- `Decision Log`
- `Surprises & Discoveries`
- `Outcomes & Retrospective`

## 与本仓库配合方式

- ExecPlan 中引用的来源必须能在 `docs/00_project/source_index.md` 找到
- 重要结论变化要同步到 `docs/00_project/decision_log.md`
- 任务推进后要同步 `current_state.md` 和 `next_step.md`
- ExecPlan 完结后，把产出沉淀进长期文档，而不是只留在计划里

## 简短示例

### Goal
重建“任务与选择”模块的证据链，区分玩家感受到的高反应性与真实系统回流机制。

### Why it matters
这是 BG3 自由感的核心模块；如果证据链不清楚，整个总论点会停留在印象层。

### Repository context
当前已有 `docs/03_analysis/02_quests_and_choices.md` 初始骨架，但来源仍以高层框架为主，缺少官方与高质量案例之间的对照。

### Inputs and evidence
- 现有 Source ID: `BG3-OFF-001`, `BG3-PLY-001`
- 待补官方来源: 开发者访谈、社区更新说明
- 待补案例: 至少 2 个可重复描述的任务分支案例

### Milestones
1. 补齐来源索引与来源笔记
2. 明确“选择点 - 状态变化 - 回流反馈”链路
3. 回写模块并修正总论点

### Validation
- 模块内每个事实都带来源 ID
- 至少有 2 个案例能区分事实、推断、待验证
- `current_state.md` 与 `next_step.md` 同步更新

### Progress
- 2026-04-22: 创建规范与示例，等待后续会话实例化。

### Decision Log
- 2026-04-22: 决定把“任务与选择”的回流机制作为首个优先深挖对象。

### Surprises & Discoveries
- 初始骨架显示，任务研究容易滑向剧情复述，因此必须强制写系统回流和实现验证层。

### Outcomes & Retrospective
- 任务完成后，需把可复用分析框架回写到 `module_template.md` 或相关方法论文档。
