# Source Index

来源 ID 统一格式建议：`BG3-OFF-###`、`BG3-PLY-###`、`BMK-###`。状态值建议使用 `to read / reading / distilled / used`。

## Benchmark deconstruction projects

| Source ID | Title | Type | Priority tier | Status | Where used | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| BMK-001 | 游戏拆解项目对照清单（待补具体案例） | benchmark frame | B | to read | `docs/02_sources/benchmark_projects.md` | 用于建立“什么样的拆解结构值得借鉴”，而不是照抄风格。 |

## BG3 official sources

| Source ID | Title | Type | Priority tier | Status | Where used | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| BG3-OFF-001 | Baldur's Gate 3 official About page | official overview | A | distilled | `docs/02_sources/source_note_bg3_off_001_about_page.md`, `docs/03_analysis/00_core_thesis.md`, `docs/03_analysis/01_macro_structure.md` | 已从集合式占位条目压实为具体官网来源；适合支撑官方定位、区域跨度与高层卖点，不单独承担具体案例结论。 |
| BG3-OFF-002 | Patch 7 Now Live! | official update / patch notes | A | distilled | `.agent/execplan_quests_and_choices.md`, `docs/02_sources/source_note_bg3_off_002_patch_7.md`, `docs/03_analysis/02_quests_and_choices.md`, `docs/03_analysis/03_party_and_camp.md`, `docs/03_analysis/05_implementation_validation.md` | 高价值官方来源；直接暴露任务流、营地夜晚、角色反应、击倒 Minthara 后续反应等修正。 |
| BG3-OFF-003 | Official Xbox Podcast: Baldur’s Gate 3 comes to Xbox and our holiday gift ideas | developer explanation | A | distilled | `.agent/execplan_quests_and_choices.md`, `docs/02_sources/source_note_bg3_off_003_xbox_podcast.md`, `docs/02_sources/case_note_minthara_knockout_path.md`, `docs/03_analysis/00_core_thesis.md`, `docs/03_analysis/01_macro_structure.md`, `docs/03_analysis/02_quests_and_choices.md`, `docs/03_analysis/04_combat_and_environment.md`, `docs/03_analysis/05_implementation_validation.md` | Adam Smith 直接解释多入口设计、非常规解法与上线后补量对话 / 结局覆盖。 |
| BG3-OFF-004 | Hotfix #20 Now Live! | official hotfix | A | distilled | `.agent/execplan_quests_and_choices.md`, `docs/02_sources/source_note_bg3_off_004_hotfix_20.md`, `docs/02_sources/case_note_minthara_knockout_path.md`, `docs/03_analysis/02_quests_and_choices.md`, `docs/03_analysis/05_implementation_validation.md` | 对 Minthara 击倒、长休、跨区域状态异常进行了明确修复，适合做状态回流证据入口。 |
| BG3-OFF-005 | Community Update #28 Closed Beta | official community update | A | distilled | `.agent/execplan_quests_and_choices.md`, `.agent/quests_and_choices_writeback_prep.md`, `docs/02_sources/source_note_bg3_off_005_cu28_dark_urge_bard.md`, `docs/02_sources/case_note_dark_urge_bard_event.md`, `docs/03_analysis/02_quests_and_choices.md`, `docs/03_analysis/03_party_and_camp.md`, `docs/03_analysis/05_implementation_validation.md` | 目前与 Dark Urge bard 事件最直接的官方来源；确认 bard 会在营地暂时作为可控制角色加入。 |
| BG3-OFF-006 | Community Update 14: Forging the Arcane | official community update | A | distilled | `.agent/execplan_quests_and_choices.md`, `docs/02_sources/source_note_bg3_off_006_cu14_grymforge.md`, `docs/02_sources/case_note_grymforge_environment_resolution.md`, `docs/03_analysis/01_macro_structure.md`, `docs/03_analysis/04_combat_and_environment.md`, `docs/03_analysis/02_quests_and_choices.md` | 以高层方式确认 Grymforge 兼具任务、选择与复杂战斗遭遇；适合作为区域结构与复杂遭遇的官方框架来源。 |

## BG3 player/community analysis

| Source ID | Title | Type | Priority tier | Status | Where used | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| BG3-PLY-001 | 高质量玩家长文与视频拆解集合（待筛选） | player analysis | B | to read | `docs/02_sources/bg3_player_analysis.md` | 先筛“有案例、有结构、有证据意识”的材料；在压实前不应被顶层正文当事实来源。 |
| BG3-PLY-002 | Reddit: Saving the bard as the Dark Urge | community case | B | reading | `.agent/execplan_quests_and_choices.md`, `docs/02_sources/case_note_dark_urge_bard_event.md`, `docs/03_analysis/02_quests_and_choices.md`, `docs/03_analysis/05_implementation_validation.md` | 可用作“长休触发 -> 角色替换 -> 后续可见差异”的案例线索；只能描述玩家案例，不可直接上升为全局事实。 |
| BG3-PLY-003 | Reddit: Minthara knocked out in the audience chamber of Moonrise | community case | B | reading | `.agent/execplan_quests_and_choices.md`, `docs/02_sources/case_note_minthara_knockout_path.md`, `docs/03_analysis/02_quests_and_choices.md`, `docs/03_analysis/05_implementation_validation.md` | 适合与 `BG3-OFF-004` 对照，区分稳定支持路径与 bug / 边缘状态；主要作为问题线索。 |
| BG3-PLY-004 | Reddit: We failed the "Owlbear from the top rope" strat. | community case | B | distilled | `.agent/execplan_quests_and_choices.md`, `docs/02_sources/source_note_bg3_ply_004_grym_environment_case.md`, `docs/02_sources/case_note_grymforge_environment_resolution.md`, `docs/03_analysis/02_quests_and_choices.md`, `docs/03_analysis/04_combat_and_environment.md` | 用于锁定 Grymforge / Grym 作为“战斗 / 环境绕解”补强方向；只作为玩家案例入口，不直接当系统事实。 |
