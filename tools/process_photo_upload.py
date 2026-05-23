#!/usr/bin/env python3
"""Process a GitHub photo-upload issue and update the static site assets."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import mimetypes
import os
import random
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "script.js"
PHOTO_ROOT = REPO_ROOT / "public" / "photos"
CARD_ROOT = REPO_ROOT / "public" / "art-cards" / "review-batch-20260521" / "accepted"

CATEGORIES = {
    "home": {
        "label": "居家日常",
        "keywords": ["home", "house", "room", "bed", "sofa", "居家", "家里", "日常", "房间", "沙发"],
    },
    "ski": {
        "label": "滑雪和雪地",
        "keywords": ["ski", "snow", "winter", "mountain", "滑雪", "雪", "雪地", "冬天", "雪山"],
    },
    "hospital": {
        "label": "生病和陪伴",
        "keywords": ["hospital", "clinic", "doctor", "nurse", "病", "医院", "门诊", "陪伴", "输液"],
    },
    "video": {
        "label": "视频里的见面",
        "keywords": ["video", "screen", "screenshot", "facetime", "zoom", "视频", "截图", "屏幕", "通话"],
    },
    "games": {
        "label": "娱乐时间",
        "keywords": ["game", "movie", "play", "switch", "娱乐", "游戏", "电影", "玩"],
    },
    "cooking": {
        "label": "美厨娘时间",
        "keywords": ["cook", "food", "meal", "kitchen", "dinner", "做饭", "吃饭", "厨房", "美食", "饭"],
    },
    "outing": {
        "label": "一起出去玩",
        "keywords": ["outing", "trip", "travel", "street", "park", "outside", "出门", "出去", "旅行", "玩", "路上"],
    },
    "moments": {
        "label": "其他小瞬间",
        "keywords": ["moment", "other", "misc", "其他", "瞬间"],
    },
}

STYLE_SEQUENCE = ["crayon", "postcard"]


@dataclass
class UploadedImage:
    url: str
    source_hash: str
    temp_path: Path
    filename_hint: str


@dataclass
class NewPhoto:
    id: int
    category: str
    file: str
    style: str
    caption: str
    issue_number: str
    source_hash: str
    source_path: Path
    card_path: Path


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    issue_body = Path(args.issue_body_file).read_text(encoding="utf-8")
    issue_number = str(args.issue_number)

    urls = extract_image_urls(issue_body)
    summary_lines = [
        "## 照片自动更新结果",
        "",
        f"- Issue: #{issue_number}",
        f"- 发现图片链接：{len(urls)} 个",
    ]

    if not urls:
        summary_lines.extend([
            "",
            "没有在 issue 正文里找到图片附件。请把照片拖到“照片附件”输入框后再提交。",
        ])
        write_summary(args.summary_file, summary_lines)
        return 0

    script_text = SCRIPT_PATH.read_text(encoding="utf-8")
    existing_hashes = set(re.findall(r'sourceHash:\s*"([^"]+)"', script_text))
    selected_category = category_from_choice(extract_issue_field(issue_body, "照片分类"))
    notes = clean_field(extract_issue_field(issue_body, "照片说明"))
    next_id = next_photo_id(script_text)

    with tempfile.TemporaryDirectory(prefix="photo-upload-") as tmp:
        tmp_dir = Path(tmp)
        uploaded = []
        for index, url in enumerate(urls, 1):
            source_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
            if source_hash in existing_hashes:
                summary_lines.append(f"- 跳过已处理图片：{source_hash}")
                continue
            try:
                uploaded.append(download_image(url, source_hash, tmp_dir, index))
            except Exception as exc:  # noqa: BLE001
                summary_lines.append(f"- 下载失败：{url} ({exc})")

        if not uploaded:
            summary_lines.extend(["", "没有新的图片需要处理。"])
            write_summary(args.summary_file, summary_lines)
            return 0

        new_photos: list[NewPhoto] = []
        for offset, item in enumerate(uploaded):
            photo_id = next_id + offset
            category, ai_caption = classify_photo(item.temp_path, item.filename_hint, notes, selected_category)
            style = STYLE_SEQUENCE[(photo_id - 1) % len(STYLE_SEQUENCE)]
            caption = caption_for_photo(category, notes, ai_caption, offset + 1, len(uploaded))
            photo_file, source_path = write_site_photo(item.temp_path, category, photo_id)
            card_path = CARD_ROOT / f"photo-{photo_id:03d}-{style}.png"
            generate_art_card(source_path, card_path, style, seed=photo_id)
            new_photos.append(
                NewPhoto(
                    id=photo_id,
                    category=category,
                    file=photo_file,
                    style=style,
                    caption=caption,
                    issue_number=issue_number,
                    source_hash=item.source_hash,
                    source_path=source_path,
                    card_path=card_path,
                )
            )

    if new_photos:
        updated = append_photos_to_script(script_text, new_photos)
        SCRIPT_PATH.write_text(updated, encoding="utf-8", newline="\n")

    summary_lines.extend([
        f"- 新增照片：{len(new_photos)} 张",
        "",
        "| ID | 分类 | 原图 | 小卡片 |",
        "|---:|---|---|---|",
    ])
    for photo in new_photos:
        summary_lines.append(
            f"| {photo.id:03d} | {CATEGORIES[photo.category]['label']} | "
            f"`public/photos/{photo.file}` | "
            f"`public/art-cards/review-batch-20260521/accepted/{photo.card_path.name}` |"
        )

    write_summary(args.summary_file, summary_lines)
    return 0


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--issue-body-file", required=True)
    parser.add_argument("--issue-number", required=True)
    parser.add_argument("--summary-file", default="photo-upload-summary.md")
    return parser.parse_args(argv)


def extract_image_urls(body: str) -> list[str]:
    markdown_urls = re.findall(r"!\[[^\]]*\]\((https?://[^)\s]+)\)", body)
    direct_urls = re.findall(r'''https?://[^\s)>\]"']+''', body)
    candidates = markdown_urls + direct_urls
    urls: list[str] = []
    seen: set[str] = set()
    for raw_url in candidates:
        url = raw_url.rstrip(".,;\"'")
        lowered = url.lower()
        looks_like_image = any(lowered.split("?")[0].endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".webp"])
        is_github_upload = "github.com/user-attachments/assets/" in lowered
        if not (looks_like_image or is_github_upload):
            continue
        if url in seen:
            continue
        seen.add(url)
        urls.append(url)
    return urls


def extract_issue_field(body: str, label: str) -> str:
    pattern = rf"###\s*{re.escape(label)}\s*\n+(.*?)(?=\n###\s|\Z)"
    match = re.search(pattern, body, flags=re.S)
    return match.group(1).strip() if match else ""


def clean_field(value: str) -> str:
    value = value.strip()
    if value in {"_No response_", "No response"}:
        return ""
    return re.sub(r"\s+", " ", value)


def category_from_choice(value: str) -> str | None:
    text = clean_field(value).lower()
    if not text or "自动识别" in text:
        return None
    for key, data in CATEGORIES.items():
        if key in text or data["label"].lower() in text:
            return key
    return None


def download_image(url: str, source_hash: str, tmp_dir: Path, index: int) -> UploadedImage:
    import requests

    headers = {"User-Agent": "photo-upload-workflow"}
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if token and "github.com/user-attachments/assets/" in url.lower():
        headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/octet-stream",
        })

    response = requests.get(url, timeout=45, headers=headers, allow_redirects=True)
    response.raise_for_status()
    content_type = response.headers.get("content-type", "").split(";")[0]
    ext = mimetypes.guess_extension(content_type) or ".jpg"
    if ext == ".jpe":
        ext = ".jpg"
    filename_hint = Path(url.split("?")[0]).name or f"upload-{index}{ext}"
    temp_path = tmp_dir / f"upload-{index:03d}{ext}"
    temp_path.write_bytes(response.content)
    return UploadedImage(url=url, source_hash=source_hash, temp_path=temp_path, filename_hint=filename_hint)


def classify_photo(image_path: Path, filename_hint: str, notes: str, selected_category: str | None) -> tuple[str, str | None]:
    if selected_category:
        return selected_category, None

    ai_result = classify_with_openai(image_path, filename_hint, notes)
    if ai_result:
        category = ai_result.get("category")
        caption = ai_result.get("caption")
        if category in CATEGORIES:
            return category, caption if isinstance(caption, str) else None

    text_category = classify_from_text(f"{filename_hint} {notes}")
    if text_category:
        return text_category, None

    stat_category = classify_from_image_stats(image_path)
    return stat_category or "moments", None


def classify_with_openai(image_path: Path, filename_hint: str, notes: str) -> dict[str, str] | None:
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_VISION_MODEL")
    if not api_key or not model:
        return None

    import requests

    mime = mimetypes.guess_type(str(image_path))[0] or "image/jpeg"
    data_url = f"data:{mime};base64,{base64.b64encode(image_path.read_bytes()).decode('ascii')}"
    category_list = ", ".join(CATEGORIES.keys())
    payload = {
        "model": model,
        "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Classify this memory photo for a Chinese personal photo website. "
                            f"Allowed categories: {category_list}. "
                            "Return compact JSON with keys category and caption. "
                            "The caption should be warm Chinese, <= 28 Chinese characters. "
                            f"Filename: {filename_hint}. Notes: {notes or 'none'}"
                        ),
                    },
                    {"type": "image_url", "image_url": {"url": data_url}},
                ],
            }
        ],
    }
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        result = json.loads(content)
        return result if isinstance(result, dict) else None
    except Exception as exc:  # noqa: BLE001
        print(f"OpenAI classification skipped after error: {exc}", file=sys.stderr)
        return None


def classify_from_text(text: str) -> str | None:
    lowered = text.lower()
    scores = {}
    for key, data in CATEGORIES.items():
        scores[key] = sum(1 for keyword in data["keywords"] if keyword.lower() in lowered)
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else None


def classify_from_image_stats(image_path: Path) -> str | None:
    from PIL import Image, ImageStat

    with Image.open(image_path) as image:
        rgb = image.convert("RGB").resize((64, 64))
    stat = ImageStat.Stat(rgb)
    brightness = sum(stat.mean) / 3
    channel_spread = max(stat.mean) - min(stat.mean)
    pixels = list(rgb.getdata())
    whiteish = sum(1 for r, g, b in pixels if r > 190 and g > 190 and b > 185) / len(pixels)

    if brightness > 160 and channel_spread < 18 and whiteish > 0.38:
        return "ski"
    return None


def caption_for_photo(category: str, notes: str, ai_caption: str | None, index: int, total: int) -> str:
    if ai_caption:
        return ai_caption.strip()
    if notes and total == 1:
        return notes[:80]
    if notes:
        return f"{notes[:56]}（第 {index} 张）"
    return f"新上传的{CATEGORIES[category]['label']}回忆。"


def next_photo_id(script_text: str) -> int:
    ids = [int(match) for match in re.findall(r"\bid:\s*(\d+)", script_text)]
    return max(ids, default=0) + 1


def write_site_photo(image_path: Path, category: str, photo_id: int) -> tuple[str, Path]:
    from PIL import Image, ImageOps

    category_dir = PHOTO_ROOT / category
    category_dir.mkdir(parents=True, exist_ok=True)
    relative_file = f"{category}/photo-{photo_id:03d}.jpg"
    target = PHOTO_ROOT / relative_file

    with Image.open(image_path) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        image.thumbnail((1800, 1800))
        image.save(target, "JPEG", quality=88, optimize=True, progressive=True)

    return relative_file, target


def generate_art_card(source_path: Path, target_path: Path, style: str, seed: int) -> None:
    from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps

    target_path.parent.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed)
    canvas_size = (1200, 1500)
    image_size = (1050, 1310) if style == "postcard" else canvas_size

    with Image.open(source_path) as source:
        source = ImageOps.exif_transpose(source).convert("RGB")
        image = cover_crop(source, image_size)

    if style == "crayon":
        image = ImageEnhance.Color(image).enhance(0.86)
        image = ImageEnhance.Contrast(image).enhance(1.08)
        poster = image.quantize(colors=42, method=Image.Quantize.MEDIANCUT).convert("RGB")
        edges = ImageOps.invert(image.convert("L").filter(ImageFilter.FIND_EDGES)).convert("RGB")
        image = Image.blend(poster, edges, 0.16)
        texture = paper_texture(canvas_size, rng, strength=24)
        image = ImageChops.multiply(image, texture)
        image = image.filter(ImageFilter.SMOOTH_MORE)
    else:
        poster = image.quantize(colors=58, method=Image.Quantize.MEDIANCUT).convert("RGB")
        poster = ImageEnhance.Color(poster).enhance(0.92)
        poster = ImageEnhance.Contrast(poster).enhance(1.04)
        canvas = Image.new("RGB", canvas_size, (255, 249, 240))
        canvas.paste(poster, ((canvas_size[0] - image_size[0]) // 2, 92))
        draw = ImageDraw.Draw(canvas)
        draw.rounded_rectangle((48, 50, 1152, 1438), radius=18, outline=(226, 214, 198), width=8)
        draw.rectangle((130, 54, 320, 94), fill=(239, 219, 207))
        draw.rectangle((882, 54, 1072, 94), fill=(239, 219, 207))
        image = ImageChops.multiply(canvas, paper_texture(canvas_size, rng, strength=18))

    image.save(target_path, "PNG", optimize=True)


def cover_crop(image, size: tuple[int, int]):
    from PIL import ImageOps

    return ImageOps.fit(image, size, method=1, centering=(0.5, 0.5))


def paper_texture(size: tuple[int, int], rng: random.Random, strength: int):
    from PIL import Image

    width, height = size
    data = []
    for _ in range(width * height):
        value = 255 - rng.randrange(strength)
        data.append((value, value, value))
    texture = Image.new("RGB", size)
    texture.putdata(data)
    return texture


def append_photos_to_script(script_text: str, photos: list[NewPhoto]) -> str:
    text = append_photo_records(script_text, photos)
    text = append_assignments(text, photos)
    text = append_scene_photo_ids(text, photos)
    return text


def append_photo_records(script_text: str, photos: list[NewPhoto]) -> str:
    marker = "\n  ],\n  sceneCategories:"
    if marker not in script_text:
        raise RuntimeError("Cannot find CONFIG.photos closing marker in script.js")

    entries = []
    for photo in photos:
        entries.append(
            "    { "
            f"id: {photo.id}, "
            f"category: {js_string(photo.category)}, "
            f"file: {js_string(photo.file)}, "
            f"style: {js_string(photo.style)}, "
            f"caption: {js_string(photo.caption)}, "
            f"sourceIssue: {js_string(photo.issue_number)}, "
            f"sourceHash: {js_string(photo.source_hash)} "
            "}"
        )

    before, after = script_text.split(marker, 1)
    if not before.rstrip().endswith(","):
        before = before.rstrip() + ","
    before += "\n" + ",\n".join(entries)
    return before + marker + after


def append_assignments(script_text: str, photos: list[NewPhoto]) -> str:
    pattern = r"(    assignments:\s*\{\n)(.*?)(\n    \}\n  \},\n  letter:)"
    match = re.search(pattern, script_text, flags=re.S)
    if not match:
        raise RuntimeError("Cannot find CONFIG.sketches.assignments in script.js")
    body = match.group(2).rstrip()
    if body and not body.endswith(","):
        body += ","
    additions = [f"      {photo.id}: {js_string(photo.style)}" for photo in photos]
    replacement = match.group(1) + body + "\n" + ",\n".join(additions) + match.group(3)
    return script_text[: match.start()] + replacement + script_text[match.end() :]


def append_scene_photo_ids(script_text: str, photos: list[NewPhoto]) -> str:
    grouped: dict[str, list[int]] = {}
    for photo in photos:
        grouped.setdefault(photo.category, []).append(photo.id)

    start = script_text.find("  sceneCategories: [")
    end = script_text.find("\n  galleryGroups:", start)
    if start == -1 or end == -1:
        raise RuntimeError("Cannot find sceneCategories block in script.js")

    scene_block = script_text[start:end]
    for category, ids in grouped.items():
        if category == "moments":
            continue
        pattern = rf'(\{{\s*key:\s*"{re.escape(category)}".*?photoIds:\s*\[)([^\]]*)(\])'
        match = re.search(pattern, scene_block, flags=re.S)
        if not match:
            continue
        existing = match.group(2).strip()
        addition = ", ".join(str(value) for value in ids)
        updated_ids = f"{existing}, {addition}" if existing else addition
        scene_block = scene_block[: match.start()] + match.group(1) + updated_ids + match.group(3) + scene_block[match.end() :]

    return script_text[:start] + scene_block + script_text[end:]


def js_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def write_summary(path: str, lines: Iterable[str]) -> None:
    Path(path).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
