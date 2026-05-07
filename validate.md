# Workflow C: Validate Documentation

The goal of validation is to find real problems that confuse or mislead readers — not to generate an impressive list of findings. Prioritize ruthlessly.

---

## Phase 1: Pre-Flight

- If no target has been given, ask: "Which file or directory would you like me to validate?" Wait.
- Confirm the file exists. If the glob returns unexpected results, ask before continuing.
- Load the UI config file if stale-label checks are in scope.
- Scope all checks to the specified file only if this was called from Workflow B.

---

## Phase 2: Run the Linter

Run the project's configured lint command. Report any errors and continue with manual review.

If the linter passes, it has already checked: terminology casing, broken links, missing files, H1 presence, minimum word count. Do not repeat those checks manually.

If the linter is unavailable or fails, manually check file-existence for relative links (Part B of item 2 below).

---

## Phase 3: Manual Checks

Work top to bottom. Stop and ask the user if context makes a finding ambiguous — do not guess.

### 1. Prohibited Terms
Grep `master|slave|blacklist|whitelist` in `*.md`. Flag every match. No exceptions.

### 2. Broken Links

**Part A — Anchor fragments** (always run, linter does not cover this):
- Grep `\]\([^)]*#[^)]+\)` to find all anchored links
- Extract headings from the target file, convert to slugs, check for a match
- Report mismatches: line number, anchor used, closest valid slug

**Part B — File paths** (only when linter is unavailable):
- Grep `\]\(\.\./[^)#]+\)` for relative paths; confirm each target exists
- Grep `!\[` for images; confirm each image path exists
- Skip external URLs and mailto — note them as unchecked

### 3. Stale UI Labels
Grep `\*\*[A-Z][^*]+\*\*` in doc files. Cross-reference each label against the UI config file. Use `git log --diff-filter=M -p -- [ui config file]` to catch recent renames. Flag labels that no longer match.

Do not flag:
- `**Save**`, `**Cancel**`, `**Apply**` — universal labels, not worth cross-referencing
- `**Prerequisites**`, `**Note**`, `**Draft**` — these are section labels or status names, not UI elements
- Labels that differ only by an optional parenthetical (e.g. doc says `**Description**`, code says `Description (optional)`) — note as informational, not a defect

### 4. Admonition Types
Grep `admonition type=`. Flag any value that is not `note` or `caution`.

### 5. Time-Stamped Language
Grep `currently|new|now|latest` (case-insensitive).
Do not flag matches inside release notes — they are intentional.

### 6. Active Voice in Instructions
Read the procedural sections. Flag passive voice only in sentences where the writer is the agent:
> ✗ "The schema is created by clicking **Save**."
> ✓ "Click **Save** to create the schema."

Do not flag passive voice that describes system behavior:
> ✓ "The file is uploaded automatically."
> ✓ "The field is required."

### 7. Procedure Format
Check that procedures follow: location before action, goal before action where purpose isn't obvious, and expected results after state-changing steps (Save, Publish, Delete, Deploy, Create). See [reference/style-rules.md](../reference/style-rules.md).

### 8. Structure
Check heading hierarchy (no skipped levels), list parallelism, and table introduction sentences.

### 9. Word Choice
Grep for terms in the Preferred Terms table — [reference/ui-terms.md](../reference/ui-terms.md). Read the context before flagging. A grep match is a signal to look, not an automatic finding.

### 10. Trademark Compliance
- Grep for the product name without a trademark symbol on its first mention per topic
- Grep `\w+'s` near trademarked names — flag possessive forms
- Check that the support name is spelled in full

### 11. UI Label Accuracy
For each bold procedural label (buttons, fields, dialog titles), check against the feature's i18n config or localized text file. Report mismatches with the line number, the doc label, and the closest code match.

Skip: universal labels (`**Save**`, `**Cancel**`), labels that are self-evidently correct, read-only or auto-populated fields.

### 12. Procedure Completeness
For each state-changing step, check whether the following sentence describes what the user sees. A step that says "Click **Publish**" and then moves to the next step without explaining what happens next leaves the reader wondering if they did it right.

Skip: steps with one or two trivial actions where the result is obvious (clicking **Cancel** closes the dialog — no need to say so).

### 13. UX Gaps (Informational Only)
Grep component templates for drawer, modal, tooltip, and confirmation dialog patterns. Note any significant UI interactions that the doc does not mention. Present as informational — the user decides whether to document them.

---

## Phase 4: Self-Check Before Reporting

For every finding, confirm:
- It has a line number and the exact text
- It has a MoS chapter reference
- It is assigned a priority tier
- It is not a false positive (re-read the context one more time)

Remove duplicates. If you are unsure whether something is a real problem, mark it advisory and explain your uncertainty.

---

## Phase 5: Report

Group findings by priority:

**Critical** — fix before publishing. Broken links, prohibited terms, stale UI labels that will confuse users, wrong admonition types.

**Important** — fix soon. Passive voice in instructions, missing expected results, timeless-language violations, heading hierarchy issues.

**Advisory** — worth considering. Word choice, paragraph length, undocumented UI patterns. The user may have good reasons to leave these as-is.

End with:
```
How would you like to proceed?
1. Fix all   2. Fix a category   3. Fix specific lines   4. Leave for now
```
