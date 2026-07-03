"""
Q2. Implement quicksort with Lomuto partition. Worst case? How to avoid it?

Answer:
    Lomuto partition: pivot = last element. Partition into [≤pivot | >pivot | pivot].
    Worst case: O(n²) when array is already sorted (pivot is always min/max).
    Avoid: randomized pivot, median-of-three, or use introsort.

    Average: O(n log n), Worst: O(n²), Space: O(log n) stack, In-place, Unstable.
"""

import random


def quicksort(arr, low=0, high=None):
    """Quicksort with Lomuto partition. In-place."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_idx = lomuto_partition(arr, low, high)
        quicksort(arr, low, pivot_idx - 1)
        quicksort(arr, pivot_idx + 1, high)


def lomuto_partition(arr, low, high):
    """
    Lomuto partition: pivot = arr[high].
    Rearranges so that all elements ≤ pivot are on the left.
    Returns the final position of the pivot.
    """
    pivot = arr[high]
    i = low - 1  # Boundary of "≤ pivot" region

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_random(arr, low=0, high=None):
    """Quicksort with randomized pivot to avoid worst case."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        rand_idx = random.randint(low, high)
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
        pivot_idx = lomuto_partition(arr, low, high)
        quicksort_random(arr, low, pivot_idx - 1)
        quicksort_random(arr, pivot_idx + 1, high)


def demonstrate():
    print("=" * 70)
    print("Q2: Quicksort — Lomuto Partition")
    print("=" * 70)
    print()

    arr = [10, 7, 8, 9, 1, 5]
    print(f"  Input: {arr}")
    print()

    # Trace partition
    print("--- Lomuto Partition Trace: pivot=5 (last element) ---")
    print()
    trace_arr = arr.copy()
    print(f"  Array: {trace_arr}, pivot = {trace_arr[-1]}")
    print()

    pivot = trace_arr[-1]
    i = -1
    print(f"  {'j':>3} | {'arr[j]':>6} | {'≤pivot?':>7} | {'Swap':>15} | {'Array':>25} | {'i'}")
    print(f"  {'-'*3} | {'-'*6} | {'-'*7} | {'-'*15} | {'-'*25} | {'-'*3}")

    for j in range(len(trace_arr) - 1):
        if trace_arr[j] <= pivot:
            i += 1
            trace_arr[i], trace_arr[j] = trace_arr[j], trace_arr[i]
            swap = f"swap [{i}]↔[{j}]"
        else:
            swap = "—"
        lte = "Yes" if arr[j] <= pivot else "No"
        print(f"  {j:>3} | {arr[j]:>6} | {lte:>7} | {swap:>15} | {str(trace_arr):>25} | {i}")

    trace_arr[i + 1], trace_arr[-1] = trace_arr[-1], trace_arr[i + 1]
    print(f"\n  Place pivot: swap [{i+1}]↔[{len(trace_arr)-1}]")
    print(f"  Result: {trace_arr}, pivot at index {i+1}")
    print(f"  Left (≤5): {trace_arr[:i+1]}, Pivot: {trace_arr[i+1]}, Right (>5): {trace_arr[i+2:]}")
    print()

    # Full sort
    arr2 = [10, 7, 8, 9, 1, 5]
    quicksort(arr2)
    print(f"  Sorted: {arr2}")
    print()

    # --- Worst Case ---
    print("--- Worst Case: O(n²) ---")
    print()
    print("  Happens when pivot is always the MIN or MAX element:")
    print("  • Already sorted array: [1,2,3,4,5], pivot=5")
    print("    Partition: [1,2,3,4] | 5 → only 1 element removed each time")
    print("    Depth = n → O(n²)")
    print()
    print("  • Already reverse sorted: [5,4,3,2,1], pivot=1")
    print("    Same problem: partition splits (0, n-1)")
    print()

    print("--- How to Avoid Worst Case ---")
    print()
    print("  1. RANDOMIZED PIVOT: Pick random element as pivot")
    print("     → Expected O(n log n), worst case still O(n²) but unlikely")
    print()
    print("  2. MEDIAN-OF-THREE: Pick median of first, middle, last")
    print("     → Avoids worst case for sorted/reverse-sorted inputs")
    print()
    print("  3. INTROSORT: Switch to heapsort when recursion depth > 2·log(n)")
    print("     → Guaranteed O(n log n). Python's sorted() uses Timsort.")
    print()

    # Verify randomized version
    tests = [[5,4,3,2,1], [1,2,3,4,5], [3,1,4,1,5,9,2,6], [1], []]
    print("--- Test Cases ---\n")
    for arr in tests:
        original = arr.copy()
        quicksort_random(arr)
        ok = arr == sorted(original)
        print(f"  {str(original):>25} → {arr}  {'✓' if ok else '✗'}")

    print()
    print("  Average: O(n log n) | Worst: O(n²) | Space: O(log n) | Unstable")


if __name__ == "__main__":
    demonstrate()
