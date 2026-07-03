"""
Q1. Implement merge sort and trace through for [38,27,43,3,9,82,10].

Answer:
    Merge sort: Divide array in half recursively until single elements,
    then MERGE sorted halves back together.

    Time:  O(n log n) — always (best, average, worst).
    Space: O(n) — temporary arrays during merge.
    Stable: Yes (equal elements keep original order).
"""


def merge_sort(arr):
    """
    Merge sort — divide and conquer.
    Time: O(n log n), Space: O(n), Stable: Yes.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


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


def merge_sort_trace(arr, depth=0):
    """Merge sort with visual trace."""
    indent = "    " * depth
    print(f"{indent}sort({arr})")

    if len(arr) <= 1:
        print(f"{indent}  → base case: {arr}")
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    print(f"{indent}  split: {left_half} | {right_half}")

    left = merge_sort_trace(left_half, depth + 1)
    right = merge_sort_trace(right_half, depth + 1)

    merged = merge(left, right)
    print(f"{indent}  merge({left}, {right}) → {merged}")
    return merged


def demonstrate():
    print("=" * 70)
    print("Q1: Merge Sort — Divide and Conquer")
    print("=" * 70)
    print()

    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"  Input: {arr}")
    print()

    # Visual divide and merge
    print("--- Divide Phase ---")
    print()
    print("  [38, 27, 43, 3, 9, 82, 10]")
    print("        /                \\")
    print("  [38, 27, 43]      [3, 9, 82, 10]")
    print("    /      \\          /         \\")
    print("  [38]  [27, 43]   [3, 9]    [82, 10]")
    print("         /   \\     /   \\      /    \\")
    print("       [27] [43] [3]  [9]  [82]  [10]")
    print()

    print("--- Merge Phase ---")
    print()
    print("       [27] [43] [3]  [9]  [82]  [10]")
    print("         \\   /     \\   /      \\    /")
    print("        [27,43]   [3, 9]    [10, 82]")
    print("    \\      /          \\         /")
    print("  [27, 38, 43]      [3, 9, 10, 82]")
    print("        \\                /")
    print("  [3, 9, 10, 27, 38, 43, 82]")
    print()

    # Actual trace
    print("--- Recursive Trace ---")
    print()
    result = merge_sort_trace(arr.copy())
    print()
    print(f"  Result: {result}")
    print()

    # Merge step detail
    print("--- Merge Step Detail: merge([27,38,43], [3,9,10,82]) ---")
    print()
    left = [27, 38, 43]
    right = [3, 9, 10, 82]
    i = j = 0
    res = []
    step = 0

    print(f"  {'Step':>4} | {'Compare':>12} | {'Pick':>5} | {'Result':>25}")
    print(f"  {'-'*4} | {'-'*12} | {'-'*5} | {'-'*25}")

    while i < len(left) and j < len(right):
        step += 1
        cmp = f"{left[i]} vs {right[j]}"
        if left[i] <= right[j]:
            res.append(left[i])
            pick = left[i]
            i += 1
        else:
            res.append(right[j])
            pick = right[j]
            j += 1
        print(f"  {step:>4} | {cmp:>12} | {pick:>5} | {res}")

    remaining = left[i:] + right[j:]
    if remaining:
        res.extend(remaining)
        print(f"  {step+1:>4} | {'append rest':>12} | {remaining} | {res}")

    print()

    # Verify
    assert merge_sort(arr) == sorted(arr)
    print(f"  Verified: merge_sort matches sorted() ✓")
    print()
    print("  Time: O(n log n) ALWAYS | Space: O(n) | Stable: Yes")
    print("  log₂(7) ≈ 3 levels of recursion, each level does O(n) merge work")


if __name__ == "__main__":
    demonstrate()
