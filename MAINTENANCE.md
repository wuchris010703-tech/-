# 后期照片上传与自动更新方案

这个仓库当前部署在 GitHub Pages 上，网页本身是纯静态 HTML/CSS/JS。静态网页可以读取仓库里的照片和小卡片，但不能直接把访客上传的文件写回 GitHub，也不能长期运行图片识别和生成任务。

因此后期维护建议分成两层：

1. 网页继续保持静态，仍由 GitHub Pages 发布。
2. 新照片通过 GitHub Issue 表单上传，由 GitHub Actions 处理后自动提交回仓库。

## 已加入的 GitHub 自动维护流程

本次新增了三个维护入口：

- `.github/ISSUE_TEMPLATE/photo_upload.yml`：照片投稿表单。
- `.github/workflows/photo-upload.yml`：自动处理照片的 GitHub Action。
- `tools/process_photo_upload.py`：下载原照片和用户上传的小卡片、分类、更新 `script.js` 的处理脚本。
- `UPLOAD_PHOTOS.md`：给普通上传者看的详细操作流程。

使用流程：

1. 在 GitHub 仓库里确认 `Settings -> Actions -> General -> Workflow permissions` 允许 `Read and write permissions`。
2. 打开仓库的 `Issues`。
3. 点击 `New issue`。
4. 选择“照片自动更新”。
5. 在“原照片附件”里拖入多张 JPG/PNG 图片。
6. 在“卡通小卡片附件”里拖入已经生成好的小卡片，数量和顺序必须与原照片一致。
7. 分类可以选择“自动识别”，也可以指定同一批照片的类别。
8. 提交 issue 后，GitHub Action 会自动运行。
9. Action 成功后会提交新照片、新小卡片和更新后的 `script.js`。
10. GitHub Pages 会在仓库更新后重新发布网页。

## 当前自动化能做什么

脚本会自动完成：

- 从 issue 正文里分别读取“原照片附件”和“卡通小卡片附件”链接。
- 检查原照片和小卡片数量是否一致，并按出现顺序一一配对。
- 跳过已经处理过的原照片，避免重复追加。
- 把原图压缩保存到 `public/photos/<category>/photo-xxx.jpg`。
- 把用户上传的小卡片规范为 PNG，保存到 `public/art-cards/review-batch-20260521/accepted/photo-xxx-uploaded.png`。
- 把新照片追加到 `script.js` 的 `CONFIG.photos`。
- 把新卡片样式追加到 `CONFIG.sketches.assignments`。
- 对已有场景分类追加照片 ID，让页面刷新后能看到新内容。

## 关于“系统识别归类”

默认情况下，脚本会按以下顺序分类：

1. 如果 issue 表单指定了分类，优先使用指定分类。
2. 如果没有指定分类，脚本会根据照片说明、文件名和简单图像特征做保守分类。
3. 如果仍然无法判断，会放入 `moments`。

## 关于“回忆小卡片”

系统不再自动生成小卡片，也不需要配置 OpenAI Secret。用户需要自己提前生成或准备好卡通小卡片，并在 issue 表单里上传。

配对规则：

- 第 1 张原照片对应第 1 张小卡片。
- 第 2 张原照片对应第 2 张小卡片。
- 以此类推。

如果数量不一致，Action 会失败并留言说明，网页不会更新。

## 关于“网页直接上传”

如果目标是让普通访客在网页上直接点“上传照片”，并且不进入 GitHub Issue 页面，那么 GitHub Pages 不够用，需要额外后端。推荐结构是：

- 前端：当前网页增加上传入口。
- 存储：Cloudinary、Supabase Storage、S3/R2 等。
- 后端任务：Vercel Function、Cloudflare Worker、Supabase Edge Function 或独立服务器。
- 处理：视觉分类、卡通图生成、压缩、审核。
- 发布：后端通过 GitHub API 提交新文件，或直接让网页读取远程数据库/JSON。

当前仓库先采用 GitHub-native 方案，因为它改动小、成本低，并且保留 GitHub Pages 的静态部署方式。

## 分类 key

当前网页支持这些分类：

- `home`：居家日常
- `ski`：滑雪和雪地
- `hospital`：生病和陪伴
- `video`：视频里的见面
- `games`：娱乐时间
- `cooking`：美厨娘时间
- `outing`：一起出去玩
- `moments`：其他小瞬间

如果以后要新增分类，需要同步修改：

- `script.js` 里的 `CONFIG.sceneCategories`
- `tools/process_photo_upload.py` 里的 `CATEGORIES`
- `.github/ISSUE_TEMPLATE/photo_upload.yml` 里的分类选项
