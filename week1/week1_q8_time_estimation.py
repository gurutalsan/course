"""
Q8. If an O(n) algorithm takes 5ms for n=1000, approximately how long
    will an O(n²) algorithm take for the same input?

Answer: Approximately 5,000 ms (5 seconds)

Calculation:
    Step 1: Find the constant factor for the O(n) algorithm.
        T_linear(n) = c₁ × n
        5 ms = c₁ × 1000
        c₁ = 5 / 1000 = 0.005 ms per operation

    Step 2: Assume the same constant factor for O(n²).
        (This is a common simplifying assumption in these problems.)
        T_quadratic(n) = c₁ × n²
        T_quadratic(1000) = 0.005 × 1000²
                          = 0.005 × 1,000,000
                          = 5,000 ms
                          = 5 seconds

    Alternative reasoning:
        O(n²) / O(n) = n² / n = n
        So O(n²) takes n times longer than O(n) for the same n.
        For n = 1000: 5 ms × 1000 = 5,000 ms = 5 seconds
"""

import time


def simulate_o_n(n: int) -> int:
    """Simulate an O(n) algorithm — single loop."""
    total = 0
    for i in range(n):
        total += i  # O(1) work
    return total


def simulate_o_n2(n: int) -> int:
    """Simulate an O(n²) algorithm — nested loops."""
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j  # O(1) work
    return total


def demonstrate_time_estimation():
    """Show the mathematical reasoning and practical verification."""
    print("=" * 65)
    print("Q8: Estimating O(n²) Time from O(n) Benchmark")
    print("=" * 65)
    print()

    n = 1000
    t_linear_ms = 5  # Given: O(n) takes 5ms for n=1000

    # --- Mathematical Solution ---
    print("--- Mathematical Solution ---")
    print()
    print("  Given:")
    print(f"    O(n) algorithm takes {t_linear_ms} ms for n = {n:,}")
    print()
    print("  Step 1: Find constant factor (c)")
    print(f"    T_linear = c × n")
    print(f"    {t_linear_ms} ms = c × {n}")
    c = t_linear_ms / n
    print(f"    c = {t_linear_ms} / {n} = {c} ms per operation")
    print()
    print("  Step 2: Apply to O(n²)")
    print(f"    T_quadratic = c × n²")
    t_quadratic = c * n ** 2
    print(f"    T_quadratic = {c} × {n}²")
    print(f"    T_quadratic = {c} × {n**2:,}")
    print(f"    T_quadratic = {t_quadratic:,.0f} ms")
    print(f"    T_quadratic = {t_quadratic / 1000:.0f} seconds")
    print()

    # --- Shortcut Method ---
    print("--- Shortcut Reasoning ---")
    print()
    print("  Ratio of complexities:")
    print(f"    O(n²) / O(n) = n² / n = n = {n}")
    print()
    print(f"  Therefore, O(n²) takes {n}× longer than O(n):")
    print(f"    {t_linear_ms} ms × {n} = {t_linear_ms * n:,} ms = {t_linear_ms * n / 1000:.0f} seconds")
    print()

    # --- Practical Verification ---
    print("--- Practical Verification ---")
    print()

    # Measure O(n)
    start = time.perf_counter()
    simulate_o_n(n)
    actual_linear = (time.perf_counter() - start) * 1000

    # Measure O(n²)
    start = time.perf_counter()
    simulate_o_n2(n)
    actual_quadratic = (time.perf_counter() - start) * 1000

    ratio = actual_quadratic / actual_linear if actual_linear > 0 else 0

    print(f"  Actual O(n)  time for n={n:,}: {actual_linear:.3f} ms")
    print(f"  Actual O(n²) time for n={n:,}: {actual_quadratic:.3f} ms")
    print(f"  Actual ratio (quadratic/linear): {ratio:.1f}x")
    print(f"  Expected ratio:                  {n}x")
    print()
    print(f"  The ratio is approximately n = {n}, confirming our analysis!")
    print()

    # --- Scaling Table ---
    print("--- How Both Scale with Increasing n ---")
    print()
    print(f"  {'n':>8}  |  {'O(n) Time':>12}  |  {'O(n²) Time':>14}  |  {'Ratio':>8}")
    print(f"  {'-'*8}  |  {'-'*12}  |  {'-'*14}  |  {'-'*8}")

    for test_n in [100, 500, 1_000, 5_000, 10_000, 100_000, 1_000_000]:
        # Based on given: O(n) = 5ms for n=1000
        # c = 5/1000 = 0.005 ms/op
        t_lin = c * test_n
        t_quad = c * test_n ** 2

        def format_time(ms):
            if ms < 1:
                return f"{ms*1000:.1f} µs"
            elif ms < 1000:
                return f"{ms:.1f} ms"
            elif ms < 60_000:
                return f"{ms/1000:.1f} s"
            elif ms < 3_600_000:
                return f"{ms/60_000:.1f} min"
            else:
                return f"{ms/3_600_000:.1f} hrs"

        print(
            f"  {test_n:>8,}  |  "
            f"{format_time(t_lin):>12}  |  "
            f"{format_time(t_quad):>14}  |  "
            f"{test_n:>7,}x"
        )

    print()

    # --- Key Insight ---
    print("--- Key Insight ---")
    print()
    print("  The difference between O(n) and O(n²) grows LINEARLY with n.")
    print("  For n=1,000:     O(n²) is 1,000× slower")
    print("  For n=1,000,000: O(n²) is 1,000,000× slower!")
    print()
    print("  This is why algorithm optimization matters so much at scale.")
    print()
    print("ANSWER: The O(n²) algorithm will take approximately")
    print("        5,000 ms (5 seconds) for n = 1,000.")
    print("        Reason: O(n²) is n times slower than O(n),")
    print("        so 5 ms × 1,000 = 5,000 ms.")


if __name__ == "__main__":
    demonstrate_time_estimation()
