# Workflow B: Edit Existing Page

Only change what the user asks for. Scope creep in editing introduces errors and erodes trust.

---

## Step 1: Confirm the Target

If the file has not been specified, ask: "Which file would you like to edit?" Wait for the answer.

---

## Step 2: Read Before You Touch Anything

- Read the full file
- Grep for cross-references (`](../`) to understand what links to this page and what it links to
- Read directly related topics if the edit could affect them

---

## Step 3: Show the Relevant Section

Present the section the user wants to change before making any edits. Confirm you have the right part.

If the request is ambiguous — for example, "fix the introduction" and there are two intro-style sections — ask which one before proceeding.

---

## Step 4: Make the Edit

- Change only what was requested
- Apply style rules from [reference/style-rules.md](../reference/style-rules.md) as you go
- If you notice an unrelated problem, note it separately — do not fix it without asking

---

## Step 5: Validate the Edited File

Run [Workflow C](validate.md) scoped to this file only. Do not re-validate the whole doc set.

**Validation loop:**
1. Make the edit
2. Check against style rules
3. If issues found → note each with line number → propose fix → confirm with user → apply
4. Repeat until clean

---

## Step 6: Present a Summary

Show what changed and any remaining findings. The user decides whether to address them.
