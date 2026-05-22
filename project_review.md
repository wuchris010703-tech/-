# Project Review: 熊熊家回忆网页

本文件是给下一位工程师或未来维护者看的项目架构说明。目标是让项目从当前本机目录迁移到 Git/GitHub Pages 后，仍然可以在不同电脑、浏览器和移动端打开，而不依赖任何本地绝对路径。

## 1. 项目定位

这是一个纯静态纪念网页，技术栈只有：

- `HTML`: 页面骨架，入口文件是 `index.html`
- `CSS`: 页面视觉、响应式布局、动画，入口文件是 `style.css`
- `JavaScript`: 数据配置、动态渲染、照片弹窗、音乐播放，入口文件是 `script.js`
- `public/`: 所有运行时资源，包括照片、音乐、回忆小卡片

没有后端，没有构建工具，没有 npm 依赖，没有框架。只要保留相对目录结构，网页可以通过两种方式打开：

- 本地双击 `index.html`
- 部署到任意静态文件服务，例如 GitHub Pages、Netlify、Vercel static hosting、Nginx、Apache

当前代码中运行时引用的资源路径都是相对路径，例如 `public/photos/...`，不是本机盘符路径或本地文件 URL。因此上传到 Git 后，只要文件结构不变，网页应当可以跨设备打开。

## 2. 当前目录快照

当前项目根目录文件统计：

- 总文件数：188
- 总大小：约 508 MB
- 主要文件类型：102 个 `.png`，75 个 `.jpg`，2 个 `.mp3`，2 个 `.json`，2 个 `.md`，1 个 `.html`，1 个 `.css`，1 个 `.js`，1 个 `.zip`
- 最大单文件：`jayee照片(1).zip`，约 70.43 MB

GitHub 普通仓库的单文件硬限制通常是 100 MB。当前最大文件低于该限制，但整个仓库体积偏大，首次上传、克隆、GitHub Pages 构建和移动网络访问都会比较重。

## 3. 根目录文件说明

| 文件 | 是否运行时必需 | 作用 |
|---|---:|---|
| `index.html` | 是 | 页面入口。只提供结构和 `data-*` 挂载点，内容主要由 `script.js` 注入。 |
| `style.css` | 是 | 全站样式、响应式布局、照片墙滚动动画、弹窗样式。 |
| `script.js` | 是 | 全站配置和交互逻辑。包含照片清单、文案、音乐路径、卡片路径和渲染函数。 |
| `README.md` | 建议保留 | 给普通使用者看的说明。当前 README 已同步为 `review-batch-20260521/accepted/` 小卡片目录，并说明 GitHub Pages 部署方式。 |
| `project_review.md` | 建议保留 | 当前架构审计和 Git 迁移说明。 |
| `jayee照片(1).zip` | 否 | 原始照片压缩包或备份包。网页运行不引用它。若要减小仓库体积，可不上传或改用外部备份。 |

## 4. 目录结构与资源角色

```text
.
├── index.html
├── style.css
├── script.js
├── README.md
├── project_review.md
├── jayee照片(1).zip
└── public/
    ├── photos/
    ├── art-cards/
    ├── music/
    └── illustrations/
```

### `public/photos/`

这是当前网页的原始照片库，运行时必需。`script.js` 中的 `PHOTO_BASE = "public/photos/"` 会和 `CONFIG.photos[].file` 拼接成最终图片路径。

照片按场景分类：

| 子目录 | 数量 | 当前用途 |
|---|---:|---|
| `public/photos/home/` | 9 | 居家日常 |
| `public/photos/ski/` | 9 | 滑雪和雪地 |
| `public/photos/hospital/` | 3 | 生病和陪伴 |
| `public/photos/video/` | 5 | 视频截图 |
| `public/photos/games/` | 4 | 娱乐/游戏 |
| `public/photos/cooking/` | 2 | 做饭/吃饭 |
| `public/photos/outing/` | 7 | 出门游玩 |
| `public/photos/moments/` | 1 | 其它瞬间 |

运行时验证结果：`CONFIG.photos` 配置的 40 张照片全部存在。

### `public/art-cards/review-batch-20260521/accepted/`

这是当前网页实际读取的回忆小卡片目录，运行时必需。

`script.js` 中配置：

```js
CONFIG.sketches.basePath = "public/art-cards/review-batch-20260521/accepted/"
```

命名规则：

```text
photo-001-postcard.png
photo-002-postcard.png
photo-003-crayon.png
...
```

实际路径由 `artCardSrc(photo, artStyle)` 自动拼接：

```text
basePath + "photo-" + 三位数编号 + "-" + crayon/postcard + ".png"
```

运行时验证结果：`CONFIG.sketches.assignments` 配置的 40 张 accepted 小卡片全部存在。

### `public/music/`

当前网页音乐目录，运行时必需。

`script.js` 中当前引用：

```js
public/music/特别的人.mp3
public/music/咏春.mp3
```

浏览器不会自动播放音乐，用户需要点击页面右上角“播放歌曲”按钮。播放逻辑会在这两首歌里随机选一首，结束后继续随机下一首。

运行时验证结果：2 个 mp3 全部存在。

### `public/art-cards/generated-random/`

历史生成批次，不是当前网页运行时入口。之前网页读取过这里，但现在 `script.js` 已经改为读取 `review-batch-20260521/accepted/`。

如果目标是“完整保留创作历史”，可以上传此目录。如果目标是“只上传可运行网页”，可以不上传这个目录，从而减少约 129 MB。

### `public/art-cards/review-batch-20260521/rejected/`

审核失败或跑偏的小卡片，不应接入网页。不是运行时必需。

建议保留在本地或单独归档；如果上传 Git，会增加仓库体积，也可能让后续维护者误用。

### `public/art-cards/home/` 等分类目录

这些是早期按照片类别整理的艺术化卡片 `.jpg`，当前网页不读取它们。它们可视为历史素材或备选素材。

如果只保留运行网页所需文件，这些目录不是必需：

- `public/art-cards/home/`
- `public/art-cards/ski/`
- `public/art-cards/hospital/`
- `public/art-cards/video/`
- `public/art-cards/games/`
- `public/art-cards/cooking/`
- `public/art-cards/outing/`
- `public/art-cards/moments/`

### `public/art-cards/generated/`

目前只看到 `generation-plan.json`，没有作为运行时图片源使用。不是运行时必需。

### `public/illustrations/`

包含若干插画图片，例如 `sketch-ski.png`、`sketch-home.png`。当前 `index.html`、`style.css`、`script.js` 没有运行时引用这些文件。不是当前网页必需，但可作为备选视觉素材保留。

## 5. 文件引用关系

### `index.html`

`index.html` 是唯一 HTML 入口。它直接引用：

```html
<link rel="stylesheet" href="style.css">
<script src="script.js"></script>
```

页面结构由几个 section 组成：

- `#home`: 封面，含 `data-hero-photos` 和标题文案挂载点
- `#timeline`: 场景回忆，含 `data-scene-grid`
- `#gallery`: 照片墙和回忆小卡片，含 `data-gallery-stack`、`data-sketch-strip`
- `#letter`: 一封信，含 `data-letter-lines`、`data-letter-signature`
- `.lightbox`: 图片弹窗，含上一张、下一张、关闭按钮

大部分文字不是写死在 HTML 里，而是通过 `data-*` 属性由 `script.js` 填充。

### `script.js`

`script.js` 是项目的数据中心和行为中心。

核心结构：

- `CONFIG`: 全站配置，包括标题、导航、音乐、照片、场景、卡片、信件文案。
- `PHOTO_BASE`: 原始照片根路径，当前为 `public/photos/`。
- `ART_STYLE_SEQUENCE`: 如果某张照片没有指定卡片样式时的 fallback 样式序列。
- `state`: 前端运行状态，包括照片数组、当前弹窗照片、当前音乐。

初始化流程：

```text
DOMContentLoaded
└── init()
    ├── 生成 state.photos
    │   ├── src = PHOTO_BASE + CONFIG.photos[].file
    │   └── artSrc = CONFIG.sketches.basePath + photo-xxx-style.png
    ├── hydrateStaticCopy()
    ├── renderHeroPhotos()
    ├── renderScenes()
    ├── renderGalleryStacks()
    ├── renderSketchCards()
    ├── renderLetter()
    ├── setupSmoothButtons()
    ├── setupLightbox()
    ├── setupMusic()
    └── setupReveal()
```

主要渲染函数：

| 函数 | 作用 |
|---|---|
| `hydrateStaticCopy()` | 把 `CONFIG` 里的标题、导航、按钮文案、页脚写入 HTML。 |
| `renderHeroPhotos()` | 根据 `CONFIG.heroPhotoIds` 渲染封面旁边的照片。 |
| `renderScenes()` | 根据 `CONFIG.sceneCategories` 渲染“场景回忆”。 |
| `renderGalleryStacks()` | 渲染“熊熊家的照片墙”横向自动滚动轨道。 |
| `renderSketchCards()` | 渲染回忆小卡片横向自动滚动轨道。当前小卡片底部不显示文字。 |
| `renderLetter()` | 渲染一封信。 |
| `setupLightbox()` | 注册图片弹窗、键盘 ESC、左右切换。 |
| `setupMusic()` | 注册音乐播放按钮。 |
| `setupReveal()` | 页面滚动时给元素添加渐入效果。 |

运行时引用的路径都来自 `CONFIG`：

- 原始照片：`PHOTO_BASE + CONFIG.photos[].file`
- 小卡片：`CONFIG.sketches.basePath + photo-编号-样式.png`
- 音乐：`CONFIG.music.tracks[]`

### `style.css`

`style.css` 负责所有视觉样式，不引用外部字体、CDN 或图片。

主要模块：

- `:root`: 色彩、字体、阴影、圆角变量。
- `.topbar`: 固定顶部导航。
- `.hero`: 封面布局。
- `.hero-photos` / `.hero-photo`: 封面照片墙。
- `.scene-*`: 场景回忆卡片和照片拼贴。
- `.gallery-*` / `.auto-rail-*`: 自动滚动照片墙。
- `.sketch-*`: 回忆小卡片轨道。
- `.letter-*`: 信件区域。
- `.lightbox-*`: 图片弹窗。
- `@media (min-width: 720px)`: 平板/桌面布局。
- `@media (min-width: 1040px)`: 大桌面微调。
- `@media (prefers-reduced-motion: reduce)`: 减少动画偏好适配。

封面照片布局的当前策略：

- 小屏幕：显示 4 张照片，使用网格拼贴，避免严重重叠。
- 720px 以上：标题和照片分为两列，右侧照片簇显示 8 张，照片尽量展示 80% 以上。
- 大屏幕：照片簇最大宽度受限，不随屏幕无限分散。

照片墙滚动速度：

- 普通照片墙 `.photo-auto-track`: `156s`
- 回忆小卡片 `.sketch-auto-track`: `156s`

## 6. 当前运行时资源清单

### 原始照片清单

| ID | 类别 | 原始照片路径 |
|---:|---|---|
| 001 | home | `public/photos/home/photo-001.jpg` |
| 002 | ski | `public/photos/ski/photo-002.jpg` |
| 003 | home | `public/photos/home/photo-003.jpg` |
| 004 | ski | `public/photos/ski/photo-004.jpg` |
| 005 | hospital | `public/photos/hospital/photo-005.jpg` |
| 006 | video | `public/photos/video/photo-006.png` |
| 007 | ski | `public/photos/ski/photo-007.jpg` |
| 008 | hospital | `public/photos/hospital/photo-008.jpg` |
| 009 | games | `public/photos/games/photo-009.jpg` |
| 010 | cooking | `public/photos/cooking/photo-010.jpg` |
| 011 | ski | `public/photos/ski/photo-011.jpg` |
| 012 | home | `public/photos/home/photo-012.jpg` |
| 013 | video | `public/photos/video/photo-013.png` |
| 014 | hospital | `public/photos/hospital/photo-014.jpg` |
| 015 | outing | `public/photos/outing/photo-015.jpg` |
| 016 | home | `public/photos/home/photo-016.jpg` |
| 017 | outing | `public/photos/outing/photo-017.jpg` |
| 018 | home | `public/photos/home/photo-018.jpg` |
| 019 | games | `public/photos/games/photo-019.jpg` |
| 020 | home | `public/photos/home/photo-020.jpg` |
| 021 | games | `public/photos/games/photo-021.jpg` |
| 022 | video | `public/photos/video/photo-022.png` |
| 023 | home | `public/photos/home/photo-023.jpg` |
| 024 | home | `public/photos/home/photo-024.jpg` |
| 025 | outing | `public/photos/outing/photo-025.jpg` |
| 026 | games | `public/photos/games/photo-026.jpg` |
| 027 | home | `public/photos/home/photo-027.jpg` |
| 028 | outing | `public/photos/outing/photo-028.jpg` |
| 029 | ski | `public/photos/ski/photo-029.jpg` |
| 030 | video | `public/photos/video/photo-030.png` |
| 031 | video | `public/photos/video/photo-031.png` |
| 032 | outing | `public/photos/outing/photo-032.jpg` |
| 033 | ski | `public/photos/ski/photo-033.jpg` |
| 034 | outing | `public/photos/outing/photo-034.jpg` |
| 035 | moments | `public/photos/moments/photo-035.jpg` |
| 036 | outing | `public/photos/outing/photo-036.jpg` |
| 037 | cooking | `public/photos/cooking/photo-037.jpg` |
| 038 | ski | `public/photos/ski/photo-038.jpg` |
| 039 | ski | `public/photos/ski/photo-039.jpg` |
| 040 | ski | `public/photos/ski/photo-040.jpg` |

### 回忆小卡片清单

当前运行时小卡片都来自：

```text
public/art-cards/review-batch-20260521/accepted/
```

样式分配由 `CONFIG.sketches.assignments` 控制：

| ID | 样式 | 小卡片路径 |
|---:|---|---|
| 001 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-001-postcard.png` |
| 002 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-002-postcard.png` |
| 003 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-003-crayon.png` |
| 004 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-004-crayon.png` |
| 005 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-005-crayon.png` |
| 006 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-006-crayon.png` |
| 007 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-007-crayon.png` |
| 008 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-008-postcard.png` |
| 009 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-009-crayon.png` |
| 010 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-010-postcard.png` |
| 011 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-011-postcard.png` |
| 012 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-012-postcard.png` |
| 013 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-013-crayon.png` |
| 014 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-014-crayon.png` |
| 015 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-015-postcard.png` |
| 016 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-016-crayon.png` |
| 017 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-017-crayon.png` |
| 018 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-018-crayon.png` |
| 019 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-019-postcard.png` |
| 020 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-020-postcard.png` |
| 021 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-021-postcard.png` |
| 022 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-022-postcard.png` |
| 023 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-023-crayon.png` |
| 024 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-024-postcard.png` |
| 025 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-025-crayon.png` |
| 026 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-026-crayon.png` |
| 027 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-027-crayon.png` |
| 028 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-028-postcard.png` |
| 029 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-029-crayon.png` |
| 030 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-030-crayon.png` |
| 031 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-031-postcard.png` |
| 032 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-032-crayon.png` |
| 033 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-033-crayon.png` |
| 034 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-034-postcard.png` |
| 035 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-035-postcard.png` |
| 036 | crayon | `public/art-cards/review-batch-20260521/accepted/photo-036-crayon.png` |
| 037 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-037-postcard.png` |
| 038 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-038-postcard.png` |
| 039 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-039-postcard.png` |
| 040 | postcard | `public/art-cards/review-batch-20260521/accepted/photo-040-postcard.png` |

## 7. 页面功能说明

### 封面

封面由 HTML 中的 `#home` section 承载。标题文案来自 `CONFIG.siteTitle`、`CONFIG.heroKicker`、`CONFIG.subtitle`。

封面照片来自：

```js
CONFIG.heroPhotoIds = [1, 2, 10, 37, 24, 33, 36, 19, 5, 14, 21, 28]
```

JS 会渲染 12 张，但 CSS 控制实际显示数量：

- 小屏幕显示前 4 张
- 桌面端显示前 8 张
- 第 9 张之后隐藏

这是一种性能和视觉折中：保留照片墙感觉，同时避免小屏幕过度堆叠、大屏幕过度分散。

### 场景回忆

由 `CONFIG.sceneCategories` 驱动。每个场景包含：

- `key`: 场景类别
- `title`: 场景标题
- `lines`: 文案段落
- `photoIds`: 该场景展示的照片 ID

渲染函数是 `renderScenes()`。

### 熊熊家的照片墙

由 `renderGalleryStacks()` 渲染。它直接使用 `state.photos` 中全部 40 张原始照片，并用 `duplicateItems(state.photos)` 复制一份，形成横向无缝滚动。

当前每张照片下方有原始配文。

### 回忆小卡片

由 `renderSketchCards()` 渲染。它同样使用全部 40 张照片的数据，但图片源换成 `photo.artSrc`，即 accepted 小卡片路径。

当前设计要求：

- 小卡片底部不显示文字
- 小卡片滚动速度和照片墙一致，都是 156 秒
- 点击小卡片打开弹窗时，弹窗底部也不显示说明文字

### 图片弹窗

所有照片和小卡片都可以打开 `.lightbox`。

行为：

- 点击图片打开
- 点击关闭按钮关闭
- 点击左右按钮切换
- 按 `Escape` 关闭
- 按键盘左右键切换

注意：从小卡片打开弹窗时，弹窗显示原始照片还是小卡片由 `openLightbox()` 的 `view` 参数控制。当前代码里小卡片 view 使用 `artSrc`，加载失败时 fallback 到原始照片。

### 音乐播放

音乐按钮由 `setupMusic()` 控制。

行为：

- 第一次点击随机选择一首歌
- 歌曲结束后自动随机下一首
- 如果浏览器阻止播放，按钮状态会回到未播放
- 如果没有配置音乐，会弹出提示

## 8. Git 上传建议

### 必须上传的运行时文件

如果目标是让网页完整运行，至少需要上传：

```text
index.html
style.css
script.js
README.md
project_review.md
public/photos/
public/music/
public/art-cards/review-batch-20260521/accepted/
```

这些文件缺任何一类，当前网页都会有明显功能缺失。

### 可选上传的历史/备份文件

这些文件不是当前网页运行时必需：

```text
jayee照片(1).zip
public/illustrations/
public/art-cards/generated/
public/art-cards/generated-random/
public/art-cards/review-batch-20260521/rejected/
public/art-cards/home/
public/art-cards/ski/
public/art-cards/hospital/
public/art-cards/video/
public/art-cards/games/
public/art-cards/cooking/
public/art-cards/outing/
public/art-cards/moments/
```

建议：

- 如果 Git 仓库只是用于部署网页，建议不上传这些可选历史文件。
- 如果 Git 仓库也用于保存创作过程和审核记录，可以上传，但仓库会明显变大。
- `rejected/` 目录不要接入网页，避免误用失败图。
- `jayee照片(1).zip` 是最大单文件，虽然低于 100 MB，但对 Git 历史不友好；更适合放在本地备份或网盘。

### 建议的 `.gitignore`

当前项目还没有看到 `.gitignore`。如果决定不上传历史素材，可以创建类似规则：

```gitignore
jayee照片(1).zip
public/art-cards/generated/
public/art-cards/generated-random/
public/art-cards/review-batch-20260521/rejected/
public/art-cards/home/
public/art-cards/ski/
public/art-cards/hospital/
public/art-cards/video/
public/art-cards/games/
public/art-cards/cooking/
public/art-cards/outing/
public/art-cards/moments/
public/illustrations/
```

如果想完整保留素材历史，不要使用上面的 ignore 规则。

### GitHub Pages 部署

推荐部署方式：

1. 在 GitHub 创建新仓库。
2. 上传项目根目录内容，确保 `index.html` 在仓库根目录。
3. 进入仓库 `Settings`。
4. 打开 `Pages`。
5. `Source` 选择 `Deploy from a branch`。
6. 分支选择 `main`，目录选择 `/root`。
7. 等待 GitHub Pages 生成链接。

部署后访问形如：

```text
https://用户名.github.io/仓库名/
```

### 跨平台注意事项

- GitHub Pages 和 Linux 静态服务器区分大小写，路径大小写必须和代码完全一致。
- 当前 mp3 文件名包含中文：`特别的人.mp3`、`咏春.mp3`。现代浏览器和 GitHub Pages 通常支持 UTF-8 中文路径，但如果未来遇到跨平台路径问题，可以改成英文名，例如 `special-person.mp3`、`yongchun.mp3`，并同步修改 `CONFIG.music.tracks`。
- 项目根目录名可以改，不影响运行，因为代码使用相对路径。
- 不要把资源路径改成本机盘符路径或本地文件 URL，否则上传后会失效。
- 不建议把源码移动到 `public/` 里面；当前结构适合 GitHub Pages 根目录部署。

## 9. 后续维护指南

### 替换一张原始照片

1. 把新图片放到对应的 `public/photos/<category>/` 目录。
2. 在 `script.js` 的 `CONFIG.photos` 中找到对应 ID。
3. 修改 `file` 路径和 `caption`。
4. 如果这张照片有对应回忆小卡片，也要在 accepted 目录里放入同编号、同样式的卡片。

### 新增照片

当前代码理论上支持新增照片，但需要同步更新：

- `CONFIG.photos`
- `CONFIG.sketches.assignments`
- `public/photos/...`
- `public/art-cards/review-batch-20260521/accepted/...`
- 需要展示在封面时，更新 `CONFIG.heroPhotoIds`
- 需要进入某个场景时，更新 `CONFIG.sceneCategories[].photoIds`

新增后应检查：

- 原始照片是否存在
- 小卡片是否存在
- 文件名是否遵守 `photo-三位数-style.png`
- GitHub Pages 上大小写是否匹配

### 修改回忆小卡片来源

只改一个地方：

```js
CONFIG.sketches.basePath
```

例如从 accepted 切回 generated-random：

```js
basePath: "public/art-cards/generated-random/"
```

但当前用户确认采用 accepted 成品图，因此不要随意切回旧目录。

### 修改封面照片布局

封面照片的数据源在：

```js
CONFIG.heroPhotoIds
```

封面照片的响应式布局在 `style.css` 的：

```css
.hero-photos
.hero-photo
@media (min-width: 720px)
@media (min-width: 1040px)
```

当前策略经过针对窗口截图调整：桌面端显示 8 张，尽量让每张照片露出 80% 以上。后续修改时建议在以下视口都检查：

- 360 x 740，手机竖屏
- 768 x 1024，平板竖屏
- 1280 x 720，常见笔记本窗口
- 1920 x 1080，桌面全屏

### 修改文案

优先修改 `script.js` 顶部的 `CONFIG`：

- `siteTitle`
- `worldName`
- `heroKicker`
- `subtitle`
- `navItems`
- `timeline`
- `gallery`
- `sketches`
- `letter`
- `footer`
- `photos[].caption`
- `sceneCategories`
- `loveLetter`

HTML 中的 `data-*` 挂载点不要随意删除，否则 JS 找不到节点。

## 10. 文档同步状态

以下文档内容已经同步：

- 根目录 `README.md` 已改为 `public/art-cards/review-batch-20260521/accepted/`。
- `public/art-cards/review-batch-20260521/README.md` 的“网页当前读取目录”也已改为 `accepted/`。

实际当前代码读取的是：

```text
public/art-cards/review-batch-20260521/accepted/
```

## 11. 验证记录

本次审计做过以下验证：

- 遍历了项目目录，统计文件数量、类型和大小。
- 检查了 `index.html`、`style.css`、`script.js` 的引用关系。
- 检查了 `script.js` 中 40 张原始照片路径：全部存在。
- 检查了 `script.js` 中 40 张 accepted 小卡片路径：全部存在。
- 检查了 `script.js` 中 2 首音乐路径：全部存在。
- 检查了脚本语法：`node --check .\script.js` 通过。
- 检查了本地代码中没有运行时依赖本机盘符路径或本地文件 URL。
