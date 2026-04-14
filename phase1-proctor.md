# Build Phase 1 — Proctor Guide

## Your Role

During Phase 1, your main job is to **unblock people quickly** and **keep energy up**. Most participants will hit the same few issues. This guide covers what to watch for and how to help.

---

## Timeline Check-ins

| Time Into Phase | Where They Should Be | Red Flag |
|-----------------|----------------------|----------|
| 15 min | Have a plan, starting project setup | Still deciding on a use case or stack |
| 30 min | Project initialized, starting frontend | Stuck on tooling install or environment issues |
| 1 hour | Frontend form exists, starting API | No code written yet, or deep in CSS/styling |
| 1.5 hours | API responds, wiring frontend to API | Still building the form or hasn't started the API |
| 2 hours | End-to-end flow works with basic validation | Frontend and API not connected |

---

## Common Blockers & Quick Fixes

### Environment / Setup Issues
- **Node.js not installed or wrong version:** Help them install via `nvm` or direct download. Don't let them spend more than 5 min on this.
- **Python virtual environment confusion:** `python -m venv venv` then activate. If it's taking too long, skip the venv and install globally.
- **Java/Maven/Gradle issues:** Spring Initializr (start.spring.io) is the fastest path. Download a pre-configured zip.
- **.NET SDK not found:** Verify with `dotnet --version`. If missing, this is a pre-req failure — help them install or pivot to another stack.

### CORS Errors
The #1 blocker when frontend and API run on different ports. Quick fixes:
- **Express:** `npm install cors` then `app.use(cors())`
- **Flask:** `pip install flask-cors` then `CORS(app)`
- **Spring Boot:** `@CrossOrigin` annotation on the controller
- **.NET:** `builder.Services.AddCors()` in Program.cs

Have these snippets ready to paste.

### Copilot Not Helping
- **Copilot giving irrelevant suggestions:** They likely don't have enough context. Suggest using `#file` references in chat, or opening relevant files so Copilot can see them.
- **Copilot generating too much at once:** Encourage smaller, focused prompts. "Add a POST endpoint" is better than "Build my entire API."
- **Plan mode not available:** Make sure they're on the latest Copilot extension version.

### Frontend/API Not Connecting
- Check the port numbers match
- Check the fetch URL (common mistake: `localhost` vs `127.0.0.1`)
- Check that the API is actually running
- Check browser console for errors — paste them into Copilot Chat

---

## When to Intervene

**Do intervene if:**
- Someone has been stuck for 10+ minutes on the same issue
- Someone is going down a rabbit hole (e.g., setting up a database, adding authentication, elaborate CSS)
- Someone hasn't written any code after 30 minutes
- Someone is not using Copilot at all — gently remind them that's the point

**Don't intervene if:**
- They're making steady progress, even if slow
- They're experimenting with Copilot prompts and learning from the results
- Their approach is different from what you'd do — that's fine

---

## Nudges for People Who Are Stuck

If someone is frozen on where to start:
> "Start with the Plan agent — describe what you want to build and let Copilot outline the steps for you."

If someone is over-thinking the architecture:
> "Just get a form that submits to an endpoint and returns something. You can refactor later."

If someone is spending too much time on styling:
> "The form can be ugly — focus on getting data from the form to the API and back. We'll polish in Phase 2."

If someone is not using Copilot:
> "Try describing what you need in Copilot Chat — something like 'Create a POST endpoint that validates this JSON.' See what it gives you."

---

## Phase 1 Success Criteria

At the end of Phase 1, each participant should have:
1. A frontend with a form (even if basic)
2. An API endpoint that receives data
3. The frontend and API are connected
4. Some validation logic runs and results display

**It's OK if:** The UI is ugly, there's only one validation rule, error handling is minimal.

**It's not OK if:** There's no working connection between frontend and API — that's the core deliverable.
