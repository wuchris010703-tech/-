# 熊熊家回忆网页

这是一个原生 HTML + CSS + JavaScript 的纯静态回忆网页，不需要后端、框架或构建工具。

## 本地打开

1. 保持这些文件在同一个项目文件夹里：`index.html`、`style.css`、`script.js`、`public/`。
2. `index.html` 必须放在项目根目录，不要移动到 `public/` 里面。
3. 双击 `index.html`，或启动本地静态服务器后在浏览器里打开它。
4. 音乐不会自动播放，需要点击页面里的“播放歌曲”按钮。

## 替换照片

照片已经按场景整理在 `public/photos/` 下面：

- `home/`：居家日常
- `ski/`：滑雪和雪地
- `hospital/`：生病和陪伴
- `video/`：视频里的见面
- `games/`：娱乐时间
- `cooking/`：美厨娘时间
- `outing/`：一起出去玩
- `moments/`：其他小瞬间

如果要换照片，建议保持类似 `photo-001.jpg` 的英文文件名。换完以后，在 `script.js` 的 `CONFIG.photos` 里修改对应的 `file`、`caption` 和 `category`。

## 修改文字

所有主要文案都在 `script.js` 顶部的 `CONFIG` 区域：

- `siteTitle`：首页标题
- `subtitle`：首页副标题
- `photos`：照片路径、分类和配文
- `sceneCategories`：场景回忆区
- `galleryGroups`：旧的照片墙分类配置，当前自动滚动照片墙不再依赖它
- `loveLetter`：信的正文
- `letter.signature`：信的落款

修改保存后刷新页面即可。

## 音乐

把 mp3 文件放进 `public/music/`，然后在 `script.js` 的 `CONFIG.music.tracks` 里加入路径，例如：

```js
tracks: [
  "public/music/song-a.mp3",
  "public/music/song-b.mp3"
]
```

点击“播放歌曲”时，网页会从这个列表里随机播放一首。

## 手绘感小卡片

页面里的小卡片图片在 `public/art-cards/review-batch-20260521/accepted/`。文件名规则是：

- `photo-001-crayon.png`
- `photo-002-postcard.png`

网页会按照片编号和 `script.js` 里的 `CONFIG.sketches.assignments` 自动寻找对应的小卡片。当前小卡片区不再分类，会把所有生成的小卡片放在一条自动滚动轨道里展示。

## 后期上传和自动更新

这个项目现在仍然是 GitHub Pages 静态网页。静态网页不能直接接收访客上传并写回仓库，所以后期自动更新采用 GitHub Issue + GitHub Actions 的方式：

1. 用户在仓库 Issues 里选择“照片自动更新”表单。
2. 把多张照片拖进表单并提交。
3. GitHub Action 自动下载图片、归类，并调用图片模型生成卡通小卡片。
4. Action 把新照片、新小卡片和更新后的 `script.js` 提交回仓库。
5. GitHub Pages 自动重新发布网页。

给上传者看的详细步骤见 `UPLOAD_PHOTOS.md`。

详细维护说明见 `MAINTENANCE.md`。

## 部署到 GitHub Pages

1. 新建一个 GitHub 仓库，把本项目作为静态网页仓库上传。
2. 确认 `index.html` 位于仓库根目录。
3. 进入仓库 `Settings`。
4. 打开 `Pages`。
5. `Source` 选择 `Deploy from a branch`。
6. 分支选择 `main`，目录选择 `/root`。
7. 保存后等待 GitHub Pages 生成访问链接。

别人访问 GitHub Pages URL 即可打开完整网页，不需要下载照片、音乐或小卡片素材。

## HEIC 和中文文件名

浏览器对 HEIC 支持不稳定，建议先转换成 JPG 或 PNG。中文文件名通常可以打开，但为了 GitHub Pages 和不同浏览器更稳，建议使用英文或数字文件名。
