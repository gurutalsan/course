"""
Q5. Compare: bubble sort, merge sort, quick sort, Python's sorted().

Answer:
    Bubble:  O(n²) avg/worst, O(1) space, stable. Only for tiny/nearly-sorted.
    Merge:   O(n log n) always, O(n) space, stable. Guaranteed performance.
    Quick:   O(n log n) avg, O(n²) worst, O(log n) space, unstable. Fastest in practice.
    Timsort: O(n log n) worst, O(n) space, stable. Python's default — hybrid merge+insert.
"""

import time
import random


def bubble_sort(arr):
    """O(n²) average, O(1) space, stable."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def merge_sort(arr):
    """O(n log n) always, O(n) space, stable."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """O(n log n) avg, O(n²) worst, O(log n) space, unstable."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def benchmark(sort_fn, arr, name):
    """Benchmark a sort function."""
    start = time.perf_counter()
    result = sort_fn(arr.copy())
    elapsed = (time.perf_counter() - start) * 1000
    return elapsed, result == sorted(arr)


def demonstrate():
    print("=" * 70)
    print("Q5: Sorting Algorithm Comparison")
    print("=" * 70)
    print()

    print("--- Complexity Comparison ---")
    print()
    print("  Algorithm   | Best      | Average   | Worst     | Space  | Stable")
    print("  ------------|-----------|-----------|-----------|--------|-------")
    print("  Bubble      | O(n)      | O(n²)     | O(n²)     | O(1)   | Yes")
    print("  Merge       | O(n logn) | O(n logn) | O(n logn) | O(n)   | Yes")
    print("  Quick       | O(n logn) | O(n logn) | O(n²)     | O(logn)| No")
    print("  Timsort★    | O(n)      | O(n logn) | O(n logn) | O(n)   | Yes")
    print()

    # Benchmarks
    sizes = [1000, 5000]
    for n in sizes:
        print(f"--- Benchmark: n = {n:,} ---")
        print()

        random_arr = [random.randint(0, n) for _ in range(n)]
        sorted_arr = sorted(random_arr)
        reversed_arr = sorted_arr[::-1]

        scenarios = [
            ("Random", random_arr),
            ("Sorted", sorted_arr),
            ("Reversed", reversed_arr),
        ]

        algos = [
            ("Bubble", bubble_sort),
            ("Merge", merge_sort),
            ("Quick", quick_sort),
            ("Timsort", sorted),
        ]

        print(f"  {'Algorithm':>10} |", end="")
        for name, _ in scenarios:
            print(f" {name:>10} |", end="")
        print()
        print(f"  {'-'*10} |" + (" " + "-"*10 + " |") * len(scenarios))

        for algo_name, algo_fn in algos:
            print(f"  {algo_name:>10} |", end="")
            for _, arr in scenarios:
                if algo_name == "Bubble" and n > 3000:
                    print(f" {'(slow)':>10} |", end="")
                    continue
                ms, correct = benchmark(algo_fn, arr, algo_name)
                mark = "✓" if correct else "✗"
                print(f" {ms:>8.1f}ms |", end="")
            print()
        print()

    # When to use each
    print("--- When to Use Each ---")
    print()
    print("  BUBBLE SORT:")
    print("    • Educational purposes only")
    print("    • Tiny arrays (n < 20)")
    print("    • Nearly sorted arrays (O(n) best case)")
    print()
    print("  MERGE SORT:")
    print("    • Need guaranteed O(n log n)")
    print("    • Need stability (preserve equal element order)")
    print("    • External sorting (data doesn't fit in memory)")
    print()
    print("  QUICK SORT:")
    print("    • General purpose, fastest in practice")
    print("    • Cache-friendly (in-place)")
    print("    • When stability doesn't matter")
    print()
    print("  TIMSORT (Python's sorted()):")
    print("    • ALWAYS use this in Python! Highly optimized.")
    print("    • Hybrid: merge sort + insertion sort")
    print("    • Exploits existing order in real-world data")
    print("    • O(n) for nearly sorted data!")


if __name__ == "__main__":
    demonstrate()
