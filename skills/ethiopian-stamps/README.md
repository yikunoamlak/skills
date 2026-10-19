# Ethiopian Stamps — README

## Overview

**Ethiopian Stamps** is a skill for creating artwork in the visual language of
Ethiopian postage stamps: single stamps, se-tenant pairs, souvenir sheets,
first-day covers, and 2:3 stamp images ready for Pinterest.

The output reads as a real philatelic object first — perforated paper, inner
frame, bilingual inscription, denomination, cancellation — and only then as
whatever subject you place inside it. The stamp is the whole image: nothing
sits outside its perforated edges. That means a serious national stamp can
carry a modern joke without turning into a novelty sticker.

## What This Skill Does

When activated, this skill:

1. **Places** the request in an era: 1894 first issue, 1901-1935 overprints,
   1941-1974 imperial commemoratives, Derg era, or contemporary.
2. **Chooses** the format: single stamp, pair, souvenir sheet, first-day cover,
   or a 2:3 export for Pinterest.
3. **Writes** one clear vignette subject and at most four text strings.
4. **Builds** a complete generation prompt with printing language, palette,
   paper, perforation, and cancellation.
5. **Validates** the result against a 12-point stamp contract and an 11-item
   quality checklist.
6. **Exports** the final size with `scripts/export_stamp.py` (1440 x 2160 for a
   2:3 stamp), adding nothing outside the perforated edges.

## When to Use This Skill

Trigger this skill whenever the user wants:

- An **Ethiopian postage stamp** or stamp design
- **Ethiopian stamp aesthetic** or **philatelic art**
- **Vintage Ethiopian** or **Habesha stamp** artwork
- A **commemorative stamp** for a subject, person, or event
- A **souvenir sheet**, **se-tenant pair**, or **first-day cover**
- A **humorous modern subject** inside an authentic stamp frame
- A **Pinterest-sized stamp image** (2:3) ready to post

### Specific Triggers

- "Ethiopian stamp"
- "Ethiopian postage stamp"
- "stamp design, Ethiopia"
- "Philately art"
- "vintage Ethiopian stamp"
- "Menelik stamp"
- "Haile Selassie stamp"
- "Derg stamp"
- "stamp souvenir sheet"
- "first day cover Ethiopia"
- "Ethiopian stamp Pinterest"
- "stamp with Amharic text"

## How It Works

### One Contract, Five Eras

Every output satisfies the stamp contract: perforated physical stamp, inner
frame, Amharic top band, one central vignette, Latin bottom band, era-correct
denomination, year, flat printing, and a concept-art label when it is not a real
issue. The era selects the printing process, palette, and typography.

| Era | Years | Look |
|---|---|---|
| First issue | 1894-1900 | Intaglio engraving, acanthus border, Menelik or Lion of Judah, guerche values |
| Early definitives | 1901-1935 | `POSTES ETHIOPIENNES`, Zewditu and Tafari portraits, animals, overprints |
| Imperial commemoratives | 1941-1974 | Oval portrait, photogravure, cents and dollars, airmail and wildlife |
| Derg | 1974-1991 | Red, yellow, green poster graphics, workers and soldiers |
| Contemporary | 1991-now | Offset lithography, flat vector, birr and santim, tourism and sports |

### Design System

| Element | Rule |
|---|---|
| Paper | Cream or off-white, matte, uncoated |
| Image boundary | The perforated edge; nothing sits outside it |
| Perforation | Gauge 11.5-14.5, usually 14, clean regular teeth |
| Frame | Fine rule plus engraved or ornamental border for historical eras |
| Top band | `ኢትዮጵያ` in Ge'ez script, 4-8% of stamp height |
| Vignette | One subject, 50-70% of the printed area |
| Bottom band | `ETHIOPIA` or `ETHIOPIE`, letterspaced capitals |
| Denomination | Lower left; guerche, cents, or birr by era |
| Year | Lower right, Latin numerals for concept stamps |
| Cancellation | Optional circular postmark, off-centre, never over the face |
| Printing | Engraved lines, lithographic ink, or offset flat colour |

### Colour Palettes

| Era | Hex anchors |
|---|---|
| 1894 engraving | #1B3A6B, #7B1E2B, #1F5C3A, #C9A227, #F2E8D5 |
| 1909-1935 | #274C77, #A63A44, #6B7A3A, #8A6A4A, #F4EBD9 |
| 1941-1974 | #2E6F5E, #C1442E, #C58B2A, #7FA8C9, #F6EFDF |
| Derg | #C62828, #F2C230, #2E7D32, #141414, #F5E9D0 |
| Contemporary | #B85C38, #1F6F78, #E0A526, #2F5D3A, #E8DCC3 |

## Directory Structure

```
ethiopian-stamps/
├── SKILL.md                          # Main skill file
├── README.md                         # This file
├── assets/
│   ├── reference-historical-stamps.jpg   # Public-domain timeline sheet
│   └── reference-layout-anatomy.png      # Labelled stamp anatomy
├── evals/
│   └── evals.json                    # 8 test prompts
├── references/
│   ├── history-and-symbols.md        # Timeline, symbols, currency, ethics
│   ├── design-grammar.md             # Anatomy, grids, type, colour, templates
│   ├── prompt-recipes.md             # Model notes, CLI, era recipes
│   └── image-sources.md              # Public-domain attribution
└── scripts/
    └── export_stamp.py                # Scale a stamp image to a posting size
```

Sample images generated with the skill are kept outside the repository.

## References Used

- Wikipedia, *Postage stamps and postal history of Ethiopia*
- Ethiopost philately and stamp archive (`ethio.post`)
- Wikimedia Commons public-domain stamp scans, 1894-2024
- PixVerse CLI 1.4.6 for the generated concept samples

## Core Philosophy

An Ethiopian stamp is a small official artwork. It carries the country name in
two scripts, a value, a year, and one subject drawn with real craft. That
seriousness is exactly what makes it a good frame for a modern subject: the
frame stays dignified, the vignette carries the joke, and the result still
looks like something a postal service would print.

> *The frame is official. The subject can smile.*

## Integration Notes

| Platform | Optimization |
|---|---|
| **PixVerse CLI** | `--model gemini-3.1-flash --quality 1440p --aspect-ratio 2:3 --count 1 --json` |
| **Midjourney** | Add `--ar 2:3 --style raw --s 150`; add `--no glossy, 3d, plastic` |
| **DALL-E / ChatGPT** | Use the prompt as written; ask for a single image |
| **Flux** | Add `intaglio engraving` or `offset print` to control the look |
| **Ideogram** | Strong with text; keep all four strings short and quoted |
| **Stable Diffusion** | Use the negative prompt; add `engraved lines, flat ink, cream paper` |

## Example Usage

**User:** "Make me an Ethiopian stamp with a cat as emperor"

**Skill produces:** an 1894 engraved-style stamp, perforated cream paper,
ornate foliage border, `ኢትዮጵያ` at the top, `ETHIOPIA` and `5 ብር` at the bottom,
an orange tabby in a gold imperial crown on a crimson cushion, fine
cross-hatching in indigo and oxblood, and a circular `ADDIS ABABA` cancellation.
The stamp fills the frame, flush to its perforated edges; nothing sits outside
them. Gently humorous but official in tone.

## Important Notes

- The stamp is the whole image. Nothing sits outside the perforated edges: no
  background paper, border rule, shadow, or caption.
- These are **concept stamps**, not real postal issues. Label them as such.
- Amharic from image models needs verification. Use short strings and check every
  glyph, or rebuild the top band with a real Ethiopic font.
- Treat the Lion of Judah, Orthodox crosses, emperors, and other national and
  sacred symbols with dignity. Put the humour in everyday subjects.
- The 1936-1941 Italian occupation stamps are colonial propaganda. Study them
  critically, do not celebrate them.

---

*Skill version: 1.1.1 | Public-domain reference sheet in `assets/` | Sample images
are kept out of the repository*
