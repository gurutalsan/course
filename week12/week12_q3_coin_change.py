"""
Q3. Coin Change: coins=[1,5,10,25], amount=37. Minimum coins needed.
    Draw DP table and trace solution.

Answer:
    dp[i] = min coins to make amount i.
    dp[0] = 0. For each amount, try each coin:
        dp[i] = min(dp[i], dp[i - coin] + 1) if i >= coin

    Time: O(amount × len(coins)), Space: O(amount).
"""


def coin_change(coins, amount):
    """
    Minimum coins to make amount.
    dp[i] = min coins for amount i.
    Time: O(amount × n_coins), Space: O(amount).
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_with_trace(coins, amount):
    """Returns min coins AND which coins were used."""
    dp = [float('inf')] * (amount + 1)
    parent = [-1] * (amount + 1)  # Track which coin was used
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    # Reconstruct which coins were used
    if dp[amount] == float('inf'):
        return -1, [], dp

    coins_used = []
    remaining = amount
    while remaining > 0:
        coins_used.append(parent[remaining])
        remaining -= parent[remaining]

    return dp[amount], coins_used, dp


def demonstrate():
    print("=" * 70)
    print("Q3: Coin Change — Minimum Coins")
    print("=" * 70)
    print()

    coins = [1, 5, 10, 25]
    amount = 37
    min_coins, used, dp = coin_change_with_trace(coins, amount)

    print(f"  Coins: {coins}")
    print(f"  Amount: {amount}")
    print(f"  Minimum coins: {min_coins}")
    print(f"  Coins used: {used}")
    print()

    # --- DP Table ---
    print("--- DP Table (selected values) ---")
    print()
    print(f"  {'Amount':>6} | {'dp[i]':>5} | {'Coin used':>9}")
    print(f"  {'-'*6} | {'-'*5} | {'-'*9}")
    for i in [0, 1, 5, 6, 10, 11, 15, 20, 25, 26, 30, 35, 36, 37]:
        if i <= amount:
            _, used_i, _ = coin_change_with_trace(coins, i)
            print(f"  {i:>6} | {dp[i]:>5} | {used_i}")
    print()

    # --- Step-by-step trace ---
    print("--- Trace: Building dp[0..10] ---")
    print()
    trace_dp = [float('inf')] * 11
    trace_dp[0] = 0

    for i in range(1, 11):
        options = []
        for coin in coins:
            if coin <= i and trace_dp[i - coin] != float('inf'):
                val = trace_dp[i - coin] + 1
                options.append(f"dp[{i}-{coin}]+1 = dp[{i-coin}]+1 = {val}")
                trace_dp[i] = min(trace_dp[i], val)
            elif coin <= i:
                options.append(f"dp[{i-coin}] = ∞")
        print(f"  dp[{i}]: {'; '.join(options)}")
        print(f"       → dp[{i}] = {trace_dp[i]}")
        print()

    # --- Reconstruct solution ---
    print("--- Reconstructing Solution for amount=37 ---")
    print()
    remaining = 37
    step = 0
    print(f"  {'Step':>4} | {'Remaining':>9} | {'Best coin':>9} | {'dp[rem]':>7}")
    print(f"  {'-'*4} | {'-'*9} | {'-'*9} | {'-'*7}")
    while remaining > 0:
        step += 1
        _, u, d = coin_change_with_trace(coins, remaining)
        best = u[0] if u else 0
        print(f"  {step:>4} | {remaining:>9} | {best:>9} | {d[remaining]:>7}")
        remaining -= best
    print(f"\n  Total: {min_coins} coins ✓")
    print()

    # --- Test cases ---
    print("--- Test Cases ---\n")
    tests = [
        ([1,5,10,25], 37, 4),
        ([1,5,10,25], 30, 2),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1,2,5], 11, 3),
        ([186,419,83,408], 6249, 20),
    ]
    for c, a, expected in tests:
        got = coin_change(c, a)
        print(f"  coins={c}, amount={a} → {got} {'✓' if got==expected else '✗'}")

    print()
    print("  Time: O(amount × n_coins) | Space: O(amount)")


if __name__ == "__main__":
    demonstrate()
