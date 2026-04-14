# Build Phase 3 — Proctor Guide

## Your Role

Phase 3 is self-directed. Your job is to **help people pick the right stretch goal**, make sure nobody wastes time on a dead end, and **start nudging people toward demo prep** in the last 15 minutes.

---

## Timeline Check-ins

| Time Into Phase | Where They Should Be | Red Flag |
|-----------------|----------------------|----------|
| 10 min | Picked a stretch goal, have prompts | Can't decide what to do / still fixing Phase 2 bugs |
| 30 min | Making progress on stretch goal | Stuck on library installation or setup |
| 45 min | Stretch goal mostly working | Just getting started on the stretch goal |
| 1 hour | Wrapping up, preparing demo | App is broken |

---

## Helping People Choose

If someone asks "What should I do?", guide them based on where they are:

| Situation | Recommended Stretch Goal |
|-----------|--------------------------|
| Strong app, wants to impress | Unit tests (Option A) — easy win, great demo moment |
| Wants more business logic | Multiple document types (Option B) |
| Comfortable with file I/O | PDF upload (Option C) — high impact but higher risk |
| Interested in data | Dashboard or persistence (Option D/E) |
| Wants takeaways for real work | Copilot customization files (Option F) |

**Steer people away from PDF upload** unless they're confident and have time. Library installation issues can eat the entire hour.

---

## Common Issues

### Library Installation Failures
For PDF upload (Option C), participants may struggle with:
- `pdf-parse` / `pdfplumber` installation issues
- PDFBox Maven dependency resolution
- Binary dependencies for Tesseract (if they attempt OCR — discourage this)

**Nudge:** "If the library isn't installing in 5 minutes, pivot to a different stretch goal. Don't spend the hour debugging npm."

### Over-Scoping
Watch for people trying to do 3+ stretch goals. One done well is better than three half-finished.

**Nudge:** "Pick one and finish it — a completed feature demos much better than three broken ones."

### Forgetting Demo Prep
With 15 minutes left, actively remind people:
> "Start wrapping up! Think about what you want to show in your demo. You have 5 minutes to present — what's the story?"

---

## Copilot Customization Files (Option F)

If participants choose this option, here's what they should produce:

**Custom Instructions** (`.github/copilot-instructions.md`):
- Should contain 5-10 specific rules about the project's conventions
- Not generic advice — specific patterns from their project

**SKILL File**:
- Should capture domain knowledge (what the document fields mean, what valid/invalid looks like)
- Should be reusable in a different project

**Custom Agent** (`.agent.md`):
- Should have clear instructions and a defined purpose
- Test it by asking the agent to generate a new validation rule

If they're unsure how to start, suggest asking Copilot in Agent Mode to create the files based on the project.

---

## Last 15 Minutes: Demo Prep

Actively walk around (or message in chat) and remind everyone:

1. **Stop coding.** Get the app in a working state.
2. **Plan your demo flow.** What screens will you show? What data will you enter?
3. **Prepare test data** that shows both passing and failing validation.
4. **Think about your Copilot story.** What was the best moment? What surprised you?
5. **Make sure the app runs.** Do a full restart and test from scratch.

---

## Phase 3 Success Criteria

**It's OK if:** They only completed part of a stretch goal, or chose to polish Phase 2 instead.

**It's not OK if:** The app is broken for the demo. Help them revert any stretch goal changes that broke things.
