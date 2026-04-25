# ExecPlan: Stage-6 Third Section First Actual Release Units

## Goal

把阶段 6 的第七个子单元固定为“第三段：延迟反馈折叠”的首批实际发布单元：

- 不再停留在 `presentation_forms.md` 里的最低 queue，而是把第三段真正落成 `1` 组可复用的 `excerpt card / asset spec / traceback card`
- 本轮只处理一个位置：`第三段：延迟反馈折叠`
- 这组单元必须同时锚到 `03_party_and_camp.md` 与 `05_implementation_validation.md`
- 不新增研究来源，不回跳阶段 5，也不提前并行处理收尾段

## Why It Matters

- 如果第三段继续只停在 queue 层，阶段 6 就会停在“开场与中段已有实物，但营地折叠仍只是说明文字”的半成品状态
- 第三段是整条展示链第一次把 `camp fold / delayed feedback` 真的压成可制作单元；如果这里仍写成营地 scene 清单、人物附录或第二条对称主链，前面的阅读顺序会立刻失效
- 这一步还负责验证仓库能否把“前序状态被重新折回营地可见层”写成发布物，而不是把 `Dark Urge`、`Minthara`、`Lae'zel`、`Karlach` 等不同强度锚点误拼成同一条虚假因果链

## Repository Context

- 当前唯一高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 直接上游子单元：
  - `.agent/execplan_stage6_second_section_actual_release_units.md`
  - `docs/00_project/stage6_second_section_release_units.md`
- 本子单元直接落地文件：
  - `docs/00_project/stage6_third_section_release_units.md`
  - `docs/01_methodology/presentation_forms.md`
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/repo_map.md`
  - `docs/03_analysis/03_party_and_camp.md`
  - `docs/03_analysis/05_implementation_validation.md`
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
  - `docs/00_project/decision_log.md`

## Inputs and Evidence

- 第三段的发布 queue 与约束：
  - `docs/01_methodology/presentation_forms.md`
- 当前最稳的营地折叠正文：
  - `docs/03_analysis/03_party_and_camp.md`
- 当前最稳的证据分级与 supporting-bundle 边界：
  - `docs/03_analysis/05_implementation_validation.md`

## Milestones

1. 新建本子单元 ExecPlan
   - 明确本轮只落第三段，不并行处理收尾段
2. 新建第三段实际发布单元承载文件
   - 写出 `1` 组 `excerpt card / asset spec / traceback card`
3. 最小回写展示 / 导航层
   - 在 `presentation_forms.md`、`deconstruction_display_overview.md` 与 `repo_map.md` 标明第三段已经从 queue 进入 actual units
4. 最小回写正文与证据边界
   - 在 `03_party_and_camp.md` 锁定第三段 release anchor
   - 在 `05_implementation_validation.md` 锁定第三段 actual units evidence lock
5. 同步状态
   - 更新 `current_state.md`
   - 更新 `next_step.md`
   - 更新 `decision_log.md`

## Validation

- 已新增 `.agent/execplan_stage6_third_section_actual_release_units.md`
- 已新增 `docs/00_project/stage6_third_section_release_units.md`
- `docs/00_project/stage6_third_section_release_units.md` 里已有：
  - `1` 组 `excerpt card`
  - `1` 份 `asset spec`
  - `1` 条 `traceback card`
- `03_party_and_camp.md` 与 `05_implementation_validation.md` 已能分别提供：
  - `camp fold / delayed feedback` 正文锚点
  - `supporting bundle / handoff` 边界与不可越级发布限制
- `presentation_forms.md`、`deconstruction_display_overview.md` 与 `repo_map.md` 已明确第三段的承载文件与下一步落点
- `python scripts/check_repo.py` 与 `make check` 通过

## Progress

- 2026-04-25：创建本计划，确认第三段首批实际发布单元只做一组“折返层卡片”，职责是把“状态如何在营地 / 长休重新可见”压实，而不是把营地重写成人物附录、camp scene 清单或第二条对称营地主干

## Decision Log

- 2026-04-25：决定把第三段实际单元单独承载在 `docs/00_project/stage6_third_section_release_units.md`，避免继续把第二段或总览文件膨胀成混合承载页
- 2026-04-25：决定第三段实际单元采用“主折返卡 + supporting-bundle 边界条”的写法：主卡负责证明 `camp fold / delayed feedback` 已成立，边界条负责明确 `reflection / roster-state`、`dialogue accessibility maintenance` 与 `ending-feedback handoff` 不能被误升为第二条公开营地主干

## Surprises & Discoveries

- 第三段当前缺的不是更多营地案例，而是一条能明确声明“这是折返层，不是人物附录，也不是第二条对称营地主链”的发布模板
- `03_party_and_camp.md` 已经有足够稳的主干与 supporting-bundle 分层，真正需要补的是把这些层级翻译成可制作单元并锁死不可越级边界

## Outcomes & Retrospective

- 本子单元完成后，阶段 6 的下一个唯一主任务应切到“收尾段：证据分级”的首批实际发布单元
- 在没有更强官方来源前，后续不应借“继续补第三段”之名回跳阶段 5，也不应把第三段扩写成 camp scene 清单、同伴人物志或第二条对称 camp spine
