"""
Q2. Climbing Stairs: How many distinct ways to reach step n?
    (1 or 2 steps). Solve for n=10. Extend to 1, 2, or 3 steps.

Answer:
    With 1-2 steps: dp[i] = dp[i-1] + dp[i-2]  (same as Fibonacci!)
    With 1-2-3 steps: dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    Why? To reach step i, you came from step i-1 (1 step) or i-2 (2 steps).
    Time: O(n), Space: O(1) with optimization.
"""


def climb_stairs(n):
    """1 or 2 steps. dp[i] = dp[i-1] + dp[i-2]. O(n) time, O(1) space."""
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def climb_stairs_3(n):
    """1, 2, or 3 steps. dp[i] = dp[i-1] + dp[i-2] + dp[i-3]."""
    if n <= 1:
        return 1
    if n == 2:
        return 2
    a, b, c = 1, 1, 2  # dp[0]=1, dp[1]=1, dp[2]=2
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c


def climb_stairs_table(n):
    """Tabulation version for visualization."""
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp


def demonstrate():
    print("=" * 70)
    print("Q2: Climbing Stairs — DP")
    print("=" * 70)
    print()

    # --- Why it's Fibonacci ---
    print("--- Why Climbing Stairs = Fibonacci ---")
    print()
    print("  To reach step n, you either:")
    print("    • Took 1 step from step (n-1) → dp[n-1] ways to get there")
    print("    • Took 2 steps from step (n-2) → dp[n-2] ways to get there")
    print("  Total: dp[n] = dp[n-1] + dp[n-2]")
    print()

    # --- DP Table ---
    print("--- DP Table for n=10 ---")
    print()
    dp = climb_stairs_table(10)
    print(f"  Step  | 0  1  2  3  4  5  6  7  8  9  10")
    print(f"  Ways  | {' '.join(f'{d:<2}' for d in dp)}")
    print()

    # Trace
    print("  Trace:")
    for i in range(2, 11):
        print(f"    dp[{i}] = dp[{i-1}] + dp[{i-2}] = {dp[i-1]} + {dp[i-2]} = {dp[i]}")
    print()
    print(f"  Answer: {climb_stairs(10)} distinct ways to reach step 10")
    print()

    # --- Small cases visualization ---
    print("--- Visualizing Small Cases ---")
    print()
    print("  n=1: {1}                             → 1 way")
    print("  n=2: {1+1, 2}                        → 2 ways")
    print("  n=3: {1+1+1, 1+2, 2+1}              → 3 ways")
    print("  n=4: {1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2} → 5 ways")
    print()

    # --- Extended: 1, 2, or 3 steps ---
    print("--- Extended: 1, 2, or 3 Steps ---")
    print()
    print("  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]")
    print()
    print(f"  {'n':>3} | {'1-2 steps':>10} | {'1-2-3 steps':>12}")
    print(f"  {'-'*3} | {'-'*10} | {'-'*12}")
    for n in range(1, 11):
        print(f"  {n:>3} | {climb_stairs(n):>10} | {climb_stairs_3(n):>12}")

    print()
    print(f"  n=10 with 1-2 steps:   {climb_stairs(10)}")
    print(f"  n=10 with 1-2-3 steps: {climb_stairs_3(10)}")
    print()
    print("  Time: O(n) | Space: O(1)")
    print("  General k steps: dp[i] = sum(dp[i-j] for j in 1..k)")


if __name__ == "__main__":
    demonstrate()
