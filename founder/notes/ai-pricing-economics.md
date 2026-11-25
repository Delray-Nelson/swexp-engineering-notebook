# AI Pricing Mechanics & Model Tier Economics

## 1. How API Token Pricing Works
API pricing is metered per token, separately for input and output:
- **Input tokens:** Everything in the context window—system prompt, rules, files, conversation history, and the current message. Re-sent and re-billed on every turn.
- **Output tokens:** Everything the model generates, including internal reasoning tokens on models that think before answering. Typically priced around **3x–5x higher** than input tokens.

### Two Mechanics That Dominate Real Bills
1. **Conversation costs compound:** Because the full history is re-sent on each turn, turn $N$ pays for turns $1$ through $N-1$ again as input. Long agent sessions are dominated by re-read context, making context curation and **prompt caching** (~90% discount on unchanged context prefixes) major cost controls.
   - *Caching rule:* Static rules files at the top of the prompt cache cleanly; putting dynamic values like timestamps in the system prompt invalidates prefix caching every turn.
2. **Output is expensive and includes thinking:** Reasoning-heavy requests on 2026 models can spend more tokens thinking than answering. Effort controls (`low` / `medium` / `high`) act directly as **cost knobs**, not just quality knobs.
3. **Seat subscriptions vs. product APIs:** Flat-ish seat tools (e.g., Claude Code, Cursor) bundle these economics into usage limits, whereas building AI features into a product exposes you directly to per-token unit economics.

---

## 2. Runnable Pricing Arithmetic (`python:3.12-slim` Reference)
Never estimate unit economics in your head—keep pricing math in a runnable script that can be updated when vendor rates change.

```python
PRICES = {  # (input $/M, output $/M) — mid-2026 published reference tiers
    "frontier (e.g. Claude Fable 5)": (10.00, 50.00),
    "flagship (e.g. Claude Opus 4.8)": (5.00, 25.00),
    "mid-tier (e.g. Claude Sonnet 5)": (3.00, 15.00),
    "small (e.g. Claude Haiku 4.5)": (1.00, 5.00),
}

def cost(tier, input_tokens, output_tokens):
    inp, out = PRICES[tier]
    return input_tokens / 1_000_000 * inp + output_tokens / 1_000_000 * out

if __name__ == "__main__":
    scenarios = [
        ("Scenario A: single code review (40k in / 3k out)", 40_000, 3_000, 1),
        ("Scenario B: 500 reviews/day x 30 days (15,000 reqs)", 40_000, 3_000, 15_000),
        ("Scenario C: ticket classification (1.2k in / 20 out x 100k)", 1_200, 20, 100_000),
    ]
    for label, inp, out, count in scenarios:
        print(f"\n{label}")
        for tier in PRICES:
            total = cost(tier, inp, out) * count
            print(f"  {tier:35s} ${total:,.4f}")
