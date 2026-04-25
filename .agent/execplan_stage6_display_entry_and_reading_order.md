# ExecPlan: Stage-6 Display Entry and Reading Order

## Goal

把阶段 6 的首个子单元固定为“展示入口与阅读顺序锁定”，而不是重开任何研究主链。

- 把阶段 5 已闭合的 unified exit matrix 转译成读者可直接使用的入口语法。
- 锁定一条在仓库入口层一致的阅读顺序：
  `README.md -> deconstruction_display_overview.md -> 00_core_thesis.md -> 01_macro_structure.md -> 04_combat_and_environment.md -> 02_quests_and_choices.md -> 03_party_and_camp.md -> 05_implementation_validation.md`
- 让 `00_core_thesis.md` 与 `01_macro_structure.md` 承担展示入口职责，而不是继续把三条横向主干展示成三份并列未完工工程。
- 同步 `current_state.md`、`next_step.md`、`decision_log.md`，正式表明仓库已进入阶段 6。

## Why it matters

- 阶段 5 现在已经闭合，但仓库入口层仍容易看起来像“三条技术收口并排摆放”，而不是一条对外可读的反应性链条。
- `deconstruction_display_overview.md` 的展示顺序与原有阅读顺序存在错位，读者仍可能先读任务 / 营地，再回头补局部行动层。
- 如果这一层不先锁定，后续会话很容易再次把 `Quest`、`Combat`、`Camp` 当成并列主线继续扩写，而不是把它们当作同一展示链上的不同段落。

## Repository context

- 当前高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 当前直接相关的上一子单元：
  - `.agent/execplan_implementation_validation_stage5_exit_matrix.md`
  - `docs/02_sources/case_note_implementation_validation_stage5_exit_matrix.md`
- 当前需要被统一的入口文件：
  - `README.md`
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/repo_map.md`
  - `docs/03_analysis/00_core_thesis.md`
  - `docs/03_analysis/01_macro_structure.md`

## Inputs and evidence

- `docs/03_analysis/05_implementation_validation.md`
- `docs/03_analysis/00_core_thesis.md`
- `docs/03_analysis/01_macro_structure.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/04_combat_and_environment.md`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-007`
- `BG3-OFF-010`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-015`
- `BG3-OFF-016`

## Milestones

1. 新建阶段 6 首个子单元 ExecPlan
   - 明确本轮只处理展示入口与阅读顺序。
   - 明确不新增研究来源、不重开任何横向主干。
2. 更新 `README.md`
   - 新增面向读者的“当前展示入口”。
   - 把阶段 6 当前最稳的阅读顺序写清楚。
3. 更新 `docs/00_project/deconstruction_display_overview.md`
   - 把 unified exit matrix 翻译成当前展示入口说明。
   - 修正阅读顺序与展示顺序之间的错位。
4. 更新 `docs/03_analysis/00_core_thesis.md` 与 `docs/03_analysis/01_macro_structure.md`
   - 把阶段 5 的统一出口结论回写成展示入口层判断。
   - 明确宏观结构与局部行动在展示链中的先后关系。
5. 最小同步导航与索引
   - 更新 `docs/00_project/repo_map.md`
   - 更新 `docs/00_project/source_index.md` 中本轮新增引用的 `Where used`
6. 同步状态与决策
   - `docs/00_project/current_state.md`
   - `docs/00_project/next_step.md`
   - `docs/00_project/decision_log.md`
7. 运行校验
   - `python scripts/check_repo.py`
   - `make check`

## Validation

- 新增 `.agent/execplan_stage6_display_entry_and_reading_order.md`
- `README.md`、`deconstruction_display_overview.md`、`repo_map.md` 对同一条展示阅读顺序表述一致
- `00_core_thesis.md` 与 `01_macro_structure.md` 都能说明：阶段 5 的 exit matrix 现在服务展示入口，而不是新研究主线
- `source_index.md` 已同步本轮新增的 `Where used`
- `current_state.md` 与 `next_step.md` 明确表明仓库已进入阶段 6
- `python scripts/check_repo.py` 与 `make check` 通过

## Progress

- 2026-04-25：创建本计划，确认本轮只处理“展示入口 / 阅读顺序锁定”，不新增研究来源，不重开任何横向主干。

## Decision Log

- 2026-04-25：决定把阶段 5 的 unified exit matrix 升级为阶段 6 的展示入口，而不是继续保留在 `05_implementation_validation.md` 内部作为技术收束说明。
- 2026-04-25：决定把当前对外阅读顺序锁定为“总命题 -> 宏观结构 -> 局部行动 -> 任务回流 -> 营地折叠 -> 实现验证”，不再把 `Quest` / `Camp` / `Combat` 作为并列导论。

## Surprises & Discoveries

- 当前最大的入口问题不是研究不足，而是展示层存在顺序错位：展示总览已经把“局部行动”放在“任务回流”之前，但读者阅读顺序还停在旧的模块顺序。
- 阶段 5 的三条横向主干虽然类型不同，但现在都已经足够稳定，可以被展示层翻译成同一条链上的不同段落，而不是三份平行工程。

## Outcomes & Retrospective

- 本子单元完成后，阶段 6 应正式进入第二个子单元：继续把已锁定的阅读顺序压成模块职责 / 展示形态 / 发布导览矩阵。
- 在没有更强官方来源前，后续不应借“优化展示入口”之名回跳阶段 5 补第二条对称 spine。
