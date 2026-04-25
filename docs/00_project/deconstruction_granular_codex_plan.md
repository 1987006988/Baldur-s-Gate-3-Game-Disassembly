# Deconstruction Granular Codex Plan

## 0. 这个文件怎么用

这不是高层路线图，而是操作脚本。每次只允许 Codex 执行一个块；做完一个块，再更新 `current_state.md` 和 `next_step.md`，再进入下一个块。

### 所有块共享的固定动作

1. **先读固定入口文件**
   - `README.md`
   - `docs/00_project/deconstruction_display_overview.md`
   - `docs/00_project/deconstruction_master_execution_plan.md`
   - `docs/00_project/current_state.md`
   - `docs/00_project/next_step.md`
   - `docs/00_project/source_index.md`
2. **先锁块的主问题**：一句话写清“这一块到底在总链条里证明什么”。
3. **先看现有来源，再补新来源**：先扫 `source_index.md`，不要一上来重搜所有资料。
4. **先写 case note，再回写 analysis**：区域包不允许直接跳过 case note 写大段正文。
5. **所有结论分三层**：`事实`、`推断`、`待验证问题`。
6. **完成后固定更新**：
   - `docs/00_project/current_state.md`
   - `docs/00_project/next_step.md`
   - `docs/00_project/decision_log.md`（如主线选择、边界或方法改变）
   - `docs/00_project/source_index.md`（如新增来源）
7. **最后跑检查**：`python scripts/check_repo.py`

### 所有块共享的“不要这样做”

- 不按剧情流水账写。
- 不只补来源、不回写正文。
- 不把玩家讨论直接升级为全局事实。
- 不把 Journal / Osiris 文档当成某条具体 shipped script 的直接实锤。
- 不让营地模块脱离前序状态单独膨胀。

---

## 1. 序章 / Nautiloid

### 1. 为什么这一块要拆

它是整个项目最适合做“模板块”的地方：边界清楚、体量可控、同时覆盖开场空间引导、多入口、早期战斗、队友收编、初始任务状态与第一批反馈埋点。

### 2. 这一块在总展示逻辑中的位置

它不负责解释整部作品，只负责给出“BG3 的反应性链条从哪里开始露头”。展示里它主要支撑：

- 宏观结构的起点设计
- 局部行动层的早期多解法
- 任务 / 队友 / 状态如何在开场就互相咬合

### 3. 这一块最该回答什么问题

- 开场为什么不是纯教程，而是一个小型多入口证明场？
- 早期队友、战斗、权限、探索和目标推进是如何被捆在一起的？
- 哪些机制只是引导，哪些机制已经在为后续反应性埋状态？

### 4. 这一块优先收哪些来源

1. 已有：`BG3-OFF-001`, `BG3-OFF-003`
2. 官方产品 / 开发者对开场、自由度、多入口的表述
3. 若需实现验证，优先看：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
4. 玩家案例只作为补线索，不先当主证据

### 5. 这一块优先用哪些代表案例

- `case_note_nautiloid_opening_state_and_multi_entry.md`（新建）
- `case_note_nautiloid_early_party_recruitment.md`（新建，可选）

### 6. 这一块最容易跑偏成什么

- 变成“飞船上发生了什么”的剧情复述
- 把开场伙伴招募写成人物介绍
- 把教程元素误写成完整系统结论

### 7. 这一块应先写什么，后写什么

- 先写：空间与目标如何组织
- 再写：玩家有哪些局部行动方式
- 再写：哪些状态会继续回流到后续
- 最后才写：这一块如何作为全项目模板

### 8. Codex 第一步做什么

1. 先读：
   - `docs/03_analysis/00_core_thesis.md`
   - `docs/03_analysis/01_macro_structure.md`
   - `docs/03_analysis/02_quests_and_choices.md`
   - `docs/03_analysis/04_combat_and_environment.md`
2. 在 `source_index.md` 里确认现有官方入口是否已足够支撑开场。
3. 若缺区域级来源，先登记并补官方 source note。

### 9. 第二步做什么

1. 新建 `docs/02_sources/case_note_nautiloid_opening_state_and_multi_entry.md`
2. 按模板写：
   - 玩家看到了哪些入口、门槛、伙伴与战斗节点
   - 哪些是空间多入口
   - 哪些是任务 / 状态埋点
   - 哪些只可写成“当前最强解释”
3. 如发现早期队友收编值得单列，再新建第二个 case note。

### 10. 第三步做什么

按以下顺序回写：

1. `docs/03_analysis/01_macro_structure.md`
2. `docs/03_analysis/04_combat_and_environment.md`
3. `docs/03_analysis/02_quests_and_choices.md`
4. 需要时只给 `05_implementation_validation.md` 增加待验证入口，不急着升级技术判断

### 11. 做到什么算完成

- 至少 1 个 Nautiloid case note 完成
- 至少 3 个分析模块完成最小回写
- 已经能说清 Nautiloid 在总逻辑里证明了什么
- 已把过度技术化部分留在 `待验证问题`

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `decision_log.md`（记录“Nautiloid 已成为模板块”）
- `source_index.md`（如新增来源）

### 13. 该块与其他块的耦合关系

- 向前无依赖
- 向后为 `Act 1 地表主区` 提供模板
- 对 `Companion / Camp / Long Rest` 只提供前置埋点，不直接写营地大结论

### 14. 哪些结论只能到 Implementation Validation 再升级

- 开场具体哪些状态由哪类脚本 / Journal 结构管理
- 具体权限门槛如何在数据结构中表示

### 15. 哪些结论可以先写成当前最强解释

- Nautiloid 是“多入口 + 早期状态埋点”的小型证明场
- 它不是纯教程，而是 BG3 核心逻辑的压缩样本

### 16. 哪些内容不能过早写死

- 不要过早断言某个早期开场分歧一定在后续大规模回流
- 不要把教程性强的设计直接外推为整游戏规律

---

## 2. Act 1 地表主区

### 1. 为什么这一块要拆

它是玩家第一次真正进入“高密度区域包”的地方，能看出 BG3 的探索、遭遇、任务触发和队伍行动如何自由交错。

### 2. 这一块在总展示逻辑中的位置

它负责把 Nautiloid 的开场样本，升级为“区域包式自由推进”的稳定形态。

### 3. 这一块最该回答什么问题

- 玩家为什么会感觉地表不是一条路，而是一张问题网？
- 区域探索与任务触发怎样互相穿插？
- 这里如何为营地、同伴、后续冲突埋下回流前史？

### 4. 这一块优先收哪些来源

1. 已有宏观结构来源：`BG3-OFF-001`, `BG3-OFF-003`
2. 若需要地表特定官方材料，优先补官方社区更新或开发者表述
3. 玩家案例只用于锁高价值入口，不直接当事实主柱

### 5. 这一块优先用哪些代表案例

- `case_note_act1_surface_route_pack.md`（新建）
- `case_note_act1_surface_recruitment_and_discovery.md`（新建，可选）

### 6. 这一块最容易跑偏成什么

- 变成“地表有哪些内容”的景点导览
- 把伙伴招募线拆成人物目录

### 7. 这一块应先写什么，后写什么

先写区域问题网，再写进入顺序差异，再写状态埋点，再写和营地 / Grove / Goblin 的连接。

### 8. Codex 第一步做什么

1. 读 `01_macro_structure.md` 与 Nautiloid 产出。
2. 画出 Act 1 地表主区的“入口 / 目标 / 阻力 / 横向支线”粗图。
3. 确认要不要为这个块新增官方来源。

### 9. 第二步做什么

1. 新建 `case_note_act1_surface_route_pack.md`
2. 只保留 2 到 3 条最能说明“问题网”的路径，不收全量路线
3. 标出每条路径如何连接后续 `Grove / Goblin`、`Underdark`、`Camp`

### 10. 第三步做什么

先回写 `01_macro_structure.md`，再回写 `02_quests_and_choices.md`，最后只在需要时给 `03_party_and_camp.md` 增加“前序状态入口”而不是直接扩写营地正文。

### 11. 做到什么算完成

- 能解释地表主区为什么是“问题网”而不是景点串联
- 至少 1 个区域 pack case note 完成
- 宏观结构与任务模块有稳定增量

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `source_index.md`（如补来源）

### 13. 该块与其他块的耦合关系

- 为 `Grove / Goblin` 冲突包提供前置网络
- 为 `Camp` 模块提供前史密度

### 14. 哪些结论只能到 Implementation Validation 再升级

- 哪些探索触发与 Journal 映射最稳定

### 15. 哪些结论可以先写成当前最强解释

- 地表主区建立了 BG3 式“当前阶段内总有不止一条接近目标的方法”

### 16. 哪些内容不能过早写死

- 不要过早宣称某条探索顺序是官方最优路径

---

## 3. Grove / Goblin 冲突

### 1. 为什么这一块要拆

这是 Act 1 最适合检验“任务不是分支树，而是状态回流网”的块。

### 2. 这一块在总展示逻辑中的位置

它主要服务展示链中的“任务 / Journal / 状态回流”部分，也会反向支撑营地与同伴反馈。

### 3. 这一块最该回答什么问题

- 冲突为什么不是二选一按钮，而是多入口、多立场、多后果组合？
- 玩家如何通过战斗、潜入、击倒、谈判、拖延等方式改写后续？
- 哪些后续会延迟到营地 / 长休或后续区域才被感知？

### 4. 这一块优先收哪些来源

1. 已有：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-005`, `BG3-PLY-002`, `BG3-PLY-003`
2. 继续优先官方 patch / hotfix / community update
3. 玩家讨论只作为验证分歧与边界案例

### 5. 这一块优先用哪些代表案例

- 复用现有 `case_note_minthara_knockout_path.md`
- 复用现有 `case_note_dark_urge_bard_event.md`
- 需要时新建 `case_note_grove_goblin_resolution_matrix.md`

### 6. 这一块最容易跑偏成什么

- 变成派系立场总结
- 变成角色评价或道德讨论
- 只盯着 Minthara 单点历史 bug

### 7. 这一块应先写什么，后写什么

先锁主案例与辅案例，再写状态链，再写营地 / 后续承接，最后才写更宏观解释。

### 8. Codex 第一步做什么

1. 先读现有 `02_quests_and_choices.md`、`03_party_and_camp.md`
2. 复核 `BG3-OFF-002`, `004`, `005`, `008`
3. 判断已有案例是否足够，是否需要新增“resolution matrix” case note

### 9. 第二步做什么

1. 若需要，新建 `case_note_grove_goblin_resolution_matrix.md`
2. 用矩阵记录：处理方式 / 即时结果 / 延迟结果 / 营地折返 / 仍待验证项
3. 不追求全覆盖，只保留最能说明状态回流的 2 到 3 条路径

### 10. 第三步做什么

1. 回写 `02_quests_and_choices.md`
2. 把确实发生营地折返的部分回写 `03_party_and_camp.md`
3. 把具体实现边界写进 `05_implementation_validation.md`

### 11. 做到什么算完成

- 冲突包已能清楚说明“多入口 + 延迟回流”
- 至少 1 条强案例和 1 条辅案例边界稳定
- 营地不再像孤立章节，而是作为下游反馈出现

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `decision_log.md`（如案例权重改变）
- `source_index.md`

### 13. 该块与其他块的耦合关系

- 强耦合 `03_party_and_camp.md`
- 强耦合 Act 1 地表、Underdark 与后续状态

### 14. 哪些结论只能到 Implementation Validation 再升级

- 击倒 / 击杀 / 跨长休 / 跨区域的具体状态边界

### 15. 哪些结论可以先写成当前最强解释

- Grove / Goblin 冲突是 BG3 “状态回流网”最早的大型证明场之一

### 16. 哪些内容不能过早写死

- 不要把角色特例直接外推为统一任务机制

---

## 4. Underdark

### 1. 为什么这一块要拆

Underdark 能说明 BG3 的自由推进并不只来自“主冲突做法不同”，还来自“同一阶段存在完全不同的空间与问题框架”。

### 2. 这一块在总展示逻辑中的位置

它主要加强“宏观结构与区域包”的部分，并补强“探索本身也是状态选择”。

### 3. 这一块最该回答什么问题

- 为什么进入 Underdark 本身就是一种阶段重构？
- 它如何重新组织任务、探索、战斗、资源与风险？
- 它和地表 / Grove / Goblin / Grymforge 之间如何互相改写阅读顺序？

### 4. 这一块优先收哪些来源

1. 已有高层来源：`BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-006`
2. 如果缺区域来源，再补官方社区更新或开发者材料

### 5. 这一块优先用哪些代表案例

- `case_note_underdark_entry_choice_pack.md`（新建）
- `case_note_underdark_to_grymforge_progression.md`（新建，可选）

### 6. 这一块最容易跑偏成什么

- 变成地下景观介绍
- 变成支线列表

### 7. 这一块应先写什么，后写什么

先写“进入 Underdark 改变了什么”，再写区域内部问题网，最后写它如何把玩家推向 Grymforge。

### 8. Codex 第一步做什么

1. 读 `01_macro_structure.md` 与 `BG3-OFF-006`
2. 先确定 Underdark 在 Act 1 里的角色：替代入口、并行路径、还是功能性转场

### 9. 第二步做什么

1. 新建 `case_note_underdark_entry_choice_pack.md`
2. 记录不同进入或推进方式会如何改变后续阅读顺序
3. 明确哪些是区域重构，哪些只是地图切换

### 10. 第三步做什么

先回写 `01_macro_structure.md`，再把与任务推进有关的稳定部分回写 `02_quests_and_choices.md`。

### 11. 做到什么算完成

- 能说明 Underdark 的价值是“阶段重构”，不是单纯新地图
- 宏观结构模块得到稳定增量

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `source_index.md`

### 13. 该块与其他块的耦合关系

- 向前连接地表 / Grove / Goblin
- 向后直接连接 Grymforge

### 14. 哪些结论只能到 Implementation Validation 再升级

- 进入与切换的具体 Journal / 状态映射

### 15. 哪些结论可以先写成当前最强解释

- Underdark 是 Act 1 内部“改写问题框架”的关键区域

### 16. 哪些内容不能过早写死

- 不要把 Underdark 的存在解释成单一正确路线

---

## 5. Grymforge

### 1. 为什么这一块要拆

它是当前仓库里最成熟的“战斗 / 环境 / 区域包耦合案例”，最适合继续用作横向主干验证点。

### 2. 这一块在总展示逻辑中的位置

它主要服务“局部行动层——战斗 / 环境 / 多入口”，并向任务模块做最小必要回流。

### 3. 这一块最该回答什么问题

- 为什么 Grymforge / Grym 不是单个 Boss 战，而是区域包式战术问题？
- 环境与战斗解法如何构成真正的选择系统？
- 这类选择如何反向支撑总论点，而不被误写成纯玩家脑洞？

### 4. 这一块优先收哪些来源

1. 已有：`BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004`
2. 如有新的官方 Grymforge / encounter 资料，再补官方 source note

### 5. 这一块优先用哪些代表案例

- 复用现有 `case_note_grymforge_environment_resolution.md`
- 必要时新建 `case_note_grymforge_encounter_bundle.md`

### 6. 这一块最容易跑偏成什么

- 变成打法攻略
- 只讨论 cheese，不解释为什么这类 cheese 会被系统承认

### 7. 这一块应先写什么，后写什么

先写高层区域框架，再写环境解法空间，再写哪些部分能回流到“任务也是选择系统”。

### 8. Codex 第一步做什么

1. 读 `04_combat_and_environment.md` 与现有 Grymforge case note
2. 复核 `BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004`
3. 判断现有 case 是否需要补第二个区域级 case

### 9. 第二步做什么

1. 只补足最能说明“环境是战术 agency 的一部分”的证据
2. 不扩成完整攻略集
3. 明确哪些打法只能算玩家案例入口

### 10. 第三步做什么

1. 先回写 `04_combat_and_environment.md`
2. 仅把“战斗 / 环境也是选择系统”这一层回写 `02_quests_and_choices.md`
3. 将需要技术化验证的部分留给 `05_implementation_validation.md`

### 11. 做到什么算完成

- Grymforge 已能稳定承担战斗模块主案例
- 回流到任务模块的边界清楚

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `decision_log.md`（如主归属发生变化）

### 13. 该块与其他块的耦合关系

- 强耦合 `04_combat_and_environment.md`
- 次级回流 `02_quests_and_choices.md`

### 14. 哪些结论只能到 Implementation Validation 再升级

- 具体机关、触发器与特殊判定的稳定实现边界

### 15. 哪些结论可以先写成当前最强解释

- Grymforge 把“战斗 / 环境 / 任务 / 区域”压到同一块里，说明 BG3 的选择系统不只在对话里

### 16. 哪些内容不能过早写死

- 不要把单条社区打法直接升格为官方主支持路径

---

## 6. Mountain Pass / Creche

### 1. 为什么这一块要拆

它是 Act 1 后段最适合检验“权限、阵营、伙伴张力与区域门槛如何交叠”的块。

### 2. 这一块在总展示逻辑中的位置

它主要补强宏观结构的“阶段性收束前的高压入口”，并向同伴 / 营地张力提供上游状态。

### 3. 这一块最该回答什么问题

- 为什么这一块既像区域门槛，又像伙伴 / 阵营压力测试？
- 进入与处理顺序如何改写后续阅读？
- 为什么它是 Act 1 到更后阶段的重要压力点？

### 4. 这一块优先收哪些来源

1. 已有：`BG3-OFF-001`, `BG3-OFF-003`
2. 若缺官方材料，优先补开发者谈权限、多入口或 companion tension 的材料

### 5. 这一块优先用哪些代表案例

- `case_note_mountain_pass_creche_gate_and_party_tension.md`（新建）

### 6. 这一块最容易跑偏成什么

- 变成剧情冲突复述
- 只写某个同伴立场，不写结构门槛与阶段压力

### 7. 这一块应先写什么，后写什么

先写区域门槛，再写权限 / 阵营 / 伙伴张力，再写它与 Act 切换的关系。

### 8. Codex 第一步做什么

1. 读 `01_macro_structure.md` 与 `03_party_and_camp.md`
2. 确认这块是以结构门槛为主，还是以伙伴张力为主；不要两边平均铺开

### 9. 第二步做什么

1. 新建 `case_note_mountain_pass_creche_gate_and_party_tension.md`
2. 用固定结构记录：入口条件、冲突对象、伙伴反应、后续影响

### 10. 第三步做什么

1. 先回写 `01_macro_structure.md`
2. 再回写 `03_party_and_camp.md` 的前置压力部分
3. 与任务回流有关的才回 `02_quests_and_choices.md`

### 11. 做到什么算完成

- 能说明这块为何是阶段门槛与关系压力的叠层
- 已形成 1 个清晰 case note

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `source_index.md`

### 13. 该块与其他块的耦合关系

- 向后强耦合 Act 2 进入逻辑
- 向下游强耦合同伴 / 营地张力

### 14. 哪些结论只能到 Implementation Validation 再升级

- 伙伴反应与特定门槛条件的具体状态映射

### 15. 哪些结论可以先写成当前最强解释

- Creche 是“结构门槛 + 关系压力”合并测试点

### 16. 哪些内容不能过早写死

- 不要把某个同伴反应直接外推为所有队友通则

---

## 7. Act 2 总框架

### 1. 为什么这一块要拆

Act 2 不是若干地点的并列集合，而是 BG3 把压力结构、节奏控制和状态收束显著加强的阶段。

### 2. 这一块在总展示逻辑中的位置

它是从 Act 1 的“多入口探索”过渡到中盘“高压收束”的桥。

### 3. 这一块最该回答什么问题

- Act 2 为什么会被玩家明显感知为“更有压力”的阶段？
- 这种压力是叙事气氛，还是系统组织方式变化？
- 营地、任务与区域推进如何在中盘更紧地互相绑定？

### 4. 这一块优先收哪些来源

1. Act 2 相关官方介绍、补丁说明、开发者表述
2. `BG3-OFF-011` ~ `014` 作为实现验证底座

### 5. 这一块优先用哪些代表案例

- `case_note_act2_pressure_and_reactivity_frame.md`（新建）

### 6. 这一块最容易跑偏成什么

- 只写气氛，不写结构
- 只写剧情冲突，不写压力如何组织玩家行为

### 7. 这一块应先写什么，后写什么

先写阶段框架，再拆具体区域点。

### 8. Codex 第一步做什么

先从 `01_macro_structure.md` 与 Act 1 产出里抽出“Act 2 之前已有的自由结构”，用来对比中盘变化。

### 9. 第二步做什么

新建 `case_note_act2_pressure_and_reactivity_frame.md`，只记录中盘框架，不急着深入某个地点。

### 10. 第三步做什么

回写 `01_macro_structure.md`，并给 `03_party_and_camp.md` 与 `05_implementation_validation.md` 准备中盘入口。

### 11. 做到什么算完成

- 已有 Act 2 的框架性 case note
- 已能说清中盘压力是结构变化，不是纯氛围变化

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`

### 13. 该块与其他块的耦合关系

- 是 `Shadow-Cursed Lands` 与 `Last Light / Moonrise / Gauntlet` 的上位框架

### 14. 哪些结论只能到 Implementation Validation 再升级

- 压力与状态限制具体如何被 Journal / script 组织

### 15. 哪些结论可以先写成当前最强解释

- Act 2 把 BG3 的自由感改造成“高压条件下的选择与承接”

### 16. 哪些内容不能过早写死

- 不要把“更压迫”简单等于“更线性”

---

## 8. Shadow-Cursed Lands

### 1. 为什么这一块要拆

这是中盘压力如何具体落地的最佳区域：风险、路径、遭遇与资源都被重新组织。

### 2. 这一块在总展示逻辑中的位置

它是 Act 2 框架的第一层实体化，用来证明中盘压力不只是一种叙事气氛。

### 3. 这一块最该回答什么问题

- 区域风险如何改变玩家推进方式？
- 为什么这里的探索、战斗和资源管理更紧耦合？
- 它如何把玩家推向 Last Light / Moonrise / Gauntlet 等收束点？

### 4. 这一块优先收哪些来源

- Act 2 官方区域资料
- 补丁 / 热修中涉及中盘可达性、反应链与同伴反馈的条目

### 5. 这一块优先用哪些代表案例

- `case_note_shadow_cursed_lands_pressure_loop.md`（新建）

### 6. 这一块最容易跑偏成什么

- 变成气氛描写
- 变成战斗难度抱怨总结

### 7. 这一块应先写什么，后写什么

先写区域风险如何组织行为，再写任务与营地如何读出这个压力。

### 8. Codex 第一步做什么

读 Act 2 框架 case note，先确认压力变量，再找具体区域例子。

### 9. 第二步做什么

新建 `case_note_shadow_cursed_lands_pressure_loop.md`，记录：风险、路线、资源、触发、反馈。

### 10. 第三步做什么

回写 `01_macro_structure.md` 与 `04_combat_and_environment.md`，再把稳定的状态回流部分写进 `02_quests_and_choices.md`。

### 11. 做到什么算完成

- 已能说明 Shadow-Cursed Lands 是“压力组织器”
- 至少 2 个模块得到稳定回写

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `source_index.md`

### 13. 该块与其他块的耦合关系

- 向后直接连接 `Last Light / Moonrise / Gauntlet`
- 也为营地反馈提供高压前史

### 14. 哪些结论只能到 Implementation Validation 再升级

- 中盘压力具体由哪些 flags / states 触发

### 15. 哪些结论可以先写成当前最强解释

- Shadow-Cursed Lands 把探索、风险与推进重新绑紧了

### 16. 哪些内容不能过早写死

- 不要把所有中盘压力都归因于单一区域机制

---

## 9. Last Light / Moonrise / Gauntlet / 相关收束点

### 1. 为什么这一块要拆

这里是 BG3 中盘最强的“收束组织器”，多个前置路径、关系与任务在这里交叉碰撞。

### 2. 这一块在总展示逻辑中的位置

它主要支撑“任务 / Journal / 状态回流”和“Act 收束”的部分。

### 3. 这一块最该回答什么问题

- 为什么这些地点 / 节点要放在一起看，而不是各自单拆？
- 前面累积的路径差异在这里如何被重新压缩与读取？
- 为什么这里能说明 BG3 的中盘不是松散分支，而是阶段收束？

### 4. 这一块优先收哪些来源

- Act 2 相关官方资料
- 已有 patch / hotfix / community update
- Journal / Osiris 文档只用于验证“任务收束如何组织”的思路

### 5. 这一块优先用哪些代表案例

- `case_note_last_light_moonrise_gauntlet_convergence.md`（新建）

### 6. 这一块最容易跑偏成什么

- 只做地点攻略
- 只追剧情高潮，不写收束结构

### 7. 这一块应先写什么，后写什么

先写收束关系图，再写个别节点，再写营地 / 同伴 / 后续承接。

### 8. Codex 第一步做什么

先画“前置路径 → 收束节点 → 后续反馈”的三段关系图。

### 9. 第二步做什么

用 `case_note_last_light_moonrise_gauntlet_convergence.md` 只收最强的 2 到 3 条收束链，不追全收集。

### 10. 第三步做什么

回写顺序：
1. `02_quests_and_choices.md`
2. `03_party_and_camp.md`
3. `01_macro_structure.md`
4. `05_implementation_validation.md`

### 11. 做到什么算完成

- 已能说清这些节点为何要作为一个收束组来写
- 至少任务模块与营地模块同时得到稳定增量

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `decision_log.md`（如对中盘结构判断升级）

### 13. 该块与其他块的耦合关系

- 强耦合 Act 2 全框架
- 为 Act 3 提供状态压缩前史

### 14. 哪些结论只能到 Implementation Validation 再升级

- 收束节点的任务状态如何被具体组织与触发

### 15. 哪些结论可以先写成当前最强解释

- 这是 BG3 中盘最强的“多路径压缩区”之一

### 16. 哪些内容不能过早写死

- 不要把所有中盘收束都归结到单一地点

---

## 10. Act 3 总框架

### 1. 为什么这一块要拆

Act 3 会把前面分散的多线程推进推到高密度城市与终局组织中，是检验 BG3 反应性能否承压的关键阶段。

### 2. 这一块在总展示逻辑中的位置

它是“Act 收束与终局压力”章节的总框架。

### 3. 这一块最该回答什么问题

- 为什么 Act 3 常被感知为密度骤增？
- 这种密度如何改变玩家的反应性体验？
- 多派系并行与城市空间如何重构前面建立的链条？

### 4. 这一块优先收哪些来源

- 官方城市 / 后期 / 终局相关资料
- 后期 patch / hotfix / 官方更新中涉及城市、终局组织和 companion reaction 的条目

### 5. 这一块优先用哪些代表案例

- `case_note_act3_density_and_resolution_load.md`（新建）

### 6. 这一块最容易跑偏成什么

- 变成城市地点列表
- 只写后期太忙、不写结构原因

### 7. 这一块应先写什么，后写什么

先写城市 / 派系 / 终局的组织方式，再拆具体区域与组织。

### 8. Codex 第一步做什么

从 `01_macro_structure.md` 与 Act 2 产出里抽出“前面已建立的阶段收束机制”，作为对照。

### 9. 第二步做什么

新建 `case_note_act3_density_and_resolution_load.md`，记录密度、并行线、城市空间和终局压力之间的关系。

### 10. 第三步做什么

先回写 `01_macro_structure.md`，再准备 `Rivington / Wyrm’s Crossing / Lower City` 分块。

### 11. 做到什么算完成

- Act 3 的框架 case note 已完成
- 已能说清后期不是“内容更多”那么简单，而是组织方式变了

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`

### 13. 该块与其他块的耦合关系

- 是 Act 3 细分区域的上位框架
- 也会影响终局组织的写法

### 14. 哪些结论只能到 Implementation Validation 再升级

- 高密度城市中的多线状态具体如何组织

### 15. 哪些结论可以先写成当前最强解释

- Act 3 是“高反应性在高密度环境下的承压测试”

### 16. 哪些内容不能过早写死

- 不要把高密度直接等同于设计失败或成功

---

## 11. Rivington / Wyrm’s Crossing / Lower City / 终局组织

### 1. 为什么这一块要拆

这是把 Act 3 框架落成具体城市包与终局组织包的层级。

### 2. 这一块在总展示逻辑中的位置

它主要服务“Act 收束与终局压力”，并部分服务“宏观结构的城市化变形”。

### 3. 这一块最该回答什么问题

- 城市不同区块如何承担不同密度与功能？
- 多派系、多目标与终局组织如何共同改写阅读顺序？
- 为什么这里仍然能保留 BG3 式多入口感，而不是彻底崩成清单？

### 4. 这一块优先收哪些来源

- 官方城市 / 派系 / 终局资料
- 补丁中涉及 Act 3 reaction、flow、accessibility 的条目

### 5. 这一块优先用哪些代表案例

- `case_note_rivington_entry_pressure.md`（新建）
- `case_note_wyrms_crossing_bridge_and_gate_pack.md`（新建）
- `case_note_lower_city_faction_resolution_pack.md`（新建）
- `case_note_endgame_organization_compression.md`（新建，可选）

### 6. 这一块最容易跑偏成什么

- 变成城市导览
- 变成派系百科
- 变成终局剧情复述

### 7. 这一块应先写什么，后写什么

先写区块功能差异，再写派系 / 终局组织如何跨区块重组玩家行为，最后写哪些状态被压缩结算。

### 8. Codex 第一步做什么

先决定本轮只做哪个子块，不要四块一起铺开。

### 9. 第二步做什么

为当轮子块新建 case note，并固定只保留：
- 一个空间组织问题
- 一个任务 / 派系交错问题
- 一个状态收束问题

### 10. 第三步做什么

根据子块性质选择回写主文：
- 空间主导：先回 `01_macro_structure.md`
- 状态主导：先回 `02_quests_and_choices.md`
- 终局压力主导：先回 `00_core_thesis.md` 与 `05_implementation_validation.md`

### 11. 做到什么算完成

- 至少完成 1 个城市子块和 1 个终局组织子块
- 已能解释 Act 3 的城市密度如何服务收束，而不是只让内容显多

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `decision_log.md`（如城市包写法需要修正）

### 13. 该块与其他块的耦合关系

- 强耦合 Act 3 总框架
- 强耦合终局组织与总论点回写

### 14. 哪些结论只能到 Implementation Validation 再升级

- 终局组织与城市多线状态的具体脚本 / Journal 映射

### 15. 哪些结论可以先写成当前最强解释

- Act 3 的城市区块在功能上并不等价，而是共同承担“高密度收束”

### 16. 哪些内容不能过早写死

- 不要把城市每一区块都写成同一种结构单元

---

## 12. Companion / Camp / Long Rest（跨阶段系统）

### 1. 为什么这一块要拆

它不是某个区域，而是所有区域包的下游反馈折叠层。单独拆它，是为了防止项目误把它看成氛围附录。

### 2. 这一块在总展示逻辑中的位置

它位于“任务回流”之后，“Act 收束”之前，是整条链中最重要的延迟反馈读出层。

### 3. 这一块最该回答什么问题

- 营地 / 长休如何折叠前序状态？
- 哪些反馈是任务后果的再解释，哪些是关系推进自己的调度？
- 为什么官方会持续修 camp scene、dialogue accessibility、companion reaction？

### 4. 这一块优先收哪些来源

1. 已有：`BG3-OFF-002`, `BG3-OFF-005`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-009`, `BG3-OFF-010`
2. 后续只在出现更强官方来源时再补
3. 玩家案例继续只作为线索

### 5. 这一块优先用哪些代表案例

- 复用 `case_note_dark_urge_bard_event.md`
- 复用 `case_note_minthara_camp_reaction_chain.md`
- 保留 `case_note_halsin_rescue_camp_feedback.md` 作为边界候选
- 如需要，新增 `case_note_camp_feedback_fold_layer.md`

### 6. 这一块最容易跑偏成什么

- 变成同伴人物志
- 变成恋爱系统总整理
- 变成围绕单一热修继续加料

### 7. 这一块应先写什么，后写什么

先写“营地折叠了什么”，再写案例，不要反过来让案例决定整个模块。

### 8. Codex 第一步做什么

1. 先复核现有 `03_party_and_camp.md`
2. 判断这次是“新增跨区域折叠证据”，还是“只是同类补丁低收益噪音”
3. 若是后者，直接停止，不新增来源

### 9. 第二步做什么

只有在出现更强来源时：
1. 补 source note
2. 补 case note
3. 只写能证明“折叠层”而不是“单角色特例”的部分

### 10. 第三步做什么

回写 `03_party_and_camp.md`，并在必要时同步到 `02_quests_and_choices.md` 与 `05_implementation_validation.md`。

### 11. 做到什么算完成

- 模块继续维持“强案例 + 候补案例 + 系统型补丁锚点”结构
- 没有重新滑回人物总整理

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `decision_log.md`（如模块边界改变）
- `source_index.md`

### 13. 该块与其他块的耦合关系

- 上游依赖所有区域包
- 下游影响 Act 收束与总论点解释

### 14. 哪些结论只能到 Implementation Validation 再升级

- 长休优先级、事件调度和对话可达性的更细实现结构

### 15. 哪些结论可以先写成当前最强解释

- 营地 / 长休是反馈折叠层，而不是纯休整界面

### 16. 哪些内容不能过早写死

- 不要把角色特例、EA 热修或单条 patch note 累积写成统一机制已被完全证实

---

## 13. Quest Reactivity（跨阶段主干）

### 1. 为什么这一块要拆

它是整条总链最核心的横向主干：解释 BG3 的反应性为何不只是剧情分支数量。

### 2. 这一块在总展示逻辑中的位置

位于“局部行动层”之后、“营地折叠层”之前，是整条链的中轴。

### 3. 这一块最该回答什么问题

- BG3 如何把处理方式写回后续状态？
- 为什么反馈经常是延迟到后续区域、营地或 Act 才被感知？
- Journal 结构、任务状态与玩法自由度如何互相支撑？

### 4. 这一块优先收哪些来源

1. 已有任务主干来源
2. `BG3-OFF-012`, `013`, `014` 用作实现验证底座
3. 补丁 / 热修继续作为状态边界证据

### 5. 这一块优先用哪些代表案例

- 复用 `case_note_minthara_knockout_path.md`
- 复用 `case_note_dark_urge_bard_event.md`
- 未来按区域包补新的 resolution matrix

### 6. 这一块最容易跑偏成什么

- 变成全任务表格
- 只写分支，不写延迟反馈与状态回流

### 7. 这一块应先写什么，后写什么

先写“选择点 → 状态变化 → 后续反馈”链，再写 Journal / 实现验证，不反过来。

### 8. Codex 第一步做什么

1. 每完成一个区域包，就抽出其中最强的一条状态回流链
2. 不足以形成链的，不回写主干

### 9. 第二步做什么

把新链条先写成 case note，明确：
- 哪些事实已稳
- 哪些只是推断
- 哪些待 Journal / Osiris 资料校验

### 10. 第三步做什么

更新 `02_quests_and_choices.md`，并在 `05_implementation_validation.md` 补“为什么这条链可升级 / 不能升级”。

### 11. 做到什么算完成

- 至少每个 Act 都有能代表该阶段的状态回流链
- Quest Reactivity 不再依赖单一 Act 1 案例支撑

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `source_index.md`

### 13. 该块与其他块的耦合关系

- 上接 Combat / Environment 与 Macro Structure
- 下接 Camp / Long Rest 与终局收束

### 14. 哪些结论只能到 Implementation Validation 再升级

- Journal / quest state 的更细组织方式

### 15. 哪些结论可以先写成当前最强解释

- BG3 的任务反应性来自状态回流，而不只来自即时分支

### 16. 哪些内容不能过早写死

- 不要把一条强案例误写成整游戏所有任务都同等复杂

---

## 14. Combat / Environment（跨阶段主干）

### 1. 为什么这一块要拆

它解释玩家最早感知到的“我想到的办法可以成立”从何而来，是反应性链的上游制造器。

### 2. 这一块在总展示逻辑中的位置

位于宏观结构之后、任务回流之前，是局部能动性的核心来源。

### 3. 这一块最该回答什么问题

- 为什么 BG3 的“选择”不只发生在对白？
- 为什么空间、地形、表面、高差、机关、开战方式能成为真正的解法资源？
- 这些战术自由如何进一步被任务与营地承接？

### 4. 这一块优先收哪些来源

- 已有：`BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004`
- 后续优先补官方区域或战术 agency 资料

### 5. 这一块优先用哪些代表案例

- 复用 `case_note_grymforge_environment_resolution.md`
- 未来按区域包补 `case_note_environment_multi_solution_cross_act.md`

### 6. 这一块最容易跑偏成什么

- 变成 build / 打法展示
- 变成战斗攻略集

### 7. 这一块应先写什么，后写什么

先写“为什么这构成真正选择”，再写具体打法与环境资源。

### 8. Codex 第一步做什么

每做完一个区域包，先问：这个包里有没有足够强的“空间 / 战斗 / 环境改写”链？没有就不回写。

### 9. 第二步做什么

对有资格回写的案例，先写 case note，只保留最能体现 agency 的行为链。

### 10. 第三步做什么

更新 `04_combat_and_environment.md`，并只把稳定层回写给 `02_quests_and_choices.md`。

### 11. 做到什么算完成

- 至少 Act 1、Act 2、Act 3 各有 1 个能代表该阶段的战术 agency 案例
- 模块不再只靠 Grymforge 一块支撑

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `source_index.md`

### 13. 该块与其他块的耦合关系

- 上游承接宏观结构
- 下游把局部行动写回任务回流

### 14. 哪些结论只能到 Implementation Validation 再升级

- 具体环境交互、触发器与行为判定的实现边界

### 15. 哪些结论可以先写成当前最强解释

- 战斗 / 环境是 BG3 反应性链的上游动作空间，而不是旁支玩法

### 16. 哪些内容不能过早写死

- 不要把单个精彩打法当成整个系统都允许同等自由的证据

---

## 15. Implementation Validation（横向校验层）

### 1. 为什么这一块要拆

如果没有这一层，项目会越来越像“高度合理的研究想象”；有了这一层，才能知道哪些结论已经够稳，哪些还必须保留为推断。

### 2. 这一块在总展示逻辑中的位置

它放在最后，不是因为不重要，而是因为它负责给前面整条链做校正和分级。

### 3. 这一块最该回答什么问题

- 哪些体验层判断已有官方或公开实现结构支撑？
- 哪些地方只能说到 Journal / Osiris / patch 暗示的层级？
- 哪些地方必须明确降级？

### 4. 这一块优先收哪些来源

1. `BG3-OFF-011`：Osiris 入门
2. `BG3-OFF-012`：Journal Editor Overview
3. `BG3-OFF-013`：Journal Structure Overview
4. `BG3-OFF-014`：Adding a Quest to a Situation
5. 已有 patch / hotfix / community update
6. 开发者说明与 UI 可观察结构

### 5. 这一块优先用哪些代表案例

- `case_note_journal_osiris_validation_matrix.md`（新建）
- 复用任务 / 营地 / 战斗主案例作为验证对象，不另起一堆新剧情案例

### 6. 这一块最容易跑偏成什么

- 变成技术概念仓库
- 为了显得深入而过度断言具体实现

### 7. 这一块应先写什么，后写什么

先写“哪些主张要验证”，再去找公开结构入口；不要反过来先啃一堆技术文档再硬找可套的结论。

### 8. Codex 第一步做什么

1. 列出当前最需要验证的 3 条主张
2. 给每条主张标注需要的公开入口：Patch / Journal / Osiris / UI / Developer explanation

### 9. 第二步做什么

1. 新建 `case_note_journal_osiris_validation_matrix.md`
2. 用矩阵记录：待验证主张 / 可用公开入口 / 证据等级 / 是否可升级

### 10. 第三步做什么

1. 更新 `05_implementation_validation.md`
2. 若某条判断被升级或降级，再回写对应主模块
3. 把无法升级的地方明确写进“待验证问题”，不要硬拗

### 11. 做到什么算完成

- 每条主干模块至少有 1 组明确验证入口
- `05_implementation_validation.md` 不再只是原则说明，而是实际验证矩阵

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `decision_log.md`（如结论等级变化）
- `source_index.md`

### 13. 该块与其他块的耦合关系

- 横向耦合所有模块
- 不独立生产总论点，只校正总论点

### 14. 哪些结论只能到 Implementation Validation 再升级

- 任何带有具体 Journal / Osiris / 脚本组织意味的判断
- 任何声称“系统就是这样实现”的句子

### 15. 哪些结论可以先写成当前最强解释

- 公开 Journal / Osiris 文档足以作为验证框架，但不足以直接证明 shipped content 的每一条私有脚本路径

### 16. 哪些内容不能过早写死

- 不要把 Modding 文档等同于开发内参
- 不要因为能说出术语，就误以为已经完成验证

---

## 16. 阶段 6 / 首轮发布包总装配 / 维护控制层

### 1. 为什么这一块要拆

五段 actual units 虽然都已落成，但它们仍需要一层统一的 assembly / review，才能避免后续会话把 supporting bundle 误写成新主链、把 handoff 顺序打乱，或借审阅之名回头重写 queue。

### 2. 这一块在总展示逻辑中的位置

它不是新的第六段，而是阶段 6 在五段闭合之后的总装配层：负责把入口页、第一段、第二段、第三段、收尾段装成同一条发布链。

### 3. 这一块最该回答什么问题

- 五段 actual units 合起来时，顺序、handoff 与 evidence lock 是否一致？
- 哪些问题只需在审阅层记录，哪些问题才真的值得回写单段文件？
- 如何在不复制五段正文的前提下，保留一份可交接的 assembly / review sheet？

### 4. 这一块优先读哪些文件

1. `docs/01_methodology/presentation_forms.md`
2. `docs/00_project/repo_map.md`
3. `docs/03_analysis/05_implementation_validation.md`
4. `docs/01_methodology/stage6_freeze_maintenance_playbook.md`
5. `docs/00_project/stage6_entry_first_section_release_units.md`
6. `docs/00_project/stage6_second_section_release_units.md`
7. `docs/00_project/stage6_third_section_release_units.md`
8. `docs/00_project/stage6_final_section_release_units.md`

### 5. 这一块优先产出什么

- `.agent/execplan_stage6_release_package_assembly_review.md`
- `.agent/execplan_stage6_release_package_assembly_review_round32.md`
- `.agent/execplan_stage6_freeze_maintenance_playbook.md`
- `docs/00_project/stage6_release_package_assembly_review_sheet.md`

### 6. 这一块最容易跑偏成什么

- 把 review sheet 写成五段正文的重复拼贴
- 借审阅之名回头重写 queue
- 把 modding / Journal 文档越级写成 shipped content 实锤
- 把 supporting bundle、handoff 或 open questions 误升级成新主链

### 7. 这一块应先写什么，后写什么

先写 assembly map，再写 review checklist，再写 writeback trigger，最后才决定是否需要局部回写单段承载文件。

### 8. Codex 第一步做什么

1. 先核对五段 actual units 的顺序、handoff 与 traceback path
2. 确认当前没有第六段 actual units 的需求，只需要总装配 / 审阅层

### 9. 第二步做什么

1. 新建 `stage6_release_package_assembly_review_sheet.md`
2. 固定写出：
   - `assembly map`
   - `review checklist`
   - `writeback trigger`
3. 不复制五段全文，只保留装配与审阅必需信息

### 10. 第三步做什么

1. 回写 `presentation_forms.md`
2. 回写 `deconstruction_display_overview.md`
3. 回写 `deconstruction_master_execution_plan.md`
4. 回写 `repo_map.md`
5. 在 `05_implementation_validation.md` 补 assembly / review anchor 与 evidence lock

### 11. 做到什么算完成

- 已有一份独立的 assembly / review sheet
- 高优先级总计划文件与方法 / 导航文件都已同步到这一步
- `05_implementation_validation.md` 已能解释 assembly / review 层当前可安全发布到哪一层
- 冻结维护态已有独立 playbook，可在 no-trigger 场景下阻止误开 `round33`

### 12. 完成后必须更新哪些文件

- `current_state.md`
- `next_step.md`
- `decision_log.md`
- 阶段 6 实际被更新的展示 / 导航 / 验证文件

### 13. 该块与其他块的耦合关系

- 上游依赖阶段 6 的五段 actual units
- 下游只耦合“条件触发维护 round”，不直接生成新段落

### 14. 哪些结论只能到 Implementation Validation 再升级

- 任何试图把 assembly / review 层写成“实现已证实”的结论
- 任何试图把 Journal / Osiris 文档直接升格为 shipped content 私有实现图的判断

### 15. 哪些结论可以先写成当前最强解释

- 五段 actual units 已可装成同一条发布链
- 当前正确下一步是执行一致性审阅，而不是新增段落或重写 queue

### 16. 哪些内容不能过早写死

- 不要把首轮 review sheet 当成永久不变的最终包装方案
- 不要把“暂未触发 writeback”写成“所有证据边界都已彻底解决”

---

## 17. 当前默认维护态

当前默认不主动执行新的阶段 6 子单元：

> `维持阶段 6 冻结后的条件触发维护态`

理由：

- `阶段 6 冻结维护态稳定化` 已完成；高优先级计划文件、`review sheet`、`current_state.md` 与 `next_step.md` 现在都应把它视为既有成果，而不是继续中的当前块
- 五段 actual units、assembly / review 层、首轮局部 writeback，以及第十轮 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` traceback 修正都已闭合；截至 2026-04-26 的 `round32` 只提供最近一次维护确认
- `docs/01_methodology/stage6_freeze_maintenance_playbook.md` 已把默认维护动作压成固定顺序：先做 trigger 判定，再决定是否只停在 review-layer / 状态入口
- 在没有新 trigger 的前提下，继续人为制造 `round33 / round34` 不会产生新的研究增量，只会把维护记录链再次误抬成主动主线

当前默认完成标准不是“再做一轮”，而是：

1. `不新增新的 review round`
2. `review sheet` 继续作为唯一主动维护入口；`round32` 只保留为最近一次维护记录
3. 先按 `docs/01_methodology/stage6_freeze_maintenance_playbook.md` 执行四步 maintenance pass
4. 若仅发生口径同步需求，只同步状态 / 方法 / 导航文件，不回写五段 actual units

只有命中以下情况，才重新生成新的执行单元：

1. 五段 actual units 之一发生正文级改动
2. `entry / opening / camp / closing / final` 的 handoff 顺序发生变化
3. evidence lock 或 benchmark traceback 出现回退、缺失、错链
4. release package assembly map 被改动后需要重新校对
5. 项目负责人明确要求对发布链做新一轮一致性审阅

若未来确需重开：

1. 先读 `docs/00_project/stage6_release_package_assembly_review_sheet.md`
2. 再读 `docs/01_methodology/stage6_freeze_maintenance_playbook.md`
3. 再按需读 `.agent/execplan_stage6_release_package_assembly_review_round32.md`
4. 然后只为新 trigger 新增对应维护记录，不回头续写旧的 addendum 指针链

不要借“维护”之名自动续轮、回头重写 queue、重开阶段 5，或把 modding / Journal 文档误写成 shipped content 实锤。那会把已经闭合的阶段 6 再次打散。
