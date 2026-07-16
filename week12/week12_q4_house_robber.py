"""
Q4. House Robber: houses=[2,7,9,3,1]. Max money, no two adjacent.
    Both memoized and tabulated solutions.

Answer:
    At each house, choose: ROB it (skip prev) or SKIP it (keep prev total).
    dp[i] = max(dp[i-1], dp[i-2] + houses[i])

    Time: O(n), Space: O(1) optimized.
"""

from functools import lru_cache


def rob_memoized(houses):
    """Top-down memoization. O(n) time, O(n) space."""
    @lru_cache(maxsize=None)
    def dp(i):
        if i < 0:
            return 0
        return max(dp(i - 1), dp(i - 2) + houses[i])

    return dp(len(houses) - 1)


def rob_tabulation(houses):
    """Bottom-up tabulation. O(n) time, O(n) space."""
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]

    n = len(houses)
    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + houses[i])

    return dp[-1], dp


def rob_optimized(houses):
    """Space-optimized. O(n) time, O(1) space."""
    if not houses:
        return 0
    prev2, prev1 = 0, 0
    for money in houses:
        prev2, prev1 = prev1, max(prev1, prev2 + money)
    return prev1


def demonstrate():
    print("=" * 70)
    print("Q4: House Robber — No Adjacent Houses")
    print("=" * 70)
    print()

    houses = [2, 7, 9, 3, 1]
    print(f"  Houses: {houses}")
    print()

    # --- Decision at each house ---
    print("--- Decision: Rob or Skip ---")
    print()
    print("  At each house i, two choices:")
    print("    ROB:  take houses[i] + best from houses[0..i-2]")
    print("    SKIP: keep best from houses[0..i-1]")
    print()
    print("  dp[i] = max(dp[i-1], dp[i-2] + houses[i])")
    print()

    # --- DP Table ---
    result, dp = rob_tabulation(houses)
    print("--- DP Table ---")
    print()
    print(f"  House  | {' '.join(f'{i:>4}' for i in range(len(houses)))}")
    print(f"  Value  | {' '.join(f'{h:>4}' for h in houses)}")
    print(f"  dp[i]  | {' '.join(f'{d:>4}' for d in dp)}")
    print()

    # Trace
    print("--- Step-by-Step ---")
    print()
    print(f"  dp[0] = houses[0] = {houses[0]}")
    print(f"  dp[1] = max(houses[0], houses[1]) = max({houses[0]}, {houses[1]}) = {dp[1]}")
    for i in range(2, len(houses)):
        skip = dp[i-1]
        rob = dp[i-2] + houses[i]
        choice = "ROB" if rob > skip else "SKIP"
        print(f"  dp[{i}] = max(dp[{i-1}], dp[{i-2}] + houses[{i}])")
        print(f"       = max({skip}, {dp[i-2]} + {houses[i]})")
        print(f"       = max({skip}, {rob}) = {dp[i]}  → {choice} house {i}")
    print()

    print(f"  Maximum money: {result}")
    print()

    # --- Which houses robbed? ---
    print("--- Which Houses Were Robbed? ---")
    print()
    robbed = []
    i = len(dp) - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i-1]:
            robbed.append(i)
            i -= 2
        else:
            i -= 1

    robbed.reverse()
    print(f"  Houses robbed: {robbed}")
    total = sum(houses[i] for i in robbed)
    print(f"  Values: {[houses[i] for i in robbed]} = {total}")
    print()

    # Verify all three approaches
    print("--- Verify All Approaches ---")
    print()
    m1 = rob_memoized(houses)
    m2 = result
    m3 = rob_optimized(houses)
    print(f"  Memoized:   {m1}")
    print(f"  Tabulation: {m2}")
    print(f"  Optimized:  {m3}")
    print(f"  All match: {'✓' if m1 == m2 == m3 else '✗'}")
    print()

    # --- Test cases ---
    print("--- Test Cases ---\n")
    tests = [
        ([2, 7, 9, 3, 1], 12),
        ([1, 2, 3, 1], 4),
        ([2, 1, 1, 2], 4),
        ([0], 0),
        ([100], 100),
        ([1, 3, 1, 3, 100], 103),
    ]
    for h, expected in tests:
        got = rob_optimized(h)
        print(f"  {str(h):>25} → {got} (expected {expected}) {'✓' if got==expected else '✗'}")

    print()
    print("  Time: O(n) | Space: O(1) optimized")


if __name__ == "__main__":
    demonstrate()
