# Baldur's Gate 3 Deconstruction Repository

这是一个面向长期维护的《博德之门3》研究仓库。目标不是收集零散笔记，而是持续回答一个核心问题：

> 《博德之门3》如何把桌面规则、电影化叙事和系统性玩家能动性缝合成一个高反应性的 CRPG？

仓库内文档而不是聊天记录，才是本项目的长期记忆主载体。未来任何一次 Codex 会话，都应优先读取仓库文件来恢复上下文。

## 项目目标

- 用三层拆解方法解释 BG3 为什么让玩家感到自由、沉浸、被反馈。
- 把体验层观察、规则系统分析和实现验证证据串成可追溯研究链。
- 为后续持续扩展模块、补充来源、修正结论保留清晰的状态和决策历史。
- 把“研究推进顺序”和“展示给人看的顺序”明确拆开，避免再次出现“为什么突然拆营地”的观感。
- 让未来 Codex 可以直接按仓库文件稳定执行，而不是依赖临时口头说明。

## 非目标

- 不做按剧情顺序的完整复述。
- 不做全量 wiki 式资料搬运。
- 不把未经证实的社区印象直接写成事实。
- 不依赖外部数据库、Notion、向量库或额外服务。
- 不把某个局部模块的推进误当成整个项目的总逻辑。

## 三层拆解方法

1. 玩家体验层：玩家在哪里感到自由、沉浸、被系统回应，具体看到了什么反馈。
2. 规则系统层：任务、选择、成长、战斗、探索、资源循环如何耦合并产生前述体验。
3. 实现验证层：尽量用官方公开资料、开发者说明、可观察 UI、术语、数据组织和工具链线索，验证这些体验为何成立。

这三层互相校正：体验层防止研究失去玩家视角，系统层防止只剩感受描述，实现层防止分析滑成纯猜测。

## 现在采用的双轨总逻辑

### 展示顺序

项目对外展示时，优先按“玩家如何感知到 BG3 的反应性链条”展开：

1. 总命题与高反应性到底在解释什么
2. 宏观结构与区域包如何制造多入口推进
3. 战斗 / 环境如何在局部场景里制造“我能这样试”的能动性
4. 任务 / Journal / 选择回流如何把局部行动写回后续状态
5. 同伴 / 营地 / 长休如何把分散状态折叠成可感知反馈
6. Act 收束与终局如何给前面状态施加压缩与结算压力
7. 实现验证层如何检验上述判断

### 研究顺序

仓库内部推进时，不按展示顺序逐章写长文，而按“区域包 / Act 包 + 横向主干回写”推进：

1. 先冻结总逻辑与方法边界
2. 再按区域包推进：`Nautiloid` → `Act 1 地表` → `Grove / Goblin` → `Underdark` → `Grymforge` → `Mountain Pass / Creche` → `Act 2` → `Act 3`
3. 每完成一个区域包，同时回写：
   - `01_macro_structure.md`
   - `02_quests_and_choices.md`
   - `04_combat_and_environment.md`
   - 必要时回写 `03_party_and_camp.md`
   - 把需要降级的部分放进 `05_implementation_validation.md`

研究顺序和展示顺序不同，是因为 BG3 的证据天然分散在区域、案例和后续反馈里；先按区域包收证据，才能稳定地写出展示链条。

## 当前展示入口（阶段 6）

阶段 5 已经把三条横向主干统一压成“`1` 条正式 spine + `1` 次 ceiling / supporting-bundle / handoff 收口”的同一种出口结构，因此当前对外入口不该再把 `Quest`、`Combat`、`Camp` 当成三份并列工程，而应把它们放回同一条反应性链条。

如果只想先按当前最稳的展示顺序读，建议按这个顺序进入：

1. `README.md`
2. `docs/00_project/deconstruction_display_overview.md`
3. `docs/03_analysis/00_core_thesis.md`
4. `docs/03_analysis/01_macro_structure.md`
5. `docs/03_analysis/04_combat_and_environment.md`
6. `docs/03_analysis/02_quests_and_choices.md`
7. `docs/03_analysis/03_party_and_camp.md`
8. `docs/03_analysis/05_implementation_validation.md`

这条顺序的含义是：

- 先用总论点与宏观结构回答“BG3 到底在解释什么、问题从哪里展开”。
- 再用战斗 / 环境回答“玩家最早在哪一层感到自己能这样试”。
- 然后才进入任务回流与营地折叠，解释“系统后来如何记住并读回这些尝试”。
- 最后用实现验证层说明哪些判断已经够稳，哪些仍只是当前最强解释。

`Act 收束与终局压力` 当前不作为单独入口文件，而是以 `01_macro_structure.md` 为骨架，与 `02_quests_and_choices.md`、`03_party_and_camp.md` 联读。

## 为什么不能按剧情复述

BG3 的优势不是“剧情很多”，而是“行动方式、状态记录、延迟反馈和后续承接”之间形成了链条。按剧情复述写，容易出现三种问题：

- 把区域推进写成事件流水账，看不出系统结构。
- 把任务、战斗、营地、同伴拆成平行栏目，看不出它们互相回流。
- 让营地、长休这类反馈节点看起来像突然插入的附录，而不是前序状态的折返点。

所以 Act / 区域会保留，但只作为**证据带**和**执行单元**，不作为“剧情目录”。

## 仓库目录

- `AGENTS.md`：全局协作规则，只写协作约束，不承载项目知识。
- `.agent/PLANS.md`：ExecPlan 使用规范，适合大型研究任务。
- `.agents/skills/bg3-research/SKILL.md`：高频研究动作的固定流程。
- `.codex/config.toml`：项目级保守默认配置。
- `docs/00_project/`：项目入口、状态、决策、路线图、展示总览、执行计划、来源总索引。
- `docs/01_methodology/`：三层拆解方法、证据规则、模块模板、展示形式原则。
- `docs/02_sources/`：来源类型导航页、来源笔记与案例工作文件；用于把索引条目压实成可追溯材料，而不只是堆链接。
- `docs/03_analysis/`：核心分析正文。
- `templates/`：来源笔记和案例拆解模板。
- `scripts/check_repo.py`：轻量仓库检查。
- `Makefile`：最小命令入口。

## 推荐工作流

新会话进入仓库后，建议按这个顺序阅读：

1. `README.md`
2. `docs/00_project/deconstruction_display_overview.md`
3. `docs/00_project/deconstruction_master_execution_plan.md`
4. `docs/00_project/deconstruction_granular_codex_plan.md`
5. `docs/00_project/current_state.md`
6. `docs/00_project/next_step.md`
7. `docs/00_project/source_index.md`
8. `docs/00_project/repo_map.md`
9. 本轮相关的分析模块、来源笔记与 ExecPlan

如果任务较复杂或跨度较大，先建立或更新 ExecPlan，再动正文。

## 如何新增资料

1. 先确认来源类型和优先级。
2. 在 `docs/00_project/source_index.md` 登记新的 Source ID。
3. 按 `templates/source_note.md` 生成来源笔记或等价结构化摘录。
4. 把提炼出的事实、推断、待验证问题写入对应分析模块。
5. 同步更新 `current_state.md` 与 `next_step.md`。

## 如何新增模块或区域包

1. 先检查 `docs/03_analysis/` 是否已有相近模块。
2. 如果是大型模块或跨区域任务，先读 `deconstruction_master_execution_plan.md` 与 `deconstruction_granular_codex_plan.md`。
3. 依据 `docs/01_methodology/module_template.md` 起草。
4. 每个结论都要能映射到 `source_index.md` 中的来源 ID。
5. 若结论改变既有判断，追加写入 `decision_log.md`。

## 如何更新状态

- 做完任何有意义的研究动作后，至少同步：
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
- 如果引入新来源，更新 `docs/00_project/source_index.md`
- 如果改了方法、结论或结构，更新 `docs/00_project/decision_log.md`

## 最小命令

```bash
make check
```

如果本机没有 `make`，可直接运行：

```bash
python scripts/check_repo.py
```

`check` 只做轻量验证：关键文件是否存在、是否为空、分析文档是否带有来源与待验证问题标记、来源索引中的 `Where used` 路径是否存在，以及当前状态文件是否和唯一主任务基本一致。
