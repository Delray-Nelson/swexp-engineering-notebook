# Discovery Interview Script & Protocol

## Objective
Validate whether engineering and operations managers experience significant time loss and stress when manually correlating web traffic logs with application errors during outages, without revealing our product concept.

---

## Part 1 — Context & Warm-Up (5 min)
* **Goal:** Establish role, infrastructure scope, and team dynamics.
* "Walk me through your current tech stack and how your team monitors application health."
* "How do responsibilities split on your team when an unexpected failure occurs in production?"

---

## Part 2 — Recounting the Last Outage (15 min)
* **Goal:** Extract concrete past behavior rather than hypothetical opinions.
* "Tell me about the last time a critical application endpoint failed or went down."
* "How did you first find out about the issue? (Alert, customer complaint, internal check?)"
* "Take me step-by-step through how you investigated the root cause. What tools or commands did you open first?"
* "What was the hardest part about correlating what happened on the web server with what happened in the app logic?"

---

## Part 3 — Quantifying the Cost & Workarounds (10 min)
* **Goal:** Measure time, money, and emotional friction spent on existing solutions.
* "How long did it take from the moment the incident started to when you identified the root cause?"
* "How many engineers were pulled into the triage channel or war room?"
* "What tools do you currently pay for or use to handle log parsing, and where do they fall short?"
* "Why haven't you set up an automated pipeline or script to handle that correlation for you?"

---

## Part 4 — The Commitment Test (5 min)
* **Goal:** Gauge real intent vs. polite agreement.
* "We are researching this problem space deeply over the next two weeks. If I synthesize our findings into an anonymized benchmark report on how engineering teams handle log pipelines, can I send it to you?"
* "Who else on your team or in your network deals directly with log triage that I should talk to?"

