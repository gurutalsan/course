"""
Q7. Best Time to Buy and Sell Stock: Given prices=[7,1,5,3,6,4],
    find the maximum profit from one buy and one sell.
    Write the solution and explain your approach.

Answer:
    Maximum profit = 5 (buy at 1, sell at 6)

    Approach: Track the minimum price seen so far and calculate
    potential profit at each step.

    For each price:
        1. Update min_price if current price is lower.
        2. Calculate profit = current_price - min_price.
        3. Update max_profit if this profit is higher.

    Time Complexity:  O(n) — single pass.
    Space Complexity: O(1) — two variables only.
"""


# ============================================================
# Optimal: Single Pass — O(n) ★ RECOMMENDED ★
# ============================================================
def max_profit(prices: list) -> tuple:
    """
    Find the maximum profit from buying and selling once.

    Track minimum price seen so far. At each step, calculate
    the profit if we sold at today's price.

    Time:  O(n) — single pass.
    Space: O(1) — two tracking variables.

    Returns:
        (max_profit, buy_day, sell_day)
    """
    if len(prices) < 2:
        return 0, -1, -1

    min_price = prices[0]
    best_profit = 0
    buy_day = 0
    sell_day = 0
    min_day = 0

    for i in range(1, len(prices)):
        # Update minimum price
        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i

        # Calculate profit if we sell today
        profit = prices[i] - min_price

        # Update best profit
        if profit > best_profit:
            best_profit = profit
            buy_day = min_day
            sell_day = i

    return best_profit, buy_day, sell_day


# ============================================================
# Brute Force — O(n²) for comparison
# ============================================================
def max_profit_brute(prices: list) -> tuple:
    """
    Brute force: check every buy-sell pair.

    Time:  O(n²) — nested loops.
    Space: O(1)
    """
    if len(prices) < 2:
        return 0, -1, -1

    best_profit = 0
    buy_day = sell_day = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > best_profit:
                best_profit = profit
                buy_day, sell_day = i, j

    return best_profit, buy_day, sell_day


def demonstrate():
    print("=" * 70)
    print("Q7: Best Time to Buy and Sell Stock")
    print("=" * 70)
    print()

    # --- Problem ---
    prices = [7, 1, 5, 3, 6, 4]
    print(f"  Prices: {prices}")
    print(f"  Days:   {list(range(len(prices)))}")
    print()

    profit, buy, sell = max_profit(prices)
    print(f"  Maximum Profit: {profit}")
    print(f"  Buy on day {buy} (price={prices[buy]}), Sell on day {sell} (price={prices[sell]})")
    print(f"  Profit = {prices[sell]} - {prices[buy]} = {profit}")
    print()

    # --- Visual Price Chart ---
    print("--- Visual: Price Chart ---")
    print()

    max_p = max(prices)
    for level in range(max_p, 0, -1):
        row = f"  {level:>2} |"
        for i, p in enumerate(prices):
            if p >= level:
                if i == buy and level == prices[buy]:
                    row += " ▼ "  # Buy marker
                elif i == sell and level == prices[sell]:
                    row += " ▲ "  # Sell marker
                else:
                    row += " █ "
            else:
                row += "   "
        print(row)

    print(f"   0 +{'---' * len(prices)}")
    day_labels = "     "
    for i in range(len(prices)):
        day_labels += f" {i} "
    print(day_labels + "  ← Day")
    print()
    print(f"  ▼ = Buy (day {buy}, ${prices[buy]})   ▲ = Sell (day {sell}, ${prices[sell]})   Profit = ${profit}")
    print()

    # --- Algorithm Explanation ---
    print("--- Algorithm Explanation ---")
    print()
    print("  Key Insight: We want to buy LOW and sell HIGH (after buying).")
    print()
    print("  Strategy:")
    print("    1. As we scan left to right, track the LOWEST price seen so far.")
    print("    2. At each price, calculate: 'If I sell NOW, what's my profit?'")
    print("       profit = today's price - lowest price so far")
    print("    3. Track the MAXIMUM profit across all days.")
    print()
    print("  Why it works:")
    print("    - We only sell AFTER buying (left to right scan ensures this).")
    print("    - By tracking min_price, we always know the best buy point.")
    print("    - We check every possible sell point against the best buy.")
    print()

    # --- Step-by-Step Walkthrough ---
    print("--- Step-by-Step Walkthrough ---")
    print()
    prices = [7, 1, 5, 3, 6, 4]
    print(f"  Prices: {prices}")
    print()

    min_price = prices[0]
    best_profit = 0

    print(f"  {'Day':>3} | {'Price':>5} | {'Min So Far':>10} | {'Profit':>7} | {'Best Profit':>11} | {'Action'}")
    print(f"  {'-'*3} | {'-'*5} | {'-'*10} | {'-'*7} | {'-'*11} | {'-'*25}")

    print(f"  {0:>3} | {prices[0]:>5} | {min_price:>10} | {'—':>7} | {best_profit:>11} | Initialize min_price={prices[0]}")

    for i in range(1, len(prices)):
        price = prices[i]
        action_parts = []

        if price < min_price:
            min_price = price
            action_parts.append(f"New min! min={min_price}")

        profit = price - min_price

        if profit > best_profit:
            best_profit = profit
            action_parts.append(f"New best! profit={profit}")

        action = ", ".join(action_parts) if action_parts else "No change"

        print(f"  {i:>3} | {price:>5} | {min_price:>10} | {profit:>7} | {best_profit:>11} | {action}")

    print()
    print(f"  Final Answer: Maximum Profit = {best_profit}")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5, "Standard case"),
        ([7, 6, 4, 3, 1], 0, "Decreasing prices (no profit)"),
        ([1, 2, 3, 4, 5], 4, "Increasing prices"),
        ([2, 4, 1], 2, "Buy early, sell before drop"),
        ([3, 3, 3, 3], 0, "Flat prices"),
        ([1, 2], 1, "Two days"),
        ([2, 1, 2, 1, 0, 1, 2], 2, "Multiple valleys"),
        ([1, 4, 2, 7], 6, "Non-adjacent buy/sell"),
    ]

    print(f"  {'Prices':>30}  | {'Expected':>8} | {'Got':>5} | {'Buy→Sell':>15} | {'✓/✗':>3}")
    print(f"  {'-'*30}  | {'-'*8} | {'-'*5} | {'-'*15} | {'-'*3}")

    for prices, expected, desc in test_cases:
        profit, buy, sell = max_profit(prices)
        status = "✓" if profit == expected else "✗"
        if profit > 0:
            trade = f"${prices[buy]}→${prices[sell]}(d{buy}→d{sell})"
        else:
            trade = "No trade"
        prices_str = str(prices) if len(str(prices)) <= 28 else str(prices)[:25] + "..."
        print(f"  {prices_str:>30}  | {expected:>8} | {profit:>5} | {trade:>15} | {status:>3}")

    print()

    # --- Edge Case: Decreasing Prices ---
    print("--- Edge Case: All Prices Decreasing ---")
    print()
    prices = [7, 6, 4, 3, 1]
    profit, buy, sell = max_profit(prices)
    print(f"  Prices: {prices}")
    print(f"  No profitable trade exists → profit = {profit}")
    print("  (We never buy if we can't sell higher later)")
    print()

    # --- Complexity ---
    print("--- Complexity Comparison ---")
    print()
    print("  Method        | Time  | Space | Approach")
    print("  --------------|-------|-------|---------------------------")
    print("  Brute Force   | O(n²) | O(1)  | Check every buy-sell pair")
    print("  One Pass ★    | O(n)  | O(1)  | Track min price + max profit")
    print()

    # --- Performance ---
    import time
    import random

    print("--- Performance Benchmark ---")
    print()
    print(f"  {'n':>8}  |  {'Brute O(n²)':>14}  |  {'One Pass O(n)':>14}  |  {'Speedup':>8}")
    print(f"  {'-'*8}  |  {'-'*14}  |  {'-'*14}  |  {'-'*8}")

    for n in [100, 1_000, 5_000, 10_000, 50_000]:
        prices = [random.randint(1, 1000) for _ in range(n)]

        if n <= 10_000:
            start = time.perf_counter()
            _ = max_profit_brute(prices)
            brute_time = (time.perf_counter() - start) * 1000
            brute_str = f"{brute_time:>11.3f} ms"
        else:
            brute_str = "    (skipped)"

        start = time.perf_counter()
        _ = max_profit(prices)
        opt_time = (time.perf_counter() - start) * 1000

        speedup = brute_time / opt_time if n <= 10_000 and opt_time > 0 else 0
        speedup_str = f"{speedup:>7.0f}x" if speedup > 0 else "     N/A"

        print(f"  {n:>8,}  |  {brute_str:>14}  |  {opt_time:>11.3f} ms  |  {speedup_str:>8}")

    print()
    print("ANSWER:")
    print("  Track min_price and max_profit in a single pass.")
    print("  For prices=[7,1,5,3,6,4]: Buy at 1, sell at 6, profit = 5.")
    print("  Time: O(n), Space: O(1)")


if __name__ == "__main__":
    demonstrate()
