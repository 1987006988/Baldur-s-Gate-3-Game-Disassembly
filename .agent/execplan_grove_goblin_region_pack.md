# ExecPlan: Grove / Goblin Region Pack

## Goal

把 `Grove / Goblin 冲突` 做成 `Act 1 地表主区` 之后的第一块“状态回流网”区域包：先用 1 份 `resolution matrix` 收束“处理方式 / 即时结果 / 延迟结果 / 营地折返”，再把稳定结论最小回写到任务、营地与实现验证三个模块。

## Why it matters

- 这是 `Act 1` 里最适合证明“任务不是派系二选一按钮，而是会跨长休、跨区域、跨反馈层回流的状态网”的块。
- 如果这一块被写成派系立场总结、道德评价或剧情摘要，`Act 1 地表主区` 刚建立起来的上游问题网会立刻断开。
- 这块做稳后，仓库就能把 `Underdark` 当作“问题框架重构”继续推进，而不是继续在 `Grove / Goblin` 上做无上限补剧情。

## Repository context

- 当前唯一主任务已切到 `Grove / Goblin 冲突`。
- 上游已完成：
  - `.agent/execplan_act1_surface_region_pack.md`
  - `docs/02_sources/case_note_act1_surface_route_pack.md`
- 本轮直接复用的既有案例：
  - `docs/02_sources/case_note_minthara_knockout_path.md`
  - `docs/02_sources/case_note_minthara_camp_reaction_chain.md`
- 本轮需要同步回写的模块是：
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/03_party_and_camp.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- `BG3-OFF-002`：击倒 Minthara 的后续落点、Act II 反应，以及更高层的 camp / reaction / flow 修复背景
- `BG3-OFF-004`：`knocked out` / `killed` 的状态差异，以及“击倒 -> 长休 -> 再处理其他首领”的时序失效点
- `BG3-OFF-008`：Minthara 在营地中的对话可达性与 `companion reaction` 修复
- `BG3-PLY-003`：玩家侧对 Minthara 路径稳定性与边界的案例线索

## Milestones

1. 锁定 `Grove / Goblin 冲突` 的边界：只写处理方式、时序与后续读出，不扩成地精营地剧情总表或 Grove 派系综述。
2. 新建 `docs/02_sources/case_note_grove_goblin_resolution_matrix.md`。
3. 把“这块最稳的写法是 resolution matrix，不是派系摘要”的结论回写到：
   - `docs/03_analysis/02_quests_and_choices.md`
   - `docs/03_analysis/03_party_and_camp.md`
   - `docs/03_analysis/05_implementation_validation.md`
4. 同步状态文件；若检查通过，则把下一唯一主任务切到 `Underdark`。

## Validation

- 至少 1 份 `Grove / Goblin` case note / resolution matrix 完成。
- `02_quests_and_choices.md` 完成显著回写，明确这块是“状态回流网”而不是“派系二选一”。
- `03_party_and_camp.md` 只同步已经被官方条目确认的营地折返，不借机扩写营地模块。
- `05_implementation_validation.md` 只新增验证入口与待验证问题，不升级私有实现断言。
- `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md` 已同步。

## Progress

- 2026-04-24：创建本计划，作为 `Grove / Goblin 冲突` 首轮区域包的执行记录。

## Decision Log

- 2026-04-24：本轮只做 1 份 `resolution matrix`，不再新增第二份 `Grove` 或 `Goblin camp` 子 note。
- 2026-04-24：现有来源足以先把这块写成“处理方式 / 时序 / 营地折返”的矩阵，但还不足以把全部首领顺序与所有派系结局写成事实表。

## Outcomes & Retrospective

- 完成后若检查通过，应直接切到 `Underdark`，不要继续围绕 `Grove / Goblin` 扩剧情细目或角色立场评论。
