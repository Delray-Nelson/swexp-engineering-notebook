# Week 3 Lab — Price a Workload for Real (`cost_model.py`)

## 1. Setup & Providers
- Script saved in `founder/exercises/cost_model.py` as ongoing repo infrastructure.
- Uses current per-million token pricing across **Anthropic** (`Claude Fable 5.2`, `Opus 5.5`, `Sonnet 5.5`, `Haiku 5.5`) and **OpenAI** (`GPT-6.2 Astra`, `GPT-6.2 Sol`, `GPT-6.1 Terra`, `GPT-6 Luna`).

## 2. Measured Workload (JBF Banter & Lore Alignment Evaluator)
- Measured real prompt/rubric + multi-turn banter sample character counts using the `chars / 4` rule rather than guessing:
  - Rubric + banter scoring prompt (`1,480` chars $\approx 370$ tokens) + multi-turn banter exchange (`2,120` chars $\approx 530$ tokens) = **900 input tokens**.
  - Structured JSON score + rationale (`640` chars) = **160 output tokens**.
  - Modeled at **15,000 requests/month** (`500/day × 30 days`) `(assumption, confidence: low)`.

## 3. Failure-Adjusted Cost & Ranking Check
- `failure_adjusted_cost` divides raw per-request cost by each model's estimated `acceptable_rate` (the share of outputs meeting our scoring schema and nuance floor without rework/retries) `(assumption, confidence: low)`.
- While relative tier order mostly holds for short structured evaluations, higher failure rates on tiny models narrow their cost advantage if retries or fallback escalations are triggered—and on longer reasoning prompts, output/thinking tokens and failure retries shift economics much more sharply.

## 4. Run Command
```bash
docker run --rm -v "$PWD":/w -w /w python:3.12-slim python founder/exercises/cost_model.py
