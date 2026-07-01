"""
Q7. What is the space complexity of merge sort?
    Why does it differ from quick sort?

Answer:
    Merge Sort Space Complexity: O(n)
    Quick Sort Space Complexity: O(log n) average, O(n) worst case

    Why they differ:
    - Merge Sort MUST create temporary arrays to merge two sorted halves.
      At each merge step, it allocates space proportional to the subarray
      being merged. The largest merge (final one) requires O(n) space.

    - Quick Sort partitions IN-PLACE by swapping elements within the array.
      It only needs space for the recursive call stack:
        • O(log n) with good pivot choices (balanced partitions)
        • O(n) worst case (already sorted array with bad pivot)
"""

import sys


# ============================================================
# Merge Sort Implementation (with space tracking)
# ============================================================
def merge_sort(arr, depth=0, space_tracker=None):
    """
    Merge Sort — Divide and Conquer.

    Time Complexity:  O(n log n) — always
    Space Complexity: O(n)       — temporary arrays for merging

    Args:
        arr: List to sort
        depth: Current recursion depth (for visualization)
        space_tracker: Dict to track max extra space used
    """
    if space_tracker is None:
        space_tracker = {"max_extra_space": 0, "current_extra_space": 0}

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Split into two halves (creates new arrays!)
    left_half = arr[:mid]    # O(n/2) space
    right_half = arr[mid:]   # O(n/2) space

    # Track space
    space_tracker["current_extra_space"] += len(left_half) + len(right_half)
    space_tracker["max_extra_space"] = max(
        space_tracker["max_extra_space"],
        space_tracker["current_extra_space"]
    )

    # Recursively sort both halves
    left_sorted = merge_sort(left_half, depth + 1, space_tracker)
    right_sorted = merge_sort(right_half, depth + 1, space_tracker)

    # Merge the two sorted halves
    merged = merge(left_sorted, right_sorted)

    # Release space (conceptually)
    space_tracker["current_extra_space"] -= len(left_half) + len(right_half)

    return merged


def merge(left, right):
    """Merge two sorted arrays into one sorted array."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ============================================================
# Quick Sort Implementation (in-place, with stack tracking)
# ============================================================
def quick_sort(arr, low=0, high=None, depth_tracker=None):
    """
    Quick Sort — In-Place, Divide and Conquer.

    Time Complexity:  O(n log n) average, O(n²) worst case
    Space Complexity: O(log n)  average (call stack only)
                      O(n)      worst case (unbalanced partitions)

    Args:
        arr: List to sort (modified in-place)
        low: Start index
        high: End index
        depth_tracker: Dict to track max recursion depth
    """
    if high is None:
        high = len(arr) - 1

    if depth_tracker is None:
        depth_tracker = {"max_depth": 0, "current_depth": 0}

    depth_tracker["current_depth"] += 1
    depth_tracker["max_depth"] = max(
        depth_tracker["max_depth"],
        depth_tracker["current_depth"]
    )

    if low < high:
        # Partition in-place (no extra arrays needed!)
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1, depth_tracker)
        quick_sort(arr, pivot_index + 1, high, depth_tracker)

    depth_tracker["current_depth"] -= 1


def partition(arr, low, high):
    """
    Lomuto partition scheme.
    Partitions array in-place around the pivot (last element).
    Returns the final position of the pivot.
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap in-place!

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def demonstrate_space_complexity():
    """Compare space usage of merge sort vs quick sort."""
    print("=" * 70)
    print("Q7: Space Complexity — Merge Sort vs Quick Sort")
    print("=" * 70)
    print()

    # --- Key Difference ---
    print("--- Key Difference ---")
    print()
    print("  MERGE SORT creates temporary arrays to merge sorted halves.")
    print("  QUICK SORT partitions IN-PLACE using element swaps.")
    print()
    print("  This is why merge sort needs O(n) extra space while")
    print("  quick sort only needs O(log n) for the call stack.")
    print()

    # --- Visual: Merge Sort Memory Usage ---
    print("--- Merge Sort: Memory Allocation at Each Level ---")
    print()
    print("  Original: [38, 27, 43, 3, 9, 82, 10]   (n=7)")
    print()
    print("  Level 0:  [38, 27, 43, 3] | [9, 82, 10]     ← 7 extra cells")
    print("  Level 1:  [38, 27] [43, 3] | [9, 82] [10]   ← 7 extra cells")
    print("  Level 2:  [38] [27] [43] [3] | [9] [82]     ← 6 extra cells")
    print("  Merge ↑:  [27, 38] [3, 43] | [9, 82] [10]   ← 7 extra cells")
    print("  Merge ↑:  [3, 27, 38, 43] | [9, 10, 82]     ← 7 extra cells")
    print("  Merge ↑:  [3, 9, 10, 27, 38, 43, 82]        ← 7 extra cells")
    print()
    print("  → At the final merge, we need O(n) = O(7) extra space.")
    print()

    # --- Visual: Quick Sort In-Place ---
    print("--- Quick Sort: In-Place Partitioning ---")
    print()
    print("  Original: [38, 27, 43, 3, 9, 82, 10]   pivot=10")
    print()
    print("  Step 1: Partition around 10 (swap elements, no new arrays)")
    print("          [3, 9, 10, 27, 43, 82, 38]")
    print("          ← left →  P  ← right →")
    print()
    print("  Step 2: Recurse on left [3, 9] and right [27, 43, 82, 38]")
    print("          (Each recursion = 1 stack frame, no array copies)")
    print()
    print("  → Only the CALL STACK uses space: O(log n) balanced, O(n) worst.")
    print()

    # --- Practical Comparison ---
    print("--- Practical Space Comparison ---")
    print()

    import random

    test_sizes = [10, 100, 1_000, 10_000]

    print(f"  {'n':>7}  |  {'Merge Sort':>20}  |  {'Quick Sort':>20}")
    print(f"  {'':>7}  |  {'Extra Space (cells)':>20}  |  {'Max Stack Depth':>20}")
    print(f"  {'-'*7}  |  {'-'*20}  |  {'-'*20}")

    for n in test_sizes:
        arr = list(range(n))
        random.shuffle(arr)

        # Merge sort space tracking
        space_tracker = {"max_extra_space": 0, "current_extra_space": 0}
        merge_sort(arr.copy(), space_tracker=space_tracker)

        # Quick sort depth tracking
        depth_tracker = {"max_depth": 0, "current_depth": 0}
        arr_copy = arr.copy()
        quick_sort(arr_copy, depth_tracker=depth_tracker)

        print(
            f"  {n:>7,}  |  "
            f"{space_tracker['max_extra_space']:>20,}  |  "
            f"{depth_tracker['max_depth']:>20,}"
        )

    print()

    # --- Summary Table ---
    print("--- Complete Comparison ---")
    print()
    print("  Property          | Merge Sort         | Quick Sort")
    print("  ------------------|--------------------|-----------------")
    print("  Time (Best)       | O(n log n)         | O(n log n)")
    print("  Time (Average)    | O(n log n)         | O(n log n)")
    print("  Time (Worst)      | O(n log n)         | O(n²)")
    print("  Space             | O(n)               | O(log n) avg")
    print("  In-Place?         | No (needs copies)  | Yes (swaps)")
    print("  Stable?           | Yes                | No (standard)")
    print("  How it divides    | Always at midpoint | At pivot position")
    print("  Extra memory from | Temporary arrays   | Call stack only")
    print()
    print("ANSWER:")
    print("  Merge Sort space: O(n) — needs temporary arrays for merging.")
    print("  Quick Sort space: O(log n) avg — partitions in-place, only")
    print("  uses the call stack. It differs because quick sort SWAPS")
    print("  elements within the original array, while merge sort must")
    print("  CREATE new arrays to combine sorted halves.")


if __name__ == "__main__":
    demonstrate_space_complexity()
