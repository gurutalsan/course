"""
Q4. Given an array of daily temperatures [73,74,75,71,69,72,76,73],
    return an array where each element tells how many days until a
    warmer temperature. Use a stack.

Answer:
    Use a MONOTONIC DECREASING STACK that stores indices.

    Scan left to right. For each temperature:
    - While stack is not empty AND current temp > stack's top temp:
        Pop the index → days_to_wait = current_index - popped_index
    - Push current index onto stack.

    Time:  O(n) — each index pushed and popped at most once.
    Space: O(n) — stack holds at most n indices.

    Result: [1, 1, 4, 2, 1, 1, 0, 0]
"""


def daily_temperatures(temps: list) -> list:
    """
    For each day, find how many days until a warmer temperature.

    Uses a monotonic decreasing stack of indices.
    When we find a warmer day, we resolve all cooler days on the stack.

    Time:  O(n) — each index pushed/popped at most once.
    Space: O(n)

    Example:
        >>> daily_temperatures([73,74,75,71,69,72,76,73])
        [1, 1, 4, 2, 1, 1, 0, 0]
    """
    n = len(temps)
    result = [0] * n
    stack = []  # Stack of indices (temps in decreasing order)

    for i in range(n):
        # Pop all indices whose temperature is less than current
        while stack and temps[i] > temps[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx

        stack.append(i)

    # Remaining indices in stack have no warmer day → already 0
    return result


def daily_temperatures_brute(temps: list) -> list:
    """Brute force O(n²) for comparison."""
    n = len(temps)
    result = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if temps[j] > temps[i]:
                result[i] = j - i
                break
    return result


def demonstrate():
    print("=" * 70)
    print("Q4: Daily Temperatures — Monotonic Stack")
    print("=" * 70)
    print()

    temps = [73, 74, 75, 71, 69, 72, 76, 73]

    print(f"  Temperatures: {temps}")
    print(f"  Day indices:  {list(range(len(temps)))}")
    print()

    result = daily_temperatures(temps)
    print(f"  Result: {result}")
    print()

    # Explain each result
    print("  Meaning:")
    for i, (temp, days) in enumerate(zip(temps, result)):
        if days > 0:
            print(f"    Day {i} ({temp}°): wait {days} day(s) → Day {i+days} ({temps[i+days]}°)")
        else:
            print(f"    Day {i} ({temp}°): no warmer day ahead")
    print()

    # --- Step-by-Step Trace ---
    print("=" * 70)
    print("STEP-BY-STEP TRACE")
    print("=" * 70)
    print()

    stack = []
    result_trace = [0] * len(temps)

    print(f"  {'Day':>3} | {'Temp':>4} | {'Stack (indices→temps)':>30} | {'Action':>35} | {'Result'}")
    print(f"  {'-'*3} | {'-'*4} | {'-'*30} | {'-'*35} | {'-'*20}")

    for i in range(len(temps)):
        actions = []

        while stack and temps[i] > temps[stack[-1]]:
            prev = stack.pop()
            result_trace[prev] = i - prev
            actions.append(f"Pop {prev}({temps[prev]}°)→{i-prev} days")

        stack.append(i)

        if not actions:
            actions.append(f"Push {i}")

        stack_display = [f"{idx}({temps[idx]}°)" for idx in stack]
        result_str = str(result_trace)

        print(f"  {i:>3} | {temps[i]:>4} | {str(stack_display):>30} | {'; '.join(actions):>35} | {result_str}")

    print()
    print(f"  Final result: {result_trace}")
    print()

    # --- Visual: Monotonic Stack ---
    print("--- Visual: How the Monotonic Stack Works ---")
    print()
    print("  The stack maintains temperatures in DECREASING order.")
    print("  When a warmer day arrives, it 'resolves' all cooler days.")
    print()
    print("  Day 0 (73): Stack: [73]")
    print("  Day 1 (74): 74 > 73 → pop 73 (waited 1 day). Stack: [74]")
    print("  Day 2 (75): 75 > 74 → pop 74 (waited 1 day). Stack: [75]")
    print("  Day 3 (71): 71 < 75 → push. Stack: [75, 71]")
    print("  Day 4 (69): 69 < 71 → push. Stack: [75, 71, 69]")
    print("  Day 5 (72): 72 > 69 → pop 69 (1 day)")
    print("              72 > 71 → pop 71 (2 days). Stack: [75, 72]")
    print("  Day 6 (76): 76 > 72 → pop 72 (1 day)")
    print("              76 > 75 → pop 75 (4 days). Stack: [76]")
    print("  Day 7 (73): 73 < 76 → push. Stack: [76, 73]")
    print()
    print("  End: [76, 73] remain → no warmer day → result = 0")
    print()

    # --- Temperature bar chart ---
    print("--- Temperature Visualization ---")
    print()
    max_temp = max(temps)
    min_temp = min(temps) - 1

    for level in range(max_temp, min_temp, -1):
        row = f"  {level:>2} |"
        for i, t in enumerate(temps):
            if t >= level:
                row += " ██"
            else:
                row += "   "
        print(row)

    print(f"     +{'---' * len(temps)}")
    labels = "      "
    for i in range(len(temps)):
        labels += f"D{i} "
    print(labels)

    result_line = "  →   "
    for r in result:
        result_line += f" {r} "
    print(result_line + "  (days to wait)")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([60, 50, 40, 30], [0, 0, 0, 0]),
        ([70, 70, 70, 70], [0, 0, 0, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([55], [0]),
    ]

    all_pass = True
    for t, expected in test_cases:
        got = daily_temperatures(t)
        status = "✓" if got == expected else "✗"
        if got != expected: all_pass = False
        print(f"  {str(t):>35} → {str(got):>25}  {status}")

    print(f"\n  All passed: {'✓' if all_pass else '✗'}")
    print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Method           | Time | Space")
    print("  -----------------|------|------")
    print("  Brute force      | O(n²)| O(n)")
    print("  Monotonic stack ★| O(n) | O(n)")
    print()
    print("  Why O(n)? Each index is pushed once and popped at most once.")
    print("  Total pushes + pops ≤ 2n → O(n).")
    print()
    print("ANSWER: Use a monotonic decreasing stack of indices.")
    print("When a warmer temp appears, pop and compute the difference.")
    print("Result: [1, 1, 4, 2, 1, 1, 0, 0]")


if __name__ == "__main__":
    demonstrate()
