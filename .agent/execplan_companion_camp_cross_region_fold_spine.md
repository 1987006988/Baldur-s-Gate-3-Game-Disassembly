# ExecPlan: Companion / Camp / Long Rest Cross-Region Camp Fold Spine

## Goal

完成阶段 5 / `Companion / Camp / Long Rest` 的首个横向子单元，把既有营地正文、`Dark Urge bard`、`Minthara` 营地反应链与已完成区域包压成第一条可复述的跨区域 `camp fold / delayed feedback` 主干，并明确哪些节点仍只能停在 `feedback fold / dialogue accessibility bundle` 层，而不能误写成新的 `objective` 主链。

## Why it matters

- 如果营地模块继续停在“强案例 + 候补案例 + 补丁锚点”的并列结构，阶段 5 就还没有真正形成自己的横向主干。
- 如果反过来把 `Act 2` 收束点组、late-game `ending feedback` 与零散 camp fix 都拉成对称主链，仓库又会重犯把弱锚点误升格的错误。
- 当前最需要的不是再补一轮补丁侦察，而是把现有证据压成一条带边界的 spine，让后续能明确区分“进入主干的读回层”和“只作为 supporting bundle 的维护层”。

## Repository context

- 当前项目高优先级逻辑已经固定在：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 当前阶段 5 的前两条横向主干已形成并收口：
  - `Quest Reactivity`: 一条显式 spine + 多个支撑 bundle，且 objective-adjacent narrowing 已完成
  - `Combat / Environment`: 首条环境 spine + second spine ceiling / late-game boundary 已完成
- 因此当前唯一正确动作，不是回跳区域包，也不是再补营地零散条目，而是为 `Companion / Camp / Long Rest` 建立同等级的首条横向 spine。

## Inputs and evidence

### Direct analysis/context inputs

- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/05_implementation_validation.md`
- `docs/02_sources/case_note_dark_urge_bard_event.md`
- `docs/02_sources/case_note_minthara_camp_reaction_chain.md`
- `docs/02_sources/case_note_grove_goblin_resolution_matrix.md`
- `docs/02_sources/case_note_last_light_moonrise_gauntlet_convergence.md`
- `docs/02_sources/case_note_endgame_organization_compression.md`

### Primary source anchors reused in this subunit

- `BG3-OFF-002`
- `BG3-OFF-005`
- `BG3-OFF-007`
- `BG3-OFF-008`
- `BG3-OFF-010`
- `BG3-OFF-016`
- `BG3-OFF-001`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-PLY-002`

## Milestones

1. 锁定第一条 `camp fold / delayed feedback` spine 的链段与边界。
2. 新建 1 份跨区域 case note，只压最强链段，不扩成同伴人物志。
3. 回写 `docs/03_analysis/03_party_and_camp.md`，明确：
   - 哪些链段进入第一条营地主干
   - 哪些链段只停在 `feedback fold / dialogue accessibility bundle`
   - 哪些晚期节点应被理解为 `ending feedback handoff`
4. 回写 `docs/03_analysis/05_implementation_validation.md`，把营地主干放到阶段 5 的横向验证矩阵中。
5. 同步 `current_state.md`、`next_step.md` 与 `decision_log.md`，把下一唯一主任务切到营地主干的证据上限 / second-spine ceiling 子单元。

## Validation

- 必须新增 1 份阶段 5 专用 ExecPlan。
- 必须新增 1 份跨区域 case note。
- 必须在 `03_party_and_camp.md` 与 `05_implementation_validation.md` 中出现新的横向 spine 分层，而不是只追加补丁条目。
- 必须把 `Dark Urge bard`、`Grove / Goblin`、`Mountain Pass / Creche`、`Act 2` 收束点组与 `终局组织与收束压力` 放进同一条可复述链里。
- 必须写清：
  - `Dark Urge bard` 与 `Minthara` 为什么能进入主干
  - `Karlach` 反思、非 `Minthara` 营地修复为什么暂时只能停在 supporting bundle 层
  - late-game `ending feedback` 为什么是 handoff，而不是第二条 `objective` 主链

## Progress

- 2026-04-25：读取阶段 5 当前状态、三份高优先级计划文件、营地正文、实现验证正文、既有营地 case note 与相关 source note，确认本轮唯一主任务是“首条 `camp fold / delayed feedback` spine”，而不是继续做同类补丁侦察。
- 2026-04-25：完成本 ExecPlan，并据此新增跨区域 case note 与正文回写。

## Decision Log

- 2026-04-25：决定把 `Act 1 地表主区 -> Dark Urge bard / Grove / Goblin -> Mountain Pass / Creche -> Last Light / Moonrise / Gauntlet -> 终局组织与收束压力` 写成同一条营地主干，但只允许其中直接营地可见的节点承担 `camp fold` 身份；`Act 2` 收束点组与 late-game 终局组织只承担 `convergence-adjacent reread` 与 `ending feedback handoff`。
- 2026-04-25：决定不在本轮重新打开“第三案例候选”侦察，也不把 `Karlach` 跨 Act 反思与非 `Minthara` 营地修复强拉成第二条对称营地主干。

## Surprises & Discoveries

- 当前营地模块其实不缺证据入口，缺的是一条把这些入口按阶段串起来的 spine。
- `Dark Urge bard` 与 `Minthara` 并不是竞争关系：前者更像局部 `camp-state-shift sample`，后者更像第一块稳定的 delayed camp readout bundle。
- `Act 2` 与 late-game 的价值不在于再补 camp scene 摘录，而在于说明营地读回会逐步向 `convergence` 与 `ending feedback` 层移交。

## Outcomes & Retrospective

- 本子单元完成后，阶段 5 / `Companion / Camp / Long Rest` 将不再只是“营地模块正文已写过”，而会拥有自己的第一条横向 spine。
- 下一子单元应优先测试 second public camp spine ceiling / late-game boundary：判断 `Karlach` 反思、非 `Minthara` camp fix 与 late-game `ending feedback` 是否还能形成第二条公开 spine；若不能，就应明确降回 `reflection / dialogue accessibility / ending feedback bundle` 层。
