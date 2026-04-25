# ExecPlan: Stage-6 First Actual Release Units for Entry Page and Opening Section

## Goal

把阶段 6 的第五个子单元固定为“入口页 + 第一段的首批实际发布单元”：

- 不再讨论“每段最低要带什么”，而是先把已经锁定的 queue 落成第一批真的可复用产物。
- 本轮只处理两个位置：`入口页` 与 `第一段：命题与导航`。
- 每个位置都必须落成 `1` 组实际 `excerpt card`、`1` 份 `asset spec`、`1` 条 `traceback card`。
- 不新增研究来源，不回跳阶段 5，也不提前展开第二段以后的发布物。

## Why It Matters

- 如果阶段 6 停在“最低配置已经锁定”，发布层仍然只是结构化空表，后续会话会继续在“定义什么该做”与“真正做出第一批物料”之间来回摆动。
- 入口页与第一段承担的是整个展示链的边界与导航；只要这两段先落成，仓库就不再是纯计划状态，而进入可复用发布单元状态。
- 这一步也能验证当前 queue 是否真的够具体，还是仍然需要回到方法文件重写。

## Repository Context

- 当前唯一高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 直接上游子单元：
  - `.agent/execplan_stage6_display_entry_and_reading_order.md`
  - `.agent/execplan_stage6_module_guide_and_release_matrix.md`
  - `.agent/execplan_stage6_release_walkthrough_section_skeleton.md`
  - `.agent/execplan_stage6_first_release_package_excerpt_asset_queue.md`
- 本子单元直接落地文件：
  - `docs/00_project/stage6_entry_first_section_release_units.md`
  - `docs/01_methodology/presentation_forms.md`
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/repo_map.md`
  - `docs/03_analysis/00_core_thesis.md`
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/05_implementation_validation.md`
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
  - `docs/00_project/decision_log.md`

## Inputs and Evidence

- 现有入口边界与总逻辑：
  - `README.md`
  - `docs/00_project/deconstruction_display_overview.md`
- 现有命题与导航正文：
  - `docs/03_analysis/00_core_thesis.md`
  - `docs/03_analysis/01_macro_structure.md`
- 现有方法与发布最小清单：
  - `docs/01_methodology/presentation_forms.md`
- 现有发布证据边界：
  - `docs/03_analysis/05_implementation_validation.md`

## Milestones

1. 新建本子单元 ExecPlan
   - 明确本轮只落入口页与第一段的首批实际发布单元。
2. 新建首批发布单元承载文件
   - 为入口页写出 1 组实际 `excerpt card / asset spec / traceback card`
   - 为第一段写出 1 组实际 `excerpt card / asset spec / traceback card`
3. 最小回写方法 / 导航层
   - 在 `presentation_forms.md` 标明第五子单元已从 queue 进入 actual units。
   - 在 `deconstruction_display_overview.md` 与 `repo_map.md` 标明承载文件位置与下一步落点。
4. 最小回写正文与证据边界
   - 在 `00_core_thesis.md` 与 `01_macro_structure.md` 锁定可被首批发布单元安全摘录的 release anchor。
   - 在 `05_implementation_validation.md` 锁定这两组实际单元的 evidence lock / boundary。
5. 同步状态
   - 更新 `current_state.md`
   - 更新 `next_step.md`
   - 更新 `decision_log.md`

## Validation

- 已新增 `.agent/execplan_stage6_first_actual_release_units_entry_and_first_section.md`
- 已新增 `docs/00_project/stage6_entry_first_section_release_units.md`
- `docs/00_project/stage6_entry_first_section_release_units.md` 里，入口页与第一段各自都有：
  - `1` 组 `excerpt card`
  - `1` 份 `asset spec`
  - `1` 条 `traceback card`
- `presentation_forms.md`、`deconstruction_display_overview.md` 与 `repo_map.md` 已明确这批实际单元的位置，而不是仍停留在最低配置口径
- `00_core_thesis.md`、`01_macro_structure.md` 与 `05_implementation_validation.md` 已能为这批实际单元提供可回链锚点与不可越级边界
- `python scripts/check_repo.py` 与 `make check` 通过

## Progress

- 2026-04-25：创建本计划，确认本轮只把入口页与第一段落成第一批实际发布单元，不新增来源，不回跳阶段 5。

## Decision Log

- 2026-04-25：决定把首批实际发布单元单独落在 `docs/00_project/stage6_entry_first_section_release_units.md`，避免把方法文件继续膨胀成“既管规则又承载实物”的混合文件。
- 2026-04-25：决定继续遵守“只先做两段”的粒度约束，不提前铺开第二段以后内容，防止第五子单元再次退化成新的最低配置表。

## Surprises & Discoveries

- 当前缺的不是更多展示原则，而是第一批真正可被复制、审阅和继续扩写的发布单元样板。
- 入口页与第一段之所以适合先落地，是因为它们只依赖已经最稳定的边界与高层结构，不需要重新打开区域包侦察。

## Outcomes & Retrospective

- 本子单元完成后，阶段 6 的下一唯一主任务应切到“第二段：局部行动到状态回流”的首批实际发布单元，而不是继续重写入口说明或模块职责矩阵。
- 在没有更强官方来源前，后续依然不得借“继续补发布单元”之名回跳阶段 5、重开第二条对称主链。
