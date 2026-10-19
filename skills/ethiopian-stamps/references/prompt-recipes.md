# Prompt Recipes

Model settings, ready-made prompts, and repair strategies for stamp generation.

## Model Notes

The PixVerse CLI default image model is `gpt-image-2.5-flare`. For stamp work,
pick a model by its text strength:

| Model | Also called | Strengths | Watch out for |
|---|---|---|---|
| `gemini-3.1-flash` | Nano Banana 2 | Best layout and text-in-image, follows long prompts, good frames | May invent Glyphs in Amharic; verify every glyph |
| `gemini-3.0` | Nano Banana Pro | Highest detail, complex scenes, 2160p | Slower, more expensive; same Amharic caveat |
| `gpt-image-2.5-flare` | — | Crisp Latin typography, strong instruction following | Can look too clean; add paper and print cues |
| `gpt-image-2.5-sunburst` | — | Alternate GPT image style, good illustration | Check availability in your CLI version |
| `seedream-5.0-pro` | — | Painterly illustration, rich colour | Weak text; generate art only, compose type in post |
| `qwen-image` | — | Flat graphic and vector looks | Weak text; good for modern stamps |

There is no `nano-banana-2.5` model in PixVerse 1.4.6. The newest Nano Banana is
`gemini-3.1-flash` (Nano Banana 2). `gemini-3.0` is Nano Banana Pro. If the user
asks for "Nano Banana 2.5", use `gemini-3.1-flash` and say why.

## PixVerse CLI

Write prompts that contain Amharic to a UTF-8 text file, then pass the file path
to `--prompt`. This avoids shell encoding problems.

```powershell
# Generate
pixverse create image `
  --prompt 'C:\path\to\prompt.txt' `
  --model gemini-3.1-flash `
  --quality 1440p `
  --aspect-ratio 2:3 `
  --count 1 `
  --idempotency-key eth-stamp-my-subject-01 `
  --timeout 300 `
  --json

# Download the result
pixverse asset download <image_id> --type image --json
```

Useful flags: `--count 2` or `3` for variants, `--seed` for repeatability,
`--detail-level high` or `xhigh` for GPT Image models. Check the installed
version with `pixverse --version` and the model list with
`pixverse capabilities create image --json`.

Cost discipline: generate one variant, inspect at full size, then generate more
only if the frame, perforation, and text are close. Every rejected image still
costs credits.

## Text Strategy

1. Use four strings at most: country (Amharic), country (Latin), denomination,
   year.
2. Quote each string exactly in the prompt: `"ኢትዮጵያ"`, `"ETHIOPIA"`, `"5 ብር"`,
   `"2026"`.
3. Keep Amharic short. Long phrases are the first thing to break.
4. Check every glyph. If the Amharic is wrong, move on instead of accepting it.
5. Repair options, in order: regenerate with fewer words; regenerate with English
   only and add Amharic in post; crop the vignette and rebuild the frame with a
   real font such as Noto Serif Ethiopic or Abyssinica SIL.
6. Never publish a stamp with invented Amharic. It reads as fake to any Amharic
   speaker.

## Base Prompt Template

```
A single [vertical / horizontal] Ethiopian postage stamp, [ERA] style, cropped
flush to its perforated edges so the stamp fills the entire frame — nothing
exists outside the perforation. The stamp has a fine inner frame. Top band:
"ኢትዮጵያ". Bottom band: "ETHIOPIA". Denomination "[VALUE] ብር" at lower left.
Year "[YEAR]" at lower right. Central vignette: [SUBJECT]. [PRINTING LANGUAGE
AND PALETTE]. [PAPER AND CANCELLATION]. No background, no border rule, no
shadow, no caption, no glossy 3D, no modern poster, no extra text, no gibberish
lettering.
```

## Era Recipes

### 1894 First Issue

```
A single vertical Ethiopian postage stamp in the style of the 1894 Menelik II
first issue, cropped flush to its perforated edges so the stamp fills the frame.
A fine engraved frame with an ornate acanthus border on the stamp's own cream
paper. Top: "ኢትዮጵያ" in Ge'ez script. Bottom:
"ETHIOPIA". Denomination "4 G" in a small circle at the bottom. Central vignette:
[SUBJECT], rendered in intaglio engraving with fine cross-hatching and flat
indigo, oxblood, and ochre ink. A faint circular cancellation
"ADDIS ABABA" in one corner. No background, no border rule, no shadow, no
caption, no glossy 3D, no modern poster, no extra text, no gibberish lettering.
```

### 1909-1935 Overprint

```
A single vertical Ethiopian postage stamp in the 1920s style, cropped flush to
its perforated edges so the stamp fills the frame. Cream stamp paper,
perforation 14, fine frame. Top band: "POSTES ETHIOPIENNES". Bottom: "ETHIOPIE".
Denomination "2 G" at lower left, year at lower right. Central vignette:
[SUBJECT] in four-colour lithography with soft halftone and slight
misregistration, French blue, carmine, olive, and sepia. A diagonal overprint
"PAR AVION" or a commemorative surcharge across the lower third. No background,
no border rule, no shadow, no caption, no glossy 3D, no modern poster, no extra
text, no gibberish lettering.
```

### 1941-1974 Commemorative

```
A single horizontal Ethiopian postage stamp in the 1949 commemorative style,
cropped flush to its perforated edges so the stamp fills the frame. Cream stamp
paper, perforation 14. Top left: "ኢትዮጵያ", top right: "PAR AVION". Bottom:
"ETHIOPIA". Denomination "15 c" at lower right, year at lower left. Central
vignette: [SUBJECT]. On the left, a globe and cherub motif; on the right, an oval
portrait medallion. Four-colour lithography, emerald, vermilion, mustard, and
sky blue, delicate gold border. No background, no border rule, no shadow, no
caption, no glossy 3D, no modern poster, no extra text, no gibberish lettering.
```

### Derg Era

```
A single vertical Ethiopian postage stamp in the 1970s Derg style, cropped flush
to its perforated edges so the stamp fills the frame. Cream stamp paper,
perforation 14. Top: "ኢትዮጵያ" in bold Ge'ez. Bottom band: "ETHIOPIA" in yellow
on green. Denomination "60 c" in a corner. Central vignette: [SUBJECT] rendered
as a flat bold poster in red, yellow, green, and black, strong diagonal
composition, heroic silhouette, no imperial symbols. An Amharic slogan band
above the bottom. No background, no border rule, no shadow, no caption, no
glossy 3D, no modern poster, no extra text, no gibberish lettering.
```

### Contemporary

```
A single vertical Ethiopian postage stamp, contemporary Ethiopost style, cropped
flush to its perforated edges so the stamp fills the frame. Cream stamp paper,
perforation 14, clean geometric frame. Top band: "ኢትዮጵያ". Bottom:
"ETHIOPIA". Denomination "20 ብር" at lower left, "2026" at lower right. Central
vignette: [SUBJECT] in flat offset-print illustration, terracotta, teal, saffron,
and forest green, generous negative space, crisp bilingual typography, one gold
accent. No background, no border rule, no shadow, no caption, no glossy 3D, no
modern poster, no extra text, no gibberish lettering.
```

## Negative Prompt

```
glossy 3D, plastic texture, modern poster layout, rounded corners, background
paper around the stamp, linen texture, border rule, drop shadow, caption,
presentation card, mockup, extra text, gibberish lettering, missing perforations,
double stamp, sheet edges, watermark, signature, camera, photograph, neon
colours, pastel gradient, oversized text, collage
```

## Ready-Made Prompts

### Cat Emperor (1894 engraved)

```
A single Ethiopian postage stamp in vertical 2:3 format, cropped flush to its
perforated edges so the stamp fills the entire frame. Nothing exists outside the
perforation: no background paper, no linen texture, no border rule, no shadow,
no caption. The stamp has authentic perforated edges, cream paper, and a fine
engraved frame. At the top, the Amharic
word "ኢትዮጵያ" in elegant Ge'ez script. At the bottom, "ETHIOPIA" in spaced serif
capitals, with "5 ብር" in the lower left and "2026" in the lower right. The central
vignette is a regal orange tabby cat wearing a miniature gold imperial crown,
seated on a crimson velvet cushion and holding a tiny Lion of Judah flag. Render
it in the style of an 1894 Ethiopian engraved stamp: fine cross-hatching, flat ink
colours, ornate foliage border, imperial gold, deep blue, crimson, and cream. A
circular black cancellation mark in one corner reads "ADDIS ABABA". Collectible,
dignified, gently humorous. No background, no border, no shadow, no caption, no
glossy 3D, no modern poster, no extra text, no gibberish lettering.
```

### Coffee Ceremony 2.0 (1960s commemorative)

```
A single Ethiopian postage stamp in vertical 2:3 format, cropped flush to its
perforated edges so the stamp fills the entire frame. Nothing exists outside the
perforation: no background paper, no linen texture, no border rule, no shadow,
no caption. The stamp has authentic perforated edges, cream paper, and a fine
engraved frame. At the top, the Amharic
word "ኢትዮጵያ" in elegant Ge'ez script. At the bottom, "ETHIOPIA" in spaced serif
capitals, with "10 ብር" in the lower left and "2026" in the lower right. The
central vignette is a friendly vintage brass robot pouring coffee from a
traditional black clay jebena into a small white cup at an Ethiopian coffee
ceremony. A woman in a white habesha kemis with a colourful tilet border sits
nearby, incense smoke curls from a rekbot, and a woven mesob stands in the
background. Render it in the style of a 1960s Ethiopian commemorative stamp:
four-colour lithography, fine linework, slightly muted emerald green, ochre,
crimson, and cream, with delicate gold accents. Dignified, warm, gently humorous.
No background, no border, no shadow, no caption, no
glossy 3D, no modern poster, no extra text, no gibberish lettering.
```

### Remote Work, Simien Mountains (1970s commemorative)

```
A single Ethiopian postage stamp in vertical 2:3 format, cropped flush to its
perforated edges so the stamp fills the entire frame. Nothing exists outside the
perforation: no background paper, no linen texture, no border rule, no shadow,
no caption. The stamp has authentic perforated edges, cream paper, and a fine
engraved frame. At the top, the Amharic
word "ኢትዮጵያ" in elegant Ge'ez script. At the bottom, "ETHIOPIA" in spaced serif
capitals, with "20 ብር" in the lower left and "2026" in the lower right. The
central vignette is a gelada baboon with a laptop and headphones sitting on a
cliff in the Simien Mountains, a small coffee cup beside it, a walia ibex on a
distant ridge, and a faint outline map of Ethiopia in the sky. Render it in the
style of a 1970s Ethiopian commemorative stamp: flat saturated lithographic
colours, red, yellow, green, deep blue, and cream, fine engraved lines, a bold but
orderly border. Dignified, modern, gently humorous, like a serious national stamp
that happens to show a remote worker. No background, no border, no shadow, no
caption, no glossy 3D, no modern poster, no extra
text, no gibberish lettering.
```

### Injera, National Treasure (contemporary)

```
A single Ethiopian postage stamp in vertical 2:3 format, cropped flush to its
perforated edges so the stamp fills the entire frame. Nothing exists outside the
perforation: no background paper, no linen texture, no border rule, no shadow,
no caption. The stamp has authentic perforated edges, cream paper, and a fine
engraved frame. At the top, the Amharic
word "ኢትዮጵያ" in elegant Ge'ez script. At the bottom, "ETHIOPIA" in spaced serif
capitals, with "50 ብር" in the lower left and "2026" in the lower right. The
central vignette is a giant round injera on a woven mesob, displayed like a
national treasure in a museum spotlight, with a small golden crown hovering above
it, velvet ropes, and tiny bowls of berbere, honey wine, and coffee around the
base. A hand reaches in from the side to tear a piece of injera. Render it in the
style of a modern Ethiopian commemorative stamp: flat vector-like illustration,
warm earth tones, ochre, teal, crimson, and cream, crisp geometric border, subtle
gold foil accents. Playful, proud, gently humorous. No background, no border, no
shadow, no caption, no glossy 3D, no modern
poster, no extra text, no gibberish lettering.
```

## Other Platforms

| Platform | Settings and notes |
|---|---|
| Midjourney | `--ar 2:3 --style raw --s 150`. Add `--no glossy, 3d, plastic, background, border, shadow`. Ask for the stamp cropped flush to its perforated edges |
| DALL-E / ChatGPT | Use the prompt as written. Ask for a single image, not a sheet |
| Flux | Use the base template. Add `intaglio engraving` or `offset print` to control the look |
| Ideogram | Strong with text. Put all four strings in quotes and keep them short |
| Stable Diffusion | Use the negative prompt. Add `engraved lines, flat ink, cream paper` to the positive |

## Post-Processing

Use post-processing when the vignette is good but the typography is wrong.

- **Rebuild the frame.** Crop the vignette, then place it inside a vector frame
  with correct Amharic and Latin type. Free tools: Inkscape, Affinity Designer,
  Figma, Canva. Fonts: Noto Serif Ethiopic or Abyssinica SIL for Amharic.
- **Export the final size.** `scripts/export_stamp.py` scales a stamp image to a
  posting size (1440 x 2160 for 2:3). It adds nothing outside the perforated
  edges: no background, border, shadow, or caption, and it never crops the teeth.
- **Add a cancellation.** Draw a circle, a town name, and a date, then place it
  off-centre at 70 to 85 per cent opacity. Keep it away from the face.
- **Check the result.** Open the final image at 100 per cent and read every
  string aloud. If a glyph is wrong, fix it before publishing.
