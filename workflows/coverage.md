# Workflow D: Feature Coverage Analysis

This workflow answers: "Do we have a doc for everything users can actually do?" It also catches stale UI labels — menu items that were renamed in code but not updated in docs.

---

## Step 1: Map the Terrain (run in parallel)

1. List source code feature directories — exclude infrastructure and shared libraries
2. List directories under the documentation root
3. Parse the UI config file to get all current menu labels and routes

---

## Step 2: Build the Coverage Map

| Feature / Module | Doc Topic | Menu Label |
|------------------|-----------|------------|
| (populate from step 1) | | |

---

## Step 3: Find the Gaps

Report gaps in three categories — all informational, none treated as errors:

- **In the menu but no doc** — users can navigate there but will find nothing
- **Feature exists but no doc** — the capability is built but undocumented
- **Doc exists but no feature** — possibly stale; the feature may have been removed or renamed

---

## Step 4: Check for Stale UI Labels

Build the current label set from the UI config file. Grep doc Markdown for bold and quoted UI references. Cross-reference every match.

Use `git log --diff-filter=M -p -- [ui config file]` to find recent label renames. Suggest the corrected label with a line reference.

---

## Step 5: Present and Let the User Decide

Present the coverage map and stale label findings. Ask: "Which of these would you like to work on first?" Wait for the answer.

Do not prioritize gaps on behalf of the user — they know which features matter most right now.
