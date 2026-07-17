# Prompt Engineering — Ethiopian Traditional Painting

## Core Principles

1. **Specificity over generality** — "almond-shaped eyes" not "expressive eyes"
2. **Style keywords first** — establish the visual language before the subject
3. **Forbidden terms** — explicitly exclude what you don't want
4. **Layer the details** — subject → style → composition → color → borders → details

---

## Prompt Structure

Every prompt should follow this layered structure:

### Layer 1: Subject
What is being depicted?
```
An Ethiopian coffee farmer holding freshly picked coffee cherries
A family gathered for a coffee ceremony
King Solomon receiving the Queen of Sheba
```

### Layer 2: Style Establishment
The core visual language:
```
traditional Ethiopian painting style, inspired by Ethiopian Orthodox manuscript art and the work of Etsubdink Legesse
```

### Layer 3: Technical Characteristics
The flat 2D system:
```
flat 2D composition, bold black outlines, vibrant flat unshaded colors
```

### Layer 4: Figure Details
The human form:
```
large almond-shaped expressive eyes, warm brown skin tones, simplified rounded anatomy
```

### Layer 5: Garment/Attribute Details
What figures wear and carry:
```
wearing traditional white habesha kemis with colorful geometric embroidered borders
```

### Layer 6: Background
The setting:
```
warm ivory background, single stylized coffee tree behind
```

### Layer 7: Border/Frame
The decorative frame:
```
geometric ornamental red and terracotta border
```

### Layer 8: Text/Inscription
Manuscript elements:
```
Ge'ez manuscript text as decorative title at top
```

### Layer 9: Negative Prompts
What to exclude:
```
(no negative prompt needed in main prompt — use platform-specific negative prompts)
```

---

## Prompt Templates by Type

### Portrait (Single Figure)
```
[DESCRIPTION] portrait, traditional Ethiopian painting style, inspired by Ethiopian Orthodox manuscript art and Etsubdink Legesse, flat 2D composition, bold black outlines, vibrant flat unshaded colors, large almond-shaped expressive eyes, warm brown skin tones, [GARMENT DETAILS], [BACKGROUND ELEMENT], geometric ornamental border, handcrafted Ethiopian painting aesthetic.
```

### Group Scene
```
[N] [DESCRIPTION] in traditional Ethiopian painting style, flat 2D composition, bold black outlines, vibrant flat colors, large almond-shaped eyes, warm brown skin tones, [GARMENT DETAILS], [ARRANGEMENT], warm ivory background, [BACKGROUND ELEMENTS], geometric terracotta border, narrative composition, Etsubdink Legesse style.
```

### Narrative Scene
```
[STORY DESCRIPTION], traditional Ethiopian painting style, inspired by Ethiopian Orthodox manuscript art, flat 2D composition, bold black outlines, flat unshaded colors, [FIGURE DETAILS], [ACTION], [SETTING], warm ivory background, Ge'ez inscriptions, geometric ornamental border, narrative composition, Etsubdink Legesse manuscript style.
```

### Modern Subject
```
[MODERN DESCRIPTION], rendered in traditional Ethiopian painting style, flat 2D composition, bold black outlines, vibrant flat colors, large almond-shaped eyes, warm brown skin tones, [MODERN ELEMENTS AS SIMPLIFIED FORMS], traditional Ethiopian patterned accents, warm ivory background, geometric terracotta border, timeless Ethiopian visual language.
```

---

## Keyword Reference

### Style Keywords (use all)
- traditional Ethiopian painting style
- inspired by Ethiopian Orthodox manuscript art
- Etsubdink Legesse
- flat 2D composition
- bold black outlines
- vibrant flat unshaded colors
- handcrafted Ethiopian painting aesthetic

### Figure Keywords (use all)
- large almond-shaped expressive eyes
- warm brown skin tones
- simplified rounded anatomy
- decorative textile patterns

### Composition Keywords (as needed)
- narrative composition
- balanced composition
- front-facing
- direct gaze
- bilateral symmetry

### Background Keywords (as needed)
- warm ivory background
- warm cream background
- simple symbolic background
- stylized [element]

### Border Keywords (always include)
- geometric ornamental border
- red and terracotta border
- decorative geometric frame
- patterned border

### Detail Keywords (as appropriate)
- Ethiopian crosses
- ceremonial umbrella
- Ge'ez manuscript text
- traditional Ethiopian garments
- habesha kemis
- netela shawl

---

## Advanced Techniques

### For Multi-Panel Compositions
Generate each panel separately, then arrange:
```
Panel 1: [SCENE 1], traditional Ethiopian painting, flat 2D, bold outlines, geometric border.
Panel 2: [SCENE 2], traditional Ethiopian painting, flat 2D, bold outlines, geometric border.
[etc.]
Arrange in grid layout with consistent red borders between panels.
```

### For Religious Subjects
Add:
```
halo or nimbus behind head, Ethiopian cross motifs, ceremonial vestments, Ge'ez inscriptions, sacred atmosphere
```

### For Royal Subjects
Add:
```
crown or headpiece, ceremonial parasol/umbrella, elaborate patterned robes, attendants flanking, throne or seat of honor
```

### For Nature/Landscape
Add:
```
stylized trees with rounded canopies, simple triangular mountains, terraced fields, tukul huts, warm ivory sky
```

### For Celebration/Festival
Add:
```
joyful atmosphere, dancing figures, musical instruments, colorful garments, ceremonial objects, communal gathering
```

---

## Platform-Specific Optimizations

### Midjourney
Append to prompt:
```
--ar 1:1 --s 250 --q 2
```
Square format matches the panel tradition.

### DALL-E / ChatGPT
Use prompt as-is. DALL-E handles descriptive prompts well.

### Stable Diffusion
Add negative prompt:
```
photorealistic, 3D, gradients, shadows, anime, comic, western illustration, glossy, modern digital art, realistic anatomy, perspective, depth, cinematic lighting, brush strokes, texture
```

### Flux
Use prompt as-is. Specify square format if available.

### Ideogram
Use prompt as-is. Good for text elements.

---

## Common Prompt Mistakes

1. **Too vague**: "Ethiopian style art" → Too ambiguous
2. **Missing key traits**: "flat colors" → Specify "flat unshaded colors"
3. **No border**: Omitting the geometric border removes a defining feature
4. **No eye description**: Eyes are the most important facial feature
5. **No background**: Always specify warm ivory background
6. **Modern terms**: "3D", "depth", "perspective" → Never use
7. **Western elements**: "realistic anatomy", "shading" → Never use
8. **Too many subjects**: Keep compositions clear and readable
9. **No garment details**: Specify traditional Ethiopian clothing
10. **Missing negative prompts**: Always exclude non-Ethiopian styles

---

## Prompt Quality Checklist

Before finalizing any prompt, verify it includes:

- [ ] Specific subject description
- [ ] "traditional Ethiopian painting style" or equivalent
- [ ] "flat 2D composition"
- [ ] "bold black outlines"
- [ ] "flat unshaded colors" or "vibrant flat colors"
- [ ] "large almond-shaped eyes"
- [ ] "warm brown skin tones"
- [ ] Garment description
- [ ] Background specification (warm ivory)
- [ ] Border description
- [ ] At least one cultural detail (crosses, text, objects)

If any item is missing, add it before presenting the prompt.
