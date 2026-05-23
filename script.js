const CONFIG = {
  siteTitle: "和我，和你，和我们",
  worldName: "熊熊家",
  heroKicker: "只属于两个人的小世界",
  subtitle: "欢迎来到熊熊家，这里收藏着一些只属于我们的瞬间。",
  enterButton: "进入我们的回忆",
  scrollNote: "",
  navLabel: "页面导航",
  navItems: {
    timeline: "场景回忆",
    gallery: "照片墙",
    letter: "一封信"
  },
  music: {
    tracks: [
      "public/music/特别的人.mp3",
      "public/music/咏春.mp3"
    ],
    playLabel: "播放歌曲",
    pauseLabel: "暂停歌曲",
    missingLabel: "请先放入音乐文件",
    missingMessage: "请把 mp3 音乐文件放到 public/music/，并在 script.js 的 CONFIG.music.tracks 里添加文件名。"
  },
  timeline: {
    kicker: "",
    title: "我们的小日子",
    intro: ""
  },
  gallery: {
    kicker: "",
    title: "熊熊家的照片墙",
    intro: ""
  },
  sketches: {
    kicker: "回忆小卡片",
    intro: "",
    basePath: "public/art-cards/review-batch-20260521/accepted/",
    styleNames: {
      crayon: "蜡笔小卡片",
      postcard: "旅行涂鸦小卡片"
    },
    assignments: {
      1: "postcard",
      2: "postcard",
      3: "crayon",
      4: "crayon",
      5: "crayon",
      6: "crayon",
      7: "crayon",
      8: "postcard",
      9: "crayon",
      10: "postcard",
      11: "postcard",
      12: "postcard",
      13: "crayon",
      14: "crayon",
      15: "postcard",
      16: "crayon",
      17: "crayon",
      18: "crayon",
      19: "postcard",
      20: "postcard",
      21: "postcard",
      22: "postcard",
      23: "crayon",
      24: "postcard",
      25: "crayon",
      26: "crayon",
      27: "crayon",
      28: "postcard",
      29: "crayon",
      30: "crayon",
      31: "postcard",
      32: "crayon",
      33: "crayon",
      34: "postcard",
      35: "postcard",
      36: "crayon",
      37: "postcard",
      38: "postcard",
      39: "postcard",
      40: "postcard",
      41: "crayon"
    }
  },
  letter: {
    kicker: "写给你",
    title: "一封信",
    intro: "",
    signature: "可爱茄子熊"
  },
  footer: "熊熊家",
  lightbox: {
    close: "关闭",
    previous: "上一张",
    next: "下一张"
  },
  photos: [
    { id: 1, category: "home", file: "home/photo-001.jpg", style: "crayon", caption: "窝在熊熊家的小日子，安静但很有我们自己的味道。" },
    { id: 2, category: "ski", file: "ski/photo-002.jpg", style: "oil", caption: "滑雪的时候，冷风也挡不住一点点开心。" },
    { id: 3, category: "home", file: "home/photo-003.jpg", style: "watercolor", caption: "在家里放松下来的样子，也值得被好好收藏。" },
    { id: 4, category: "ski", file: "ski/photo-004.jpg", style: "ink", caption: "雪地里的我们，像把冬天过成了同一页。" },
    { id: 5, category: "hospital", file: "hospital/photo-005.jpg", style: "pencil", caption: "那次我生病了，谢谢老婆崽崽一直在旁边。" },
    { id: 6, category: "video", file: "video/photo-006.png", style: "watercolor", caption: "视频里的你，隔着屏幕也很近。" },
    { id: 7, category: "ski", file: "ski/photo-007.jpg", style: "oil", caption: "出去玩的路上，连冷空气都变得可爱了一点。" },
    { id: 8, category: "hospital", file: "hospital/photo-008.jpg", style: "crayon", caption: "被照顾、被陪着，是很具体的安心。" },
    { id: 9, category: "games", file: "games/photo-009.jpg", style: "ink", caption: "玩游戏的时候，你认真起来也很可爱。" },
    { id: 10, category: "cooking", file: "cooking/photo-010.jpg", style: "oil", caption: "美厨娘下厨的照片必须单独夸一夸，太厉害了。" },
    { id: 11, category: "ski", file: "ski/photo-011.jpg", style: "watercolor", caption: "呜呜呜，美少女流浪日记" },
    { id: 12, category: "home", file: "home/photo-012.jpg", style: "pencil", caption: "大大的眼睛，圆圆的脑袋。" },
    { id: 13, category: "video", file: "video/photo-013.png", style: "crayon", caption: "视频那头的笑，也能让一天亮起来。" },
    { id: 14, category: "hospital", file: "hospital/photo-014.jpg", style: "watercolor", caption: "在医院的那天，谢谢老婆崽崽。" },
    { id: 15, category: "outing", file: "outing/photo-015.jpg", style: "ink", caption: "一起出门时，普通走廊也能变成回忆。" },
    { id: 16, category: "home", file: "home/photo-016.jpg", style: "oil", caption: "靠近一点，再靠近一点，就是我们。" },
    { id: 17, category: "outing", file: "outing/photo-017.jpg", style: "watercolor", caption: "出去玩的照片里，笑得很自然。" },
    { id: 18, category: "home", file: "home/photo-018.jpg", style: "crayon", caption: "家里的轻松感，像把心放回原位。" },
    { id: 19, category: "games", file: "games/photo-019.jpg", style: "oil", caption: "娱乐时间的小片段，笑起来就很有熊熊家的感觉。" },
    { id: 20, category: "home", file: "home/photo-020.jpg", style: "pencil", caption: "有些瞬间不用摆好，真实就已经很好。" },
    { id: 21, category: "games", file: "games/photo-021.jpg", style: "crayon", caption: "生活就是小火车，快乐的时候马上启航。" },
    { id: 22, category: "video", file: "video/photo-022.png", style: "ink", caption: "屏幕里的见面，也算我们认真靠近的一种方式。" },
    { id: 23, category: "home", file: "home/photo-023.jpg", style: "watercolor", caption: "在家里也要好好拍一张，因为你真的很好看。" },
    { id: 24, category: "home", file: "home/photo-024.jpg", style: "pencil", caption: "贴近镜头的我们，是很真实的我们。" },
    { id: 25, category: "outing", file: "outing/photo-025.jpg", style: "oil", caption: "出去玩的时候，我们把开心带在身上。" },
    { id: 26, category: "games", file: "games/photo-026.jpg", style: "watercolor", caption: "游戏、电影和出门的小快乐，都被这一张装下。" },
    { id: 27, category: "home", file: "home/photo-027.jpg", style: "ink", caption: "家里的慵懒瞬间，也是熊熊家的存档。" },
    { id: 28, category: "outing", file: "outing/photo-028.jpg", style: "crayon", caption: "出门时拍下的亲近感，很轻也很稳。" },
    { id: 29, category: "ski", file: "ski/photo-029.jpg", style: "pencil", caption: "滑雪时的夸张表情，要留给以后一起笑。" },
    { id: 30, category: "video", file: "video/photo-030.png", style: "oil", caption: "视频里的笑容，像把距离悄悄缩短。" },
    { id: 31, category: "video", file: "video/photo-031.png", style: "watercolor", caption: "隔着屏幕看见你，也会觉得今天值得。" },
    { id: 32, category: "outing", file: "outing/photo-032.jpg", style: "ink", caption: "出去玩的照片里，风景和你都在。" },
    { id: 33, category: "ski", file: "ski/photo-033.jpg", style: "crayon", caption: "滑雪的合照，是冬天送给我们的纪念。" },
    { id: 34, category: "outing", file: "outing/photo-034.jpg", style: "pencil", caption: "出去玩的路上，一起站进雪景里。" },
    { id: 35, category: "moments", file: "moments/photo-035.jpg", style: "oil", caption: "这一张像一个小小的暂停键，先把当时留住。" },
    { id: 36, category: "outing", file: "outing/photo-036.jpg", style: "watercolor", caption: "出门时的小自拍，越看越像我们的日常。" },
    { id: 37, category: "cooking", file: "cooking/photo-037.jpg", style: "crayon", caption: "美厨娘认真吃饭的样子，也很值得夸。" },
    { id: 38, category: "ski", file: "ski/photo-038.jpg", style: "ink", caption: "滑雪累了也要拍一张。" },
    { id: 39, category: "ski", file: "ski/photo-039.jpg", style: "oil", caption: "滑雪路上的一张，雪落下来也刚刚好。" },
    { id: 40, category: "ski", file: "ski/photo-040.jpg", style: "watercolor", caption: "滑雪这一类，要用这张收个漂亮的尾。" },
    { id: 41, category: "home", file: "home/photo-041.jpg", style: "crayon", caption: "呼呼小猪！", sourceIssue: "2", sourceHash: "6f7918c57f00" }
  ],
  sceneCategories: [
    {
      key: "home",
      title: "窝在熊熊家：",
      lines: [
        "咱们是两餐三季，有你在家里，感觉日子就很快乐踏实，崽崽大人！"
      ],
      photoIds: [1, 3, 12, 16, 18, 20, 23, 24, 27, 41]
    },
    {
      key: "ski",
      title: "滑雪gogogo！",
      lines: [
        "最好的coach wang！",
        "会怀念每一个亮亮的雪季！"
      ],
      photoIds: [39, 33, 40, 2, 4, 7, 11, 29, 38]
    },
    {
      key: "hospital",
      title: "被陪着的那天",
      lines: [
        "那次我生病了，谢谢老婆崽崽一直在旁边。",
        "不是很大的场面，但这种陪伴我会记很久。"
      ],
      photoIds: [5, 14, 8]
    },
    {
      key: "video",
      title: "隔着屏幕也靠近",
      lines: [
        "视频里的见面也算数，想念有时候就是这样被接住的。",
        "所爱隔山海，山海皆可平。"
      ],
      photoIds: [6, 13, 22, 30, 31]
    },
    {
      key: "games",
      title: "娱乐时间~",
      lines: [
        "生活就是小火车，快上车，马上启航喽！嘟嘟嘟！"
      ],
      photoIds: [19, 21, 9, 26]
    },
    {
      key: "cooking",
      title: "美厨娘！到！！！",
      lines: [
        "美厨娘做饭的照片必须放在这里，太厉害了。",
        "会做饭、会认真生活，也会把熊熊家变得更有烟火气。"
      ],
      photoIds: [10, 37]
    },
    {
      key: "outing",
      title: "一起出去玩",
      lines: [
        "出去玩的照片里，有路、有风景，也有我们把普通一天过得更开心的样子。",
        "很多地方去过之后，就会悄悄变成只属于我们的坐标。"
      ],
      photoIds: [36, 32, 15, 17, 25, 28, 34]
    }
  ],
  galleryGroups: [
    { key: "ski", title: "雪地叠叠乐", text: "把滑雪和雪景都放在一起，像一小摞发亮的冬天。", photoIds: [39, 33, 40, 2, 4, 7, 11, 29, 38] },
    { key: "home", title: "熊熊家的日常", text: "居家、靠近和一些可爱表情，都是最像我们的部分。", photoIds: [1, 3, 12, 16, 18, 20, 23, 24, 27] },
    { key: "hospital", title: "被陪着的那天", text: "生病时的陪伴，要单独放在柔软一点的位置。", photoIds: [5, 14, 8] },
    { key: "video", title: "屏幕里的靠近", text: "视频里的见面，也能把想念轻轻接住。", photoIds: [6, 13, 22, 30, 31] },
    { key: "games", title: "娱乐时间", text: "游戏、电影和小快乐，都是不用隆重也值得存下来的瞬间。", photoIds: [19, 21, 9, 26] },
    { key: "cooking", title: "美厨娘时间", text: "烟火气也可以很可爱，尤其是你认真做饭的时候。", photoIds: [10, 37] },
    { key: "outing", title: "出门的小坐标", text: "一起去过的地方，会慢慢变成以后能认出来的回忆。", photoIds: [36, 32, 15, 17, 25, 28, 34] },
  ],
  heroPhotoIds: [1, 2, 10, 37, 24, 33, 36, 19, 5, 14, 21, 28],
  loveLetter: [
    "老婆崽崽：",
    "我把这个小网页做成熊熊家的样子，不是为了哪一天才可以打开，而是想让你在任何一个普通晚上，都能有一个地方翻翻我们的照片。",
    "和你在一起之后，我越来越喜欢那些很小的瞬间：一起走路、一起笑、一起视频、一起玩游戏，也一起把日子过得热乎一点。它们不一定轰轰烈烈，但都很真实。",
    "以后如果你想回头看看，就来这里。这里收藏着和我，和你，和我们，也收藏着我想继续陪你的心情。"
  ]
};

const PHOTO_BASE = "public/photos/";
const ART_STYLE_SEQUENCE = [
  "crayon", "postcard", "crayon", "postcard", "crayon",
  "postcard", "crayon", "postcard", "crayon", "postcard"
];

const state = {
  activePhoto: 0,
  activeLightboxView: "photo",
  photos: [],
  audio: null,
  currentTrackIndex: -1,
  isMusicPlaying: false
};

document.addEventListener("DOMContentLoaded", init);

function init() {
  state.photos = CONFIG.photos.map((photo) => {
    const artStyle = artStyleFor(photo);
    return {
      ...photo,
      artStyle,
      src: PHOTO_BASE + photo.file,
      artSrc: artCardSrc(photo, artStyle)
    };
  });

  hydrateStaticCopy();
  renderHeroPhotos(byIds(CONFIG.heroPhotoIds));
  renderScenes();
  renderGalleryStacks();
  renderSketchCards();
  renderLetter();
  setupSmoothButtons();
  setupLightbox();
  setupMusic();
  setupReveal();
}

function hydrateStaticCopy() {
  document.title = `${CONFIG.siteTitle} | ${CONFIG.worldName}`;
  text("[data-world-name]", CONFIG.worldName);
  text("[data-hero-kicker]", CONFIG.heroKicker);
  text("[data-site-title]", CONFIG.siteTitle);
  text("[data-subtitle]", CONFIG.subtitle);
  text("[data-enter-button]", CONFIG.enterButton);
  text("[data-scroll-note]", CONFIG.scrollNote);
  text("[data-nav-timeline]", CONFIG.navItems.timeline);
  text("[data-nav-gallery]", CONFIG.navItems.gallery);
  text("[data-nav-letter]", CONFIG.navItems.letter);
  text("[data-music-toggle]", CONFIG.music.playLabel);
  text("[data-timeline-kicker]", CONFIG.timeline.kicker);
  text("[data-timeline-title]", CONFIG.timeline.title);
  text("[data-timeline-intro]", CONFIG.timeline.intro);
  text("[data-gallery-kicker]", CONFIG.gallery.kicker);
  text("[data-gallery-title]", CONFIG.gallery.title);
  text("[data-gallery-intro]", CONFIG.gallery.intro);
  text("[data-letter-kicker]", CONFIG.letter.kicker);
  text("[data-letter-title]", CONFIG.letter.title);
  text("[data-letter-intro]", CONFIG.letter.intro);
  text("[data-footer]", CONFIG.footer);
  text("[data-lightbox-close]", "×");
  text("[data-lightbox-prev]", "‹");
  text("[data-lightbox-next]", "›");

  document.querySelector(".nav-links")?.setAttribute("aria-label", CONFIG.navLabel);
  setAria("[data-music-toggle]", CONFIG.music.playLabel);
  setAria("[data-lightbox-close]", CONFIG.lightbox.close);
  setAria("[data-lightbox-prev]", CONFIG.lightbox.previous);
  setAria("[data-lightbox-next]", CONFIG.lightbox.next);
}

function renderHeroPhotos(photos) {
  const root = document.querySelector("[data-hero-photos]");
  if (!root) return;
  root.innerHTML = "";

  photos.forEach((photo) => {
    const frame = document.createElement("div");
    frame.className = "hero-photo";
    const img = document.createElement("img");
    img.src = photo.src;
    img.alt = "";
    img.loading = "eager";
    frame.appendChild(img);
    root.appendChild(frame);
  });
}

function renderScenes() {
  const root = document.querySelector("[data-scene-grid]");
  if (!root) return;
  root.innerHTML = "";

  CONFIG.sceneCategories.forEach((scene) => {
    const photos = byIds(scene.photoIds);
    const card = document.createElement("article");
    card.className = `scene-card scene-${scene.key}`;
    card.setAttribute("data-reveal", "");

    const header = document.createElement("div");
    header.className = "scene-copy";

    const title = document.createElement("h3");
    title.textContent = scene.title;
    header.appendChild(title);

    scene.lines.forEach((line) => {
      const paragraph = document.createElement("p");
      paragraph.textContent = line;
      header.appendChild(paragraph);
    });

    const collage = document.createElement("div");
    collage.className = "scene-collage";
    photos.slice(0, 7).forEach((photo, index) => {
      collage.appendChild(makePhotoButton(photo, `scene-photo scene-photo-${index + 1}`));
    });

    card.append(collage, header);
    root.appendChild(card);
  });
}

function renderGalleryStacks() {
  const root = document.querySelector("[data-gallery-stack]");
  if (!root) return;
  root.innerHTML = "";

  const card = document.createElement("article");
  card.className = "stack-card stack-card-wide";
  card.setAttribute("data-reveal", "");

  const rail = document.createElement("div");
  rail.className = "auto-rail photo-auto-rail";
  rail.setAttribute("aria-label", CONFIG.gallery.title);

  const track = document.createElement("div");
  track.className = "auto-rail-track photo-auto-track";
  duplicateItems(state.photos).forEach((photo) => {
    track.appendChild(makeGalleryPhotoCard(photo));
  });

  rail.appendChild(track);
  card.appendChild(rail);
  root.appendChild(card);
}

function renderSketchCards() {
  const root = document.querySelector("[data-sketch-strip]");
  if (!root) return;
  root.innerHTML = "";

  const intro = document.createElement("div");
  intro.className = "sketch-intro";
  intro.setAttribute("data-reveal", "");
  const kicker = document.createElement("p");
  kicker.className = "eyebrow";
  kicker.textContent = CONFIG.sketches.kicker;
  const textLine = document.createElement("p");
  textLine.textContent = CONFIG.sketches.intro;
  intro.append(kicker, textLine);
  root.appendChild(intro);

  const grid = document.createElement("div");
  grid.className = "auto-rail sketch-grid";
  grid.setAttribute("aria-label", CONFIG.sketches.kicker);

  const track = document.createElement("div");
  track.className = "auto-rail-track sketch-auto-track";
  duplicateItems(state.photos).forEach((photo) => {
    const card = document.createElement("figure");
    card.className = "sketch-card";

    const button = document.createElement("button");
    button.className = "art-button";
    button.type = "button";
    button.setAttribute("aria-label", photo.caption);
    button.addEventListener("click", () => openLightboxById(photo.id, "art"));

    const img = document.createElement("img");
    img.src = photo.artSrc;
    img.alt = photo.caption;
    img.loading = "lazy";
    img.addEventListener("error", () => {
      img.src = photo.src;
      img.classList.add("is-source-fallback");
    }, { once: true });
    button.appendChild(img);

    card.appendChild(button);
    track.appendChild(card);
  });
  grid.appendChild(track);
  root.appendChild(grid);
}

function renderLetter() {
  const lines = document.querySelector("[data-letter-lines]");
  const signature = document.querySelector("[data-letter-signature]");
  if (!lines || !signature) return;

  lines.innerHTML = "";
  CONFIG.loveLetter.forEach((line) => {
    const paragraph = document.createElement("p");
    paragraph.textContent = line;
    lines.appendChild(paragraph);
  });
  signature.textContent = CONFIG.letter.signature;
}

function makePhotoButton(photo, className) {
  const button = document.createElement("button");
  button.className = className;
  button.type = "button";
  button.setAttribute("aria-label", photo.caption);
  button.addEventListener("click", () => openLightboxById(photo.id));

  const img = document.createElement("img");
  img.src = photo.src;
  img.alt = photo.caption;
  img.loading = "lazy";
  button.appendChild(img);
  return button;
}

function makeGalleryPhotoCard(photo) {
  const card = document.createElement("figure");
  card.className = "gallery-photo-card";

  const button = makePhotoButton(photo, "rail-photo");
  const caption = document.createElement("figcaption");
  caption.textContent = photo.caption;

  card.append(button, caption);
  return card;
}

function setupSmoothButtons() {
  document.querySelector("[data-enter-button]")?.addEventListener("click", () => {
    document.querySelector("#timeline")?.scrollIntoView({ behavior: "smooth" });
  });
}

function setupLightbox() {
  document.querySelector("[data-lightbox-close]")?.addEventListener("click", closeLightbox);
  document.querySelector("[data-lightbox-prev]")?.addEventListener("click", () => shiftLightbox(-1));
  document.querySelector("[data-lightbox-next]")?.addEventListener("click", () => shiftLightbox(1));

  document.querySelector("[data-lightbox]")?.addEventListener("click", (event) => {
    if (event.target.matches("[data-lightbox]")) closeLightbox();
  });

  document.addEventListener("keydown", (event) => {
    const isOpen = document.querySelector("[data-lightbox]")?.classList.contains("is-open");
    if (event.key === "Escape") closeLightbox();
    if (!isOpen) return;
    if (event.key === "ArrowLeft") shiftLightbox(-1);
    if (event.key === "ArrowRight") shiftLightbox(1);
  });
}

function openLightboxById(id, view = "photo") {
  const index = state.photos.findIndex((photo) => photo.id === id);
  if (index >= 0) openLightbox(index, view);
}

function openLightbox(index, view = state.activeLightboxView) {
  const modal = document.querySelector("[data-lightbox]");
  const img = document.querySelector("[data-lightbox-img]");
  const caption = document.querySelector("[data-lightbox-caption]");
  if (!modal || !img || !caption) return;

  const photo = state.photos[index];
  state.activePhoto = index;
  state.activeLightboxView = view;
  img.onerror = () => {
    img.onerror = null;
    if (view === "art") img.src = photo.src;
  };
  img.src = view === "art" ? photo.artSrc : photo.src;
  img.alt = photo.caption;
  caption.hidden = view === "art";
  caption.textContent = view === "art" ? "" : photo.caption;
  modal.classList.add("is-open");
  modal.setAttribute("aria-hidden", "false");
  document.body.classList.add("modal-open");
}

function shiftLightbox(direction) {
  const total = state.photos.length;
  state.activePhoto = (state.activePhoto + direction + total) % total;
  openLightbox(state.activePhoto, state.activeLightboxView);
}

function closeLightbox() {
  const modal = document.querySelector("[data-lightbox]");
  if (!modal) return;
  modal.classList.remove("is-open");
  modal.setAttribute("aria-hidden", "true");
  document.body.classList.remove("modal-open");
}

function setupMusic() {
  const button = document.querySelector("[data-music-toggle]");
  if (!button) return;

  button.addEventListener("click", async () => {
    if (state.isMusicPlaying && state.audio) {
      state.audio.pause();
      setMusicState(false);
      return;
    }

    try {
      await playRandomTrack();
    } catch (error) {
      setMusicState(false);
      button.textContent = CONFIG.music.missingLabel;
      window.alert(CONFIG.music.missingMessage);
    }
  });
}

async function playRandomTrack() {
  const tracks = (CONFIG.music.tracks || []).filter(Boolean);
  if (!tracks.length) throw new Error("No music tracks configured.");

  const nextIndex = randomTrackIndex(tracks.length);
  const nextTrack = tracks[nextIndex];
  if (state.audio) {
    state.audio.pause();
    state.audio.removeAttribute("src");
    state.audio.load();
  }

  state.currentTrackIndex = nextIndex;
  state.audio = new Audio(nextTrack);
  state.audio.preload = "none";
  state.audio.addEventListener("ended", () => {
    playRandomTrack().catch(() => setMusicState(false));
  }, { once: true });
  state.audio.addEventListener("error", () => setMusicState(false));

  await state.audio.play();
  setMusicState(true);
}

function randomTrackIndex(total) {
  if (total <= 1) return 0;
  let next = Math.floor(Math.random() * total);
  if (next === state.currentTrackIndex) next = (next + 1) % total;
  return next;
}

function setMusicState(isPlaying) {
  const button = document.querySelector("[data-music-toggle]");
  state.isMusicPlaying = isPlaying;
  if (!button) return;
  const label = isPlaying ? CONFIG.music.pauseLabel : CONFIG.music.playLabel;
  button.textContent = label;
  button.setAttribute("aria-label", label);
}

function setupReveal() {
  const items = document.querySelectorAll("[data-reveal]");
  if (!("IntersectionObserver" in window)) {
    items.forEach((item) => item.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  items.forEach((item) => observer.observe(item));
}

function byIds(ids) {
  return ids
    .map((id) => state.photos.find((photo) => photo.id === id))
    .filter(Boolean);
}

function duplicateItems(items) {
  return [...items, ...items];
}

function artCardSrc(photo, artStyle = artStyleFor(photo)) {
  const name = `photo-${String(photo.id).padStart(3, "0")}-${artStyle}.png`;
  return `${CONFIG.sketches.basePath}${name}`;
}

function artStyleFor(photo) {
  if (photo.artStyle) return photo.artStyle;
  const assigned = CONFIG.sketches.assignments?.[photo.id];
  if (assigned) return assigned;
  return ART_STYLE_SEQUENCE[(photo.id - 1) % ART_STYLE_SEQUENCE.length];
}

function text(selector, value) {
  const node = document.querySelector(selector);
  if (node) node.textContent = value;
}

function setAria(selector, value) {
  const node = document.querySelector(selector);
  if (node) node.setAttribute("aria-label", value);
}
