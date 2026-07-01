"""
Q5. Rank these from fastest to slowest:
    O(n!), O(2^n), O(n log n), O(1), O(n^2), O(log n), O(n)

Answer (Fastest → Slowest):
    1. O(1)        — Constant
    2. O(log n)    — Logarithmic
    3. O(n)        — Linear
    4. O(n log n)  — Linearithmic
    5. O(n²)       — Quadratic
    6. O(2^n)      — Exponential
    7. O(n!)       — Factorial

Explanation:
    As n grows, each complexity class grows faster than the one above it.
    The "fastest" means it uses the fewest operations for large n.
"""

import math
import time


def compute_complexity_values(n: int) -> dict:
    """Compute the number of operations for each complexity at a given n."""
    values = {
        "O(1)": 1,
        "O(log n)": math.log2(n) if n > 0 else 0,
        "O(n)": n,
        "O(n log n)": n * math.log2(n) if n > 0 else 0,
        "O(n²)": n ** 2,
    }

    # Only compute these for small n (they grow astronomically)
    if n <= 25:
        values["O(2^n)"] = 2 ** n
    else:
        values["O(2^n)"] = float("inf")

    if n <= 15:
        values["O(n!)"] = math.factorial(n)
    else:
        values["O(n!)"] = float("inf")

    return values


def demonstrate_ranking():
    """Demonstrate the ranking with numerical comparisons."""
    print("=" * 70)
    print("Q5: Rank Complexities from Fastest to Slowest")
    print("=" * 70)
    print()

    # --- The Ranking ---
    print("ANSWER: Fastest → Slowest")
    print()
    ranking = [
        ("1", "O(1)", "Constant", "Hash table lookup, array access"),
        ("2", "O(log n)", "Logarithmic", "Binary search"),
        ("3", "O(n)", "Linear", "Linear search, single loop"),
        ("4", "O(n log n)", "Linearithmic", "Merge sort, Tim sort"),
        ("5", "O(n²)", "Quadratic", "Bubble sort, nested loops"),
        ("6", "O(2^n)", "Exponential", "Recursive Fibonacci (naive)"),
        ("7", "O(n!)", "Factorial", "Brute-force permutations (TSP)"),
    ]

    print(f"  {'Rank':>4}  |  {'Big O':>10}  |  {'Name':>14}  |  {'Example'}")
    print(f"  {'-'*4}  |  {'-'*10}  |  {'-'*14}  |  {'-'*35}")
    for rank, big_o, name, example in ranking:
        print(f"  {rank:>4}  |  {big_o:>10}  |  {name:>14}  |  {example}")

    print()

    # --- Numerical Comparison ---
    print("--- Numerical Comparison: Operations for Various n ---")
    print()

    header = f"  {'n':>5}  |  {'O(1)':>8}  |  {'O(log n)':>10}  |  {'O(n)':>10}  |  {'O(n log n)':>12}  |  {'O(n²)':>12}  |  {'O(2^n)':>15}  |  {'O(n!)':>15}"
    separator = f"  {'-'*5}  |  {'-'*8}  |  {'-'*10}  |  {'-'*10}  |  {'-'*12}  |  {'-'*12}  |  {'-'*15}  |  {'-'*15}"
    print(header)
    print(separator)

    for n in [1, 2, 5, 10, 15, 20, 25]:
        vals = compute_complexity_values(n)

        def fmt(v):
            if v == float("inf"):
                return "∞ (too large)"
            elif v > 1_000_000_000:
                return f"{v:.2e}"
            else:
                return f"{v:,.0f}"

        print(
            f"  {n:>5}  |  "
            f"{fmt(vals['O(1)']):>8}  |  "
            f"{fmt(vals['O(log n)']):>10}  |  "
            f"{fmt(vals['O(n)']):>10}  |  "
            f"{fmt(vals['O(n log n)']):>12}  |  "
            f"{fmt(vals['O(n²)']):>12}  |  "
            f"{fmt(vals['O(2^n)']):>15}  |  "
            f"{fmt(vals['O(n!)']):>15}"
        )

    print()

    # --- Visual Growth Comparison ---
    print("--- Visual Growth (bar chart for n=10) ---")
    print()
    n = 10
    vals = compute_complexity_values(n)

    # Normalize to fit in terminal (max bar = 50 chars)
    max_val = vals["O(n²)"]  # Use n² as max for display (2^n and n! are too large)

    visual_data = [
        ("O(1)", vals["O(1)"]),
        ("O(log n)", vals["O(log n)"]),
        ("O(n)", vals["O(n)"]),
        ("O(n log n)", vals["O(n log n)"]),
        ("O(n²)", vals["O(n²)"]),
    ]

    for name, val in visual_data:
        bar_len = max(1, int((val / max_val) * 50))
        print(f"  {name:>10}  |  {'█' * bar_len} ({val:,.1f})")

    # These are too large to display proportionally
    print(f"  {'O(2^n)':>10}  |  {'█' * 50}{'→':>1} ({vals['O(2^n)']:,})")
    print(f"  {'O(n!)':>10}  |  {'█' * 50}{'→→→':>1} ({vals['O(n!)']:,})")

    print()

    # --- Practical Impact ---
    print("--- Practical Impact: Time at 1 billion ops/sec ---")
    print()
    ops_per_sec = 1_000_000_000  # 1 GHz
    n = 100

    scenarios = [
        ("O(1)", 1),
        ("O(log n)", math.log2(n)),
        ("O(n)", n),
        ("O(n log n)", n * math.log2(n)),
        ("O(n²)", n ** 2),
        ("O(2^n)", 2 ** n),
        ("O(n!)", math.factorial(n) if n <= 100 else float("inf")),
    ]

    print(f"  For n = {n}, at {ops_per_sec:,} operations/second:")
    print()

    for name, ops in scenarios:
        if ops <= ops_per_sec:
            time_str = f"{ops / ops_per_sec * 1e9:.2f} nanoseconds"
        elif ops <= ops_per_sec * 60:
            time_str = f"{ops / ops_per_sec:.6f} seconds"
        elif ops <= ops_per_sec * 3600:
            time_str = f"{ops / ops_per_sec / 60:.2f} minutes"
        elif ops <= ops_per_sec * 86400 * 365:
            time_str = f"{ops / ops_per_sec / 3600:.2f} hours"
        else:
            years = ops / ops_per_sec / (86400 * 365)
            if years > 1e20:
                time_str = f"{years:.2e} years (longer than universe age!)"
            else:
                time_str = f"{years:.2e} years"

        print(f"  {name:>10}  →  {time_str}")

    print()
    print("ANSWER (Fastest → Slowest):")
    print("  O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n) < O(n!)")


if __name__ == "__main__":
    demonstrate_ranking()
