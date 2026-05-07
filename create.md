# Workflow A: Create New Page

Before writing a single word, make sure you understand what the user needs. A page written without context wastes everyone's time.

---

## Step 1: Gather Requirements

Ask the user for each missing input, **one question at a time**:

1. What does this feature do, and why would someone use it?
2. Who is the audience — administrator, end user, developer?
3. Are there related existing topics to link to?
4. Is there source material — a spec, a ticket, a UI mockup?

Do not move to Step 2 until you have clear answers to all four.

---

## Step 2: Determine Placement

- Identify the right weight category from [reference/weights.md](../reference/weights.md)
- Check what weights are already in use in that range
- Suggest the midpoint between the two nearest neighbors
- If the topic fits two categories, present both options and ask — do not guess

---

## Step 3: Create the File

- Filename: lowercase, hyphens, no spaces — `feature-name/index.md`
- If the intended name is ambiguous, confirm with the user before creating it

---

## Step 4: Write the Front Matter

Adapt to the project's SSG. See [reference/syntax.md](../reference/syntax.md) for examples.

---

## Step 5: Draft the Content

Use the new page template from [reference/syntax.md](../reference/syntax.md).

Follow this pattern: **Concept → Task → Reference**

- **Concept:** Two sentences maximum — what the feature does and why it matters
- **Task:** Step-by-step procedures with expected results after state-changing steps
- **Reference:** Troubleshooting table and related topic links

A short, accurate page is better than a long, padded one. If the overview needs more than two sentences, the feature probably needs a dedicated overview page.

---

## Step 6: Validate

Run [Workflow C](validate.md) scoped to the new file only. Present findings. The user decides what to address.
