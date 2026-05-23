#!/usr/bin/env python3
"""Process a GitHub photo-upload issue and update the static site assets."""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import re
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

UPLOADED_CARD_STYLE = "uploaded"


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

    photo_urls = extract_image_urls(extract_issue_field(issue_body, "原照片附件"))
    card_urls = extract_image_urls(extract_issue_field(issue_body, "卡通小卡片附件"))
    if not photo_urls and not card_urls:
        photo_urls = extract_image_urls(extract_issue_field(issue_body, "照片附件"))
    summary_lines = [
        "## 照片自动更新结果",
        "",
        f"- Issue: #{issue_number}",
        f"- 发现原照片：{len(photo_urls)} 张",
        f"- 发现卡通小卡片：{len(card_urls)} 张",
    ]

    if not photo_urls:
        summary_lines.extend([
            "",
            "没有在 issue 正文里找到原照片附件。请把照片拖到“原照片附件”输入框后再提交。",
        ])
        write_summary(args.summary_file, summary_lines)
        return 0
    if not card_urls:
        summary_lines.extend([
            "",
            "没有在 issue 正文里找到卡通小卡片附件。请把已经生成好的小卡片拖到“卡通小卡片附件”输入框后再提交。",
        ])
        write_summary(args.summary_file, summary_lines)
        return 1
    if len(photo_urls) != len(card_urls):
        summary_lines.extend([
            "",
            "原照片和卡通小卡片数量不一致，网页没有更新。",
            "请确认第 1 张小卡片对应第 1 张原照片，第 2 张对应第 2 张，以此类推。",
        ])
        write_summary(args.summary_file, summary_lines)
        return 1

    script_text = SCRIPT_PATH.read_text(encoding="utf-8")
    existing_hashes = set(re.findall(r'sourceHash:\s*"([^"]+)"', script_text))
    selected_category = category_from_choice(extract_issue_field(issue_body, "照片分类"))
    notes = clean_field(extract_issue_field(issue_body, "照片说明"))
    next_id = next_photo_id(script_text)

    with tempfile.TemporaryDirectory(prefix="photo-upload-") as tmp:
        tmp_dir = Path(tmp)
        uploaded: list[tuple[UploadedImage, UploadedImage]] = []
        download_failures = 0
        for index, (photo_url, card_url) in enumerate(zip(photo_urls, card_urls), 1):
            source_hash = hashlib.sha1(photo_url.encode("utf-8")).hexdigest()[:12]
            if source_hash in existing_hashes:
                summary_lines.append(f"- 跳过已处理照片：{source_hash}")
                continue
            try:
                photo_item = download_image(photo_url, source_hash, tmp_dir, index, "photo")
                card_hash = hashlib.sha1(card_url.encode("utf-8")).hexdigest()[:12]
                card_item = download_image(card_url, card_hash, tmp_dir, index, "card")
                uploaded.append((photo_item, card_item))
            except Exception as exc:  # noqa: BLE001
                download_failures += 1
                summary_lines.append(f"- 第 {index} 组附件下载失败：{exc}")

        if not uploaded:
            if download_failures:
                summary_lines.extend(["", "所有图片都下载失败，网页没有更新。请检查附件链接或重新触发流程。"])
            else:
                summary_lines.extend(["", "没有新的图片需要处理。"])
            write_summary(args.summary_file, summary_lines)
            return 1 if download_failures else 0

        new_photos: list[NewPhoto] = []
        for offset, (photo_item, card_item) in enumerate(uploaded):
            photo_id = next_id + offset
            category = classify_photo(photo_item.temp_path, photo_item.filename_hint, notes, selected_category)
            style = UPLOADED_CARD_STYLE
            caption = caption_for_photo(category, notes, offset + 1, len(uploaded))
            photo_file, source_path = write_site_photo(photo_item.temp_path, category, photo_id)
            card_path = CARD_ROOT / f"photo-{photo_id:03d}-{style}.png"
            write_uploaded_card(card_item.temp_path, card_path)
            new_photos.append(
                NewPhoto(
                    id=photo_id,
                    category=category,
                    file=photo_file,
                    style=style,
                    caption=caption,
                    issue_number=issue_number,
                    source_hash=photo_item.source_hash,
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


def download_image(url: str, source_hash: str, tmp_dir: Path, index: int, kind: str) -> UploadedImage:
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
    temp_path = tmp_dir / f"{kind}-{index:03d}{ext}"
    temp_path.write_bytes(response.content)
    return UploadedImage(url=url, source_hash=source_hash, temp_path=temp_path, filename_hint=filename_hint)


def classify_photo(image_path: Path, filename_hint: str, notes: str, selected_category: str | None) -> str:
    if selected_category:
        return selected_category

    text_category = classify_from_text(f"{filename_hint} {notes}")
    if text_category:
        return text_category

    stat_category = classify_from_image_stats(image_path)
    return stat_category or "moments"


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


def caption_for_photo(category: str, notes: str, index: int, total: int) -> str:
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


def write_uploaded_card(image_path: Path, target_path: Path) -> None:
    from PIL import Image, ImageOps

    target_path.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(image_path) as image:
        image = ImageOps.exif_transpose(image)
        if image.mode not in {"RGB", "RGBA"}:
            image = image.convert("RGBA")
        image.thumbnail((1800, 1800))
        image.save(target_path, "PNG", optimize=True)


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
