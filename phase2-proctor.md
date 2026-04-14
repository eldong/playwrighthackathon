# Build Phase 2 — Proctor Guide

## Your Role

During Phase 2, participants should already have a working app. Your job shifts from **unblocking setup issues** to **keeping people focused on the right things** and helping them prioritize.

---

## Timeline Check-ins

| Time Into Phase | Where They Should Be | Red Flag |
|-----------------|----------------------|----------|
| 10 min | Have a Phase 2 plan and prompts saved | Still fixing Phase 1 bugs |
| 30 min | Adding validation rules | Over-engineering a single rule or going down a rabbit hole |
| 50 min | Working on results display | Still haven't added any new validation rules |
| 1 hour | Polishing UX | No visible improvements to results display |
| 1.5 hours | Testing edge cases, wrapping up | App is broken with no working demo |

---

## Common Issues

### Still Fixing Phase 1

If someone's Phase 1 isn't working yet:
- Help them get the minimum: form → API → response displayed
- Suggest simplifying: drop the frontend framework and use plain HTML + fetch
- Don't let them restart from scratch — fix what they have

### Over-Engineering Validation

Watch for people building overly complex validation frameworks:
- Regex patterns that are impossible to debug
- Generic validation engines instead of specific rules
- Trying to validate things that don't apply to their use case

**Nudge:** "You need 5-8 rules that work and produce clear messages. Simple if-statements are fine — this isn't production code."

### Spending Too Long on Styling

CSS rabbit holes are the #1 time sink in Phase 2.

**Nudge:** "Try adding Water.css with a single line — it makes any HTML look decent without custom CSS. Then move on to the results display."

Quick CSS wins to suggest:
- Water.css: `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">`
- Or just add 10 lines of basic CSS via Copilot: *"Add minimal styling to make this form look clean and readable"*

### Copilot Generating Inconsistent Code

If Copilot is generating code that doesn't match their existing patterns:
- Suggest adding a `copilot-instructions.md` file with project conventions (this is also a Phase 3 stretch goal)
- Use `#file` references to give Copilot context on existing code
- Remind them to review and adjust generated code, not just accept everything

---

## When to Intervene

**Do intervene if:**
- Someone is stuck on a Phase 1 issue — help them fix it fast so they can move to Phase 2
- Someone has been on CSS/styling for 20+ minutes
- Someone's validation logic is getting overly complex
- Someone's app is broken and they don't realize it

**Don't intervene if:**
- They're making different UX choices than you would
- They're adding creative validation rules you didn't expect
- They're spending time on the results display — that's the point of Phase 2

---

## Nudges

If someone doesn't know what rules to add:
> "Think about what would actually go wrong with a real [document type]. What would make you reject it?"

If someone's results display is just raw JSON:
> "Can you add a pass/fail banner and list each error as a bullet point? That's all you need."

If someone is moving fast:
> "Great progress — try submitting an empty form and see what happens. Then look at the Phase 3 stretch goals."

---

## Phase 2 Success Criteria

At the end of Phase 2, each participant should have:
1. Multiple validation rules (5+ ideally) with clear error messages
2. A results display that makes pass/fail obvious
3. At least one UX improvement beyond Phase 1

**It's OK if:** The styling is basic, there are only 3-4 rules, some edge cases aren't handled.

**It's not OK if:** The app looks the same as Phase 1 — some visible improvement should be there for the demo.
