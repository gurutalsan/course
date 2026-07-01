"""
Q8. Write a function that removes all duplicates from a list while
    preserving the original order of first occurrences.

Answer:
    Use a SET to track seen elements and build a new list with only
    first occurrences.

    Time Complexity:  O(n) — single pass, O(1) set operations.
    Space Complexity: O(n) — set + result list.

    Key insight: A plain set() or list(set()) does NOT preserve order.
    We need to track what we've seen while iterating in order.
"""


# ============================================================
# Method 1: Set + List (Optimal) ★ RECOMMENDED ★
# ============================================================
def remove_duplicates_ordered(lst: list) -> list:
    """
    Remove duplicates while preserving insertion order.

    Uses a set for O(1) lookup to check if an element was already seen.

    Time:  O(n) — single pass through the list.
    Space: O(n) — set for tracking + result list.

    Example:
        >>> remove_duplicates_ordered([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
        [3, 1, 4, 5, 9, 2, 6]
    """
    seen = set()
    result = []

    for item in lst:
        if item not in seen:    # O(1) set lookup
            seen.add(item)      # O(1) set insertion
            result.append(item) # O(1) list append
    return result


# ============================================================
# Method 2: dict.fromkeys() (Python 3.7+ trick)
# ============================================================
def remove_duplicates_dict(lst: list) -> list:
    """
    Remove duplicates using dict.fromkeys() — leverages dict's
    insertion-order guarantee (Python 3.7+).

    Time:  O(n)
    Space: O(n)
    """
    return list(dict.fromkeys(lst))


# ============================================================
# Method 3: Using OrderedDict (pre-Python 3.7 compatible)
# ============================================================
from collections import OrderedDict

def remove_duplicates_ordered_dict(lst: list) -> list:
    """
    Remove duplicates using OrderedDict — works in all Python 3.x versions.

    Time:  O(n)
    Space: O(n)
    """
    return list(OrderedDict.fromkeys(lst))


# ============================================================
# WRONG Method: set() alone (does NOT preserve order)
# ============================================================
def remove_duplicates_set_only(lst: list) -> list:
    """
    ⚠ WRONG: Using set() alone does NOT preserve original order!
    Sets are unordered collections.
    """
    return list(set(lst))  # Order is NOT guaranteed!


# ============================================================
# Method 4: Brute Force — O(n²) (for comparison)
# ============================================================
def remove_duplicates_brute(lst: list) -> list:
    """
    Remove duplicates using nested check — O(n²).
    No extra set, but much slower.
    """
    result = []
    for item in lst:
        if item not in result:  # O(n) list lookup!
            result.append(item)
    return result


def demonstrate():
    import time
    import random

    print("=" * 70)
    print("Q8: Remove Duplicates While Preserving Order")
    print("=" * 70)
    print()

    # --- The Problem ---
    print("--- The Problem ---")
    print()
    print("  Input:  [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]")
    print("  Goal:   [3, 1, 4, 5, 9, 2, 6]  ← first occurrences only, order kept")
    print()
    print("  Why not just use set()?")
    original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"    set({original})")
    print(f"    = {set(original)}")
    print(f"    → Order is LOST! ❌")
    print()

    # --- The Solution ---
    print("--- Solution: Set + Ordered Iteration ---")
    print()
    print("  def remove_duplicates_ordered(lst):")
    print("      seen = set()")
    print("      result = []")
    print("      for item in lst:")
    print("          if item not in seen:    # O(1) lookup")
    print("              seen.add(item)")
    print("              result.append(item)")
    print("      return result")
    print()

    # --- Step-by-Step Walkthrough ---
    print("--- Step-by-Step Walkthrough ---")
    print()
    lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"  Input: {lst}")
    print()

    seen = set()
    result = []
    for i, item in enumerate(lst):
        if item not in seen:
            seen.add(item)
            result.append(item)
            action = f"✓ NEW   → add to result"
        else:
            action = f"✗ SEEN  → skip"

        print(f"  Step {i+1:>2}: item={item}, seen={sorted(seen):>25}, result={result}")
        print(f"          {action}")

    print()
    print(f"  Final result: {result}")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], "Mixed duplicates"),
        ([1, 1, 1, 1, 1], "All same"),
        ([1, 2, 3, 4, 5], "No duplicates"),
        ([], "Empty list"),
        ([42], "Single element"),
        (["a", "b", "a", "c", "b", "d"], "String elements"),
        ([True, 1, False, 0], "Bool/int overlap"),
        ([3, 2, 1, 2, 3, 4, 5, 4], "Pattern with dups"),
    ]

    print(f"  {'Input':>35}  |  {'Result':>30}  |  {'Correct?':>8}")
    print(f"  {'-'*35}  |  {'-'*30}  |  {'-'*8}")

    for lst_test, desc in test_cases:
        result = remove_duplicates_ordered(lst_test)
        # Verify: no duplicates and order preserved
        no_dups = len(result) == len(set(result))
        order_ok = all(
            lst_test.index(result[i]) < lst_test.index(result[i+1])
            for i in range(len(result) - 1)
        ) if len(result) > 1 else True
        correct = "✓" if (no_dups and order_ok) else "✗"

        print(f"  {str(lst_test):>35}  |  {str(result):>30}  |  {correct:>8}")

    print()

    # --- Method Comparison ---
    print("--- Method Comparison ---")
    print()
    lst_demo = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"  Input: {lst_demo}")
    print()
    print(f"  Method 1 (set+list):       {remove_duplicates_ordered(lst_demo)}")
    print(f"  Method 2 (dict.fromkeys):  {remove_duplicates_dict(lst_demo)}")
    print(f"  Method 3 (OrderedDict):    {remove_duplicates_ordered_dict(lst_demo)}")
    print(f"  Method 4 (brute force):    {remove_duplicates_brute(lst_demo)}")
    print(f"  ⚠ WRONG (set only):        {remove_duplicates_set_only(lst_demo)}  ← order lost!")
    print()

    print("  Method           | Time  | Space | Preserves Order?")
    print("  -----------------|-------|-------|------------------")
    print("  set + list  ★    | O(n)  | O(n)  | ✓ Yes")
    print("  dict.fromkeys    | O(n)  | O(n)  | ✓ Yes (Python 3.7+)")
    print("  OrderedDict      | O(n)  | O(n)  | ✓ Yes")
    print("  Brute force      | O(n²) | O(n)  | ✓ Yes (but slow)")
    print("  set() alone ⚠    | O(n)  | O(n)  | ✗ NO!")
    print()

    # --- Performance Benchmarks ---
    print("--- Performance Benchmarks ---")
    print()

    sizes = [100, 1_000, 10_000, 50_000, 100_000]

    print(f"  {'n':>8}  |  {'set+list O(n)':>14}  |  {'dict.fromkeys':>14}  |  {'brute O(n²)':>14}")
    print(f"  {'-'*8}  |  {'-'*14}  |  {'-'*14}  |  {'-'*14}")

    for n in sizes:
        data = [random.randint(1, n // 2) for _ in range(n)]

        # set + list
        start = time.perf_counter()
        _ = remove_duplicates_ordered(data)
        set_list_time = (time.perf_counter() - start) * 1000

        # dict.fromkeys
        start = time.perf_counter()
        _ = remove_duplicates_dict(data)
        dict_time = (time.perf_counter() - start) * 1000

        # brute force (skip for large n)
        if n <= 50_000:
            start = time.perf_counter()
            _ = remove_duplicates_brute(data)
            brute_time = (time.perf_counter() - start) * 1000
            brute_str = f"{brute_time:>11.3f} ms"
        else:
            brute_str = "    (skipped)"

        print(
            f"  {n:>8,}  |  "
            f"{set_list_time:>11.3f} ms  |  "
            f"{dict_time:>11.3f} ms  |  "
            f"{brute_str:>14}"
        )

    print()

    # --- One-liner alternatives ---
    print("--- Pythonic One-Liners ---")
    print()
    lst_demo = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"  Input: {lst_demo}")
    print()
    print("  # Best one-liner (Python 3.7+):")
    print(f"  list(dict.fromkeys({lst_demo}))")
    print(f"  → {list(dict.fromkeys(lst_demo))}")
    print()
    print("  # Using a generator + set (more explicit):")
    print("  seen = set()")
    print("  [seen.add(x) or x for x in lst if x not in seen]")
    seen = set()
    result = [seen.add(x) or x for x in lst_demo if x not in seen]
    print(f"  → {result}")
    print()

    print("ANSWER:")
    print("  Use a SET to track seen elements + build result list in order.")
    print("  Time: O(n), Space: O(n).")
    print("  Key: iterate the original list IN ORDER, adding only first")
    print("  occurrences to the result. The set provides O(1) 'already seen?' checks.")


if __name__ == "__main__":
    demonstrate()
