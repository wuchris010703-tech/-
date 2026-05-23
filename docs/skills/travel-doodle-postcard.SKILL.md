---
name: travel-doodle-postcard
description: Transform real photos into humorous cute hand-drawn travel diary comic postcards. Use when the user asks to turn an input photo into a doodle postcard, travel journal comic, humorous hand-drawn postcard, rough ink plus colored-pencil style, or wants handwritten notes, speech bubbles, arrows, funny side comments, and tiny anthropomorphic details added while preserving the original photo composition and subjects.
---

# Travel Doodle Postcard

Create image-model edits that keep the original photo recognizable while turning it into a playful travel diary doodle comic postcard.

## Workflow

1. Identify the target photo and the important things to preserve: people, pose, composition, setting, background objects, and overall aspect ratio.
2. Use the `imagegen` skill and the built-in image generation/editing tool. If the UI exposes a model choice, prefer the current image2/gpt-image-2 path. Do not replace model generation with only a local filter when the user asks for this style.
3. Preserve the source structure:
   - Keep the same main subjects, camera angle, and framing.
   - Keep distinctive background objects when they are visible.
   - Keep people recognizable, but allow simplified hand-drawn facial features.
4. Add only a small number of doodle elements so the image stays clean:
   - 2-4 handwritten annotations
   - 1-2 speech bubbles or thought bubbles
   - 1-3 arrows
   - 1-2 tiny anthropomorphic object details
5. Keep annotation text short, legible, casual, and context-specific. Prefer Chinese if the source project or user request is Chinese.
6. Avoid turning the image into a childish cartoon. The target look is warm, humorous, handmade, and postcard-like.
7. Save project-bound outputs into the active project with a clear filename such as `photo-025-doodle-postcard.png`. Inspect the result before wiring it into a webpage.

## Prompt Template

Use this as the base prompt:

```text
Edit the provided photo into a humorous, cute hand-drawn comic postcard in the style of a travel diary doodle.
Preserve the original composition, aspect ratio, main subjects, pose, camera angle, setting, and important background objects.
Transform the actual image into rough ink-line illustration with colored-pencil shading, pastel colors, visible paper texture, slightly uneven handmade outlines, and playful sketchbook energy.
Add only a small amount of handwritten Chinese annotations, speech bubbles, arrows, funny side comments, and tiny anthropomorphic details, integrated naturally like a travel journal page.
Keep the main people recognizable and charming, not childish.
No watermark, no UI, no heavy decorative border, no unrelated new objects.
```

Then add scene-specific notes.

## Scene Notes

For pool, beach, spa, or water photos:

```text
Keep the waterline, wet hair or water reflections, pool background, and playful vacation feeling. Possible tiny notes: “泡泡熊出没”, “水里也要自拍”, “今日快乐值+1”. Add one small sleepy face to a bottle, float, or background object if present.
```

For street, travel, hotel, airport, or outdoor photos:

```text
Keep the original location cues, road signs, buildings, bags, outfits, and travel framing. Possible notes: “出门小坐标”, “今日路线：快乐”, “走走停停也很好”. Add tiny arrows to snacks, signs, tickets, or bags.
```

For snow or ski photos:

```text
Keep the helmets, goggles, jackets, snow, mountain background, and selfie framing. Possible notes: “雪地勇士”, “coach上线”, “摔倒也可爱”. Add tiny doodle sparkles, motion arrows, or a sleepy face on a helmet sticker.
```

For home, food, cooking, or cafe photos:

```text
Keep the food, cookware, table objects, laptop, kitchen or cafe setting, and casual everyday feeling. Possible notes: “美厨娘到”, “今日好吃”, “开饭啦”. Add tiny faces to cups, bowls, bottles, or pans.
```

## Text Rules

- Keep each note under 8 Chinese characters when possible.
- Use 2-4 notes total unless the user asks for more.
- Use handwriting-like annotations, not large poster typography.
- If text quality is likely to fail, ask for text-free doodle marks or keep text very short.

## Quality Checks

Reject or retry if:

- The people are no longer recognizable.
- The prompt adds many unrelated objects.
- The annotations cover faces.
- The style becomes anime, mascot cartoon, flat vector, or photorealistic filter.
- Text dominates the image instead of feeling like small travel-diary notes.
