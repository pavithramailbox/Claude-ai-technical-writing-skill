# Workflow E: Code-to-Docs Impact Analysis

Code changes without doc updates create a gap between what the product does and what the docs say it does. This workflow finds that gap.

---

## Step 1: Find What Changed

```bash
git diff --name-only HEAD~10..HEAD
```

Group changed files by feature or module directory.

If the user wants a different commit range, ask: "Would you like to check a different range — for example, a specific branch or release tag?" Wait for the answer.

---

## Step 2: Map Modules to Doc Topics

Use the feature-to-doc map from the session setup. Exclude infrastructure and shared modules.

If a module cannot be mapped to a doc topic, note it as unmapped. Ask the user if they know the correct mapping before skipping it — do not silently drop it.

---

## Step 3: Check How Fresh the Docs Are

```bash
git log -1 --format="%ci %s" -- [module-path]
git log -1 --format="%ci %s" -- [doc-path]
```

Flag any doc that has not been updated since the last code change to its corresponding module.

---

## Step 4: Report

Present a table:

| Module | Doc Topic | Code Last Changed | Doc Last Changed | Status |
|--------|-----------|-------------------|------------------|--------|
| | | | | ✓ Current / ⚠ Stale |

Unmapped modules get their own section. Everything is informational.

---

## Step 5: Let the User Decide

Present the findings and ask: "Which of these docs would you like to review first?" Wait.

Do not assume priority. A stale admin doc for a minor config change may matter less than a stale getting-started page.
