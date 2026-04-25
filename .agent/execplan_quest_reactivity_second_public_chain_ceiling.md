# ExecPlan: Quest Reactivity Second Public Cross-Act Chain Ceiling

## Goal

把阶段 5 / `Quest Reactivity` 的第四个子单元固化为一次“证据上限判断”而不是继续空扩主干：判断现有公开来源里，除 `Minthara -> Moonrise Towers -> Act II reaction` 外，是否还能压出第二条同级别的公开跨阶段链；若不能，就把原因、降级口径与后续不该越级写死的边界正式写回正文与实现验证层。

## Why it matters

- 如果这一轮继续假装“第二条链应该马上存在”，阶段 5 会退回为了对称而硬拼案例，最后把 `Quest Reactivity` 写成全局 objective 表或补丁摘抄集。
- 如果这一轮把所有跨阶段读回都混在一起，仓库会失去最重要的层级区分：有些公开锚点足以支撑明确的 `Act I -> Act II` 读回链，有些锚点只能支撑 `gate`、`camp fold` 或 `ending feedback` 级别的 bundle。
- 当前真正需要的不是更多区域包，而是明确“第二条链为什么还不能成立”，这样后续阶段 5 才能从“继续找链”转为“巩固哪些判断能逼近 `objective / step`、哪些必须停在公开边界”。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：在首条 `readback spine`、上游前置链与 late `Act 1` / early `Act 2` 接缝基础上，评估是否还能压出第二条不依赖 `Minthara -> Moonrise Towers` 的同级别公开跨阶段链；若不能，就把证据上限与降级口径压回 `05_implementation_validation.md`。
- 上游已完成并可直接复用：
  - `.agent/execplan_quest_reactivity_cross_act_readback_spine.md`
  - `.agent/execplan_quest_reactivity_upstream_entry_diversion_gate_chain.md`
  - `.agent/execplan_quest_reactivity_late_act1_early_act2_transition_boundary.md`
  - `docs/02_sources/case_note_quest_reactivity_cross_act_readback_spine.md`
  - `docs/02_sources/case_note_quest_reactivity_upstream_entry_diversion_gate_chain.md`
  - `docs/02_sources/case_note_quest_reactivity_late_act1_early_act2_transition_boundary.md`
- 本轮主回写模块：
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- `BG3-OFF-016`：提供 `Mountain Pass / Creche` 的对话门槛、`Voss` 敌意变化、`Lae'zel` 即时反应与 `camp night` 后果读取时机。
- `BG3-OFF-007`：提供 `Karlach` 在 `Acts 1 and 2` 之间的反思时刻，以及营地作为队伍状态处理入口的公开边界。
- `BG3-OFF-010`：提供非 `Minthara` 的营地 scene / dialogue accessibility 锚点，包括 `Astarion`、`Mizora`、`Wyll` 与 `Voss`。
- `BG3-OFF-002`：提供 late-game `ending feedback`、`writing and flow` / `scripting` 维护边界，以及当前唯一被明确点名的 `Minthara -> Moonrise Towers -> Act II reaction` 链。
- `BG3-OFF-003`：提供 `Swiss cheese` 多入口设计语言，用于约束“高压 / 高收束 ≠ 多入口消失”。
- `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`：提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，用于判断哪些候选只够写到 bundle / fold 层。

## Milestones

1. 新建 `docs/02_sources/case_note_quest_reactivity_second_public_chain_ceiling.md`
   - 只评估三组候选：
     - `Mountain Pass / Creche -> Voss / camp night`
     - `Karlach` 跨 Act 反思 + 非 `Minthara` 营地可达性修复
     - late-game `evil ending cinematics` / `writing and flow` / `scripting`
   - 明确每组候选当前能写到哪一层，以及为什么还不够成为第二条同级别跨阶段链
2. 回写 `docs/03_analysis/02_quests_and_choices.md`
   - 新增一段“第二条公开跨阶段链为何暂不能成立”的正式口径
   - 明确当前最稳写法是“一条显式 readback spine + 数条较弱的跨阶段锚点”，而不是全局 objective 表
3. 回写 `docs/03_analysis/05_implementation_validation.md`
   - 新增“第二条公开跨阶段链证据上限”矩阵
   - 把候选分别降到 `gate / tension / camp fold / ending feedback bundle` 等公开边界
4. 同步状态文件
   - 更新 `current_state.md`、`next_step.md`、`decision_log.md`
   - 若无新来源，不强制修改 `source_index.md`
5. 运行 `python scripts/check_repo.py` 与 `make check`

## Validation

- `docs/03_analysis/02_quests_and_choices.md` 明确写出：当前还没有第二条不依赖 `Minthara -> Moonrise Towers` 的同级别公开跨阶段链，以及为什么。
- `docs/03_analysis/05_implementation_validation.md` 明确区分：
  - 哪些候选只够写到 `gate / tension / camp fold / ending feedback bundle`
  - 为什么它们还不够升级成“指定上游处理 -> 指定下游节点 -> 指定跨 Act 反应”的显式链
- `docs/00_project/current_state.md` 与 `docs/00_project/next_step.md` 能直接说明：阶段 5 的第四个子单元已完成，主线从“继续找第二条链”切换为“在既有主干上巩固 objective / step 与 bundle / flow 的分层上限”。
- 不新增任何与该判断无关的区域包扩写、剧情摘要或无关来源侦察。

## Progress

- 2026-04-24：创建本计划，锁定阶段 5 / `Quest Reactivity` 的第四个子单元为“第二条公开跨阶段链的证据上限判断”。

## Decision Log

- 2026-04-24：决定本轮不为了对称而强行拼出第二条 readback spine，而是优先把“为什么现在不能成立”写成仓库正式口径。
- 2026-04-24：决定将 `Mountain Pass / Creche`、`camp` 反应锚点与 late-game `ending feedback` 继续视作不同层级的 supporting anchors，而不是假装它们已经构成同级别显式跨阶段链。

## Surprises & Discoveries

- 现有公开来源里，非 `Minthara` 锚点并不稀少；真正稀缺的是“被明确点名的上游处理方式 -> 被明确点名的后续节点 -> 被明确点名的跨阶段反应”这一整条闭合链。
- 这说明阶段 5 目前的核心任务不是“再找一条看起来像链的东西”，而是主动承认公开证据的强弱分层：`Quest Reactivity`、`Party/Camp` 与 `ending feedback` 的锚点不能互相冒充。

## Outcomes & Retrospective

- 本子单元完成后，阶段 5 / `Quest Reactivity` 的下一个动作不应继续无上限寻找第二条链，而应在现有“一条显式主干 + 多条较弱锚点”基础上，继续巩固哪些结论可以逼近 `objective / step`，哪些必须停在 `bundle / flow / ending feedback` 的公开边界。
