# Repo Map

## 新会话从哪里开始

1. 先读 `README.md`，理解仓库目标、边界、双轨总逻辑与基本工作流。
2. 再读 `docs/00_project/deconstruction_display_overview.md`，先解决“项目到底按什么逻辑拆、为什么不是剧情复述”。
3. 再读 `docs/00_project/deconstruction_master_execution_plan.md`，理解阶段划分、依赖关系与完成标准。
4. 再读 `docs/00_project/deconstruction_granular_codex_plan.md`，确认每个区域包 / 跨阶段系统的实际执行脚本。
5. 再读 `docs/00_project/current_state.md`，确认当前阶段与最近变更。
6. 再读 `docs/00_project/next_step.md`，获取当前唯一主任务。
7. 再读 `docs/00_project/source_index.md`，确认来源状态与可追溯入口。
8. 然后进入本轮相关模块、来源笔记或 ExecPlan。

## 关键文件作用

- `docs/00_project/overview.md`：项目总命题、范围与方法价值。
- `docs/00_project/deconstruction_display_overview.md`：面向读者 / 观众解释“这个项目到底怎么拆、为什么现在拆这一块”。
- `docs/00_project/deconstruction_master_execution_plan.md`：阶段划分、输入输出、依赖与暂停条件。
- `docs/00_project/deconstruction_granular_codex_plan.md`：操作级执行脚本，给 Codex 直接用。
- `docs/00_project/master_roadmap.md`：项目级主路线摘要，负责保持总线稳定。
- `docs/00_project/current_state.md`：单页状态看板。
- `docs/00_project/decision_log.md`：追加式决策历史。
- `docs/00_project/next_step.md`：本轮执行入口。
- `docs/00_project/source_index.md`：来源总索引与 Source ID 主表。

## 长期记忆核心

- `README.md`
- `docs/00_project/deconstruction_display_overview.md`
- `docs/00_project/deconstruction_master_execution_plan.md`
- `docs/00_project/deconstruction_granular_codex_plan.md`
- `docs/00_project/current_state.md`
- `docs/00_project/next_step.md`
- `docs/00_project/decision_log.md`
- `docs/00_project/source_index.md`

这些文件共同承担长期记忆；不要把关键上下文留在聊天记录里。

## 分析正文

- `docs/03_analysis/00_core_thesis.md`：总论点与当前最强解释版本。
- `docs/03_analysis/01_macro_structure.md`：Act / 区域 / 入口 / 推进结构。
- `docs/03_analysis/02_quests_and_choices.md`：任务、分支、回流与反馈。
- `docs/03_analysis/03_party_and_camp.md`：同伴、营地、长休与反馈折返点。
- `docs/03_analysis/04_combat_and_environment.md`：战斗、构筑、环境战术与多解法空间。
- `docs/03_analysis/05_implementation_validation.md`：公开可验证证据链与实现层判断。

## 来源层

- `docs/02_sources/*.md` 既包括来源类型导航页，也包括来源笔记与案例工作文件。
- 来源导航页用于说明“该类来源怎么整理”。
- 来源笔记用于把具体 Source ID 压实成事实、推断、限制与可用位置。
- 案例工作文件用于在回写正文前保存最小证据链、归属判断与未决问题。
- 区域包执行时，应优先在来源层形成“官方锚点 + 案例线索 + 实现验证入口”的三件套，再回写正文。

## 模板和工具

- `templates/source_note.md`：单个来源读书卡模板。
- `templates/case_note.md`：单个案例拆解模板。
- `scripts/check_repo.py`：结构与内容完整性检查。
- `Makefile`：统一命令入口。
