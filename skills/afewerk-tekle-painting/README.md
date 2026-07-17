# Afewerk Tekle Painting Style — README

## Overview

**Afewerk Tekle Painting Style** is a skill for generating illustrations in the monumental, luminous oil painting style of Afewerk Tekle (1932–2012), Ethiopia's most celebrated modern artist and the first African to win the Triennale d'Arte in Rome.

The output captures his unique fusion of classical Western realism, dramatic chiaroscuro, and stained-glass cubism with Ethiopian cultural motifs, textiles, and subjects.

## What This Skill Does

When activated, this skill:

1. **Analyzes** the user's subject and determines the composition approach
2. **Chooses a path** — Classical Realism, Stained-Glass Cubism, or Combined
3. **Constructs** a complete AI image generation prompt following Tekle's visual language
4. **Validates** against a 14-point quality checklist
5. **Delivers** a ready-to-use prompt for any AI image generator

## When to Use This Skill

Trigger this skill whenever the user wants:

- Any image in **Afewerk Tekle's style**
- **Monumental, luminous oil painting** of Ethiopian subjects
- **Heroic portraiture** with dignity and gravitas
- **Stained-glass cubism** Ethiopian art
- **Ethiopian fine art** or **Ethiopian classical painting**
- **Jewel-toned, chiaroscuro** painting of Ethiopian subjects
- **Allegorical** Ethiopian scenes
- **Ethiopian mural** or **monumental painting**

### Specific Triggers

- "Afewerk Tekle"
- "Afewerk style"
- "Ethiopian oil painting"
- "monumental Ethiopian art"
- "stained glass Ethiopian"
- "Ethiopian cubism"
- "heroic Ethiopian portrait"
- "Ethiopian classical art"
- "luminous Ethiopian painting"
- "jewel-toned Ethiopian art"
- "Ethiopian fine art"
- "Addis Ababa school"
- "Ethiopian modernism"
- "chiaroscuro Ethiopian"
- "monumental painting style"

## How It Works

### Two Paths, One Voice

Tekle's style oscillates between two approaches:

| Path | Characteristics |
|---|---|
| **Classical Realism** | Smooth oil painting, volumetric forms, dramatic chiaroscuro, monumental figures |
| **Stained-Glass Cubism** | Same classical forms fractured by intersecting dark geometric lines, creating a stained-glass effect |

Both paths maintain his signature luminosity, dignity, and Ethiopian identity.

### Style System

| Element | Rule |
|---|---|
| **Medium** | Oil painting with visible brushwork |
| **Composition** | Monumental, heroic framing |
| **Figures** | Graceful elongated necks, statuesque posture |
| **Eyes** | Large, soulful, deeply expressive |
| **Skin** | Rich warm tones (golden, bronze, mahogany) |
| **Garments** | Luminous white with colorful tilet borders |
| **Lighting** | Dramatic chiaroscuro |
| **Colors** | Saturated jewel tones |
| **Texture** | Visible oil painting brushwork, canvas texture |

### Color Palette (Jewel-Toned)

| Color | Hex | Usage |
|---|---|---|
| Titanium White | #F8F4E8 | Luminous garments, highlights |
| Deep Emerald | #1B5E20 | Garments, backgrounds |
| Rich Crimson | #8B0000 | Shawls, curtains, borders |
| Majestic Gold | #D4A017 | Tilet borders, crowns, halos |
| Sapphire Blue | #1A3A6B | Garments, stained glass |
| Warm Bronze | #8B6914 | Skin highlights |
| Deep Mahogany | #3E1A00 | Skin shadows, hair |
| Royal Purple | #4A0E4E | Ceremonial (sparingly) |

## Directory Structure

```
afewerk-tekle-painting/
├── SKILL.md                              # Main skill file
├── README.md                             # This file
├── assets/
│   ├── reference-afewerk-tekle-composite.jpg  # 9 paintings composite
│   └── reference-afewerk-pinterest.jpg        # Pinterest board (24 works)
├── evals/
│   └── evals.json                        # 8 test prompts
└── references/
    ├── style-analysis.md                 # Tekle's visual language breakdown
    ├── color-system.md                   # Complete palette with hex values
    ├── subject-catalog.md                # How to render garments, objects, figures
    └── prompt-engineering.md             # Prompt construction techniques
```

## References Used

- **Afewerk Tekle** — Complete body of work (1950s–2012)
- **UN Headquarters stained-glass windows** — His most famous commission
- **Africa Hall, Addis Ababa** — Major stained-glass commission
- **Reference images**: `assets/` — curated collections of his work

## Core Philosophy

Afewerk Tekle saw Ethiopian people and culture as worthy of the grandest artistic treatment. His work elevates every subject to heroic status — a woman holding cotton becomes an allegory of national industry, a portrait becomes a monument. This is not ego; it is a worldview rooted in deep cultural pride and classical artistic mastery.

> *"The painting should make the viewer feel the weight and dignity of Ethiopian identity."*

## Integration Notes

| Platform | Optimization |
|---|---|
| **Midjourney** | Add `--ar 3:4 --s 250 --q 2` (portrait) or `--ar 16:9` (landscape) |
| **DALL-E / ChatGPT** | Use prompt as-is |
| **Stable Diffusion** | Add positive: `oil painting, textured canvas, visible brushwork`; use negative prompt from skill |
| **Flux** | Use prompt as-is, specify format |
| **Ideogram** | Use prompt as-is |

## Example Usage

**User:** "Generate a portrait of an Ethiopian woman in traditional white clothing"

**Skill produces:**
```
Oil painting in the style of Afewerk Tekle, monumental Ethiopian fine art. A dignified Ethiopian woman with graceful elongated neck and large soulful expressive eyes, rich golden-brown skin tones with soft glowing highlights. She wears a luminous white netela with intricate gold and red woven tilet borders along the edges. In the background, a dark saturated emerald field that makes the white fabric glow. Dramatic chiaroscuro lighting, luminous saturated colors, rich jewel tones, visible oil painting brushwork texture, dignified and majestic composition.
```

## Important Distinction

This skill is **NOT** the same as the Ethiopian Traditional Painting skill:
- **Traditional Painting (Etsubdink Legesse)**: Flat 2D, bold outlines, unshaded colors, manuscript style
- **Afewerk Tekle**: Volumetric, chiaroscuro, oil painting texture, classical realism, monumental

Never confuse the two. Tekle uses perspective, depth, shadow, and volume — the opposite of flat traditional art.

---

*Skill version: 1.0 | Based on analysis of Afewerk Tekle's complete body of work | References: assets/*
