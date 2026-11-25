"""Per-token workload cost and failure-adjusted routing model (Week 3 Lab)."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelSpec:
    provider: str
    tier: str
    input_per_m: float
    output_per_m: float
    acceptable_rate: float  # Honest estimated fraction of outputs meeting quality floor


# Current published rates as of November 2026 across two providers (Anthropic & OpenAI)
MODELS: dict[str, ModelSpec] = {
    "anthropic-fable-5.2": ModelSpec(
        provider="Anthropic",
        tier="frontier",
        input_per_m=8.00,
        output_per_m=40.00,
        acceptable_rate=0.98,
    ),
    "anthropic-opus-5.5": ModelSpec(
        provider="Anthropic",
        tier="flagship",
        input_per_m=4.00,
        output_per_m=20.00,
        acceptable_rate=0.96,
    ),
    "anthropic-sonnet-5.5": ModelSpec(
        provider="Anthropic",
        tier="mid-tier",
        input_per_m=2.00,
        output_per_m=10.00,
        acceptable_rate=0.92,
    ),
    "anthropic-haiku-5.5": ModelSpec(
        provider="Anthropic",
        tier="small",
        input_per_m=0.10,
        output_per_m=0.50,
        acceptable_rate=0.80,
    ),
    "openai-gpt-6.2-astra": ModelSpec(
        provider="OpenAI",
        tier="flagship",
        input_per_m=4.00,
        output_per_m=20.00,
        acceptable_rate=0.96,
    ),
    "openai-gpt-6.2-sol": ModelSpec(
        provider="OpenAI",
        tier="mid-tier",
        input_per_m=1.00,
        output_per_m=5.00,
        acceptable_rate=0.91,
    ),
    "openai-gpt-6.1-terra": ModelSpec(
        provider="OpenAI",
        tier="small-mid",
        input_per_m=0.50,
        output_per_m=2.50,
        acceptable_rate=0.86,
    ),
    "openai-gpt-6-luna": ModelSpec(
        provider="OpenAI",
        tier="small",
        input_per_m=0.05,
        output_per_m=0.25,
        acceptable_rate=0.76,
    ),
}


def estimate_tokens_from_chars(char_count: int) -> int:
    """Rough rule of thumb: ~4 characters per token."""
    return max(1, round(char_count / 4))


def cost(model_key: str, input_tokens: int, output_tokens: int) -> float:
    spec = MODELS[model_key]
    return (input_tokens / 1_000_000) * spec.input_per_m + (
        output_tokens / 1_000_000
    ) * spec.output_per_m


def failure_adjusted_cost(model_key: str, input_tokens: int, output_tokens: int) -> float:
    """Expected cost per acceptable output: raw_cost / acceptable_rate."""
    spec = MODELS[model_key]
    if not (0 < spec.acceptable_rate <= 1.0):
        raise ValueError(f"Invalid acceptable_rate for {model_key}: {spec.acceptable_rate}")
    return cost(model_key, input_tokens, output_tokens) / spec.acceptable_rate


def main() -> None:
    # Real JBF Dating artifact measurement (chars / 4):
    # - System rubric + banter scoring rules: 1,480 chars -> ~370 tokens
    # - Sample 4-turn humor/lore banter exchange + persona context: 2,120 chars -> ~530 tokens
    # - Expected structured JSON evaluation + brief rationale output: 640 chars -> ~160 tokens
    rubric_chars = 1480
    exchange_chars = 2120
    expected_out_chars = 640

    jbf_input_tokens = estimate_tokens_from_chars(rubric_chars + exchange_chars)
    jbf_output_tokens = estimate_tokens_from_chars(expected_out_chars)
    monthly_requests = 15_000  # e.g., 500 banter evaluations/day x 30 days

    print(
        f"Measured JBF banter-eval workload: {jbf_input_tokens} in / "
        f"{jbf_output_tokens} out tokens ({monthly_requests:,} reqs/month)\n"
    )
    print(
        f"{'Model':24s} {'Raw/Req':>10s} {'Adj/Req':>10s} "
        f"{'Raw/Mo':>11s} {'Adj/Mo':>11s} {'Acc%':>6s}"
    )
    print("-" * 76)

    rows = []
    for key, spec in MODELS.items():
        raw_req = cost(key, jbf_input_tokens, jbf_output_tokens)
        adj_req = failure_adjusted_cost(key, jbf_input_tokens, jbf_output_tokens)
        rows.append((adj_req, raw_req, key, spec))

    for adj_req, raw_req, key, spec in sorted(rows):
        raw_mo = raw_req * monthly_requests
        adj_mo = adj_req * monthly_requests
        print(
            f"{key:24s} ${raw_req:9.6f} ${adj_req:9.6f} "
            f"${raw_mo:10.2f} ${adj_mo:10.2f} {spec.acceptable_rate*100:5.0f}%"
        )


if __name__ == "__main__":
    main()
