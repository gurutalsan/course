"""
Q6. Rewrite this O(n²) duplicate-check to O(n) using a different data structure:

    def has_dup(arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]: return True
        return False

Answer:
    Use a SET (hash set) to achieve O(n) time complexity.
    A set provides O(1) average-case lookup and insertion.
    We iterate through the array once, checking if each element is already
    in the set. If yes → duplicate found. If no → add it to the set.

    Time Complexity:  O(n) — single pass through the array
    Space Complexity: O(n) — set can store up to n elements
"""

import time
import random


# ============================================================
# Original: O(n²) — Brute Force with Nested Loops
# ============================================================
def has_dup_brute_force(arr):
    """
    Original O(n²) duplicate check.
    Compares every pair of elements.

    Time Complexity:  O(n²) — two nested loops
    Space Complexity: O(1)  — no extra data structures
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


# ============================================================
# Optimized: O(n) — Using a Set (Hash Set)
# ============================================================
def has_dup_set(arr):
    """
    Optimized O(n) duplicate check using a set.
    Sets provide O(1) average lookup and insertion.

    Time Complexity:  O(n) — single pass, O(1) set operations
    Space Complexity: O(n) — set stores up to n elements
    """
    seen = set()
    for element in arr:
        if element in seen:  # O(1) average lookup
            return True
        seen.add(element)    # O(1) average insertion
    return False


# ============================================================
# Alternative: O(n log n) — Using Sorting
# ============================================================
def has_dup_sort(arr):
    """
    Alternative O(n log n) duplicate check by sorting first.
    After sorting, duplicates will be adjacent.

    Time Complexity:  O(n log n) — dominated by the sort
    Space Complexity: O(n) — sorted copy (to avoid mutating input)
    """
    sorted_arr = sorted(arr)  # O(n log n)
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == sorted_arr[i - 1]:
            return True
    return False


def demonstrate_optimization():
    """Compare all three approaches."""
    print("=" * 65)
    print("Q6: Rewrite O(n²) Duplicate Check to O(n)")
    print("=" * 65)
    print()

    # --- Show the transformation ---
    print("--- Original Code (O(n²)) ---")
    print()
    print("  def has_dup(arr):")
    print("      for i in range(len(arr)):             # n iterations")
    print("          for j in range(i+1, len(arr)):     # ~n iterations each")
    print("              if arr[i] == arr[j]:           # O(1) comparison")
    print("                  return True")
    print("      return False")
    print()
    print("  Problem: For each element, we compare with ALL remaining elements.")
    print("  Total comparisons ≈ n(n-1)/2 = O(n²)")
    print()

    print("--- Optimized Code (O(n)) ---")
    print()
    print("  def has_dup(arr):")
    print("      seen = set()                          # Hash set")
    print("      for element in arr:                   # n iterations")
    print("          if element in seen:               # O(1) avg lookup")
    print("              return True")
    print("          seen.add(element)                 # O(1) avg insert")
    print("      return False")
    print()
    print("  Key Insight: Sets use HASHING for O(1) lookups instead of")
    print("  comparing against every previous element.")
    print()

    # --- Correctness Test ---
    print("--- Correctness Verification ---")
    print()

    test_cases = [
        ([1, 2, 3, 4, 5], False, "No duplicates"),
        ([1, 2, 3, 2, 5], True, "Duplicate: 2"),
        ([1, 1], True, "Two same elements"),
        ([1], False, "Single element"),
        ([], False, "Empty array"),
        ([5, 5, 5, 5], True, "All same"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 1], True, "Duplicate at end"),
    ]

    print(f"  {'Input':>30}  |  {'Expected':>8}  |  {'Brute':>6}  |  {'Set':>5}  |  {'Sort':>5}")
    print(f"  {'-'*30}  |  {'-'*8}  |  {'-'*6}  |  {'-'*5}  |  {'-'*5}")

    all_correct = True
    for arr, expected, desc in test_cases:
        r_brute = has_dup_brute_force(arr)
        r_set = has_dup_set(arr)
        r_sort = has_dup_sort(arr)
        ok = r_brute == r_set == r_sort == expected
        if not ok:
            all_correct = False
        print(f"  {str(arr):>30}  |  {str(expected):>8}  |  {str(r_brute):>6}  |  {str(r_set):>5}  |  {str(r_sort):>5}")

    print()
    print(f"  All methods agree: {'✓ YES' if all_correct else '✗ NO'}")
    print()

    # --- Performance Comparison ---
    print("--- Performance Comparison ---")
    print()

    sizes = [100, 500, 1_000, 5_000, 10_000]

    print(f"  {'n':>7}  |  {'O(n²) Brute':>14}  |  {'O(n) Set':>12}  |  {'Speedup':>8}")
    print(f"  {'-'*7}  |  {'-'*14}  |  {'-'*12}  |  {'-'*8}")

    for size in sizes:
        # Create array with no duplicates (worst case for both)
        arr = list(range(size))
        random.shuffle(arr)

        # Time brute force
        start = time.perf_counter()
        _ = has_dup_brute_force(arr)
        brute_time = time.perf_counter() - start

        # Time set approach
        start = time.perf_counter()
        _ = has_dup_set(arr)
        set_time = time.perf_counter() - start

        speedup = brute_time / set_time if set_time > 0 else float("inf")

        print(
            f"  {size:>7,}  |  "
            f"{brute_time*1000:>11.3f} ms  |  "
            f"{set_time*1000:>9.3f} ms  |  "
            f"{speedup:>7.1f}x"
        )

    print()

    # --- Complexity Summary ---
    print("--- Complexity Summary ---")
    print()
    print("  Method        | Time       | Space  | Data Structure")
    print("  --------------|------------|--------|---------------")
    print("  Brute Force   | O(n²)      | O(1)   | None (nested loops)")
    print("  Hash Set      | O(n)       | O(n)   | set (hash table)")
    print("  Sorting       | O(n log n) | O(n)   | sorted array")
    print()
    print("  The SET approach trades O(n) space for a dramatic improvement")
    print("  from O(n²) → O(n) time. This is a classic space-time tradeoff.")
    print()
    print("ANSWER: Use a SET for O(1) lookups, reducing overall time to O(n).")


if __name__ == "__main__":
    demonstrate_optimization()
