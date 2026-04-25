# ExecPlan: Stage-6 Freeze Maintenance Playbook

## Goal

把阶段 6 冻结维护态从“规则散落在 review sheet、状态页与实现验证页里”推进到“已有一份独立、可复用、可交接的 maintenance playbook”：

- 新建一份只服务冻结维护态的操作清单
- 明确默认检查顺序、trigger 判定与允许写回范围
- 把 `review sheet` 与 `05_implementation_validation.md` 的分工再压清一层
- 在不命中新 trigger 的前提下，继续保持五段 actual units 原文件不动

## Why It Matters

- 高优先级计划已经明确：阶段 6 已闭合，当前默认动作不是继续开新 round，而是维持条件触发维护态。
- 但仓库里还没有一份把“先看什么、检查什么、什么情况下禁止写回单段文件”压成单页操作清单的文件。
- 如果这层继续散落在状态页、review sheet 与实现验证页之间，后续会话仍更容易误把维护理解成“再开一轮 addendum”，而不是“先做 trigger 判定，再决定是否允许写回”。

## Repository Context

- 唯一高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 当前主动维护入口：
  - `docs/00_project/stage6_release_package_assembly_review_sheet.md`
- 当前维护结论承载：
  - `docs/03_analysis/05_implementation_validation.md`
- 当前状态入口：
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
- 本轮新增方法文件：
  - `docs/01_methodology/stage6_freeze_maintenance_playbook.md`

## Inputs and Evidence

- 阶段 6 首批发布包已经闭合。
- 第十轮 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 修正仍保持有效。
- 第十一轮到第三十二轮没有再命中新 actual-unit 级 trigger。
- 当前剩余风险已不是“有没有 review sheet”，而是“后续会话会不会绕过 assembly / review 层，重新误开 round 或误写回单段文件”。

## Milestones

1. 新建冻结维护态 playbook 方法文件
   - 固定默认阅读顺序
   - 固定四步 maintenance pass
   - 固定 no-trigger / trigger-hit 两类允许动作
2. 回写 review sheet
   - 把 playbook 纳入当前维护入口
   - 在 review sheet 中只保留摘要级维护 pass，不复制整份方法文件
3. 回写实现验证正文
   - 把“需要建立实现验证检查清单”从待验证问题转为已落地事实
   - 明确该清单当前服务的是 stage-6 冻结维护态，而不是新一轮 stage-5 扩写
4. 同步状态入口
   - 更新 `current_state.md`
   - 更新 `next_step.md`
   - 更新 `decision_log.md`
   - 更新 `repo_map.md`

## Validation

- 已新增 `docs/01_methodology/stage6_freeze_maintenance_playbook.md`
- `stage6_release_package_assembly_review_sheet.md` 已把 playbook 视为默认维护动作的配套入口
- `05_implementation_validation.md` 不再把“实现验证检查清单”留作未落地问题
- `current_state.md`、`next_step.md`、`repo_map.md` 对默认维护动作的描述一致
- `python scripts/check_repo.py` 与 `make check` 通过

## Progress

- 2026-04-26：创建本计划，锁定本轮只做冻结维护态 playbook 落档与入口同步，不重开 `round33`，也不回写五段 actual units。

## Decision Log

- 2026-04-26：决定把阶段 6 的默认维护动作再压成单独方法文件，避免规则继续散落在 review sheet、状态页与实现验证页中。
- 2026-04-26：决定把 playbook 定位为“冻结维护态操作清单”，而不是新的 project-level 总逻辑文件；它只服务 stage-6 review-layer 维护，不改写阶段划分。

## Outcomes & Retrospective

- 本子单元完成后，阶段 6 的默认维护入口将不只是一句“维持冻结态”，而是一套明确的执行顺序、trigger 判定与允许动作。
- 后续会话若未命中新 trigger，应先按 playbook 做 no-trigger 判定，再决定是否仅同步 review-layer / 状态文件；而不是直接续开新的 round 文件。
