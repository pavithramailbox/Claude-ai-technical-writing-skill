# UI Verbs and Preferred Terms

The right word depends on what the user is actually doing. When in doubt, match the verb to the physical action.

---

## UI Verb Reference

| What the user does | Use | Avoid |
|--------------------|-----|-------|
| Press a button, link, tab, or icon | click | click on, tap, hit |
| Choose from a list, checkbox, radio button, or menu | select | highlight, pick, choose |
| Remove a checkbox or radio button selection | clear | deselect, uncheck |
| Type in a text field | enter or type | input, fill in, populate |
| Push a keyboard key | press | hit, type, click |
| Open a dialog, panel, or file | open | launch, invoke, trigger |
| Move between toggle states | turn on / turn off | toggle (as a verb) |
| Go somewhere in one step | go to | navigate |
| Go somewhere in multiple steps | navigate | go to |
| Move something by dragging | drag | click and drag, drag and drop |
| Show or hide a collapsible section | expand / collapse | open/close (save those for dialogs) |

Reference: MoS Ch. 7, Ch. 8

---

## UI Element Naming

Name the element by its label. Do not name the widget type.

| Correct | Avoid |
|---------|-------|
| Click **Save** | Click the **Save** button |
| In the **Name** field | In the **Name** text box |
| From the **Region** list | From the **Region** dropdown |
| On the **Overview** tab | On the **Overview** tab tab |

Other rules:
- Cards, not tiles
- Tooltip, not flyover or pop-up
- Do not document tooltip content unless it is the only place a constraint is explained

---

## Preferred Terms

| Avoid | Use | MoS |
|-------|-----|-----|
| click on | click | Ch. 7 |
| deselect / uncheck | clear | Ch. 7 |
| dropdown | list | Ch. 8 |
| launch / invoke | open (UI) or start (process) | Ch. 7 |
| highlight (for selection) | select | Ch. 7 |
| the user | you | Ch. 1 |
| we / our | [company or product name] | Ch. 1 |
| refer to | see | Ch. 7 |
| click here | [descriptive link text] | Ch. 7 |
| utilize | use | Ch. 7 |
| hence / thus | therefore or so | Ch. 7 |
| once (meaning "after") | after or when | Ch. 7 |
| out-of-the-box | built-in or preconfigured | Ch. 7 |
| setting up | configuring | Ch. 7 |
| let / permit | allow or enable | Ch. 7 |
| comprise / compose | include, contain, or consist of | Ch. 7 |
| editing (as a heading) | Modifying or Updating | Ch. 5 |
| end user | user | Ch. 7 |
| screenshot | screen shot | MoS Glossary |
| on-premise | on-premises | MoS Glossary |
| log on / logon | sign in / sign-in | MoS Glossary |

---

## Grep Patterns for Validation

Run these against `*.md` files to find likely violations. Always read the surrounding context before flagging — not every match is a real problem.

| Pattern | Likely issue | MoS |
|---------|--------------|-----|
| `(?i)\bclick on\b` | "click on" instead of "click" | Ch. 7 |
| `(?i)\bdeselect\b` | "deselect" instead of "clear" | Ch. 7 |
| `(?i)\bdropdown\b` | "dropdown" instead of "list" | Ch. 8 |
| `(?i)\blaunch\b` | "launch" instead of "open" (check: not inside code) | Ch. 7 |
| `(?i)\bhighlight\b` | "highlight" used for selection | Ch. 7 |
| `(?i)\binvoke\b` | "invoke" in non-developer context | Ch. 7 |
| `(?i)\bthe user\b` | "the user" instead of "you" | Ch. 1 |
| `(?i)\b(we|our|us)\b` | first-person plural (check: not inside code) | Ch. 1 |
| `(?i)\brefer to\b` | "refer to" instead of "see" | Ch. 7 |
| `(?i)\bclick here\b` | non-descriptive link text | Ch. 7 |

**Before flagging any grep match:** read the full sentence. `launch` in "the rocket launch sequence" is not a violation. `the user` in a quoted error message is not a violation. Use judgment.
