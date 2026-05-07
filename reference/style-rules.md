# Style Rules

The goal of every rule here is the same: make the doc easier for the reader. If applying a rule makes a sentence harder to understand, note it as advisory and explain the trade-off.

---

## Voice and Tone

**Write to the reader, not about them.**

Use imperative voice for instructions:
> Click **Save**. ✓
> The user clicks Save. ✗

Use active voice for explanations:
> The system sends a confirmation email. ✓
> A confirmation email is sent. ✗ (unless the agent is genuinely unknown)

Keep it human. Short sentences. Plain words. No jargon unless you've defined it.

Avoid time-stamped language outside release notes. "Currently," "new," "now," and "latest" age badly.

Reference: MoS Ch. 1

---

## Procedures

A procedure is a promise to the reader: follow these steps and you'll get the result. Break that promise and you lose trust.

**Location before action.** Tell people where to look before telling them what to do:
> In the **Settings** panel, click **Save**. ✓
> Click **Save** in the Settings panel. ✗

**Goal before step.** State why when it isn't obvious:
> To publish the record, click **Publish**.

**Expected results.** After any step that changes state (Save, Publish, Delete, Deploy, Create), tell the reader what they should see:
> The record appears in the list with **Draft** status.

**Procedural heading format.** Use a gerund phrase:
> Creating a Record ✓
> Create a Record ✗
> Editing a Record ✗ → use Modifying a Record or Updating a Record

Reference: MoS Ch. 6

---

## Headings

- Use **Title Case**: capitalize all major words; lowercase articles, prepositions under five letters, and coordinating conjunctions unless they open the heading
- Do not skip levels (H1 → H3 breaks screen readers and navigation)
- The static site generator renders H1 from front matter `title`; body headings start at H2

Reference: MoS Ch. 5

---

## Lists

- Parallel structure throughout — if the first item is a verb phrase, all items are verb phrases
- Capitalize the first word of each item
- Use a period only if the item is a complete sentence
- Bullet lists for unordered items; numbered lists when sequence matters

Reference: MoS Ch. 7

---

## Tables

- Introduce every table with a sentence before it — never drop a table in without context
- No punctuation in column headers
- Keep cells short; if a cell needs a paragraph, the table is the wrong format

Reference: MoS Ch. 7

---

## Numbers

- Spell out zero through nine; numerals for 10 and above
- Always use numerals for measurements: "3 MB," "10 minutes," "2 cores"
- Never start a sentence with a numeral — rewrite the sentence or spell out the number
- Percentages: 50% (no space)
- Four or more digits: use a comma — 1,024 not 1024

Reference: MoS Ch. 7

---

## Terminology

**Prohibited substitutions — no exceptions:**

| Avoid | Use |
|-------|-----|
| master / slave | primary / secondary |
| blacklist / whitelist | blocklist / allowlist |

**Define acronyms on first use:** "micro-frontend (MFE)" then "MFE" thereafter.

**Contractions:** fine in conversational docs and UI copy; avoid in formal reference material. Be consistent within a single document.

---

## Trademark and Brand Rules

- Apply the trademark symbol (® or ™) on the first mention of a registered name per topic
- Use the full, correct product name every time — no abbreviations unless the abbreviation is the official brand
- Never form possessives: "the architecture of [Product]" not "[Product]'s architecture"
- Always use the full support name (e.g. "Acme Support") — never shorten it

Reference: MoS Ch. 10

---

## What Not to Flag

Some things look like problems but aren't. Don't waste the user's time on these:

- Passive voice describing system behavior: "The file is uploaded" or "The field is required" — the system is the agent, passive is correct
- Style rules inside code fences — those are code, not prose
- Terms inside backticks — identifiers, not prose
- Example URLs in code blocks (`example.com`, `your-domain.com`) — these are intentional placeholders
- Missing H1 in the body — the SSG renders it from front matter
- A single sentence under a heading that serves as an introduction — that's fine
