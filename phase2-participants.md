# Build Phase 2 — Enhance (1.5 hours)

## Goal

By the end of this phase, your app should have **real validation logic** and a **polished user experience**. The ugly-but-working app from Phase 1 becomes something you'd be comfortable demoing.

---

## Step 1: Plan and Generate Your Prompts (10 min)

Follow the **Copilot Workflow Guide** (`copilot-workflow-guide.md`) again:

1. Use **Plan agent** to plan your Phase 2 enhancements — describe what you built in Phase 1 and what you want to improve
2. Switch to **Agent Mode** and break the plan into step-by-step prompts
3. Have Copilot save the prompts to a `phase2-prompts.md` file in your project

**Example Plan agent prompt:**
> "I have a working [use case] app with a [stack] frontend and API. The form submits data, the API validates it, and results display on screen. Now I want to: add more validation rules, improve the results display with pass/fail indicators, and improve the overall UX. Help me plan the steps."

---

## Step 2: Expand Validation Rules (30 min)

Add more meaningful business rules to your validation logic.

**Ideas by use case:**

| Use Case | Rules to Add |
|----------|-------------|
| Invoice | Amount within a range, date not more than 30 days old, vendor name minimum length, duplicate PO detection |
| HR Form | Start date before end date, department must be from a valid list, employee ID format check |
| ID Document | Expiry date in the future, document number regex pattern, issuing authority not empty |
| Expense Report | Each line item has a category, total matches sum of line items, no single item exceeds policy limit |

**Aim for 5-8 rules total.** Each rule should return a clear, human-readable error message.

> **Copilot tip:** *"Add these validation rules to my validator: [list your rules]. Return each error as a separate item in the errors array with a clear message."*

---

## Step 3: Improve Results Display (20 min)

Make validation results easy to understand at a glance.

**What to add:**
- A clear **pass/fail indicator** (green checkmark / red X, or a status banner)
- Individual error messages listed with which field they relate to
- A summary line (e.g., "3 of 5 checks passed")

> **Copilot tip:** *"Update the results display to show a green banner if all checks pass, or a red banner with a list of errors if validation fails. Show a summary of how many checks passed out of the total."*

---

## Step 4: Improve the User Experience (20 min)

Small UX improvements make a big difference in the demo.

**Pick a few of these:**
- Loading indicator while the API processes
- Disable the submit button while a request is in-flight
- Clear previous results when submitting again
- Form validation on the client side (e.g., required fields before submit)
- Helpful placeholder text in form fields
- Basic styling — even a simple CSS framework like Water.css (one line to add) makes a big difference

> **Copilot tip:** *"Add a loading spinner while the API request is in progress. Disable the submit button during the request and re-enable it when the response comes back."*

---

## Step 5: Test Edge Cases (10 min)

Try to break your own app:
- Submit an empty form — does it handle it gracefully?
- Submit invalid data types (text in a number field)
- Submit extremely long values
- What happens if the API is down?

Fix anything that crashes or produces confusing output.

> **Copilot tip:** *"What edge cases could break my validation? Add handling for empty submissions, invalid data types, and extremely long field values."*

---

## Checkpoint

By now you should have:
- [ ] 5-8 validation rules with clear error messages
- [ ] A results display with pass/fail indicators
- [ ] Basic UX improvements (loading state, client validation, etc.)
- [ ] Edge cases handled gracefully

**If you're ahead of schedule:** Move on to Phase 3 stretch goals — unit tests, multiple document types, or Copilot customization files.

**If you're behind:** Focus on making sure your existing validation rules produce clear, readable output. A few good rules with a clean display beats many rules with confusing output.
