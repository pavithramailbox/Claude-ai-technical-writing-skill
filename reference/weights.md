# Topic Weight Categories

Weight controls the order topics appear in the navigation. Lower number = appears earlier.

These are defaults. The project may use different ranges — confirm with the user if uncertain.

| Weight | Category | Typical topics |
|--------|----------|----------------|
| 10–20 | Getting started | Overview, intro, first steps |
| 30–50 | Core data | Schemas, data assets, business terms |
| 50–70 | Processing | Pipelines, feature management |
| 70–100 | Business logic | Rules, composition, approvals |
| 100–120 | Quality and operations | Testing, deployment |
| 120–130 | Administration | Access control, user management |
| 130+ | Reference and appendix | Operators, contact support, legal |

## Placing a New Topic

1. Identify the category that matches the topic's purpose
2. List the existing weights in that range
3. Suggest the midpoint between the two nearest neighbors
4. If a topic fits two categories equally, ask the user which fits best — do not guess

## Flags Worth Raising

- **Duplicate weights** — two topics at the same weight will display in unpredictable order
- **Gaps over 20** — a gap suggests a topic might be missing or miscategorized
- **Topics in the wrong category** — a getting-started topic at weight 110 is hard to find
