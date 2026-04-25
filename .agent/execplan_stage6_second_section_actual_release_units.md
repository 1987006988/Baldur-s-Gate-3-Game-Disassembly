# ExecPlan: Stage-6 Second Section First Actual Release Units

## Goal

把阶段 6 的第六个子单元固定为“第二段：局部行动到状态回流”的首批实际发布单元：

- 不再停留在 `presentation_forms.md` 里的最低 queue，而是把第二段真正落成 `1` 组可复用的 `excerpt card / asset spec / traceback card`
- 本轮只处理一个位置：`第二段：局部行动到状态回流`
- 这组单元必须同时锚到 `04_combat_and_environment.md` 与 `02_quests_and_choices.md`
- 不新增研究来源，不回跳阶段 5，也不提前铺开第三段或收尾段

## Why It Matters

- 如果第二段继续只停在 queue 层，阶段 6 会卡在“入口页与第一段已有实物，但中段仍只是计划表”的半成品状态
- 第二段是整条展示链第一次把两份正文模块真正压成同一组发布物；如果这里做不好，后面的营地折叠与证据分级也会失去粒度模板
- 这一步还能验证仓库能否把“局部 agency”与“状态读回”安全并排，而不误写成单一案例因果链或全游戏 objective 总表

## Repository Context

- 当前唯一高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 直接上游子单元：
  - `.agent/execplan_stage6_first_actual_release_units_entry_and_first_section.md`
  - `docs/00_project/stage6_entry_first_section_release_units.md`
- 本子单元直接落地文件：
  - `docs/00_project/stage6_second_section_release_units.md`
  - `docs/01_methodology/presentation_forms.md`
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/repo_map.md`
  - `docs/03_analysis/04_combat_and_environment.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
  - `docs/00_project/decision_log.md`

## Inputs and Evidence

- 第二段的发布 queue 与约束：
  - `docs/01_methodology/presentation_forms.md`
- 当前最稳的左侧局部 agency 正文：
  - `docs/03_analysis/04_combat_and_environment.md`
- 当前最稳的右侧状态读回正文：
  - `docs/03_analysis/02_quests_and_choices.md`
- 当前最稳的证据边界：
  - `docs/03_analysis/05_implementation_validation.md`

## Milestones

1. 新建本子单元 ExecPlan
   - 明确本轮只落第二段，不并行处理第三段
2. 新建第二段实际发布单元承载文件
   - 写出 `1` 组 `excerpt card / asset spec / traceback card`
3. 最小回写展示 / 导航层
   - 在 `presentation_forms.md`、`deconstruction_display_overview.md` 与 `repo_map.md` 标明第二段已经从 queue 进入 actual units
4. 最小回写正文与证据边界
   - 在 `04_combat_and_environment.md` 锁定左侧 release anchor
   - 在 `02_quests_and_choices.md` 锁定右侧 release anchor
   - 在 `05_implementation_validation.md` 锁定第二段 actual units evidence lock
5. 同步状态
   - 更新 `current_state.md`
   - 更新 `next_step.md`
   - 更新 `decision_log.md`

## Validation

- 已新增 `.agent/execplan_stage6_second_section_actual_release_units.md`
- 已新增 `docs/00_project/stage6_second_section_release_units.md`
- `docs/00_project/stage6_second_section_release_units.md` 里已有：
  - `1` 组 `excerpt card`
  - `1` 份 `asset spec`
  - `1` 条 `traceback card`
- `04_combat_and_environment.md`、`02_quests_and_choices.md`、`05_implementation_validation.md` 已能分别提供：
  - 左侧局部 agency 锚点
  - 右侧状态读回锚点
  - 不可越级发布的边界
- `presentation_forms.md`、`deconstruction_display_overview.md` 与 `repo_map.md` 已明确第二段的承载文件与下一步落点
- `python scripts/check_repo.py` 与 `make check` 通过

## Progress

- 2026-04-25：创建本计划，确认第二段首批实际发布单元只做一组“双联卡”，职责是把“局部 agency”与“状态读回”并排压实，而不是伪造单一案例因果链

## Decision Log

- 2026-04-25：决定把第二段首批实际发布单元单独承载在 `docs/00_project/stage6_second_section_release_units.md`，避免把入口页 / 第一段文件继续膨胀成混合文件
- 2026-04-25：决定第二段实际单元采用“章节接力双联卡”写法：左侧锚定 `04_combat_and_environment.md` 的局部 agency，右侧锚定 `02_quests_and_choices.md` 的状态读回；不把 `Grymforge` 与 `Minthara` 误写成同一条具体因果链

## Surprises & Discoveries

- 第二段当前缺的不是更多段落原则，而是一条能明确声明“这是一组章节接力关系，不是同一案例的硬因果链”的发布单元模板
- `04` 与 `02` 都已有足够稳的高层结论，但若没有专门的 trace card 约束，很容易在展示层被误读成“所有局部解法都会被同等级读回”

## Outcomes & Retrospective

- 本子单元完成后，阶段 6 的下一唯一主任务应切到“第三段：延迟反馈折叠”的首批实际发布单元
- 在没有更强官方来源前，后续不应借“继续补第二段”之名回跳阶段 5，也不应把第二段扩写成全游戏 objective 总表或第二条对称 spine
