# Technical Writing Skill for Claude

A modular Claude skill for enterprise software technical writers. It applies the **Microsoft Manual of Style for Technical Writing (4th Edition)** and guides Claude through creating, editing, validating, and auditing documentation.

Built to be generic. Works with any product, any static site generator, and any documentation team. Runs a five-minute onboarding wizard to customize it for your company.

---

## Get Started in Two Ways

### Option A — Customize First (Recommended)

1. Open `customizer.html` in any browser
2. Answer five short question sets (about 3–5 minutes)
3. Click **Download All Files** on the final screen
4. Replace `SKILL.md`, `reference/style-rules.md`, and `reference/syntax.md` with the downloaded versions
5. Load the skill in Claude — done

### Option B — Use As-Is

1. Load `SKILL.md` as the Claude skill entry point
2. Claude will ask for your project details at the start of the first session

---

## What Is in the Box

```
writing-technical-docs/
├── README.md                 ← You are here
├── customizer.html           ← Browser-based onboarding wizard
├── SKILL.md                  ← Claude skill entry point (47 lines)
│
├── reference/                ← Loaded by Claude only when needed
│   ├── style-rules.md        ← Voice, tone, procedures, numbers, terminology
│   ├── ui-terms.md           ← UI verbs, preferred terms, grep patterns
│   ├── syntax.md             ← Admonitions, cross-references, page template
│   └── weights.md            ← Topic placement and nav weight categories
│
└── workflows/                ← One file per task; loaded only when relevant
    ├── create.md             ← Write a new doc page from scratch
    ├── edit.md               ← Edit a specific section of an existing page
    ├── validate.md           ← Check a doc for quality, style, and link issues
    ├── coverage.md           ← Find coverage gaps and stale UI labels
    └── impact.md             ← Find docs that need updating after code changes
```

The entry point (`SKILL.md`) is intentionally short. Claude loads reference and workflow files only when the task requires them, keeping the context window free for the actual work.

---

## The Customizer

`customizer.html` runs entirely in your browser — no server, no install, no internet connection needed.

**What it collects:**

| Step | Information |
|------|-------------|
| Company and Product | Company name, product name, support label, style guide choice |
| Doc Stack | Documentation root, static site generator, UI config file path, lint command |
| Style Preferences | Voice, heading capitalization, admonition syntax, company-specific term substitutions |
| Workflows | Toggle each of the five workflows on or off |
| Download | Generates pre-filled `SKILL.md`, `style-rules.md`, and `syntax.md` |

The downloaded files have your company name, product, style guide, and preferred terms built in. No find-and-replace needed.

---

## The Five Workflows

### A — Create New Page
Guides Claude through requirements gathering, topic placement, front matter, and content drafting. Follows the Concept → Task → Reference pattern. Runs validation at the end.

### B — Edit Existing Page
Reads the current file, confirms the scope, makes only the requested changes, and validates the edited file. Never edits beyond what was asked.

### C — Validate Documentation
The main quality-check workflow. Runs in five phases:

1. Pre-flight — confirms the target file exists and loads the UI config
2. Automated linting — runs the project lint command
3. Manual review — 13 checks covering prohibited terms, broken links, stale UI labels, admonition types, timeless language, active voice, procedure format, structure, word choice, trademark compliance, UI label accuracy, procedure completeness, and UX gaps
4. Self-check — removes duplicates and false positives before reporting
5. Report — Critical / Important / Advisory findings with line numbers, the user chooses what to fix

### D — Feature Coverage Analysis
Maps source modules to doc topics, identifies gaps, and cross-references UI labels against the navigation config to find stale references.

### E — Code-to-Docs Impact Analysis
Compares the last-changed dates of source modules and their corresponding doc topics. Flags docs that are out of date.

---

## Style Guide

The default reference is **Microsoft Manual of Style for Technical Writing (4th Edition)**. If your team uses a different guide, select it in the customizer — chapter citations in all generated files will update automatically.

### The Principles Behind the Rules

Every style rule in this skill exists to serve the reader. The skill applies rules with common sense:

- A passive construction that describes system behavior is **not** flagged
- A grep match is **a signal to look**, not an automatic finding
- Advisory findings are presented as options — the writer decides, not Claude
- Short, accurate docs are valued over long, comprehensive-looking ones

### Non-Negotiable Rules

These are flagged as Critical every time:

| Rule | Why It Matters |
|------|----------------|
| No master/slave, blacklist/whitelist | Inclusivity; industry standard |
| No broken links | A broken link is a failed user |
| Stale UI labels | Users click the wrong thing and lose trust |
| Trademark symbols on first mention | Legal requirement |

---

## Customizing Without the Wizard

**Change the style guide:** Replace all instances of `Microsoft Manual of Style (4th Edition)` and `MoS Ch.` in `SKILL.md` and `reference/style-rules.md` with your guide's name and citation format.

**Add preferred terms:** Add rows to the Preferred Terms table in `reference/ui-terms.md` and matching grep patterns to the Grep Patterns table.

**Change admonition syntax:** Update the admonition code blocks in `reference/syntax.md`.

**Add a feature-to-doc map:** Document the mapping between source module names and doc topic names in the session setup section of `SKILL.md`. Workflows D and E use this.

**Disable a workflow:** Delete or comment out the corresponding row in the Workflows table in `SKILL.md` and remove the workflow file.

---

## Requirements

- Claude with skill or system prompt support
- A documentation project using Markdown source files
- A static site generator (Hugo, MkDocs, Docusaurus, or equivalent)
- Git (for Workflows D and E)
- A UI navigation config file (for stale label checks in Workflows C and D)

---

## Design Decisions

| Decision | Reason |
|----------|--------|
| `SKILL.md` under 50 lines | Claude reads it fully on every turn; long entry points waste context |
| Reference files loaded on demand | Keeps the context window free for the actual doc work |
| One question at a time | Multiple questions in one message confuse the writer and slow things down |
| Report, don't enforce | The writer knows which findings matter in their context; Claude does not |
| Common sense over checklists | A 13-item checklist that flags passive system descriptions is noise, not help |

---

## License

Generic template. Adapt freely for your organization.
