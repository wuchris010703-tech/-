# 回忆小卡片生成状态

记录时间：2026-05-21

本文件用于接续“回忆小卡片”的图片生成工作。当前目标是：对 `public/photos/` 里的每一张原始照片生成一张对应小卡片，随机使用两个技能之一，并把生成图保存到新的审核文件夹中，确认后再接入网页。

## 当前文件夹

- 审核总目录：`public/art-cards/review-batch-20260521/`
- 已通过目录：`public/art-cards/review-batch-20260521/accepted/`
- 问题隔离目录：`public/art-cards/review-batch-20260521/rejected/`
- 网页当前读取目录：`public/art-cards/review-batch-20260521/accepted/`
- 历史生成计划：`public/art-cards/generated-random/generation-plan.json`

## 已完成并暂时可用

以下 12 张已经复制到 `accepted/`：

| 编号 | 文件 | 风格 |
| --- | --- | --- |
| 001 | `photo-001-postcard.png` | `travel-doodle-postcard` |
| 002 | `photo-002-postcard.png` | `travel-doodle-postcard` |
| 003 | `photo-003-crayon.png` | `photo-crayon-style-transfer` |
| 004 | `photo-004-crayon.png` | `photo-crayon-style-transfer` |
| 005 | `photo-005-crayon.png` | `photo-crayon-style-transfer` |
| 006 | `photo-006-crayon.png` | `photo-crayon-style-transfer` |
| 007 | `photo-007-crayon.png` | `photo-crayon-style-transfer` |
| 008 | `photo-008-postcard.png` | `travel-doodle-postcard` |
| 009 | `photo-009-crayon.png` | `photo-crayon-style-transfer` |
| 010 | `photo-010-postcard.png` | `travel-doodle-postcard` |
| 011 | `photo-011-postcard.png` | `travel-doodle-postcard` |
| 012 | `photo-012-postcard.png` | `travel-doodle-postcard` |

## 已隔离的问题图

`photo-013` 生成时出现了模型没有跟住输入图的问题。最后两张输出已经复制到：

- `public/art-cards/review-batch-20260521/rejected/photo-013-wrong-1.png`
- `public/art-cards/review-batch-20260521/rejected/photo-013-wrong-2.png`

这两张不要接入网页，也不要当作 `photo-013` 的最终结果。

## 出现的问题

问题发生在 `photo-013`，源图是：

`public/photos/video/photo-013.png`

原图是一张视频通话截图，但模型输出跑偏，没有稳定保留原图构图和人物。因此后续生成时不要只依赖“最近显示的图片”这种模糊描述，应该在提示词中明确：

- 使用当前显示的图片作为唯一编辑目标
- 保持原始截图构图、横向比例、主画面人物、右上角视频通话小窗
- 不要发明新场景
- 不要把别的参考图当成目标图

如果再次生成仍跑偏，先保存到 `rejected/`，不要复制到 `accepted/`。

## 后续继续生成规则

1. 从 `photo-013` 开始继续，不要重做 `photo-001` 到 `photo-012`，除非明确要替换。
2. 每张原图只生成一张小卡片。
3. 两个技能按 `generation-plan.json` 和 `script.js` 里的分配使用：
   - `photo-crayon-style-transfer`
   - `travel-doodle-postcard`
4. 每生成一张，先保存到：
   `public/art-cards/review-batch-20260521/accepted/`
5. 确认图片和源图对应后，保留在：
   `public/art-cards/review-batch-20260521/accepted/`
6. 文件名必须保持：
   `photo-编号-风格.png`
7. 不要覆盖原始照片。
8. 不要把明显跑偏的图片放进 `accepted/`。

## 剩余生成清单

| 编号 | 源图 | 应生成文件 | 技能 |
| --- | --- | --- | --- |
| 013 | `public/photos/video/photo-013.png` | `photo-013-crayon.png` | `photo-crayon-style-transfer` |
| 014 | `public/photos/hospital/photo-014.jpg` | `photo-014-crayon.png` | `photo-crayon-style-transfer` |
| 015 | `public/photos/outing/photo-015.jpg` | `photo-015-postcard.png` | `travel-doodle-postcard` |
| 016 | `public/photos/home/photo-016.jpg` | `photo-016-crayon.png` | `photo-crayon-style-transfer` |
| 017 | `public/photos/outing/photo-017.jpg` | `photo-017-crayon.png` | `photo-crayon-style-transfer` |
| 018 | `public/photos/home/photo-018.jpg` | `photo-018-crayon.png` | `photo-crayon-style-transfer` |
| 019 | `public/photos/games/photo-019.jpg` | `photo-019-postcard.png` | `travel-doodle-postcard` |
| 020 | `public/photos/home/photo-020.jpg` | `photo-020-postcard.png` | `travel-doodle-postcard` |
| 021 | `public/photos/games/photo-021.jpg` | `photo-021-postcard.png` | `travel-doodle-postcard` |
| 022 | `public/photos/video/photo-022.png` | `photo-022-postcard.png` | `travel-doodle-postcard` |
| 023 | `public/photos/home/photo-023.jpg` | `photo-023-crayon.png` | `photo-crayon-style-transfer` |
| 024 | `public/photos/home/photo-024.jpg` | `photo-024-postcard.png` | `travel-doodle-postcard` |
| 025 | `public/photos/outing/photo-025.jpg` | `photo-025-crayon.png` | `photo-crayon-style-transfer` |
| 026 | `public/photos/games/photo-026.jpg` | `photo-026-crayon.png` | `photo-crayon-style-transfer` |
| 027 | `public/photos/home/photo-027.jpg` | `photo-027-crayon.png` | `photo-crayon-style-transfer` |
| 028 | `public/photos/outing/photo-028.jpg` | `photo-028-postcard.png` | `travel-doodle-postcard` |
| 029 | `public/photos/ski/photo-029.jpg` | `photo-029-crayon.png` | `photo-crayon-style-transfer` |
| 030 | `public/photos/video/photo-030.png` | `photo-030-crayon.png` | `photo-crayon-style-transfer` |
| 031 | `public/photos/video/photo-031.png` | `photo-031-postcard.png` | `travel-doodle-postcard` |
| 032 | `public/photos/outing/photo-032.jpg` | `photo-032-crayon.png` | `photo-crayon-style-transfer` |
| 033 | `public/photos/ski/photo-033.jpg` | `photo-033-crayon.png` | `photo-crayon-style-transfer` |
| 034 | `public/photos/outing/photo-034.jpg` | `photo-034-postcard.png` | `travel-doodle-postcard` |
| 035 | `public/photos/moments/photo-035.jpg` | `photo-035-postcard.png` | `travel-doodle-postcard` |
| 036 | `public/photos/outing/photo-036.jpg` | `photo-036-crayon.png` | `photo-crayon-style-transfer` |
| 037 | `public/photos/cooking/photo-037.jpg` | `photo-037-postcard.png` | `travel-doodle-postcard` |
| 038 | `public/photos/ski/photo-038.jpg` | `photo-038-postcard.png` | `travel-doodle-postcard` |
| 039 | `public/photos/ski/photo-039.jpg` | `photo-039-postcard.png` | `travel-doodle-postcard` |
| 040 | `public/photos/ski/photo-040.jpg` | `photo-040-postcard.png` | `travel-doodle-postcard` |

## 建议的继续流程

对每张图执行：

1. 用 `view_image` 打开对应源图。
2. 用对应技能生成图片。
3. 生成后先复制到 `review-batch-20260521/accepted/`。
4. 快速查看结果是否和源图对应。
5. 如果对应，保留在 `accepted/`。
6. 如果不对应，复制到 `rejected/`，并在本文件追加备注。

图片生成工具可能会把结果先保存到工具自己的临时输出目录。最终接入网页时，需要把成品复制到项目内的 `public/art-cards/review-batch-20260521/accepted/`，不能只留在临时目录里。
