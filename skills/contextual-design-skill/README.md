# Contextual Design Skill

A reusable design-reasoning skill built around Eliel Saarinen's **next larger context** principle.

## What it is

This skill helps an AI or designer avoid treating a design as an isolated artifact. It asks what the thing belongs to, who encounters it, what surrounds it, what happens before and after it, and which larger system gives it meaning.

It works across:

- graphic design
- branding and identity
- typography and editorial
- websites, products, UI/UX
- motion graphics, animation, film/video
- industrial/product design
- packaging
- architecture and interiors
- exhibitions, signage and environmental graphics
- art and illustration
- presentations and information design
- services and experiences

## Folder structure

```text
contextual-design-skill/
├── SKILL.md
├── README.md
├── templates/
│   ├── contextual-brief.md
│   ├── context-intake.md
│   ├── context-ladder.md
│   ├── forces-map.md
│   ├── design-decision-record.md
│   ├── context-review.md
│   ├── real-context-test.md
│   └── pattern-card.md
├── playbooks/
│   ├── graphic-design.md
│   ├── branding-identity.md
│   ├── typography-editorial.md
│   ├── web-product-ui-ux.md
│   ├── video-film-motion.md
│   ├── product-packaging.md
│   ├── architecture-space.md
│   ├── environmental-exhibition.md
│   ├── art-illustration.md
│   └── presentation-information.md
├── references/
│   ├── framework-index.md
│   └── contextual-toolkit.md
└── examples/
    └── worked-context-examples.md
```

## Recommended behavior

The skill should ask **only the questions needed to establish context**. Once enough is known, it should stop asking and produce recommendations.

For a substantial request, output:

1. Context diagnosis
2. Context ladder
3. What this changes
4. Prioritized recommendations
5. Trade-offs
6. Validation tests
7. Open assumptions

The core principle is simple:

> **Do not design the part until you understand the whole that gives the part its job.**

## Important attribution

The quote is commonly attributed online to Eero Saarinen, but the National Park Service records it as teaching from his father, Eliel Saarinen. The skill therefore uses **Eliel Saarinen** as the attribution. See `SKILL.md` and `references/framework-index.md`.

## Practical toolkit

Use `references/contextual-toolkit.md` when the skill needs an actual method to investigate context rather than just a checklist. It includes 33 methods/tools and a selection matrix.
