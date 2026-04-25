# ExecPlan: Companion / Camp / Long Rest Second Public Camp Spine Ceiling / Late-Game Boundary

## Goal

完成阶段 5 / `Companion / Camp / Long Rest` 的第二个横向子单元，测试 `BG3-OFF-007`、`BG3-OFF-010` 与既有 late-game `ending-feedback handoff` 结论是否足以压成第二条公开营地主干；若不能，就明确把它们降回 `reflection / roster-state bundle`、`dialogue accessibility maintenance bundle` 与 `ending-feedback handoff bundle`，关闭当前来源下的营地主干扩写冲动。

## Why it matters

- 如果第一条 `camp fold / delayed feedback` spine 建立后不立刻做 ceiling 测试，仓库很容易把 `Karlach` 反思、非 `Minthara` camp fix 与 late-game 读回误写成第二条对称营地主链。
- `Quest Reactivity` 与 `Combat / Environment` 都已经完成“首条主干 + 证据上限”两步；`Companion / Camp / Long Rest` 只有补齐同等边界，阶段 5 的三条横向主干才算同级闭合。
- 当前需要的不是再补 camp scene 条目，而是把“哪些只证明系统维护广度、哪些真的能进入 public spine”写清楚，避免后续会话重新回到人物志或对白清单。

## Repository context

- 当前高优先级逻辑以以下三份项目级文件为准：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 阶段 5 现状：
  - `Quest Reactivity`：已完成首条 readback spine、objective-adjacent narrowing 与 second public chain ceiling，当前来源下已收口。
  - `Combat / Environment`：已完成首条环境 spine 与 second spine ceiling / late-game boundary。
  - `Companion / Camp / Long Rest`：已完成首条 `camp fold / delayed feedback` spine，但尚未把 `BG3-OFF-007`、`BG3-OFF-010` 与 late-game handoff 正式压成 ceiling 结论。

## Inputs and evidence

### Direct analysis/context inputs

- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/05_implementation_validation.md`
- `.agent/execplan_companion_camp_cross_region_fold_spine.md`
- `docs/02_sources/case_note_companion_camp_cross_region_fold_spine.md`
- `docs/02_sources/case_note_endgame_organization_compression.md`
- `docs/02_sources/source_note_bg3_off_007_patch_2_party_camp.md`
- `docs/02_sources/source_note_bg3_off_010_hotfix_3_camp_reactivity.md`

### Primary source anchors reused in this subunit

- `BG3-OFF-007`
- `BG3-OFF-010`

## Milestones

1. 锁定第二条公开营地主干最可能被误升的候选锚点：
   - `Withers' Wardrobe` + `Karlach` 跨 `Act` 反思
   - 非 `Minthara` 的 camp scene / dialogue accessibility 修复
   - 既有 `Act II` 收束 reread 与 late-game `ending-feedback handoff`
2. 新建 1 份阶段 5 case note，只回答“这些锚点为什么不足以组成第二条 public camp spine”，不扩成 camp scene 清单。
3. 回写 `docs/03_analysis/03_party_and_camp.md`，明确：
   - 第一条营地主干已经成立
   - 第二条公开营地主干在当前来源下不成立
   - `BG3-OFF-007`、`BG3-OFF-010` 与 late-game handoff 分别停在哪类 supporting bundle
4. 回写 `docs/03_analysis/05_implementation_validation.md`，把同一 ceiling 结论写成公开验证分层矩阵。
5. 同步 `current_state.md`、`next_step.md`、`decision_log.md` 与 `source_index.md`，把下一唯一主任务切到阶段 5 / `Implementation Validation` 的收束子单元。

## Validation

- 必须新增 1 份阶段 5 专用 ExecPlan。
- 必须新增 1 份阶段 5 的 second public camp spine ceiling / late-game boundary case note。
- 必须在 `03_party_and_camp.md` 与 `05_implementation_validation.md` 中出现新的 ceiling 结论，而不是只补一行 open question。
- 必须明确写清：
  - `BG3-OFF-007` 为什么只稳定支撑 `reflection / roster-state bundle`
  - `BG3-OFF-010` 为什么只稳定支撑 `dialogue accessibility maintenance bundle`
  - late-game `ending feedback` 为什么继续是 handoff，而不是第二条公开营地主干
- 必须把阶段 5 / `Companion / Camp / Long Rest` 的当前状态收束为“1 条 public spine + supporting bundles + handoff boundary”，而不是保留“也许还有第二条 spine”的模糊口径。

## Progress

- 2026-04-25：已读取项目入口、阶段 5 当前状态、第一条营地主干 ExecPlan / case note，以及 `BG3-OFF-007`、`BG3-OFF-010` 的 source note，确认本轮唯一主任务是 second public camp spine ceiling / late-game boundary，而不是继续补 camp scene 条目。
- 2026-04-25：已建立本 ExecPlan，下一步按此新增 ceiling case note，并把结论回写到正文与状态文件。

## Decision Log

- 2026-04-25：决定不把 `BG3-OFF-007` 的 `Withers' Wardrobe` 与 `Karlach` 反思时刻强拉成第二条公开 camp spine；它们当前最稳的身份是 `reflection / roster-state bundle`。
- 2026-04-25：决定不把 `BG3-OFF-010` 中分散的 Astarion / Voss / Mizora / Wyll camp fix 强拉成第二条公开 camp spine；它们当前最稳的身份是 `dialogue accessibility maintenance bundle`。
- 2026-04-25：决定沿用既有 `Act II` 收束 reread 与 late-game `ending-feedback handoff` 结论，不把它们改写成第二条 camp-centered readback spine。

## Surprises & Discoveries

- 当前营地主干最缺的不是新材料，而是把“系统维护广度”和“public spine 强度”分开写的 ceiling 动作。
- `BG3-OFF-007` 与 `BG3-OFF-010` 的价值不在于补出一条更长的剧情链，而在于证明营地反馈层被广泛维护；这恰恰说明它们更像 bundle，而不是 spine。
- 第一条营地主干已经天然包含一个晚期 handoff，因此第二条 spine 若想成立，必须出现比 `Karlach` 反思或零散 accessibility fix 更强的官方跨区域读回锚点。

## Outcomes & Retrospective

- 本子单元完成后，阶段 5 / `Companion / Camp / Long Rest` 将不再停留在“首条营地主干已经有了，但第二条也许还能找”的模糊状态，而会形成与其余两条横向主干对齐的“主干 + ceiling”结构。
- 下一唯一主任务应切到阶段 5 / `Implementation Validation` 收束子单元：把三条横向主干的一条 spine、supporting bundle 与 ceiling / handoff 边界统一成阶段出口判断，而不是继续重开任何单条主干。
