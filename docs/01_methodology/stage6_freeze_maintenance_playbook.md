# Stage 6 Freeze Maintenance Playbook

## 作用

本文件只服务阶段 6 已闭合之后的冻结维护态。

它回答三件事：

1. 未来会话若碰到 stage-6 维护，应先读什么。
2. 如何判断这次只是 `no-trigger` 维护，还是已经命中新 trigger。
3. 命中与未命中 trigger 时，分别允许改哪些文件，禁止改哪些文件。

它不是新的阶段计划，也不替代 `stage6_release_package_assembly_review_sheet.md`。`review sheet` 继续负责 assembly map、review checklist 与 writeback trigger；本文件只把这些规则压成可执行动作顺序。

## 适用范围

- 适用于：阶段 6 已闭合之后的默认维护、复核、状态同步。
- 不适用于：重开阶段 5、补新的区域包、重写任何一段 actual units、或为“再谨慎看一轮”而新开 round。

## 默认阅读顺序

如果没有新的明确 trigger，按下面顺序恢复上下文：

1. `README.md`
2. `docs/00_project/current_state.md`
3. `docs/00_project/next_step.md`
4. `docs/00_project/stage6_release_package_assembly_review_sheet.md`
5. `docs/03_analysis/05_implementation_validation.md`

只有在 `review sheet` 已判定命中新 trigger 时，才补读：

6. `.agent/execplan_stage6_release_package_assembly_review_round32.md`

## 四步 Maintenance Pass

### Pass 1：Trigger 判定

先只回答一个问题：这次有没有命中 `ASSEMBLY-TRIGGER-001`？

命中条件只有 5 类：

1. 五段 actual units 之一发生正文级改动。
2. `entry / opening / camp / closing / final` 的 handoff 顺序发生变化。
3. evidence lock 或 benchmark traceback 出现回退、缺失、错链。
4. release package assembly map 被改动后需要重新校对。
5. 项目负责人明确要求对发布链做新一轮一致性审阅。

如果以上 5 类都没有命中，直接把本轮归类为 `no-trigger maintenance`。

### Pass 2：Review-Layer 一致性检查

在 `no-trigger maintenance` 下，只检查 review-layer 与状态入口是否仍保持同一口径：

- `review sheet` 仍是默认主动维护入口。
- `round32` 仍只被写成最近一次维护记录。
- 没有任何文件重新把 `round33` 写成默认下一步。
- 没有任何文件重新把 supporting bundle、handoff 或 modding / Journal 文档误升为新主链或实现实锤。

### Pass 3：Evidence-Lock 检查

重点只看两类仍会影响后续判断的维护结论：

1. `FINAL-ASSET-001` 必须继续保留独立 `入口页` 行。
2. `ENTRY-TRACE-001` 必须继续保留 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback。

若这两类结论都保持有效，则本轮不得以“保险起见”为理由回写 actual units。

### Pass 4：允许动作判定

#### 若判定为 `no-trigger maintenance`

允许：

- 更新 `review sheet` 的维护规则摘要
- 更新 `05_implementation_validation.md` 中的 review-layer 结论
- 更新 `current_state.md`、`next_step.md`、`decision_log.md`、`repo_map.md`
- 新增或更新维护态说明文件

禁止：

- 新开 `round33`
- 回写任何五段 actual units
- 回跳阶段 5
- 借维护之名重写 queue、section skeleton 或 release unit

#### 若判定为 `trigger-hit maintenance`

允许：

- 先更新 `review sheet`
- 再只回写被 trigger 直接命中的 actual-unit 承载文件
- 同步 `05_implementation_validation.md`、`current_state.md`、`next_step.md`、`decision_log.md`
- 视需要补新的 `round*.md` 维护记录

禁止：

- 把局部 trigger 扩写成新的 project-level 主线
- 因为命中一个 trigger 就顺手重写其它未命中的段落

## 当前默认结论

- 阶段 6 已闭合。
- 默认动作是维持冻结后的条件触发维护态。
- `review sheet` 是唯一主动维护入口。
- `round32` 是最近一次维护记录，不是默认主任务。
- 在没有新 trigger 的前提下，正确动作是维持 review-layer / 状态入口清晰，而不是新增 round 文件。

## 常见误操作

- 把“再谨慎检查一轮”当成新 trigger。
- 因为最新 round 文件名还能继续递增，就自动新开 `round33`。
- 绕过 `review sheet` 直接回头重写五段 actual units。
- 把 `BG3-OFF-011` 到 `BG3-OFF-014` 越级写成 shipped content 私有实现实锤。
- 借 stage-6 维护之名回跳阶段 5，重新追第二条对称 spine。

## 输出要求

一次合格的 stage-6 冻结维护 run，至少应能给出：

1. 本轮是否命中新 trigger。
2. 若未命中，明确说明没有新增 review round、没有回写 actual units。
3. 若命中，明确说明命中的是哪一类 trigger、只回写了哪些直接相关文件。
4. 已同步哪些状态入口文件。
5. `python scripts/check_repo.py` 与 `make check` 是否通过。

## 与其它文件的分工

- `docs/00_project/stage6_release_package_assembly_review_sheet.md`
  负责当前 assembly map、review checklist、writeback trigger 与维护规则摘要。
- `docs/03_analysis/05_implementation_validation.md`
  负责记录阶段 6 维护结论为什么成立、哪些 evidence lock 仍有效。
- `docs/00_project/current_state.md`
  负责告诉未来会话“当前默认动作是什么”。
- `docs/00_project/next_step.md`
  负责告诉未来会话“这次应不应该真的重开 stage-6 review”。
