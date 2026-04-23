# Current State

## 当前阶段

仓库整改已完成 `M1`、`M2`、`M3`、`M4`，当前回到正常研究推进。当前唯一主任务重新切回 `party_and_camp` 的来源筛选阶段，用已修复的总论点、来源索引与检查机制继续推进模块 5。

## 已完成模块

- 仓库结构与协作规则
- 三层拆解方法与证据规则
- 展示形式方法文件 `presentation_forms.md`
- 来源索引骨架与初始来源分组
- 核心分析模块初始骨架
- 轻量检查脚本升级为来源 / 状态联动检查器
- 项目级主路线图 `master_roadmap.md`
- `quests_and_choices` 首轮 ExecPlan 与正文回写
- `combat_and_environment` 首轮 Grymforge / Grym 回写
- `party_and_camp` 第二份 ExecPlan 与边界锁定
- 整改型 ExecPlan `.agent/execplan_repo_rectification.md`
- `00_core_thesis.md` 首轮整改补强：已形成当前最强解释版本，并移除对集合式占位来源的直接依赖
- `01_macro_structure.md` 首轮整改补强：已补入 Grymforge 作为结构性支撑点，并移除对集合式占位来源的直接依赖
- `BG3-OFF-001` 已从集合式占位条目压实为具体官网来源，并补出来源笔记
- `05_implementation_validation.md` 已完成整改 `M2` 的最小必要清理，不再直接引用集合式玩家来源占位条目
- Grymforge case 的模块归属口径已统一：主归 `04_combat_and_environment`，次级回流到 `02_quests_and_choices`
- README 与 `repo_map.md` 已完成与当前 `docs/02_sources/` 真实用途的最小同步
- `scripts/check_repo.py` 已补上 Source ID、Where used、状态文件联动与集合式来源误用检查

## 进行中模块

- 模块 5：同伴、营地与长休循环，当前回到 `execplan_party_and_camp` 的 `Milestone 2`
- 模块 7：实现验证层，后续仍可继续补强方法化检查与验证清单

## 阻塞点

- 暂无硬阻塞。
- 当前主要风险不是仓库结构，而是恢复正常研究后再次滑回“局部案例先于上位解释层”的推进习惯；后续应继续用状态文件与检查器压住这个风险。

## 最近一次重要变更

- 2026-04-23：完成整改 `M4`，升级 `scripts/check_repo.py`，补上 Source ID、Where used、状态文件联动与集合式来源误用检查。
- 2026-04-23：完成整改 `M3`，统一 Grymforge case 的模块归属口径，并同步修正 README 与 `repo_map.md` 中对 `docs/02_sources/` 的描述。
- 2026-04-23：完成整改 `M2` 的最小必要部分，清除 `05_implementation_validation.md` 中对 `BG3-PLY-001` 的直接依赖，并改用具体社区案例 ID 作为案例线索。
- 2026-04-23：完成整改 `M1`，将 `docs/03_analysis/00_core_thesis.md` 与 `docs/03_analysis/01_macro_structure.md` 从骨架稿补到首轮可引用版本。

## 接下来 1~3 个最优先动作

1. 按 `.agent/execplan_party_and_camp.md` 执行 `Milestone 2`，筛出首批 3 到 5 条与营地 / 长休反馈直接相关的高价值来源。
2. 判断这些来源中哪些可作为事实锚点，哪些只能作为案例线索，并同步 `source_index.md`。
3. 在来源筛选稳定后，进入 `Milestone 3`，为营地模块锁定 1 条强案例方向和 1 条候补案例方向。
