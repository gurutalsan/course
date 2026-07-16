"""
Q7. 0/1 Knapsack: weights=[2,3,4,5], values=[3,4,5,6], capacity=5.
    Find max value. Show DP table.

Answer:
    dp[i][w] = max value using first i items with capacity w.
    For each item: include (if fits) or exclude.
    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])

    Time: O(n × W), Space: O(n × W).
"""


def knapsack(weights, values, capacity):
    """
    0/1 Knapsack with full DP table.
    dp[i][w] = max value using items 0..i-1 with capacity w.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i-1][w]

            # Take item i (if it fits)
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])

    return dp[n][capacity], dp


def reconstruct(weights, values, dp, capacity):
    """Find which items were selected."""
    items = []
    w = capacity
    for i in range(len(weights), 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items.append(i - 1)  # Item i-1 was taken
            w -= weights[i-1]
    items.reverse()
    return items


def demonstrate():
    print("=" * 70)
    print("Q7: 0/1 Knapsack Problem")
    print("=" * 70)
    print()

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    print(f"  Items: {list(zip(weights, values))}")
    print(f"  (weight, value) pairs")
    print(f"  Capacity: {capacity}")
    print()

    max_val, dp = knapsack(weights, values, capacity)
    selected = reconstruct(weights, values, dp, capacity)

    print(f"  Maximum value: {max_val}")
    print(f"  Items selected: {selected}")
    sel_w = sum(weights[i] for i in selected)
    sel_v = sum(values[i] for i in selected)
    print(f"  Total weight: {sel_w}, Total value: {sel_v}")
    print()

    # --- DP Table ---
    print("--- DP Table ---")
    print()
    print(f"  Item\\Cap |", end="")
    for w in range(capacity + 1):
        print(f" {w:>3}", end="")
    print()
    print(f"  {'-'*10}|{'----' * (capacity + 1)}")

    for i in range(len(weights) + 1):
        if i == 0:
            label = "  (none)   |"
        else:
            label = f"  w={weights[i-1]},v={values[i-1]} |"
        print(label, end="")
        for w in range(capacity + 1):
            marker = ""
            if i > 0 and dp[i][w] != dp[i-1][w]:
                marker = "*"
            print(f" {dp[i][w]:>2}{marker}", end="")
        print()

    print()
    print("  (* = this cell chose to INCLUDE the item)")
    print()

    # --- Trace ---
    print("--- Trace Key Decisions ---")
    print()
    for i in range(1, len(weights) + 1):
        w_item = weights[i-1]
        v_item = values[i-1]
        print(f"  Item {i-1} (w={w_item}, v={v_item}):")
        for w in range(capacity + 1):
            exclude = dp[i-1][w]
            if w_item <= w:
                include = dp[i-1][w - w_item] + v_item
                choice = "TAKE" if include > exclude else "SKIP"
                print(f"    cap={w}: skip={exclude}, take=dp[{i-1}][{w-w_item}]+{v_item}={include} → {choice}")
            else:
                print(f"    cap={w}: too heavy, skip={exclude}")
        print()

    # --- 0/1 vs Fractional ---
    print("--- 0/1 vs Fractional Knapsack ---")
    print()
    print("  0/1 Knapsack: Take whole item or nothing. Use DP.")
    print("  Fractional:   Can take fractions. Use GREEDY (sort by value/weight).")
    print()

    # --- Test cases ---
    print("--- Test Cases ---\n")
    tests = [
        ([2,3,4,5], [3,4,5,6], 5, 7),
        ([1,2,3], [6,10,12], 5, 22),
        ([10], [100], 5, 0),
        ([1,1,1], [1,1,1], 2, 2),
    ]
    for w, v, c, expected in tests:
        got, _ = knapsack(w, v, c)
        print(f"  w={w}, v={v}, cap={c} → {got} {'✓' if got==expected else '✗'}")

    print()
    print("  Time: O(n × W) | Space: O(n × W)")
    print("  Can optimize space to O(W) using single row + reverse iteration.")


if __name__ == "__main__":
    demonstrate()
