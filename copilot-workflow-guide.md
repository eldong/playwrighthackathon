# Copilot Workflow Guide: Plan → Prompt → Build

This is the core workflow you'll follow for each build phase. It keeps you in control, breaks work into manageable pieces, and gives you reusable prompts you can refer back to.

---

## The Pattern

### 1. Plan (Plan Agent)

Switch to **Plan agent** in Copilot and describe what you want to accomplish for this phase.

**Example for Phase 1:**
> "I want to build an invoice validator. I'll use React for the frontend and Express for the API. Help me plan the file structure, components, API endpoints, and the steps to get a working end-to-end flow."

**Example for Phase 2:**
> "I have a working invoice validator with a React frontend and Express API. Now I want to add validation rules for required fields, date checks, and amount validation. I also want to improve the results display with pass/fail indicators. Help me plan the steps."

Review the plan. Ask follow-up questions. Adjust until it makes sense.

### 2. Generate Step-by-Step Prompts (Agent Mode)

Switch to **Agent Mode** and ask Copilot to turn the plan into individual prompts:

> "Take this plan and break it down into a series of focused prompts I can use one at a time. Each prompt should tackle one piece — don't combine multiple steps. Don't execute them yet, just give me the list of prompts."

You should get back something like:
1. *"Set up a new Express project in the api/ folder with a package.json and basic server on port 3001"*
2. *"Create a React component with a form that has fields for vendor name, amount, date, and PO number"*
3. *"Add a POST /validate endpoint that accepts JSON and returns a validation response"*
4. *"Wire the form to call the API on submit and display the result"*

### 3. Save the Prompts to a Markdown File (Agent Mode)

**Important:** Still in **Agent Mode**, ask Copilot to save the prompts to a markdown file in your project:

> "Save these prompts as a checklist to a file called phase1-prompts.md in my project root."

Do this for each phase:
- `phase1-prompts.md`
- `phase2-prompts.md`

This gives you:
- A checklist to track progress
- A reference you can go back to if you get lost
- A record of your approach for the demo presentation
- Reusable prompts for future projects

You can check off each prompt as you complete it:
```markdown
# Phase 1 Prompts

- [x] Set up Express project in api/ folder
- [x] Create React form component with invoice fields
- [ ] Add POST /validate endpoint
- [ ] Wire form to API and display results
```

### 4. Execute One Prompt at a Time (Agent Mode)

Stay in **Agent Mode** and feed each prompt to Copilot individually. After each one:

- **Review** what Copilot generated — do you understand it?
- **Test** that it works — run the app, check the output
- **Check off** the prompt in your markdown file
- **Move to the next prompt**

If something doesn't work, paste the error into Copilot Chat and ask for help before moving on.

---

## Why This Pattern Works

- **You stay in control.** You're directing Copilot step by step, not hoping one big prompt works.
- **Each step is testable.** You can verify each piece works before building on it.
- **You learn as you go.** Reviewing each output builds understanding of the code.
- **You have a record.** The prompt markdown files document your journey for the demo.

---

## Repeat for Each Phase

Use this same pattern at the start of each build phase:
1. **Plan** what you want to accomplish in this phase
2. **Generate prompts** from the plan
3. **Save them** to a markdown file
4. **Execute** one at a time
