# Syntax Reference

Adapt every example here to match the project's static site generator and front matter format.

---

## Front Matter

### Hugo
```yaml
---
title: 'Page Title'
service: 'User Guide'
weight: 30
---
```

### MkDocs
```yaml
---
title: Page Title
---
```

### Docusaurus
```yaml
---
id: page-title
title: Page Title
sidebar_position: 3
---
```

---

## Admonitions

Only two types: `note` and `caution`. A note gives useful context. A caution warns of data loss, irreversible actions, or security risk. Do not use caution for minor warnings — if it doesn't put data or access at risk, it's a note.

### Hugo
```
{{< admonition type="note" title="Note" >}}
Text here.
{{< /admonition >}}

{{< admonition type="caution" title="Caution" >}}
Text here.
{{< /admonition >}}
```

### MkDocs Material
```
!!! note
    Text here.

!!! warning
    Text here.
```

### Docusaurus
```
:::note
Text here.
:::

:::caution
Text here.
:::
```

---

## Cross-References

```markdown
For more information, see [Topic Name](../topic-name).
For more information, see [Specific Section](../feature-name#section-heading).
```

Rules:
- Use **see**, not "refer to"
- Use **about**, not "on": "information about indexes" not "information on indexes"
- Link text must describe the destination — never "click here" or "this page"
- Don't repeat the same cross-reference more than once per topic
- Don't create reference chains (A links to B which links to C to get the answer)

---

## Heading Slugs (Hugo default)

Slugs are auto-generated: lowercase, spaces become hyphens, non-`[a-z0-9-]` characters stripped, consecutive hyphens collapsed.

`## Manage Segmentation Units` → `#manage-segmentation-units`

Confirm slug behavior if using a different SSG — they differ.

---

## New Page Template

Use this as a starting point. Remove sections that don't apply — a short, accurate page beats a long, padded one.

```markdown
One or two sentences: what this feature does and why someone would use it.

## Prerequisites

- What the user needs before starting (access, data, another completed task)

## [Task Name — gerund phrase, e.g. "Creating a Record"]

1. In the **[Location]**, click **[Action]**.
2. Complete the required fields.

   Expected result: describe what the user sees.

3. Click **Save**.

   Expected result: The record appears in the list with **Draft** status.

[admonition if genuinely needed]

## Troubleshooting

| Problem | Solution |
|---------|----------|
| [specific error or symptom] | [concrete fix] |

## Related Topics

- [Topic Name](../topic-name)
```

**Pattern to follow:** Concept (what and why) → Task (how) → Reference (troubleshooting, related topics).

Keep the overview to two sentences. If you need more, the feature probably needs a dedicated overview page.
