# Design Grammar

The rules that separate an Ethiopian stamp from a generic vintage label. Read
this file when you are composing a prompt, drawing a frame, or checking a result.

## Anatomy

```
┌──────────────────────────────────────┐  ← perforated edge
│  cream paper margin (2-4 mm)         │
│  ┌────────────────────────────────┐  │  ← inner frame rule
│  │  ኢትዮጵያ   (Amharic top band)   │  │
│  ├────────────────────────────────┤  │
│  │                                │  │
│  │        CENTRAL VIGNETTE        │  │  ← portrait, animal, landscape,
│  │        (one clear subject)     │  │     emblem, or event
│  │                                │  │
│  ├────────────────────────────────┤  │
│  │ 5 ብር    ETHIOPIA    2026       │  │  ← value, country, year
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘
```

1. **Paper.** Cream or off-white, uncoated, matte. The paper carries the ink; it
   is not a white canvas behind a coloured rectangle.
2. **Perforation.** Regular teeth around all four sides. Perforation gauge 11.5 to
   14.5, usually 14. Teeth about 0.8 to 1 mm. Corners clean, no missing teeth.
3. **Margin.** 2 to 4 mm of unprinted paper between the perforation and the frame.
   This is what makes the object read as a stamp.
4. **Frame.** One or two thin rules, with corner ornaments or an engraved border
   for historical eras. The frame colour follows the era palette.
5. **Top band.** The Amharic country name `ኢትዮጵያ`. For the 1900s-1930s look,
   `POSTES ETHIOPIENNES` may sit at the top instead.
6. **Vignette.** One subject in one action. It fills 50 to 70 per cent of the
   printed area. Historical portraits sit in an oval or circular medallion.
7. **Bottom band.** `ETHIOPIA` or `ETHIOPIE`, letterspaced. On modern stamps it
   sits below the vignette, never over it.
8. **Denomination.** Lower left or bottom centre. Numeral plus currency word or
   abbreviation for the era.
9. **Year.** Lower right or under the vignette. Latin numerals for concept
   stamps; Ge'ez numerals optional for historical looks.
10. **Overprints.** `PAR AVION`, surcharges, and commemorative overprints sit
    centred and horizontal. They are printed over the design, not merged into it.
11. **Cancellation.** Optional. A circular date stamp, wavy lines, or a slogan
    cancel in black ink, 20 to 35 mm across, placed off-centre and away from the
    face and the value.
12. **Texture.** Subtle paper fibre, light foxing, faint plate wear. Stop before
    it becomes grunge.

## Proportions

| Element | Share of stamp height |
|---|---|
| Top band | 12-15% |
| Vignette | 60-70% |
| Bottom band | 12-15% |
| Side margins | 5-8% of width |

**Stamp shapes.**

- Vertical: 2:3 to 3:4. The classic portrait format.
- Horizontal: 3:2. Landscapes, airmail, panoramas, se-tenant strips.
- Real-world reference: a 1994 Ethiopian commemorative measured 40.5 x 30.45 mm
  (landscape). A 2011 coffee commemorative used perforation 14.

**Pinterest pin.**

- Canvas 1440 x 2160 or 1696 x 2528 (2:3).
- Stamp occupies 55 to 70 per cent of the height, centred.
- Cream paper background with a very soft shadow under the stamp.
- Keep 120 px of safe margin on every side. Pinterest overlays UI at the edges.
- Caption below the stamp, outside the perforation. One line, serif, small.
- Export JPEG, quality 90 or higher.

## Typography

**Amharic (Ge'ez script).**

- Fonts: Noto Serif Ethiopic, Abyssinica SIL, Nyala, Ethiopic Abay, Ethiopic
  Lessan.
- Rounded, slightly condensed letterforms. No italic, no fake bold, no distorted
  arches.
- Amharic is written left to right with spaces between words. Do not letterspace
  it the way you letterspace `ETHIOPIA`.
- Use short strings only. Long generated Ge'ez almost always breaks.

**Latin.**

- Historical: Didone, Clarendon, or transitional serif for country names and
  values.
- Mid-century: grotesque or humanist sans for captions, serif for the country.
- Contemporary: clean sans or serif with generous tracking.
- `ETHIOPIA` and `POSTES ETHIOPIENNES` are always letterspaced capitals.
- Numerals are tabular and centred in their corner.

**Placement.**

- Top band: country name, centred, cap height 4 to 8 per cent of stamp height.
- Bottom band: country name, centred, same size or slightly larger.
- Denomination: lower left or bottom centre, cap height 6 to 10 per cent.
- Year: lower right, cap height 3 to 5 per cent.
- Slogan: one line above the bottom band. Never a paragraph.

**Verified strings.**

| Amharic | Transliteration | Meaning |
|---|---|---|
| ኢትዮጵያ | Ityop'ya | Ethiopia |
| የኢትዮጵያ ፖስታ አገልግሎት | Ye-Ityop'ya Posta Agelgilot | Ethiopian Postal Service |
| ፖስታ | Posta | Post, mail |
| ቴምብር | Tembir | Stamp |
| ብር | Birr | Birr |
| ሳንቲም | Santim | Santim |
| ቡና | Buna | Coffee |
| የቡና ሥርዓት | Ye-buna Sirat | Coffee ceremony |
| እንጀራ | Injera | Injera |
| ሰላም | Selam | Peace |
| የይሁዳ አንበሳ | Ye-Yihuda Anbessa | Lion of Judah |

**Ge'ez numerals.** ፩ 1, ፪ 2, ፫ 3, ፬ 4, ፭ 5, ፮ 6, ፯ 7, ፰ 8, ፱ 9, ፲ 10, ፳ 20,
፴ 30, ፵ 40, ፶ 50, ፷ 60, ፸ 70, ፹ 80, ፺ 90, ፻ 100.

## Colour

| Era | Inks | Hex anchors |
|---|---|---|
| 1894 engraving | Indigo, oxblood, forest, ochre, cream | #1B3A6B, #7B1E2B, #1F5C3A, #C9A227, #F2E8D5 |
| 1909-1935 | French blue, carmine, olive, sepia, cream | #274C77, #A63A44, #6B7A3A, #8A6A4A, #F4EBD9 |
| 1941-1974 | Emerald, vermilion, mustard, sky, cream | #2E6F5E, #C1442E, #C58B2A, #7FA8C9, #F6EFDF |
| Derg | Red, yellow, green, black, cream | #C62828, #F2C230, #2E7D32, #141414, #F5E9D0 |
| Contemporary | Terracotta, teal, saffron, forest, sand | #B85C38, #1F6F78, #E0A526, #2F5D3A, #E8DCC3 |

**Rules.**

- Two to four inks plus paper. More than four looks like a poster.
- Black is for text and cancellation ink. Do not tint the text.
- One gold or metallic accent at most. Gold suits crowns, frames, and years.
- Keep the paper cream. A pure white background kills the vintage feel.
- No neon, no pastel wash, no glossy gradient mesh.

## Printing Language

| Era | Process | Visual cues | Prompt words |
|---|---|---|---|
| 1894-1930s | Intaglio engraving | Fine parallel lines, cross-hatching, crisp edges, one or two inks | `intaglio engraving`, `fine cross-hatching`, `flat ink on cream paper` |
| 1930s-1980s | Photogravure and lithography | Continuous tone, soft halftone, slight misregistration, four inks | `photogravure`, `four-colour lithography`, `soft halftone`, `slight misregistration` |
| 1990s-now | Offset lithography | Flat even fills, crisp type, high saturation, spot colour, foil | `offset print`, `flat vector ink`, `crisp typography`, `spot colour` |

## Cancellations

- Circular date stamp: town name around the top, date in the centre, `ETHIOPIA`
  or a code at the bottom.
- Wavy line cancel: three to five parallel waves beside the circle.
- Slogan cancel: a rectangle of small text with a pictorial element.
- First-day cancel: a special design, often with the issue name and date.
- Manuscript cancel: a pen cross or initials, common on early covers.
- Italian colonial cancels: a Maltese cross or a colonial town name. Use only in
  critical historical work.

Place the cancellation off-centre: lower left, upper right, or across a corner.
Never over the face, the value, or the country name.

## Layout Templates

**Single vertical stamp.**

```
┌─────────────┐
│  ኢትዮጵያ    │
│   [vignette]│
│ 5 ብር ETHIOPIA 2026
└─────────────┘
```

**Single horizontal stamp (airmail).**

```
┌───────────────────────────────┐
│ ኢትዮጵያ        PAR AVION       │
│   [wide vignette]    5c        │
│ ETHIOPIA             1949      │
└───────────────────────────────┘
```

**Se-tenant pair.**

```
┌────────┬────────┐
│ ኢትዮጵያ │ ኢትዮጵያ │
│ [subj] │ [subj] │
│ 5 ብር  │ 10 ብር │
│ ETHIOPIA│ETHIOPIA│
└────────┴────────┘
```

**Souvenir sheet.**

```
┌──────────────────────────────────┐
│         ኢትዮጵያ                    │
│   ┌──────────┐  ┌──────────┐     │
│   │  stamp   │  │  stamp   │     │
│   └──────────┘  └──────────┘     │
│   ┌──────────┐  ┌──────────┐     │
│   │  stamp   │  │  stamp   │     │
│   └──────────┘  └──────────┘     │
│   ETHIOPIA · 2026 · concept      │
└──────────────────────────────────┘
```

**First-day cover.**

```
┌──────────────────────────────────────┐
│  ┌────────┐                          │
│  │ stamp  │   ◉ ADDIS ABABA          │
│  └────────┘   first day of issue     │
│   [cachet illustration]              │
│  ────────────────────────────────    │
│  name                              │
│  address                           │
└──────────────────────────────────────┘
```

## Do and Do Not

| Do | Do not |
|---|---|
| Show perforated paper | Float a flat design on white |
| Keep the cream margin | Bleed the design to the pin edge |
| Use one clear vignette | Collage five motifs into one stamp |
| Use verified short Amharic | Generate a paragraph of Ge'ez |
| Match currency to the era | Put birr on an 1894 stamp |
| Keep cancellation off the face | Stamp the cancellation over the eyes |
| Use two to four inks | Use a rainbow gradient |
| Preserve dignity for sacred symbols | Make the Lion of Judah a meme |
| Label concept art | Claim a fantasy stamp is real |
| Keep text inside the frame | Let the caption cross the perforation |
