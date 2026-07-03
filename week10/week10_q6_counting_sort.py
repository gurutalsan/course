"""
Q6. Implement counting sort for integers in range [0, k].
    Limitations vs comparison-based sorts?

Answer:
    Counting sort counts occurrences, then reconstructs the sorted array.
    Time: O(n + k), Space: O(k). NOT comparison-based.

    Limitations:
    - Only works for integers (or items mappable to integers).
    - Space O(k) — impractical when k >> n (e.g., [1, 1000000]).
    - Not in-place.
"""


def counting_sort(arr, max_val=None):
    """
    Counting sort for non-negative integers.
    Time: O(n + k), Space: O(k), Stable: Yes.
    """
    if not arr:
        return []

    if max_val is None:
        max_val = max(arr)

    # Count occurrences
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1

    # Reconstruct sorted array
    result = []
    for val in range(max_val + 1):
        result.extend([val] * count[val])

    return result


def counting_sort_stable(arr, max_val=None):
    """Stable counting sort preserving relative order of equal elements."""
    if not arr:
        return []
    if max_val is None:
        max_val = max(arr)

    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1

    # Cumulative count (prefix sum)
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # Build output in reverse for stability
    output = [0] * len(arr)
    for num in reversed(arr):
        count[num] -= 1
        output[count[num]] = num

    return output


def demonstrate():
    print("=" * 70)
    print("Q6: Counting Sort — Non-Comparison Sort")
    print("=" * 70)
    print()

    arr = [4, 2, 2, 8, 3, 3, 1, 7, 5, 2]
    print(f"  Input: {arr}")
    print()

    # Step by step
    print("--- Step-by-Step ---")
    print()
    max_val = max(arr)
    count = [0] * (max_val + 1)

    print(f"  Step 1: Count occurrences (k = {max_val})")
    for num in arr:
        count[num] += 1
    print(f"    Count array: {count}")
    print(f"    Index:       {list(range(max_val + 1))}")
    print()

    for i, c in enumerate(count):
        if c > 0:
            print(f"    Value {i} appears {c} time(s)")
    print()

    print("  Step 2: Reconstruct sorted array")
    result = []
    for val in range(max_val + 1):
        result.extend([val] * count[val])
        if count[val] > 0:
            print(f"    Add {count[val]}×{val}: {result}")

    print(f"\n  Sorted: {result}")
    print()

    # Verify
    assert counting_sort(arr) == sorted(arr)
    print(f"  Verified: matches sorted() ✓")
    print()

    # --- Limitations ---
    print("--- Limitations vs Comparison-Based Sorts ---")
    print()
    print("  ┌─────────────────────────────────────────────────────────────┐")
    print("  │ Limitation              │ Why it matters                    │")
    print("  ├─────────────────────────┼───────────────────────────────────┤")
    print("  │ Integer-only            │ Can't sort strings, floats, etc  │")
    print("  │ Range-dependent O(k)    │ [1, 10⁹] needs 10⁹ memory!      │")
    print("  │ Non-negative (basic)    │ Negative nums need offset        │")
    print("  │ Not in-place            │ Needs O(n + k) extra space       │")
    print("  │ Not comparison-based    │ Can beat O(n log n) bound!       │")
    print("  └─────────────────────────┴───────────────────────────────────┘")
    print()

    # Comparison
    print("  Counting Sort | Comparison Sort (merge/quick)")
    print("  --------------|-------------------------------")
    print("  O(n + k) time | O(n log n) time")
    print("  O(k) space    | O(n) or O(log n) space")
    print("  Integers only | Any comparable type")
    print("  Stable: Yes   | Merge: Yes, Quick: No")
    print()
    print("  Best when: k ≈ n (range is close to array size)")
    print("  Bad when:  k >> n (wastes space and time on empty buckets)")
    print()

    # Test cases
    print("--- Test Cases ---\n")
    tests = [[4,2,2,8,3,3,1], [0,0,0], [5,4,3,2,1], [1], [], [3,1,4,1,5,9,2,6]]
    for arr in tests:
        got = counting_sort(arr)
        ok = got == sorted(arr)
        print(f"  {str(arr):>25} → {got}  {'✓' if ok else '✗'}")

    print()
    print("  Time: O(n + k) | Space: O(k) | Stable: Yes")


if __name__ == "__main__":
    demonstrate()
