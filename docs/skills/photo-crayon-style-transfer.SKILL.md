---
name: photo-crayon-style-transfer
description: Transform real camera photos into warm hand-drawn crayon, colored-pencil, or paper-grain memory-card images while preserving identity, composition, and setting. Use when the user asks to convert a real photo into the same look as a crayon-style reference, make photo-based couple memory cards, or requests image-model style transfer from a real photo.
---

# Photo Crayon Style Transfer

Create image-model edits that preserve a real photo's people, setting, and composition while turning it into a handmade crayon or colored-pencil memory-card illustration. Not for unrelated character generation, vector redraws, UI mockups, or local filter effects.

## Input Contract

Identify image roles before generation:

- **Edit target:** the real camera photo to transform. Required.
- **Style reference:** optional crayon, colored-pencil, or paper-grain example.
- **Supporting reference:** optional context image; never replace the target composition.

If the target or style reference is a local file and is not already visible, inspect it with `view_image` first. Ask only when the target is ambiguous.

## Workflow

1. Confirm this is a style-transfer edit of a real photo. If no real photo is provided, use the general `imagegen` workflow instead. Add text, stickers, borders, extra people, or new objects only when explicitly requested.
2. Choose the style source.
   - Use the user's provided stylized image when available.
   - If no reference is provided and the task matches the 熊熊家 memory-page style, use `assets/crayon-cooking-reference.png`.
   - If no visual reference applies, use the textual style recipe below and retry phrases from `references/style-prompts.md`.
3. Use the `imagegen` skill and built-in image generation/editing tool for model-native style transfer. Prefer the built-in path and current image2/gpt-image-2 path if exposed. Do not substitute PIL filters, SVG traces, CSS/canvas, or local-only effects.
4. Preserve source invariants: same people, pose, face direction, clothing, equipment, important objects, background, camera framing, and aspect ratio unless the user asks for a crop. No invented props, labels, UI, watermark, or decorative border unless requested.
5. Prompt for a sophisticated handmade look: visible crayon or colored-pencil strokes, warm paper texture, uneven outlines, layered waxy marks, recognizable simplified faces, cozy album-card feeling, cute but not childish.
6. Save project-bound outputs into the current project. Built-in generation may first save to the runtime's generated-images directory; move or copy the final output into the project for code, webpage, or document use. Do not rely on a destination-path argument or overwrite existing assets unless requested.
7. Inspect identity, composition, background, aspect ratio, style strength, and avoid-list violations. If too photographic or drifted, run one targeted retry using `references/style-prompts.md`. Keep the better result and report the retained project-local path.

## Prompt Template

Use this structure and fill in concrete photo details:

```text
Use case: style-transfer
Asset type: <project asset / preview / memory card>
Input images: Image 1 is the edit target photo; Image 2 is the style reference.
Primary request: Edit the target photo using the crayon-style reference.
Preserve: composition, aspect ratio, people, facial direction, pose, clothing, important objects, background, and scene layout.
Style/medium: warm handmade crayon and colored-pencil illustration with paper grain, waxy strokes, uneven outlines, gentle warm color, simplified but recognizable faces, and cozy personal memory-card feeling.
Avoid: text, watermark, border, UI, stickers, extra people, new objects, anime, mascot style, flat vector, photorealistic filter, oil painting, thick black comic outlines.
```

If there is no visual style reference, change the input line:

```text
Input images: Image 1 is the edit target photo. No visual style reference is provided; use the warm crayon memory-card style described below.
```

For snow/outdoor photos, add: keep the snowy landscape, sky, helmets, goggles, jackets, original selfie framing, and bright winter atmosphere recognizable.

For cooking/home photos, add: keep the kitchen/home setting, cookware, food, laptop or table objects, original selfie angle, and warm everyday atmosphere recognizable.

## Retry Guidance

Use one targeted retry, not a broad rewrite:

- Too photographic: add "stronger visible crayon wax texture", "colored-pencil crosshatching on shadows", "handmade paper grain across the whole image", and "soft uneven graphite outlines".
- Identity drift: add "simplified illustrated facial features while preserving identity", "keep both people in the same positions", and concrete clothing/background details.
- Scene drift: name the exact setting and objects that must remain.

After one focused retry, choose the better output and briefly note any limitation.

## Output Naming

Prefer:

- `public/art-cards/<category>/photo-###-crayon-model.png` for webpage assets.
- `public/illustrations/<short-name>-crayon-model.png` for standalone illustrations.
- `<source-stem>-crayon-model-v2.png` when preserving an existing generated file.

Update consuming HTML/CSS/JS only after inspection and after the final project-local asset path is known.
