"""Break-even finder, 20-turn cache-aware session model, and two-model routing sketch."""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class TierRate:
    name: str
    input_per_m: float
    output_per_m: float
    acceptable_rate: float


RATES: dict[str, TierRate] = {
    "small": TierRate(
        name="small (e.g. Haiku / mini)",
        input_per_m=0.10,
        output_per_m=0.50,
        acceptable_rate=0.80,
    ),
    "mid": TierRate(
        name="mid-tier (e.g. Sonnet / mid)",
        input_per_m=2.00,
        output_per_m=10.00,
        acceptable_rate=0.92,
    ),
    "flagship": TierRate(
        name="flagship (e.g. Opus / flagship)",
        input_per_m=4.00,
        output_per_m=20.00,
        acceptable_rate=0.96,
    ),
}


def raw_request_cost(tier_key: str, input_tokens: int, output_tokens: int) -> float:
    r = RATES[tier_key]
    return (input_tokens / 1_000_000) * r.input_per_m + (
        output_tokens / 1_000_000
    ) * r.output_per_m


def break_even_requests(
    small_key: str,
    flagship_key: str,
    input_tokens: int,
    output_tokens: int,
    engineer_day_cost: float,
) -> tuple[float, int]:
    """Return (per_request_savings, ceiling_monthly_requests_for_1_eng_day)."""
    small_c = raw_request_cost(small_key, input_tokens, output_tokens)
    flag_c = raw_request_cost(flagship_key, input_tokens, output_tokens)
    diff_per_req = flag_c - small_c
    if diff_per_req <= 0:
        raise ValueError("Expected flagship cost per request to exceed small cost.")
    req_needed = math.ceil(engineer_day_cost / diff_per_req)
    return diff_per_req, req_needed


def session_20_turn_cache_comparison(
    tier_key: str,
    stable_context_tokens: int = 30_000,
    new_input_per_turn: int = 1_500,
    output_per_turn: int = 600,
    turns: int = 20,
    cache_read_multiplier: float = 0.10,
) -> tuple[float, float]:
    """Compare 20-turn session cost with no caching vs. 0.10x cached stable prefix."""
    r = RATES[tier_key]
    uncached_total = 0.0
    cached_total = 0.0

    for turn in range(1, turns + 1):
        # Prior turns' new inputs and outputs accumulate as history over turns
        prior_turns = turn - 1
        growing_history_tokens = prior_turns * (new_input_per_turn + output_per_turn)

        # Uncached: full stable context + growing history + current turn message billed at full input rate
        total_in_uncached = stable_context_tokens + growing_history_tokens + new_input_per_turn
        uncached_total += (total_in_uncached / 1_000_000) * r.input_per_m + (
            output_per_turn / 1_000_000
        ) * r.output_per_m

        # Cached: stable_context_tokens billed at 0.10x input rate; history + current prompt at full input rate
        cached_in_cost = (
            (stable_context_tokens / 1_000_000) * r.input_per_m * cache_read_multiplier
        )
        fresh_in_cost = (
            ((growing_history_tokens + new_input_per_turn) / 1_000_000) * r.input_per_m
        )
        out_cost = (output_per_turn / 1_000_000) * r.output_per_m
        cached_total += cached_in_cost + fresh_in_cost + out_cost

    return uncached_total, cached_total


def two_model_routing_comparison(
    small_key: str,
    flagship_key: str,
    input_tokens: int,
    output_tokens: int,
    escalation_rate: float = 0.15,
) -> tuple[float, float, float]:
    """Compute blended per-item cost vs single-small and single-flagship per-item cost."""
    small_c = raw_request_cost(small_key, input_tokens, output_tokens)
    flag_c = raw_request_cost(flagship_key, input_tokens, output_tokens)

    # Every routed item runs small once; escalated items also run flagship once
    blended_per_item = small_c + escalation_rate * flag_c
    return blended_per_item, small_c, flag_c


def main() -> None:
    print("=== 1. BREAK-EVEN FINDER ===")
    # Workload shape: 2,400 input tokens / 450 output tokens per banter-quality & lore check
    inp_t, out_t = 2_400, 450
    eng_day_rate = 800.00  # e.g., $800/engineer-day (~$200k/yr loaded equivalent)
    diff_per_req, breakeven_reqs = break_even_requests(
        "small", "flagship", inp_t, out_t, eng_day_rate
    )
    small_c = raw_request_cost("small", inp_t, out_t)
    flag_c = raw_request_cost("flagship", inp_t, out_t)
    print(f"Workload: {inp_t} in / {out_t} out | Engineer-day anchor: ${eng_day_rate:,.2f}")
    print(f"Small cost/req: ${small_c:.6f} | Flagship cost/req: ${flag_c:.6f}")
    print(f"Savings/req (small vs flagship): ${diff_per_req:.6f}")
    print(f"Break-even volume: {breakeven_reqs:,} requests/month\n")

    print("=== 2. CACHE-AWARE 20-TURN AGENT SESSION (30k STABLE CONTEXT) ===")
    for key in ("flagship", "mid"):
        uncached, cached = session_20_turn_cache_comparison(key, stable_context_tokens=30_000)
        savings = uncached - cached
        pct = (savings / uncached) * 100
        print(
            f"{RATES[key].name:30s} -> Uncached: ${uncached:.4f} | "
            f"Cached (0.1x): ${cached:.4f} | Saved: ${savings:.4f} ({pct:.1f}%)"
        )
    print()

    print("=== 3. TWO-MODEL ROUTING SKETCH (JBF BANTER MODERATION & LORE SCORER) ===")
    # Assume 1,200 in / 180 out tokens per banter turn; 15% of turns trigger deterministic escalation
    r_inp, r_out, esc_rate = 1_200, 180, 0.15
    blended, single_small, single_flag = two_model_routing_comparison(
        "small", "flagship", r_inp, r_out, escalation_rate=esc_rate
    )
    print(f"Per-turn workload: {r_inp} in / {r_out} out | Escalation rate: {esc_rate*100:.0f}%")
    print(f"Single small/item:    ${single_small:.6f}")
    print(f"Blended (15% esc):  ${blended:.6f}")
    print(f"Single flagship/item: ${single_flag:.6f}")


if __name__ == "__main__":
    main()
