---
name: storytelling-for-designers
description: Interview-driven storytelling toolkit drawn from the 100 principles of "Universal Principles of Storytelling for Designers" by Lyle H. Sandler. Use when the user wants a design, brand, landing page, deck, campaign, report, talk, service, or product experience to tell a story, bring an idea to life, connect with an audience, make people care, or have impact. Also use when they ask what story their design should tell, how to structure a narrative, how to explain something complex, how to make data land, how to write an about or origin story, how to pitch or persuade, how to review a design for narrative weakness, or mention storytelling, narrative structure, hero's journey, three-act structure, show don't tell, conflict, emotional impact, or audience transformation. Extracts what the user wants to tell through structured discovery, then returns a tailored selection of principles with concrete edits, a narrative arc, and a QA checklist.
---

# Storytelling for Designers

Turn what a person wants to say into a design that actually says it. The skill interviews the user until the message, audience, and impact are clear, then selects the principles from the 100 that change decisions for that specific brief.

The 100 principles are grouped into five categories: Literary Device, Structure, Emotion, Psychology + Philosophy, Methods / Tools. A story needs at least three of the five, or it becomes a checklist instead of a narrative.

## Modes

Choose one from what the user gives you, and say which you are in.

- **Build** - nothing exists yet. Discover, then design the story and the artifact.
- **Shape** - a draft exists. Read it first, then restructure it around the brief.
- **Review** - a finished artifact. Diagnose against the principles and rank findings by impact.

## Phase 1 - Discovery

Ask in batches, never one question at a time. Round one, all four together:

1. **What do you want to tell?** One sentence: what should the audience believe, feel, or do when they are done?
2. **Who is it for?** The specific audience, what they already believe, and what they care about.
3. **What are you making?** Artifact, medium, where it lives, and what stage it is at.
4. **What should happen next?** The concrete action or shift, and how they will know it worked.

Round two fills only the gaps that matter for this brief:

- **Stakes and conflict** - what is at stake, and what opposes the outcome (88, 11)
- **Transformation** - the before and the after they want the audience to cross (12, 95)
- **Protagonist** - whose story this is; usually the audience or their client, not the maker (83, 60, 9)
- **Evidence** - real scenes, numbers, quotes, examples available to show it (15, 73, 96)
- **Emotion target** - the single feeling to leave behind (22, 1, 68)
- **Constraints** - brand, length, deadline, culture, language, accessibility, ethics (35, 26)
- **Existing material** - copy, data, brand rules, references, and anti-references
- **Non-goals** - what it must not say or not look like

Extraction rules:

- Accept partial answers. If they do not know, record it as an open question rather than pushing.
- Ask at most three rounds. If the user says "use your judgment", stop and proceed with labelled assumptions.
- In **Shape** and **Review** modes, read the artifact before round two; the artifact answers several questions already.
- Never invent facts, quotes, numbers, or outcomes. Anything not stated goes in the brief as `(assumed)`.

### Asking - use the native question tool

When the session has OpenCode's built-in `question` tool, the interview happens through it, not as typed questions in chat.

- One call per round, at most four questions. Each question carries a header of 2-4 words naming the topic, the question in a single sentence, and 3-5 options; every option gets a 1-5 word label plus a one-line description of what choosing it commits them to.
- Options are concrete and mutually exclusive, and they come from what the user already told you - never generic probes.
- Always leave an exit: an option like "Mixed - I'll explain", or the tool's own custom-answer input, so nothing they mean goes unrecorded.
- Keep the questions independent, so one unanswered screen cannot stall the rest.
- Feed the returned answers straight into the brief fields; whatever is still open becomes round two.

If the tool is not available in the session, ask the same questions in chat as one compact numbered batch of at most four, then move on.

## Phase 2 - Confirm the brief

Fill `templates/story-brief.md` from the answers and hand it back in 6-8 compressed lines. Ask for confirmation once, then move on. Do not re-interview.

## Phase 3 - Select the toolkit

Selection rules:

1. **Spine first.** Pick 4-6 principles that define the story: usually one conflict/problem, one structure, one emotion principle, one showing/evidence principle, one close.
2. **Add by situation only.** A principle earns a place when it changes a concrete decision in this artifact.
3. **Cover at least three of the five categories.** Structure alone is a skeleton; Emotion alone is a mood.
4. **Cap at 15.** If over, cut the ones that would not change the work.
5. **Depth over coverage.** Three principles applied to the artifact beat fifteen named in a list.

Where to look:

- A playbook matches the user's words -> load `references/playbooks.md`, then only the category files the playbook names.
- No playbook fits -> scan `references/principles-index.md`, then open the category files for the entries you shortlist.
- The user names a principle or asks to see the full set -> show `references/principles-index.md` grouped by category, then narrow with them.
- Need the reasoning behind an entry -> the five category files in `references/`.

Load only what the current step needs. Never paste all 100 principles into the conversation.

## Phase 4 - Deliver

Fill `templates/story-plan.md`. The parts that matter:

- **Through-line** - message, protagonist, conflict, transformation, feeling.
- **Narrative arc** - beats mapped onto the artifact's real sections, so the plan can be executed top to bottom.
- **Toolkit table** - principle, why it fits this brief, and the change it forces.
- **Concrete edits** - numbered, ordered by impact, with the actual words or structure where possible.
- **What to cut** - diluting elements, each with the principle that condemns it.
- **Next test** - the cheapest check that would prove or disprove the plan.

If the user wants the artifact produced, apply the plan after it is agreed. The plan comes first so edits are made for a reason.

## Phase 5 - Quality checks

Tick before saying it is done:

- A stranger can state the message after five seconds.
- The beginning and the end are visibly different states (12).
- There is a conflict or stake, not a description (11, 88).
- At least one moment shows instead of telling (73).
- The protagonist is the audience or their client (83).
- The peak lands where memory concentrates; the ending is engineered (86).
- One clear next step (7).
- Claims are evidenced; nothing invented (26, 96).
- Jargon and clutter removed; nothing that does not serve the story (43, 79, 1).
- It works for the actual reader's culture, language, and access needs (35).

In **Review** mode, rank findings by impact and cap them at ten.

## Guardrails

- These are study summaries, not the book. Do not quote the source text; apply it.
- If the user publishes derived work commercially, credit *Universal Principles of Storytelling for Designers* by Lyle H. Sandler.
- Do not recommend a principle to sound knowledgeable. If it changes nothing in the artifact, leave it out.
- Do not optimise output length. The plan must be complete, not terse.

## Files

- `README.md` - overview, install line, and source note for anyone landing on the folder.
- `references/playbooks.md` - 15 need-based recipes: what the user wants to tell -> which principles.
- `references/principles-index.md` - all 100 principles with a one-line summary, for routing.
- `references/literary-device.md` (24) - conveying meaning and influencing emotion.
- `references/structure.md` (21) - sequencing the narrative.
- `references/emotion.md` (15) - what moves people to transform.
- `references/psychology-philosophy.md` (19) - how people receive and respond.
- `references/methods-tools.md` (21) - the working mechanics.
- `templates/story-brief.md` - the intake record.
- `templates/story-plan.md` - the delivery format.
- `examples/worked-examples.md` - two briefs carried through to a plan.
