"""
Q4. Given two lists of user IDs, write a function that returns IDs present
    in both lists. What is the most efficient approach?

Answer:
    Most efficient approach: Convert both lists to SETS and use set intersection.

    Approach Comparison:
    ┌─────────────────────────┬──────────────┬──────────────┐
    │ Method                  │ Time         │ Space        │
    ├─────────────────────────┼──────────────┼──────────────┤
    │ Nested loops (brute)    │ O(n × m)     │ O(min(n,m))  │
    │ Sort + two pointers     │ O(n log n)   │ O(n + m)     │
    │ Set intersection (best) │ O(n + m)     │ O(n + m)     │
    └─────────────────────────┴──────────────┴──────────────┘

    Set intersection is O(n + m) because:
    - Building set from list A: O(n)
    - Building set from list B: O(m)
    - Intersection: O(min(n, m))
    - Total: O(n + m)
"""

import time
import random


# ============================================================
# Method 1: Brute Force — Nested Loops O(n × m)
# ============================================================
def common_ids_brute(list_a: list, list_b: list) -> list:
    """
    Find common IDs using nested loops.

    Time:  O(n × m) — for each element in A, scan all of B.
    Space: O(min(n, m)) — result list.
    """
    common = []
    for user_id in list_a:
        if user_id in list_b:  # O(m) scan for each element
            if user_id not in common:  # Avoid duplicates in result
                common.append(user_id)
    return common


# ============================================================
# Method 2: Sort + Two Pointers — O(n log n + m log m)
# ============================================================
def common_ids_sorted(list_a: list, list_b: list) -> list:
    """
    Find common IDs by sorting both lists and using two pointers.

    Time:  O(n log n + m log m) — dominated by sorting.
    Space: O(n + m) — sorted copies.
    """
    sorted_a = sorted(set(list_a))  # Sort + deduplicate
    sorted_b = sorted(set(list_b))
    common = []

    i, j = 0, 0
    while i < len(sorted_a) and j < len(sorted_b):
        if sorted_a[i] == sorted_b[j]:
            common.append(sorted_a[i])
            i += 1
            j += 1
        elif sorted_a[i] < sorted_b[j]:
            i += 1
        else:
            j += 1

    return common


# ============================================================
# Method 3: Set Intersection — O(n + m) ★ MOST EFFICIENT ★
# ============================================================
def common_ids_set(list_a: list, list_b: list) -> set:
    """
    Find common IDs using set intersection — MOST EFFICIENT.

    Time:  O(n + m) — build two sets + intersection.
    Space: O(n + m) — two sets.
    """
    return set(list_a) & set(list_b)


# ============================================================
# Bonus: Using set.intersection() method
# ============================================================
def common_ids_set_method(list_a: list, list_b: list) -> set:
    """
    Same as above using the .intersection() method.
    Slightly more efficient when one list is much smaller —
    convert the smaller one to a set.
    """
    set_a = set(list_a)
    return set_a.intersection(list_b)  # Doesn't need to convert list_b to set


def demonstrate():
    print("=" * 70)
    print("Q4: Common User IDs — Most Efficient Approach")
    print("=" * 70)
    print()

    # --- Small Example ---
    print("--- Small Example ---")
    print()

    list_a = [101, 205, 330, 442, 550, 667, 789]
    list_b = [205, 442, 600, 789, 901, 330]

    print(f"  Platform A users: {list_a}")
    print(f"  Platform B users: {list_b}")
    print()

    result_brute = common_ids_brute(list_a, list_b)
    result_sorted = common_ids_sorted(list_a, list_b)
    result_set = common_ids_set(list_a, list_b)

    print(f"  Brute force result: {result_brute}")
    print(f"  Sort+pointer result: {result_sorted}")
    print(f"  Set intersection:    {result_set}")
    print()

    # --- How Set Intersection Works ---
    print("--- How Set Intersection Works ---")
    print()
    print(f"  set_a = set({list_a})")
    print(f"        = {set(list_a)}")
    print()
    print(f"  set_b = set({list_b})")
    print(f"        = {set(list_b)}")
    print()
    print(f"  set_a & set_b = {set(list_a) & set(list_b)}")
    print()
    print("  Internal process:")
    print("    For each element in the SMALLER set:")
    print("      → Check if it exists in the LARGER set (O(1) hash lookup)")
    print("    Total: O(min(n, m)) for intersection + O(n + m) for building sets")
    print()

    # --- Complexity Comparison ---
    print("--- Method Comparison ---")
    print()
    print("  Method              | Time           | Space      | Notes")
    print("  --------------------|----------------|------------|------------------")
    print("  Nested loops        | O(n × m)       | O(min)     | Slowest")
    print("  Sort + two pointers | O(n log n)     | O(n + m)   | Good if pre-sorted")
    print("  Set intersection ★  | O(n + m)       | O(n + m)   | FASTEST (use this!)")
    print()

    # --- Performance Benchmarks ---
    print("--- Performance Benchmarks ---")
    print()

    sizes = [100, 1_000, 5_000, 10_000, 50_000]

    print(f"  {'n=m':>7}  |  {'Brute O(n×m)':>14}  |  {'Sort O(nlogn)':>14}  |  {'Set O(n+m)':>12}  |  {'Speedup':>8}")
    print(f"  {'-'*7}  |  {'-'*14}  |  {'-'*14}  |  {'-'*12}  |  {'-'*8}")

    for n in sizes:
        # Create two lists with ~30% overlap
        a = random.sample(range(n * 3), n)
        b = random.sample(range(n * 3), n)

        # Brute force (skip for large n — too slow)
        if n <= 10_000:
            start = time.perf_counter()
            _ = common_ids_brute(a, b)
            brute_time = (time.perf_counter() - start) * 1000
            brute_str = f"{brute_time:>11.3f} ms"
        else:
            brute_str = "    (skipped)"

        # Sort + two pointers
        start = time.perf_counter()
        _ = common_ids_sorted(a, b)
        sort_time = (time.perf_counter() - start) * 1000

        # Set intersection
        start = time.perf_counter()
        _ = common_ids_set(a, b)
        set_time = (time.perf_counter() - start) * 1000

        speedup = sort_time / set_time if set_time > 0 else 0

        print(
            f"  {n:>7,}  |  "
            f"{brute_str:>14}  |  "
            f"{sort_time:>11.3f} ms  |  "
            f"{set_time:>9.3f} ms  |  "
            f"{speedup:>7.1f}x"
        )

    print()

    # --- Pythonic One-Liners ---
    print("--- Pythonic Ways to Write This ---")
    print()
    print("  # Method 1: & operator (both must be sets)")
    print("  common = set(list_a) & set(list_b)")
    print()
    print("  # Method 2: .intersection() method (accepts any iterable)")
    print("  common = set(list_a).intersection(list_b)")
    print()
    print("  # Method 3: List comprehension (preserves order, but O(n×m))")
    print("  common = [x for x in list_a if x in set(list_b)]")
    print()

    # --- Edge Cases ---
    print("--- Edge Cases ---")
    print()
    edge_cases = [
        ([], [1, 2, 3], "One empty list"),
        ([1, 2, 3], [4, 5, 6], "No overlap"),
        ([1, 2, 3], [1, 2, 3], "Identical lists"),
        ([1, 1, 2, 2], [2, 2, 3, 3], "Duplicates in input"),
    ]

    for a, b, desc in edge_cases:
        result = common_ids_set(a, b)
        print(f"  {desc:>25}: {a} ∩ {b} = {result}")

    print()
    print("ANSWER:")
    print("  Most efficient: SET INTERSECTION → set(list_a) & set(list_b)")
    print("  Time: O(n + m)  |  Space: O(n + m)")
    print("  Sets use hash tables for O(1) lookups, making intersection fast.")


if __name__ == "__main__":
    demonstrate()
