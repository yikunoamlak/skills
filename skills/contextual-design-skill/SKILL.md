---
name: contextual-design
version: 1.0.0
description: >-
  Apply Eliel Saarinen's "next larger context" principle to any design, art,
  architecture, product, interface, graphic, motion, video, spatial, brand,
  or communication task. Before proposing or evaluating a solution, identify
  what is being designed, its immediate context, the next larger contexts,
  the people and behaviors around it, the system it belongs to, its cultural,
  environmental, technical, temporal, and business constraints, and what
  comes before and after it. Produce context-driven recommendations that
  connect strategy, structure, form, use, and implementation. Ask for missing
  context when it would materially change the design; otherwise make explicit
  assumptions and proceed. Never treat aesthetics as independent of context.
triggers:
  - contextual design
  - design this
  - improve this design
  - review this design
  - redesign
  - make it look better
  - logo
  - brand identity
  - poster
  - social post
  - packaging
  - editorial design
  - typography
  - illustration
  - website
  - web design
  - UI
  - UX
  - app
  - dashboard
  - product design
  - industrial design
  - architecture
  - interior
  - exhibition
  - environmental graphics
  - signage
  - video
  - film
  - motion graphics
  - animation
  - presentation
  - campaign
  - service
  - installation
  - art
---

# Contextual Design Skill

## 1. Core belief

Design the thing **and the situation that gives the thing meaning**.

The governing question is:

> **What is the next larger context in which this design must succeed?**

Eliel Saarinen taught a design habit of moving outward in scale: a chair belongs to a room, the room to a house, the house to an environment, and the environment to a city plan. The National Park Service records this teaching in its biography of Eero Saarinen; other sources reproduce the wording while attributing it to Eliel Saarinen. Prefer **Eliel Saarinen** when crediting the quotation. [1][2]

This skill generalizes that idea beyond physical scale. A design can sit inside several nested contexts at once:

- **Scale context:** component → object → composition → environment → system.
- **Human context:** person → task → situation → journey → relationship.
- **Communication context:** element → message → artifact → campaign → brand/culture.
- **Technical context:** component → screen/object → product/service → platform/ecosystem.
- **Spatial context:** detail → room/space → building/site → neighborhood/city.
- **Temporal context:** moment → sequence → session → lifecycle → history/future.
- **Cultural context:** individual → group → community → institution → culture.
- **Business/ecological context:** deliverable → offering → organization → market/ecosystem/environment.

A good answer should determine which of these contexts actually matter instead of mechanically asking every possible question.

## 2. What this skill does

Use this skill to:

1. **Diagnose context before styling.**
2. **Find the next larger context** that can change the design decision.
3. **Map the surrounding system**: inputs, outputs, neighboring parts, actors, touchpoints, dependencies, and constraints.
4. **Separate essential constraints from arbitrary preferences.**
5. **Translate context into concrete design decisions** about hierarchy, scale, typography, color, composition, materials, interaction, pacing, architecture, motion, sound, content, technology, and implementation.
6. **Check the design at multiple scales**, from the smallest meaningful unit to the largest relevant system.
7. **Test the design in realistic use**, not only as an isolated artifact.
8. **Explain trade-offs**: what is optimized, what is sacrificed, and why.
9. **Prevent local optimization**: a beautiful part that damages the whole should be treated as a design failure.
10. **Carry context forward** into adjacent outputs and future states.

## 3. First interaction: Context Intake

When the user starts a design task and the context is missing, ask only for the information that will materially affect the recommendation. Start with:

> **What are you creating, where will it live, who will experience it, and what should it accomplish?**

Then, as needed, gather the fields in `templates/context-intake.md`.

Do not interrogate the user with the full template if the request already contains the answer. Infer what is obvious, state assumptions briefly, and continue.

### Minimum intake

- **Artifact:** What are we making?
- **Purpose:** What job must it perform?
- **Audience/user:** Who encounters or uses it?
- **Context of encounter:** Where, when, and under what conditions?
- **Next larger context:** What is it a part of?
- **Adjacent context:** What surrounds it or appears before/after it?
- **Constraints:** technical, physical, cultural, legal, budget, time, brand, accessibility, platform.
- **Success:** What would make this work?
- **Known references:** Existing brand, system, architecture, content, visual language, competitors, precedents.

## 4. The Next-Larger-Context Method (NLC)

Run this sequence for every significant design decision.

### NLC-0 — Name the thing

State exactly what is being designed. Avoid vague labels like "the page" or "the logo." Name the usable unit: hero section, identity mark, app navigation, title sequence, chair arm, storefront sign, poster series, etc.

### NLC-1 — Immediate context

Ask:

- What directly contains, supports, frames, or surrounds it?
- What does it touch or connect to?
- What competes with it for attention?
- What must it visually, physically, semantically, or behaviorally relate to?

### NLC-2 — Next larger context

Ask:

- What larger thing is this a component of?
- What larger goal does it serve?
- What rules, proportions, conventions, or identity does that parent system impose?
- Does the component reinforce or fight the parent?

This is the closest translation of Saarinen's principle.

### NLC-3 — System context

Map:

`inputs → transformation → artifact/experience → output → next action`

Identify people, tools, content, technology, physical surroundings, channels, dependencies, and handoffs.

### NLC-4 — Human/use context

Consider:

- Who is present?
- What are they trying to accomplish?
- What do they already know?
- What are they doing immediately before and after?
- What is their attention level?
- What device, body position, environment, distance, lighting, noise, movement, or social situation affects use?
- What errors, misunderstandings, or unintended behaviors are likely?

For interactive/product work, apply affordances, signifiers, mapping, feedback, constraints, and conceptual models. [3]

### NLC-5 — Cultural/place context

Consider:

- Local visual conventions and cultural meanings.
- Language, script, reading direction, symbolism, color associations, imagery, etiquette.
- Local history, climate, materials, craft, landscape, architecture, and social practices.
- Whether "global" references erase useful local specificity.

In architecture and place-based work, use context-sensitive reasoning about site, climate, topography, materiality, culture, and existing urban fabric; avoid treating context as mere visual imitation. [4]

### NLC-6 — Temporal context

Consider:

- What came before this?
- What follows it?
- Is it static or changing?
- How does it behave on first encounter, repeated use, and long-term use?
- How will it age, update, scale, migrate, degrade, or be replaced?
- What historical or future condition is it participating in?

### NLC-7 — Ecosystem / lifecycle context

Consider:

- What happens to this design after delivery?
- Who maintains it?
- What resources does it consume?
- What other teams, products, services, platforms, materials, or environments depend on it?
- What happens at failure, edge cases, decommissioning, reuse, recycling, archiving, or redesign?

## 5. The Context Ladder

When possible, render the design as a ladder or nested chain:

`[THING] → [IMMEDIATE CONTAINER] → [NEXT LARGER SYSTEM] → [ECOSYSTEM] → [CULTURE / PLACE / TIME]`

Then add the human journey:

`before → encounter → use → outcome → after`

And the implementation chain:

`content/data/material → production → artifact → distribution/channel → maintenance`

The ladder must be **specific to the project**, not generic.

### Example mappings

**Logo**

`symbol → logo system → identity system → brand touchpoints → organization/category/culture`

**Poster**

`layout → poster series/campaign → event/communication goal → physical/social environment → audience culture`

**Website**

`component → page → site → product/service → organization/ecosystem`

**UI screen**

`control → component group → screen → task flow → product/service → real-world job`

**Video shot**

`frame → shot → scene → sequence → story → release/platform/audience context`

**Motion graphic**

`motion event → component/scene → sequence → narrative/message → viewing context/platform`

**Product**

`part → product → task/use situation → service/lifecycle → environment/market/culture`

**Architecture**

`detail → room → building → site → neighborhood → city/landscape`

**Exhibition**

`object/label → display → gallery → visitor journey → institution/place/cultural context`

**Artwork**

`mark/form → work → body of work → exhibition/archive → audience/cultural context`

**Packaging**

`pack → shelf/distribution environment → product line → retail/brand system → consumer/cultural context`

## 6. The Five Context Questions

For any design, ask at least these five:

1. **What is it part of?**
2. **Who is it for and what are they doing?**
3. **What surrounds it and competes with it?**
4. **What happens immediately before and after it?**
5. **What larger system, place, culture, technology, or lifecycle gives it meaning?**

If one of the answers changes, re-evaluate the design.

## 7. Context-to-Decision Translation

Never stop at "consider the context." Convert context into design instructions.

Use this structure:

| Context finding | Design implication | Concrete decision | Verification |
|---|---|---|---|
| User sees poster from 8–15 m | Recognition dominates detail | Increase silhouette, type scale, reduce fine information | Distance test |
| Logo must work on embroidery | Fine gaps may disappear | Simplify internal counters and stroke detail | 16–32 px + embroidery sample |
| Site is mostly mobile | Thumb and viewport constraints matter | Reflow hierarchy; enlarge targets; shorten paths | Real-device test |
| Scene is emotionally quiet | Motion should not over-perform | Long holds, restrained camera motion, fewer cuts | Full-sequence review |
| Building has strong local craft tradition | Material language carries place | Use locally legible material/tectonic logic without pastiche | Context review with local perspective |

## 8. Context Has Forces, Not Just Facts

A good contextual diagnosis identifies competing forces.

Record:

- **Goal:** what should improve?
- **Forces:** what is pulling the design in different directions?
- **Constraints:** what cannot change?
- **Priorities:** which forces matter most?
- **Trade-off:** what is deliberately sacrificed?

Use an Alexander-style pattern structure when a recurring design problem appears:

`CONTEXT → PROBLEM → FORCES → SOLUTION → VARIANTS → RELATIONSHIPS`

Christopher Alexander's pattern language explicitly connects context, problems, forces, solutions, and patterns at multiple scales. [5][6]

## 9. Use established frameworks as lenses, not as rituals

### 9.1 Design Council Double Diamond

Use:

`DISCOVER → DEFINE → DEVELOP → DELIVER`

The purpose is not to force a linear process. Use divergence and convergence to avoid solving the wrong problem, and iterate between research, making, testing, and refinement. [7]

### 9.2 UX Five Planes

For digital products, test alignment from:

`STRATEGY → SCOPE → STRUCTURE → SKELETON → SURFACE`

A surface-level problem may actually originate in strategy, scope, or structure. [8]

### 9.3 Gestalt / perceptual context

Use proximity, similarity, continuation, closure, figure-ground, common region, connectedness, symmetry/order, and common fate to understand how parts become wholes. In motion, common fate is especially useful. [9][10]

### 9.4 Norman / action context

For interactive systems, verify:

`discoverability → action → feedback → interpretation`

Use affordances/signifiers, mappings, constraints, feedback, and conceptual models. Do not patch a structural usability problem with decoration. [3]

### 9.5 Information architecture

Check whether organization, labeling, navigation, and findability reflect the user's mental model and the larger information environment. Provide a sense of place and clear relationships between levels. [11][12]

### 9.6 Responsive/adaptive context

For web/app design, design for the viewing/use environment instead of a single screenshot. Reflow, reposition, resize, or replace components as the available space and input conditions change. [13][14]

### 9.7 Accessibility as contextual design

Accessibility is not a final compliance pass. It changes the conditions under which the design is encountered. Consider vision, hearing, motor control, cognition, language, assistive technology, lighting, noise, motion sensitivity, and zoom/reflow. WCAG 2.2 includes criteria for contrast, reflow, non-text contrast, keyboard and pointer interactions, and target sizing. [15]

### 9.8 Service / ecosystem context

When a design is one touchpoint in a larger service, map frontstage and backstage actions, support processes, dependencies, and physical/digital evidence. A "beautiful interface" can still be a broken service. [16]

## 10. Domain Playbooks

Load the matching playbook when the project belongs clearly to a domain. These playbooks are **specializations of the same contextual method**, not separate philosophies.

- `playbooks/graphic-design.md`
- `playbooks/branding-identity.md`
- `playbooks/typography-editorial.md`
- `playbooks/web-product-ui-ux.md`
- `playbooks/video-film-motion.md`
- `playbooks/product-packaging.md`
- `playbooks/architecture-space.md`
- `playbooks/environmental-exhibition.md`
- `playbooks/art-illustration.md`
- `playbooks/presentation-information.md`

## 11. The Context Review Protocol

When asked to review an existing design:

### A. Do not start with taste

First identify:

- What the artifact is.
- Its parent system.
- Its user/observer.
- Its use environment.
- Its constraints.
- Its intended outcome.

### B. Review at four scales

**Micro:** individual elements, spacing, edges, alignment, legibility, motion details, construction.

**Artifact:** composition, hierarchy, rhythm, material, interaction, narrative, usability.

**System:** relationship to adjacent screens/pages/assets/spaces/products/campaigns.

**World:** culture, place, platform, business, environment, lifecycle, audience behavior.

### C. Classify every issue

Use one of:

- **Context mismatch** — the design solves the wrong situation.
- **System mismatch** — the part conflicts with its parent system.
- **Hierarchy failure** — important information is not prioritized.
- **Perception failure** — people are unlikely to group, distinguish, or scan it as intended.
- **Interaction failure** — action, feedback, or mental model is unclear.
- **Technical mismatch** — implementation constraints were ignored.
- **Cultural mismatch** — local meaning or audience conventions were ignored.
- **Temporal mismatch** — it works at one moment but fails across sequence/lifecycle.
- **Aesthetic weakness** — after the contextual problems are resolved.

### D. Rank recommendations

Use:

`CRITICAL → HIGH → MEDIUM → POLISH`

Aesthetic polish must not outrank structural/contextual corrections.

## 12. Design Decision Heuristics

Use these as prompts, not laws.

### Context before style

Do not choose a visual language until you know what the artifact must coexist with.

### Parent before child

Solve the larger system enough to know what the component is supposed to do.

### Relationship before ornament

Prefer relationships—scale, alignment, rhythm, adjacency, hierarchy, sequence, material continuity—over decoration.

### Real environment before mockup

Evaluate the work where it will actually be seen, touched, heard, printed, installed, watched, or used.

### Sequence before frame

For motion, video, presentations, onboarding, and interactive experiences, evaluate transitions and before/after states rather than isolated frames.

### Exceptions should explain themselves

A deviation from the system should have a contextual reason, not simply "to make it interesting."

### Specificity beats generic polish

A contextually specific solution should contain evidence of the actual user, place, task, medium, or system—not generic "professional" styling.

### Design for the edge, not only the ideal

Check low bandwidth, small screens, long text, translation, dark/light conditions, distance, noise, accessibility, production tolerances, failure states, and real maintenance.

### Good constraints can create identity

Do not remove every constraint. Some constraints provide coherence, economy, recognition, or meaningful local character.

## 13. Domain-specific contextual recommendations

### Graphic design

Think:

`element → composition → series/campaign → publication/channel → audience/culture`

Prioritize hierarchy, viewing distance, reproduction method, typography, image context, cropping, platform conventions, series consistency, and how the piece behaves beside neighboring communications.

### Branding

Think:

`mark → identity system → touchpoint → customer experience → brand/ecosystem`

Test the identity on actual applications, not only a logo sheet. Consider behavior across sizes, materials, motion, digital UI, signage, packaging, social media, and co-branding.

### Web/UI/UX

Think:

`control → component → screen → flow → product → service/ecosystem`

Ask what happens before and after each action. Test responsive behavior, accessibility, content growth, empty/error/loading states, information architecture, and implementation feasibility.

### Video/film/motion

Think:

`frame → shot → scene → sequence → story → audience/platform`

Check screen size, sound, watch conditions, pacing, continuity, transition logic, attention hierarchy, subtitles, safe areas, aspect ratios, and where the viewer's attention should enter/leave each shot.

### Product / industrial design

Think:

`part → product → task → environment → service/lifecycle`

Evaluate grip, reach, force, storage, transport, cleaning, repair, manufacturing, material aging, safety, misuse, packaging, disposal, and the surrounding environment.

### Architecture / spatial design

Think:

`detail → room → building → site → neighborhood → landscape/city`

Evaluate site, climate, light, view, circulation, human scale, material, structure, sound, thresholds, public/private gradients, local culture, and long-term adaptation.

### Art / illustration

Think:

`mark → work → body/series → presentation → audience/cultural context`

Consider why this work exists in this body of work, how it changes when exhibited/printed/published, the viewing distance and duration, adjacent works, and the cultural references it activates.

## 14. Research rule

When context is specialized, unfamiliar, regulated, location-sensitive, technically current, or materially consequential, research before giving a strong recommendation.

Prefer primary/high-authority sources for:

- standards and accessibility,
- platform guidelines,
- building and safety requirements,
- manufacturing constraints,
- software APIs and implementation rules,
- current device/platform behavior.

Use secondary sources for comparative practice, historical discussion, examples, critique, and broader interpretation.

When research changes the recommendation, state **which contextual fact changed the decision**.

## 15. Output format

For substantial design requests, produce:

### Context diagnosis
A short statement of what the artifact is and the larger system it belongs to.

### Context ladder
A project-specific nested map of the design's immediate, larger, ecosystem, human, cultural/place, and temporal contexts.

### What this changes
The 3–8 most consequential design implications.

### Recommendations
Concrete recommendations, ordered by impact.

### Trade-offs
What each recommendation improves and what it may cost.

### Validation
Specific tests in the real context: viewport, distance, print, prototype, user flow, full-sequence playback, physical mockup, environmental placement, etc.

### Open assumptions
Only the assumptions that could change the design.

For a quick/simple task, compress this to a few sentences while still applying the context principle.

## 16. Anti-patterns

Do not:

- treat the artifact as an isolated picture;
- optimize the most visible component while ignoring the system;
- start with colors/fonts/effects when purpose or hierarchy is unresolved;
- use trends as a substitute for contextual reasoning;
- copy a precedent without understanding the context that made it successful;
- call something "minimal" merely because it has fewer elements;
- add UI animation that has no relationship to user action or narrative;
- design a responsive site from only one desktop screenshot;
- approve a logo only because it looks good on a white presentation board;
- judge architecture from the building alone without site and urban context;
- design a poster without considering viewing distance and the surrounding environment;
- judge a film frame without checking the shot/sequence/story relationship;
- finish with "make it more modern" without defining what the target environment demands.

## 17. Templates

Use these templates as working documents:

- `templates/context-intake.md` — initial project intake.
- `templates/context-ladder.md` — nested context map.
- `templates/forces-map.md` — competing forces and trade-offs.
- `templates/design-decision-record.md` — evidence-to-decision trace.
- `templates/context-review.md` — critique/review report.
- `templates/real-context-test.md` — real-world validation protocol.
- `templates/contextual-brief.md` — context-driven creative brief.
- `templates/pattern-card.md` — reusable problem/context/force/solution pattern.

For practical methods, use `references/contextual-toolkit.md`, which contains contextual inquiry, ecosystem mapping, touchpoint audits, attention maps, state matrices, sequence strips, site analysis, lifecycle mapping, in-situ prototyping, and other methods.

## 18. Example behavior

### User: "Make this logo look more premium."

Do not immediately propose colors, typefaces, or effects.

First infer or ask:

- What brand/category is it?
- Where will the logo appear most often?
- What other brands will it sit beside?
- Is "premium" meant to signal price, trust, rarity, heritage, technical quality, or status?
- What audiences need to read into it?
- Does it need to work in small digital UI, signage, packaging, embroidery, or motion?

Then say, for example:

> The next larger context is not the logo board; it is the brand system and the category environment. That means the strongest route to "premium" may be restraint in the full identity system—spacing, type, material cues, photography, motion, and touchpoint behavior—rather than making the mark itself more ornate.

### User: "Design a landing page."

Map:

`hero section → landing page → acquisition journey → product/service → user's decision context`

Then determine the user's entry source, intent, credibility requirements, information sequence, CTA, responsive behavior, and post-click expectation.

## 19. Quality gate

Before finalizing a design recommendation, ask:

- Did I identify the parent system?
- Did I identify the actual encounter/use condition?
- Did I account for what comes before and after?
- Did I identify meaningful constraints and competing forces?
- Did I convert context findings into concrete design decisions?
- Did I test at more than one scale?
- Did I account for accessibility and realistic edge cases where relevant?
- Did I avoid imposing a generic style without evidence?
- Did I distinguish structural problems from surface polish?
- Can I explain why the recommendation belongs specifically to this context?

If several answers are "no," continue contextual analysis before recommending polish.

## 20. Research references

The skill is synthesized from the following bodies of work:

1. U.S. National Park Service, Eero Saarinen biography: records the "next largest context" teaching and its relationship to Saarinen's architectural thinking. https://home.nps.gov/people/eero-saarinen.htm [1]
2. John Pawson, "Considering the next larger context" (2025), reproducing the quotation and identifying Eliel Saarinen. https://www.johnpawson.com/journal/considering-the-next-larger-context [2]
3. Don Norman, *The Design of Everyday Things*: affordances, signifiers, constraints, mappings, feedback, and conceptual models. See the cited text at Penn State and supporting summaries. https://media.aanda.psu.edu/sites/media/aa/files/documents/norman_design-of-everyday-things.pdf [3]
4. Kenneth Frampton / contextual architecture literature: critical regionalism emphasizes geographical context, topography, climate, light, tectonic form, and local culture rather than superficial visual imitation. https://link.springer.com/article/10.1057/s41289-025-00302-6 [4]
5. Christopher Alexander, Sara Ishikawa, Murray Silverstein, *A Pattern Language*: patterns link problem, context, forces, solution, and larger/smaller patterns. https://arl.human.cornell.edu/linked%20docs/Alexander_A_Pattern_Language.pdf [5]
6. Hillside, "A Pattern Language for Pattern Writing": context, problem, forces, solution, and rationale. https://www.hillside.net/index.php/a-pattern-language-for-pattern-writing [6]
7. Design Council, Double Diamond / Framework for Innovation: Discover, Define, Develop, Deliver; people-centred, collaborative, visual communication, iteration. https://www.designcouncil.org.uk/resources/the-double-diamond/ [7]
8. Jesse James Garrett's Five Planes as summarized by BCcampus: strategy, scope, structure, skeleton, surface. https://pressbooks.bccampus.ca/technicalwriting2ed/chapter/6-3/ [8]
9. Scholarpedia, Gestalt principles: grouping by proximity, similarity, continuity, closure, common fate, etc. https://www.scholarpedia.org/article/Gestalt_principles [9]
10. Nielsen Norman Group, Gestalt similarity principle in user interfaces. https://www.nngroup.com/articles/gestalt-similarity/ [10]
11. U.S. Department of Veterans Affairs Design System, Information Architecture: sense of place, consistency, prioritization, findability, focused navigation, scalability. https://design.va.gov/ia/ [11]
12. O'Reilly, *Information Architecture for the World Wide Web*, "Building Context": contextual clues and orientation in complex websites. https://www.oreilly.com/library/view/information-architecture-for/1565922824/ch04s02.html [12]
13. MDN, Responsive Design: layouts should respond to the device/viewing environment; modern CSS supports this directly. https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design [13]
14. Android / Material guidance, Adaptive Layout: layouts should adapt to window size, device conventions, and ergonomics; components may reposition or switch for context. https://developer.android.com/codelabs/adaptive-material-guidance [14]
15. W3C WCAG 2.2: contrast, resize, reflow, non-text contrast, target sizing and input considerations. https://www.w3.org/TR/WCAG22/ [15]
16. Service blueprinting literature: maps customer actions, frontstage, backstage, support processes, and physical evidence across a service. https://www.uxatlas.io/methods/service-blueprint [16]

## 21. Attribution note

The principle comes from Eliel Saarinen, not Eero Saarinen. Because the quotation is frequently misattributed online, preserve the distinction in future outputs unless the user explicitly wants the commonly circulated Eero attribution. [1][2]
