# Build Phase 3 — Stretch (1 hour)

## Goal

You have a working, polished app. Phase 3 is about **going further** — pick one or more stretch goals that interest you. There's no required path here; choose what excites you or what would make your demo stand out.

---

## Step 1: Plan and Generate Your Prompts (5-10 min)

Same workflow as before — follow the **Copilot Workflow Guide** (`copilot-workflow-guide.md`):

1. Use **Plan agent** to describe which stretch goal(s) you want to tackle
2. **Agent Mode** to break it into prompts
3. Have Copilot save them to `phase3-prompts.md`

---

## Stretch Goal Options

Pick **one or two** — don't try to do them all.

### Option A: Add Unit Tests

Use Copilot to generate tests for your validation logic.

**How:**
1. Open your validation file
2. Ask Copilot: *"Write unit tests for this validation logic. Cover passing cases, failing cases, and edge cases like empty input."*
3. Run the tests and make sure they pass

**Stack-specific test frameworks:**
- JavaScript: Jest or Vitest
- Python: pytest
- Java: JUnit
- .NET: xUnit or NUnit

> This is a great Copilot showcase — it can generate comprehensive tests in seconds.

---

### Option B: Support Multiple Document Types

Add a second document type with different validation rules.

**How:**
1. Add a dropdown or selector to your frontend for document type
2. Create a new set of validation rules for the second type
3. Route to the correct validator based on the selection

> **Copilot tip:** *"Add a document type selector with options for Invoice and HR Form. Route to different validation logic based on the selection."*

---

### Option C: Accept PDF Uploads

Replace form input with file upload and text extraction.

**How:**
1. Add a file upload input to the frontend
2. Send the file to the API
3. Extract text from the PDF using a library:
   - JavaScript: `pdf-parse`
   - Python: `pdfplumber` or `PyPDF2`
   - Java: Apache PDFBox
   - .NET: PdfSharpCore
4. Run your existing validation on the extracted text

> This is the hardest stretch goal — only attempt if you're comfortable with file handling.

---

### Option D: Build a Summary Dashboard

Show an overview of all validations run during the session.

**How:**
1. Store validation results in memory (an array on the server is fine)
2. Add a `/results` or `/dashboard` endpoint that returns all past results
3. Build a simple dashboard page showing: total runs, pass rate, most common errors

---

### Option E: Add Data Persistence

Save validation results so they survive a server restart.

**How:**
1. Write results to a JSON file or SQLite database
2. Add a GET endpoint to retrieve past results
3. Display history on the frontend

> **Copilot tip:** *"Add a simple SQLite database to store validation results. Save each result on POST and add a GET /history endpoint to retrieve them."*

---

### Option F: Create Copilot Customization Files

Build files that make Copilot smarter for your project — and take them back to your real work.

**Custom Instructions (`.github/copilot-instructions.md`):**
> Ask Copilot: *"Create a copilot-instructions.md file that defines project conventions: always validate required fields first, use the { valid, errors } response format, and follow [your coding style preferences]."*

**SKILL File:**
> Ask Copilot: *"Create a SKILL.md file that captures the validation patterns and domain knowledge from this project, so Copilot can apply them in future projects."*

**Custom Agent (`.agent.md`):**
> Ask Copilot: *"Create a custom agent called 'validation-expert' that knows our document schema, validation rules, and error format. It should help generate new validation rules that follow our patterns."*

These are reusable beyond the hackathon — they make Copilot better for your day-to-day work.

---

## Checkpoint

By the end of Phase 3:
- [ ] You tackled at least one stretch goal
- [ ] Your app does something it didn't at the end of Phase 2
- [ ] You're ready to demo

**Start preparing your demo.** Think about:
- What's the best way to show your app in 5 minutes?
- What was the most impressive Copilot moment?
- What did you learn about working with Copilot?
