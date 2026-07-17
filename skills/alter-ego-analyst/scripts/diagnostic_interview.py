#!/usr/bin/env python3
"""
Alter Ego Analyst - Diagnostic Questionnaire Engine

This script runs the interactive diagnostic interview to gather all necessary
information for creating a comprehensive Alter Ego Profile.

Usage:
    python scripts/diagnostic_interview.py [--output-dir PATH] [--subject-name NAME]
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

# --- Diagnostic Questions ---

DIAGNOSTIC_SECTIONS = [
    {
        "id": "subject_identity",
        "title": "[1] Subject Identity",
        "description": "Who is this Alter Ego for? Define the core subject.",
        "questions": [
            {"key": "subject_name", "prompt": "What is the subject's name? (Can be yourself, a character, a team, a brand)", "type": "text", "required": True},
            {"key": "subject_role", "prompt": "What is their primary role/identity? (e.g., CEO, athlete, artist, student, parent)", "type": "text", "required": True},
            {"key": "subject_context", "prompt": "Brief context: What do they do? What's their current situation?", "type": "textarea", "required": True},
        ]
    },
    {
        "id": "field_of_play",
        "title": "[2] Field of Play (The Arena)",
        "description": "Where does the transformation need to happen? Be specific.",
        "questions": [
            {"key": "field_name", "prompt": "Name the specific Field of Play (e.g., 'Boardroom Q4 Pitch', 'Championship Tennis Match', 'Family Dinner', 'Investor Demo Day')", "type": "text", "required": True},
            {"key": "field_description", "prompt": "Describe the environment: physical space, audience, stakes, duration, frequency", "type": "textarea", "required": True},
            {"key": "moment_of_impact", "prompt": "What is the EXACT Moment of Impact? (The single highest-stakes action: 'Closing the $500k deal', 'Serving for match point', 'Setting boundary with teenager')", "type": "text", "required": True},
        ]
    },
    {
        "id": "enemy_diagnosis",
        "title": "[3] The Enemy (Internal Forces)",
        "description": "Identify what holds the subject back. This becomes the antagonist the Alter Ego defeats.",
        "questions": [
            {"key": "common_forces", "prompt": "Which common forces apply? (Select all: lack_of_confidence, worrying_opinions, doubting_abilities, bad_attitude, fear_failure, procrastination, other)", "type": "multiselect", "options": ["lack_of_confidence", "worrying_opinions", "doubting_abilities", "bad_attitude", "fear_failure", "procrastination", "other"], "required": True},
            {"key": "hidden_forces", "prompt": "Which hidden forces apply? (Select all: imposter_syndrome, personal_trauma, tribal_narratives, perfectionism, comparison_trap, other)", "type": "multiselect", "options": ["imposter_syndrome", "personal_trauma", "tribal_narratives", "perfectionism", "comparison_trap", "other"], "required": True},
            {"key": "enemy_name", "prompt": "Give your Enemy a NAME and FORM. Make it small/cute (Beagle, Suzie) OR fierce (Igor, The Saboteur). What do you call it?", "type": "text", "required": True},
            {"key": "enemy_weapon", "prompt": "What is the Enemy's favorite weapon? (e.g., 'whispers you're not ready', 'replays past failures', 'makes you over-prepare and freeze')", "type": "text", "required": True},
            {"key": "enemy_trigger", "prompt": "When does the Enemy typically appear? (Specific triggers: 'Right before speaking', 'When I see the competitor', 'Sunday night before work week')", "type": "text", "required": True},
        ]
    },
    {
        "id": "superpowers",
        "title": "[4] Superpowers (Target Traits)",
        "description": "The exact 3 traits the Alter Ego must embody to win on this Field of Play.",
        "questions": [
            {"key": "wish_prompt", "prompt": "Complete: 'I wish I was ______, ______, and ______ in this moment.'", "type": "text", "required": True},
            {"key": "superpower_1", "prompt": "Superpower 1 (adjective):", "type": "text", "required": True},
            {"key": "superpower_2", "prompt": "Superpower 2 (adjective):", "type": "text", "required": True},
            {"key": "superpower_3", "prompt": "Superpower 3 (adjective):", "type": "text", "required": True},
            {"key": "why_these", "prompt": "Why these three? How do they directly defeat the Enemy and win the Moment of Impact?", "type": "textarea", "required": True},
        ]
    },
    {
        "id": "archetype_selection",
        "title": "[5] Archetype / Avatar Selection",
        "description": "Choose the inspirational source that already embodies your Superpowers.",
        "questions": [
            {"key": "archetype_category", "prompt": "Primary category:", "type": "select", "options": ["superhero", "historical_figure", "fictional_character", "animal", "machine_object", "family_ancestor", "composite", "mythological", "other"], "required": True},
            {"key": "archetype_name", "prompt": "Specific name(s): (e.g., 'Black Panther', 'Winston Churchill', 'Hermione Granger', 'Wolf', 'Locomotive', 'My grandmother', 'Composite: Payton + Lott = Geronimo')", "type": "text", "required": True},
            {"key": "archetype_traits", "prompt": "What SPECIFIC traits do you borrow from this archetype? (e.g., 'T'Challa's regal stillness', 'Churchill's rhetorical thunder', 'Wolf's pack loyalty')", "type": "textarea", "required": True},
            {"key": "deep_mapping", "prompt": "Deep Mapping -- Describe the archetype's: mannerisms, beliefs, style, voice, energy. Write as if you ARE them.", "type": "textarea", "required": True},
        ]
    },
    {
        "id": "origin_story",
        "title": "[6] Heroic Origin Story",
        "description": "The 'moving cause' -- why does this Alter Ego exist?",
        "questions": [
            {"key": "origin_type", "prompt": "Origin driver:", "type": "select", "options": ["trauma_driven", "destiny_driven", "altruism_driven", "self_expression_driven", "mastery_driven", "legacy_driven"], "required": True},
            {"key": "origin_narrative", "prompt": "Write the Origin Story (2-3 paragraphs). Include: the wound/call, the realization, the vow. Make it emotionally resonant.", "type": "textarea", "required": True},
        ]
    },
    {
        "id": "naming",
        "title": "[7] Naming the Alter Ego",
        "description": "A name gives shape and structure to the identity.",
        "questions": [
            {"key": "naming_style", "prompt": "Preferred naming style:", "type": "select", "options": ["combined_sources", "title_based", "adjective_based", "symbolic", "acronym", "other"], "required": True},
            {"key": "proposed_names", "prompt": "Propose 3-5 name candidates. Rank them.", "type": "textarea", "required": True},
            {"key": "final_moniker", "prompt": "Final chosen Moniker:", "type": "text", "required": True},
            {"key": "moniker_meaning", "prompt": "What does this name mean? Why does it resonate?", "type": "textarea", "required": True},
        ]
    },
    {
        "id": "totem_artifact",
        "title": "[8] Totem / Artifact (The Physical Anchor)",
        "description": "The physical object that triggers the transformation via enclothed cognition.",
        "questions": [
            {"key": "totem_category", "prompt": "Category:", "type": "select", "options": ["wearable", "carried", "environmental", "x_pill", "composite"], "required": True},
            {"key": "totem_object", "prompt": "Specific object: (e.g., 'signet ring', 'fountain pen', 'baseball cap', 'Tic Tac', 'boardroom chair')", "type": "text", "required": True},
            {"key": "totem_symbolism", "prompt": "What does it symbolize? How does it represent your Superpowers? (Personal meaning -- doesn't need to be obvious to others)", "type": "textarea", "required": True},
            {"key": "totem_availability", "prompt": "Is it available EVERY time on this Field of Play? If not, what's the backup?", "type": "text", "required": True},
            {"key": "totem_reset", "prompt": "Reset protocol: How do you quickly remove and re-apply it mid-performance if focus slips?", "type": "text", "required": True},
            {"key": "totem_positive_assoc", "prompt": "Do you genuinely ENJOY this object? (If no, choose another -- negative association strips power)", "type": "boolean", "required": True},
        ]
    },
    {
        "id": "activation_sequence",
        "title": "[9] Activation Sequence (The Phone Booth Moment)",
        "description": "The exact ritual to step into the Alter Ego.",
        "questions": [
            {"key": "threshold", "prompt": "Physical/mental threshold: (e.g., 'Office door', 'Locker room entrance', 'Stage wings', 'Front door at home')", "type": "text", "required": True},
            {"key": "incantation", "prompt": "Pre-entry Command Phrase (internal, 1-3 words): (e.g., 'Now.', 'Activate.', 'It's time.', 'Genesis.')", "type": "text", "required": True},
            {"key": "internal_affirmation", "prompt": "Internal Affirmation (spoken silently while activating): (e.g., 'I am [Name], and I am here to [purpose].')", "type": "text", "required": True},
            {"key": "physical_anchor", "prompt": "Physical Anchor movement: (e.g., 'Three deep breaths', 'Adjust ring', 'Knuckle crack', 'Shoulder roll', 'Specific exhale')", "type": "text", "required": True},
            {"key": "ground_punch_phrase", "prompt": "Ground Punch / Curb Kick phrase for when Enemy appears: (e.g., 'Not today, Fear.', 'Suzie, get off my court.')", "type": "text", "required": True},
            {"key": "response_proclamation", "prompt": "Response Proclamation to 'Who do you think you are?': (Based on past wins/grit)", "type": "text", "required": True},
        ]
    },
    {
        "id": "behavioral_specs",
        "title": "[10] Behavioral Specs (Code of Conduct)",
        "description": "How the Alter Ego physically and verbally operates.",
        "questions": [
            {"key": "stance", "prompt": "Stance/Posture: (e.g., 'Feet planted, shoulders back, weight balanced -- Radiant Stillness')", "type": "text", "required": True},
            {"key": "vocal_tone", "prompt": "Vocal Tone: (e.g., 'Lower register, measured pace, 2-second pause before speaking')", "type": "text", "required": True},
            {"key": "breathing", "prompt": "Breathing Pattern: (e.g., '4-7-8 before entry; box breathing during tension')", "type": "text", "required": True},
            {"key": "eye_contact", "prompt": "Eye Contact Style: (e.g., 'Steady, unwavering, brief break every 7 seconds -- The X-Ray')", "type": "text", "required": True},
            {"key": "facial_expression", "prompt": "Default Facial Expression: (e.g., 'Subtle half-smile, relaxed brow -- calm authority')", "type": "text", "required": True},
            {"key": "movement_style", "prompt": "Movement Style: (e.g., 'Deliberate, efficient, direct pathing -- Alpha Velocity')", "type": "text", "required": True},
            {"key": "failure_response", "prompt": "Default Response to FAILURE: (e.g., 'Pause -> Breathe -> Recalibrate -> Execute')", "type": "text", "required": True},
            {"key": "tension_response", "prompt": "Default Response to HIGH TENSION: (e.g., 'Slow down further. Tension is data.')", "type": "text", "required": True},
            {"key": "criticism_response", "prompt": "Default Response to CRITICISM: (e.g., 'Listen fully -> Ask clarifying question -> Integrate or dismiss')", "type": "text", "required": True},
        ]
    },
    {
        "id": "linguistic_shift",
        "title": "[11] Linguistic Shift (Vocabulary Recode)",
        "description": "The words the Core Self uses that the Alter Ego bans, and the power phrases it owns.",
        "questions": [
            {"key": "forbidden_vocab", "prompt": "Forbidden Vocabulary (Core Self phrases to ELIMINATE): List 5-7. (e.g., 'I think...', 'I'll try...', 'Sorry to bother you', 'Does that make sense?', 'I'm just...', 'Maybe...')", "type": "textarea", "required": True},
            {"key": "command_vocab", "prompt": "Command Vocabulary (Alter Ego power phrases): List 5-7. (e.g., 'Here's the play...', 'The path forward is clear.', 'I am here to [purpose].', 'What does success look like?', 'Let's execute.')", "type": "textarea", "required": True},
            {"key": "reframe_examples", "prompt": "Reframe Examples: Show 3 situations where Core Self says X, Alter Ego says Y.", "type": "textarea", "required": True},
        ]
    },
    {
        "id": "integration_decompression",
        "title": "[12] Integration & Decompression",
        "description": "Boundaries and safe return to Core Self -- prevents burnout and identity bleed.",
        "questions": [
            {"key": "field_boundaries_active", "prompt": "When IS the Alter Ego active? (Specific times, places, contexts)", "type": "textarea", "required": True},
            {"key": "field_boundaries_inactive", "prompt": "When is the Alter Ego NOT active? (Times, places, contexts to avoid bleed)", "type": "textarea", "required": True},
            {"key": "decompression_steps", "prompt": "Decompression Ritual (5 steps in order):", "type": "textarea", "required": True},
            {"key": "grounding_activity", "prompt": "Post-decompression grounding activity: (e.g., 'Walk', 'Shower', 'Meal with family', 'Journal', 'Music')", "type": "text", "required": True},
            {"key": "five_bridges", "prompt": "Five Bridges to Progress -- Fill the table:", "type": "textarea", "required": True},
        ]
    },
    {
        "id": "habituation_plan",
        "title": "[13] Habituation Plan (The Journey to Unconscious Competence)",
        "description": "Structured practice to make the Alter Ego automatic.",
        "questions": [
            {"key": "quest_1_date", "prompt": "Coffee Shop Quest target date:", "type": "date", "required": False},
            {"key": "quest_2_date", "prompt": "Number Focus Game target date:", "type": "date", "required": False},
            {"key": "quest_3_date", "prompt": "Game Play Quest target date:", "type": "date", "required": False},
            {"key": "quest_4_date", "prompt": "Clean Slate Prompt journaling target date:", "type": "date", "required": False},
            {"key": "real_world_reps", "prompt": "Real-world practice schedule: (e.g., '3 team meetings/week as Alter Ego', '2 pitches/week')", "type": "text", "required": True},
            {"key": "tracking_method", "prompt": "How will you track progress? (e.g., 'Daily log', 'Weekly review', 'Accountability partner', 'App')", "type": "text", "required": True},
            {"key": "success_metrics", "prompt": "Success metrics at 30/60/90 days:", "type": "textarea", "required": True},
        ]
    },
    {
        "id": "evaluation_monitoring",
        "title": "[14] Evaluation & Monitoring Framework",
        "description": "Quantifiable metrics to measure Alter Ego effectiveness over time.",
        "questions": [
            {"key": "activation_speed_target", "prompt": "Target activation speed (seconds):", "type": "number", "required": True, "default": 5},
            {"key": "state_stability_target", "prompt": "Target state stability (minutes maintained without slippage):", "type": "number", "required": True, "default": 30},
            {"key": "slippage_tolerance", "prompt": "Max acceptable slippage count per session:", "type": "number", "required": True, "default": 2},
            {"key": "linguistic_compliance_target", "prompt": "Target linguistic compliance (% Command Vocab used, 0 Forbidden):", "type": "number", "required": True, "default": 100},
            {"key": "decompression_time_target", "prompt": "Target decompression time (minutes):", "type": "number", "required": True, "default": 15},
            {"key": "review_cadence", "prompt": "Review cadence: (e.g., 'Weekly self-review, Monthly deep-dive, Quarterly redesign')", "type": "text", "required": True},
            {"key": "redesign_triggers", "prompt": "What triggers a redesign? (e.g., 'New Field of Play', 'Enemy evolves', 'Superpowers insufficient', 'Identity bleed')", "type": "textarea", "required": True},
        ]
    }
]

# --- Interactive Interview Engine ---

def run_interview(subject_name: str = None) -> Dict[str, Any]:
    """Run the full diagnostic interview interactively."""
    print("\n" + "="*70)
    print("   ALTER EGO ANALYST -- DIAGNOSTIC INTERVIEW")
    print("   " + "="*70)
    print("\nThis interview builds your comprehensive Alter Ego Profile.")
    print("Answer thoughtfully -- depth creates power.\n")
    
    if subject_name:
        print(f"Subject: {subject_name}\n")
    
    responses = {
        "metadata": {
            "subject_name": subject_name or "Unknown",
            "interview_date": datetime.now().isoformat(),
            "version": "1.0"
        },
        "sections": {}
    }
    
    for section in DIAGNOSTIC_SECTIONS:
        print(f"\n{'='*70}")
        print(f"  {section['title']}")
        print(f"  {section['description']}")
        print(f"{'='*70}\n")
        
        section_responses = {}
        
        for q in section["questions"]:
            key = q["key"]
            prompt = q["prompt"]
            qtype = q.get("type", "text")
            required = q.get("required", True)
            options = q.get("options", [])
            default = q.get("default", None)
            
            while True:
                if qtype == "boolean":
                    suffix = " (y/n)" + (f" [default: {'y' if default else 'n'}]" if default is not None else "")
                    ans = input(f"  {prompt}{suffix}: ").strip().lower()
                    if not ans and default is not None:
                        ans = 'y' if default else 'n'
                    if ans in ('y', 'yes', 'true', '1'):
                        section_responses[key] = True
                        break
                    elif ans in ('n', 'no', 'false', '0'):
                        section_responses[key] = False
                        break
                    print("    Please enter y/yes or n/no")
                    
                elif qtype == "select":
                    print(f"  {prompt}")
                    for i, opt in enumerate(options, 1):
                        print(f"    {i}. {opt}")
                    ans = input(f"  Select (1-{len(options)}): ").strip()
                    if not ans and default is not None:
                        ans = str(options.index(default) + 1)
                    try:
                        idx = int(ans) - 1
                        if 0 <= idx < len(options):
                            section_responses[key] = options[idx]
                            break
                    except:
                        pass
                    print(f"    Please enter a number 1-{len(options)}")
                    
                elif qtype == "multiselect":
                    print(f"  {prompt}")
                    for i, opt in enumerate(options, 1):
                        print(f"    {i}. {opt}")
                    ans = input(f"  Select numbers (comma-separated, e.g., 1,3,5): ").strip()
                    if not ans and default is not None:
                        section_responses[key] = default
                        break
                    try:
                        indices = [int(x.strip()) - 1 for x in ans.split(",")]
                        selected = [options[i] for i in indices if 0 <= i < len(options)]
                        if selected or not required:
                            section_responses[key] = selected
                            break
                    except:
                        pass
                    print(f"    Please enter valid numbers separated by commas")
                    
                elif qtype == "number":
                    suffix = f" [default: {default}]" if default is not None else ""
                    ans = input(f"  {prompt}{suffix}: ").strip()
                    if not ans and default is not None:
                        section_responses[key] = default
                        break
                    try:
                        section_responses[key] = int(ans)
                        break
                    except:
                        print("    Please enter a valid number")
                        
                elif qtype == "date":
                    suffix = " (YYYY-MM-DD, optional)" if not required else " (YYYY-MM-DD)"
                    ans = input(f"  {prompt}{suffix}: ").strip()
                    if not ans and not required:
                        section_responses[key] = None
                        break
                    try:
                        datetime.strptime(ans, "%Y-%m-%d")
                        section_responses[key] = ans
                        break
                    except:
                        print("    Please use YYYY-MM-DD format")
                        
                elif qtype == "textarea":
                    print(f"  {prompt}")
                    print("  (Enter text. Press Enter twice to finish.)")
                    lines = []
                    while True:
                        line = input("  ")
                        if line == "" and lines and lines[-1] == "":
                            break
                        lines.append(line)
                    ans = "\n".join(lines).rstrip()
                    if ans or not required:
                        section_responses[key] = ans
                        break
                    print("    This field is required")
                    
                else:  # text
                    suffix = f" [default: {default}]" if default is not None else ""
                    ans = input(f"  {prompt}{suffix}: ").strip()
                    if not ans and default is not None:
                        section_responses[key] = default
                        break
                    if ans or not required:
                        section_responses[key] = ans
                        break
                    print("    This field is required")
        
        responses["sections"][section["id"]] = section_responses
        print(f"\n  [OK] Section complete: {section['title']}")
    
    return responses


def generate_profile_markdown(responses: Dict[str, Any]) -> str:
    """Generate the comprehensive Alter Ego Profile .md document."""
    
    meta = responses["metadata"]
    s = responses["sections"]
    
    get = lambda section, key, default="": s.get(section, {}).get(key, default)
    
    subject_name = meta.get("subject_name", "The Subject")
    moniker = get("naming", "final_moniker", "The Alter Ego")
    interview_date = meta.get("interview_date", "")[:10]
    
    md = f"""# ALTER EGO PROFILE: {moniker.upper()}

> **Subject:** {subject_name}
> **Generated:** {interview_date}
> **Version:** 1.0 | **Status:** ACTIVE DEPLOYMENT
> **Classification:** CONFIDENTIAL -- For Subject Only

---

## EXECUTIVE SUMMARY

**The Mission:** Deploy `{moniker}` to dominate the **{get("field_of_play", "field_name", "Field of Play")}** by embodying **{get("superpowers", "superpower_1")}**, **{get("superpowers", "superpower_2")}**, and **{get("superpowers", "superpower_3")}** -- defeating the Enemy (**{get("enemy_diagnosis", "enemy_name")}**) at the Moment of Impact: **{get("field_of_play", "moment_of_impact")}**.

**Activation Key:** `{get("activation_sequence", "incantation")}` + **{get("totem_artifact", "totem_object")}** = **{moniker} ONLINE**

---

## PILLAR I: THE IDENTITY MATRIX

### The Moniker
**{moniker}**
*Meaning:* {get("naming", "moniker_meaning", "To be defined")}

### The Origin Story
{get("origin_story", "origin_narrative", "To be written")}

**Origin Driver:** {get("origin_story", "origin_type", "").replace("_", " ").title()}

### The Archetype Blend
| Component | Source | Borrowed Traits |
|:---|:---|:---|
| **Primary Archetype** | {get("archetype_selection", "archetype_name")} | {get("archetype_selection", "archetype_traits", "").split(chr(10))[0] if get("archetype_selection", "archetype_traits") else "--"} |
| **Category** | {get("archetype_selection", "archetype_category", "").replace("_", " ").title()} | -- |
| **Deep Mapping** | *Internalized* | {get("archetype_selection", "deep_mapping", "")[:200]}... |

---

## PILLAR II: BEHAVIORAL SPECS (THE CODE OF CONDUCT)

### Core Virtues
| # | Virtue | Why This Matters |
|:---|:---|:---|
| 1 | **{get("superpowers", "superpower_1")}** | {get("superpowers", "why_these", "").split(chr(10))[0] if get("superpowers", "why_these") else "Defined by subject"} |
| 2 | **{get("superpowers", "superpower_2")}** | {get("superpowers", "why_these", "").split(chr(10))[1] if len(get("superpowers", "why_these", "").split(chr(10))) > 1 else "Defined by subject"} |
| 3 | **{get("superpowers", "superpower_3")}** | {get("superpowers", "why_these", "").split(chr(10))[2] if len(get("superpowers", "why_these", "").split(chr(10))) > 2 else "Defined by subject"} |

### Body Language & Presence
| Channel | Specification |
|:---|:---|
| **Stance** | {get("behavioral_specs", "stance")} |
| **Vocal Tone** | {get("behavioral_specs", "vocal_tone")} |
| **Breathing** | {get("behavioral_specs", "breathing")} |
| **Eye Contact** | {get("behavioral_specs", "eye_contact")} |
| **Facial Expression** | {get("behavioral_specs", "facial_expression")} |
| **Movement Style** | {get("behavioral_specs", "movement_style")} |

### Default Response Patterns
| Trigger | Response Protocol |
|:---|:---|
| **Failure** | {get("behavioral_specs", "failure_response")} |
| **High Tension** | {get("behavioral_specs", "tension_response")} |
| **Criticism** | {get("behavioral_specs", "criticism_response")} |
| **Enemy Appearance** | 1. Name it -> 2. {get("activation_sequence", "ground_punch_phrase")} -> 3. Recommit to Mission |

---

## PILLAR III: THE ACTIVATION SEQUENCE

### The Threshold
**{get("activation_sequence", "threshold")}** -- *The boundary between Ordinary and Extraordinary World.*

### The Totem / Artifact
| Property | Specification |
|:---|:---|
| **Object** | {get("totem_artifact", "totem_object")} |
| **Category** | {get("totem_artifact", "totem_category", "").title()} |
| **Symbolism** | {get("totem_artifact", "totem_symbolism")} |
| **Availability** | {get("totem_artifact", "totem_availability")} |
| **Reset Protocol** | {get("totem_artifact", "totem_reset")} |
| **Positive Association** | {"OK" if get("totem_artifact", "totem_positive_assoc") else "NEEDS REVIEW"} |

### The Incantation / Command Phrase
| Phase | Phrase |
|:---|:---|
| **Pre-Entry** | `{get("activation_sequence", "incantation")}` |
| **Internal Affirmation** | `{get("activation_sequence", "internal_affirmation")}` |
| **Ground Punch** | `{get("activation_sequence", "ground_punch_phrase")}` |
| **Response Proclamation** | `{get("activation_sequence", "response_proclamation")}` |

### The Physical Anchor
**{get("activation_sequence", "physical_anchor")}** -- *Performed immediately after crossing the threshold.*

### Full Activation Protocol (Memorize This Sequence)
```
1. APPROACH the Threshold: {get("activation_sequence", "threshold")}
2. ENGAGE the Totem: Put on / pick up / touch {get("totem_artifact", "totem_object")}
3. BREATHE: {get("behavioral_specs", "breathing").split(";")[0] if get("behavioral_specs", "breathing") else "Deep breath"}
4. SPEAK: "{get("activation_sequence", "incantation")}"
5. AFFIRM: "{get("activation_sequence", "internal_affirmation")}"
6. ANCHOR: {get("activation_sequence", "physical_anchor")}
7. CROSS: Step into the Field of Play as {moniker}
8. EXECUTE: The Moment of Impact
```

---

## PILLAR IV: THE LINGUISTIC SHIFT

### FORBIDDEN VOCABULARY (Core Self -> BANNED)
{format_list(get("linguistic_shift", "forbidden_vocab"))}

### COMMAND VOCABULARY (Alter Ego -> NATIVE)
{format_list(get("linguistic_shift", "command_vocab"))}

### REFRAME EXAMPLES
{get("linguistic_shift", "reframe_examples", "To be documented during practice")}

> **Rule:** Every Forbidden word triggers an immediate internal correction to its Command counterpart. This is not optional -- it is the linguistic immune system.

---

## PILLAR V: INTEGRATION & DECOMPRESSION

### Field Boundaries
| State | Contexts |
|:---|:---|
| **ACTIVE** | {get("integration_decompression", "field_boundaries_active")} |
| **INACTIVE** | {get("integration_decompression", "field_boundaries_inactive")} |

### Decompression Ritual (MANDATORY -- Prevents Burnout & Identity Bleed)
{format_numbered_list(get("integration_decompression", "decompression_steps"))}

### Grounding Activity
**{get("integration_decompression", "grounding_activity")}**

### Five Bridges to Progress
{get("integration_decompression", "five_bridges")}

---

## HABITUATION PLAN: THE JOURNEY TO UNCONSCIOUS COMPETENCE

### Phase 1: Foundation Quests (Weeks 1-4)
| Quest | Target Date | Status | Purpose |
|:---|:---|:---|:---|
| **Coffee Shop Quest** | {get("habituation_plan", "quest_1_date", "TBD")} | Pending | Low-stakes public interaction as {moniker} |
| **Number Focus Game** | {get("habituation_plan", "quest_2_date", "TBD")} | Pending | 5-min concentration test as {moniker} |
| **Game Play Quest** | {get("habituation_plan", "quest_3_date", "TBD")} | Pending | Competitive game as {moniker} -- test resiliency |
| **Clean Slate Prompt** | {get("habituation_plan", "quest_4_date", "TBD")} | Pending | Journal: "If tomorrow were Day 1..." |

### Phase 2: Real-World Reps (Ongoing)
**Schedule:** {get("habituation_plan", "real_world_reps")}
**Tracking Method:** {get("habituation_plan", "tracking_method")}

### Phase 3: Success Metrics
| Timeline | Target |
|:---|:---|
| **30 Days** | {get("habituation_plan", "success_metrics").split(chr(10))[0] if get("habituation_plan", "success_metrics") else "Define at outset"} |
| **60 Days** | {get("habituation_plan", "success_metrics").split(chr(10))[1] if len(get("habituation_plan", "success_metrics").split(chr(10))) > 1 else "Review at 30-day mark"} |
| **90 Days** | {get("habituation_plan", "success_metrics").split(chr(10))[2] if len(get("habituation_plan", "success_metrics").split(chr(10))) > 2 else "Review at 60-day mark"} |

---

## EVALUATION & MONITORING FRAMEWORK

### Quantifiable KPIs
| Metric | Target | Current | How to Measure |
|:---|:---|:---|:---|
| **Activation Speed** | <= {get("evaluation_monitoring", "activation_speed_target")} sec | -- | Stopwatch: Totem touch -> State shift felt |
| **State Stability** | >= {get("evaluation_monitoring", "state_stability_target")} min | -- | Session log: Time until first slippage |
| **Slippage Count** | <= {get("evaluation_monitoring", "slippage_tolerance")} / session | -- | Tally: Enemy appearances per session |
| **Linguistic Compliance** | {get("evaluation_monitoring", "linguistic_compliance_target")}% Command / 0 Forbidden | -- | Post-session review / Observer feedback |
| **Decompression Time** | <= {get("evaluation_monitoring", "decompression_time_target")} min | -- | Timer: Field exit -> Grounding activity start |

### Review Cadence
**{get("evaluation_monitoring", "review_cadence")}**

### Redesign Triggers (Auto-Review Conditions)
{format_list(get("evaluation_monitoring", "redesign_triggers"))}

### Session Log Template
```
# SESSION LOG -- {moniker}

**Date:** ___________
**Field of Play:** ___________
**Duration:** ___________

**Activation Speed:** _____ sec
**State Stability:** _____ min
**Slippage Count:** _____
**Forbidden Words Used:** _____
**Command Words Used:** _____
**Decompression Time:** _____ min
**Identity Bleed (Y/N):** _____

**Performance Rating (1-10):** _____
**Notes / Wins / Adjustments:**
_________________________________
_________________________________
```

---

## QUICK-REFERENCE CARD (Print & Carry)

```
+---------------------------------------------+
|           {moniker.upper():^43} |
+---------------------------------------------+
|  TOTEM: {get("totem_artifact", "totem_object"):<35} |
|  TRIGGER: {get("activation_sequence", "incantation"):<34} |
|  ANCHOR: {get("activation_sequence", "physical_anchor"):<35} |
+---------------------------------------------+
|  VIRTUES: {get("superpowers", "superpower_1")[:12]:<12} {get("superpowers", "superpower_2")[:12]:<12} {get("superpowers", "superpower_3")[:12]:<12} |
|  STANCE: {get("behavioral_specs", "stance")[:35]:<35} |
|  VOICE: {get("behavioral_specs", "vocal_tone")[:35]:<35} |
+---------------------------------------------+
|  ENEMY: {get("enemy_diagnosis", "enemy_name"):<36} |
|  KICK: "{get("activation_sequence", "ground_punch_phrase")[:35]:<35}" |
+---------------------------------------------+
|  DECOMPRESS: {get("integration_decompression", "grounding_activity")[:35]:<35} |
+---------------------------------------------+
```

---

## APPENDIX: TECHNIQUE REFERENCE LIBRARY

### Diagnostic Techniques
- **Field of Play Model** -- 5-layer system (Core Self -> Field)
- **Enemy Naming** -- Psychological distance via personification
- **Five Whys** -- Root cause excavation
- **Target Mapping** -- Reverse-engineer from goal to Moment of Impact

### Architecture Techniques
- **Superpower Definition** -- "I wish I was..." + Power of Three
- **Archetype Selection** -- 7 categories (Superhero, Historical, Fictional, Animal, Machine, Ancestor, Composite)
- **Deep Mapping** -- Observer + Immersion techniques
- **Origin Story Crafting** -- 4 drivers (Trauma, Destiny, Altruism, Self-Expression)

### Materialization Techniques
- **Enclothed Cognition** -- Symbolic meaning + physical wear = performance shift
- **Totem Categories** -- Wearable (most potent) / Carried / Environmental
- **Four Mandatory Principles** -- Symbolism, Availability, Reset, Positive Association
- **Alter Ego X Pill** -- Placebo candy for inside-out activation

### Deployment Techniques
- **Activation Event** -- Phone Booth Moment ritual
- **Ground Punch** -- Curb Kick + Response Proclamation
- **Five Bridges** -- Stop/Less vs Start/Continue/More
- **Habituation Quests** -- Coffee Shop, Number Focus, Game Play, Clean Slate

### Maintenance Techniques
- **Self-Distancing** -- Third-person self-talk ("What would {moniker} do?")
- **Reset Protocol** -- Remove & re-apply totem mid-performance
- **Decompression Ritual** -- Structured return to Core Self
- **Parts Integration** -- Negotiate with Enemy rather than suppress

---

*Document generated by Alter Ego Analyst v1.0*
*Framework: Todd Herman's Alter Ego Effect + NLP + Performance Psychology*
*Classification: CONFIDENTIAL -- This document contains your psychological architecture.*

---

**END OF PROFILE**
"""
    return md


def format_list(text: str) -> str:
    """Format a text block as a markdown list."""
    if not text:
        return "*(none specified)*"
    lines = [line.strip() for line in text.split("\\n") if line.strip()]
    if not lines:
        return "*(none specified)*"
    return "\\n".join(f"- {line.lstrip('-* ').strip()}" for line in lines)


def format_numbered_list(text: str) -> str:
    """Format a text block as a numbered markdown list."""
    if not text:
        return "*(none specified)*"
    lines = [line.strip() for line in text.split("\\n") if line.strip()]
    if not lines:
        return "*(none specified)*"
    return "\\n".join(f"{i}. {line.lstrip('0123456789. ').strip()}" for i, line in enumerate(lines, 1))


def save_profile(profile_md: str, subject_name: str, output_dir: Path) -> Path:
    """Save the profile to a timestamped .md file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = "".join(c for c in subject_name if c.isalnum() or c in "_- ").strip().replace(" ", "_")
    filename = f"Alter_Ego_Profile_{safe_name}_{timestamp}.md"
    filepath = output_dir / filename
    filepath.write_text(profile_md, encoding="utf-8")
    return filepath


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Alter Ego Analyst -- Diagnostic Interview")
    parser.add_argument("--subject", "-s", help="Subject name (optional)")
    parser.add_argument("--output-dir", "-o", default=".", help="Output directory for profile")
    parser.add_argument("--input", "-i", help="Load responses from JSON file instead of interview")
    args = parser.parse_args()
    
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if args.input:
        print(f"[LOAD] Loading responses from: {args.input}")
        with open(args.input, 'r') as f:
            responses = json.load(f)
    else:
        responses = run_interview(args.subject)
        
        # Save raw responses for backup
        responses_file = output_dir / f"interview_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(responses_file, 'w') as f:
            json.dump(responses, f, indent=2)
        print(f"\n[SAVE] Raw responses saved to: {responses_file}")
    
    # Generate profile
    print("\n[GEN] Generating comprehensive Alter Ego Profile...")
    profile_md = generate_profile_markdown(responses)
    
    # Save profile
    profile_path = save_profile(profile_md, responses["metadata"]["subject_name"], output_dir)
    print(f"[OK] Profile saved to: {profile_path}")
    print(f"\n[INFO] Profile length: {len(profile_md):,} characters")
    print(f"[OK] Ready for deployment!")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
