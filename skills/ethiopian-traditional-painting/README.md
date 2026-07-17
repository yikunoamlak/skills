# Ethiopian Traditional Painting — README

## Overview

**Ethiopian Traditional Painting** is a skill for generating illustrations in the distinctive visual language of Ethiopian Orthodox manuscript art, church murals, and the contemporary work of artists like Etsubdink Legesse.

The output should always feel handcrafted, symbolic, narrative, and timeless — never realistic, digital, or modern.

## What This Skill Does

When activated, this skill:

1. **Analyzes** the user's subject and determines the appropriate composition type
2. **Constructs** a complete AI image generation prompt following the Ethiopian painting visual language
3. **Validates** the prompt against a 10-point quality checklist
4. **Delivers** a ready-to-use prompt for any AI image generator (Midjourney, DALL-E, Stable Diffusion, Flux, etc.)

## When to Use This Skill

Trigger this skill whenever the user wants:

- Any image in **Ethiopian painting style**
- Illustrations inspired by **Ethiopian Orthodox manuscript art**
- Art that looks like **Etsubdink Legesse** or similar artists
- **Habesha art** or **Ethiopian cultural illustration**
- **Ethiopian portrait**, **Ethiopian scene**, or **Ethiopian narrative**
- **African manuscript** style or **Ethiopian folk art**
- Any request mentioning "Ethiopian painting", "Ethiopian art", "Ge'ez art", or "Ethiopian mural"

### Specific Triggers

- "Ethiopian painting"
- "Ethiopian art style"
- "Ethiopian manuscript"
- "Habesha art"
- "Ethiopian illustration"
- "Ethiopian icon"
- "Ethiopian mural"
- "Ge'ez art"
- "Ethiopian Orthodox art"
- "Etsubdink Legesse style"
- "African manuscript"
- "Ethiopian portrait"
- "Ethiopian scene"
- "flat Ethiopian style"
- "Ethiopian folk art"
- "Ethiopian decorative art"
- "traditional African painting"
- "Ethiopian cultural illustration"

## How It Works

### Style System

The skill encodes the complete visual language of Ethiopian painting:

| Element | Rule |
|---|---|
| **Composition** | Flat 2D, no perspective, no depth |
| **Outlines** | Bold black, consistent weight |
| **Colors** | Flat, unshaded, warm earth tones only |
| **Eyes** | Large almond-shaped, dominant feature |
| **Skin** | Warm brown tones |
| **Garments** | Traditional Ethiopian with geometric patterns |
| **Background** | Warm ivory/cream, simple and symbolic |
| **Borders** | Red/terracotta geometric decorative frames |
| **Text** | Ge'ez/Amharic as decorative elements |

### Color Palette (Strict)

| Color | Hex | Usage |
|---|---|---|
| Warm Ivory | #F5E6C8 | Backgrounds |
| Deep Red | #8B1A1A | Borders, accents |
| Terracotta | #C65D3B | Architecture, borders |
| Golden Ochre | #D4A017 | Royalty, halos |
| Forest Green | #2D5A27 | Nature, textiles |
| Warm Brown | #6B3A2A | Skin, earth |
| Muted Blue | #3A5A7C | Sparingly |
| Black | #1A1A1A | Outlines, hair |
| White | #FFFFFF | Garments only |

### Prompt Construction

Every prompt follows a layered structure:

1. **Subject** — What is being depicted
2. **Style** — "traditional Ethiopian painting style"
3. **Technical** — "flat 2D, bold outlines, flat colors"
4. **Figure** — "almond eyes, warm brown skin"
5. **Garment** — "habesha kemis with patterned border"
6. **Background** — "warm ivory background"
7. **Border** — "geometric terracotta border"
8. **Details** — "Ge'ez text, Ethiopian crosses"

## Directory Structure

```
ethiopian-traditional-painting/
├── SKILL.md                              # Main skill file
├── README.md                             # This file
├── assets/
│   └── reference-etsubdink-legesse.png   # Reference image
├── evals/
│   └── evals.json                        # Test evaluation prompts
└── references/
    ├── style-analysis.md                 # Etsubdink Legesse visual language breakdown
    ├── color-system.md                   # Complete palette with hex values
    ├── composition-guide.md              # Panel layouts and figure arrangement
    ├── subject-catalog.md                # How to render specific objects
    └── prompt-engineering.md             # Prompt construction techniques
```

## References Used

- **Etsubdink Legesse** — Contemporary Ethiopian artist working in manuscript tradition
- **Ethiopian Orthodox church murals** — Gondarene period narrative paintings
- **Ge'ez illuminated manuscripts** — Medieval biblical texts with illustrations
- **Reference image**: `assets/reference-etsubdink-legesse.png` — curated collection of Legesse's work

## Core Philosophy

Ethiopian painting is not "primitive" or "naive" — it is a sophisticated visual language that prioritizes **narrative clarity** over **realistic representation**. Every element serves the story. The flat composition, bold outlines, and symbolic colors are deliberate choices that have been refined over a millennium.

> *"The painting tells a story, it does not simulate a window."*

## Integration Notes

This skill works with any AI image generator:

| Platform | Optimization |
|---|---|
| **Midjourney** | Append `--ar 1:1 --s 250 --q 2` |
| **DALL-E / ChatGPT** | Use prompt as-is |
| **Stable Diffusion** | Add negative: "photorealistic, 3D, gradients, anime, comic" |
| **Flux** | Use prompt as-is, square format |
| **Ideogram** | Use prompt as-is |

## Example Usage

**User:** "Generate an image of an Ethiopian coffee farmer"

**Skill produces:**
```
An Ethiopian coffee farmer holding freshly picked coffee cherries, traditional Ethiopian painting style, inspired by Ethiopian Orthodox manuscript art and Etsubdink Legesse, flat 2D composition, bold black outlines, vibrant flat unshaded colors, large almond-shaped expressive eyes, warm brown skin tones, wearing traditional white habesha kemis with colorful patterned shawl, warm ivory background, single stylized coffee tree behind, geometric ornamental red border, handcrafted Ethiopian painting aesthetic.
```

## License

This skill is for creating art in the Ethiopian traditional painting style. It respects and honors the cultural heritage of Ethiopian manuscript illumination and church art.

---

*Skill version: 1.0 | Based on analysis of Etsubdink Legesse's work | Reference: assets/reference-etsubdink-legesse.png*
