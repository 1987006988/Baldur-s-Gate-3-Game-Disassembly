# Repo Rectification ExecPlan

## Goal

在不扩目录、不继续扩写局部新案例的前提下，先修复仓库的上位解释层、来源压实层、一致性层与基础检查层，使 `00_core_thesis.md` 与 `01_macro_structure.md` 能重新承担总入口作用。

## Why it matters

当前仓库最明显的问题不是缺少局部案例，而是局部案例已经跑在总论点和宏观结构前面。若不先纠偏，后续会继续把分析写成局部精彩片段堆叠，而不是可恢复、可验证、可持续迭代的研究仓库。

## Repository context

- `docs/03_analysis/02_quests_and_choices.md` 与 `docs/03_analysis/04_combat_and_environment.md` 已有首轮可引用正文。
- `docs/03_analysis/00_core_thesis.md` 与 `docs/03_analysis/01_macro_structure.md` 曾停留在骨架层，并直接引用集合式占位来源。
- `docs/00_project/source_index.md` 中曾有 `BG3-OFF-001`、`BG3-PLY-001`、`BMK-001` 这类集合式条目直接影响顶层正文可信度。
- `docs/02_sources/case_note_grymforge_environment_resolution.md` 曾与当前正文存在模块归属口径偏差。
- 原始 `scripts/check_repo.py` 只做存在性与非空检查，已落后于仓库当前复杂度。

## Inputs and evidence

- 当前状态入口：`README.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 项目主路线图：`docs/00_project/master_roadmap.md`
- 现有分析正文：`docs/03_analysis/00_core_thesis.md` 至 `docs/03_analysis/05_implementation_validation.md`
- 来源索引：`docs/00_project/source_index.md`
- 已可复用的官方来源：
  - `BG3-OFF-003` Official Xbox Podcast
  - `BG3-OFF-006` Community Update 14: Forging the Arcane
- 本次压实的关键来源：
  - `BG3-OFF-001` 从集合式占位改为具体官网 About 页面

## Milestones

1. `M1：补强模块 3（总论点与宏观结构）`
   - 目标文件：`docs/03_analysis/00_core_thesis.md`、`docs/03_analysis/01_macro_structure.md`
   - 要求：形成首轮可引用版本，明确区分事实、推断、待验证问题，并移除对集合式占位来源的直接依赖。
2. `M2：压实占位来源`
   - 只处理会影响模块 3 与实现验证层可信度的最小必要部分。
   - 能拆实就拆实；不能拆实就避免顶层正文继续把集合式来源当证据。
3. `M3：一致性清扫`
   - 只修正已确认问题：Grymforge case 归属、README 中 `docs/02_sources/` 描述、`repo_map.md` 的最小同步。
4. `M4：升级检查脚本`
   - 增加 Source ID、Where used、状态文件联动与集合式来源误用检查。

## Validation

- 每完成一个里程碑，都运行 `python scripts/check_repo.py`
- `M1` 完成时：
  - `00_core_thesis.md` 与 `01_macro_structure.md` 各自至少有 2 条非占位来源
  - 两文件都显式区分 `事实 / 推断 / 待验证问题`
  - 顶层正文不再把 `to read` 的集合式来源当实际证据
- `M2` 完成时：
  - 顶层正文与实现验证层不再直接引用集合式占位来源
- `M3` 完成时：
  - 已确认的口径冲突被修正，且不引入新的目录与流程
- `M4` 完成时：
  - `check_repo.py` 能对 Source ID、Where used、状态文件联动作出最小必要校验

## Progress

- 2026-04-23：创建整改型 ExecPlan，正式把当前主线切换为“仓库整改”，用于临时纠偏而非永久替换项目主路线图。
- 2026-04-23：完成 `M1`，补强 `00_core_thesis.md` 与 `01_macro_structure.md`，并将 `BG3-OFF-001` 从集合式占位条目压实为具体官网来源。
- 2026-04-23：完成 `M2` 的最小必要部分，清除 `05_implementation_validation.md` 中对集合式玩家来源 `BG3-PLY-001` 的直接依赖，改用具体社区案例 ID 作为案例线索。
- 2026-04-23：完成 `M3`，统一 Grymforge case 的模块归属口径，并同步修正 README 与 `repo_map.md` 对 `docs/02_sources/` 的描述。
- 2026-04-23：完成 `M4`，升级 `scripts/check_repo.py`，把来源与状态联动规则沉入自动检查。

## Decision Log

- 2026-04-23：决定先补强模块 3，再处理占位来源与一致性问题，避免继续让局部案例先于总论点扩写。
- 2026-04-23：决定在整改完成后立即切回 `master_roadmap.md` 定义的主路线，而不是继续让整改占用主线。

## Surprises & Discoveries

- 当前真正拖慢仓库可信度的，不是案例数量不足，而是上位解释层过薄、占位来源被直接上升为正文证据。
- 当来源索引、状态文件和检查器三者对齐后，仓库的“可接力性”提升比单纯补更多案例更明显。

## Outcomes & Retrospective

- 整改已完成四个里程碑，仓库重新具备“先读总论点与宏观结构，再进入局部案例”的稳定入口。
- 集合式来源仍可保留在索引层作为待筛来源池，但不再被顶层正文或实现验证层直接当作证据使用。
- 下一步已恢复到项目主路线：继续执行 `.agent/execplan_party_and_camp.md` 的 `Milestone 2`。
