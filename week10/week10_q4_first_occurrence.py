"""
Q4. Binary search for FIRST occurrence in sorted array with duplicates.
    Example: [1,2,2,2,3,4], target=2 → index 1.

Answer:
    Standard binary search finds ANY occurrence. To find the FIRST:
    When target is found, DON'T return — keep searching LEFT (right = mid - 1).
    Record the position and continue until left > right.

    Time: O(log n), Space: O(1).
"""


def first_occurrence(nums, target):
    """Find the FIRST occurrence of target. O(log n)."""
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid       # Record position
            right = mid - 1    # Keep searching LEFT for earlier occurrence
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def last_occurrence(nums, target):
    """Find the LAST occurrence of target. O(log n)."""
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid       # Record position
            left = mid + 1     # Keep searching RIGHT for later occurrence
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def count_occurrences(nums, target):
    """Count occurrences using first and last. O(log n)."""
    first = first_occurrence(nums, target)
    if first == -1:
        return 0
    last = last_occurrence(nums, target)
    return last - first + 1


def demonstrate():
    print("=" * 70)
    print("Q4: First Occurrence — Binary Search with Duplicates")
    print("=" * 70)
    print()

    nums = [1, 2, 2, 2, 3, 4]
    target = 2
    print(f"  Array:  {nums}")
    print(f"  Target: {target}")
    print()

    # Trace
    print("--- Trace: Finding FIRST occurrence of 2 ---")
    print()
    left, right = 0, len(nums) - 1
    result = -1

    print(f"  {'Step':>4} | {'L':>2} {'M':>2} {'R':>2} | {'nums[M]':>7} | {'Action':>30} | {'Result'}")
    print(f"  {'-'*4} | {'-'*8} | {'-'*7} | {'-'*30} | {'-'*6}")

    step = 0
    while left <= right:
        step += 1
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            action = f"Found! Record {mid}, go LEFT"
            right = mid - 1
        elif nums[mid] < target:
            action = f"{nums[mid]} < {target}, go RIGHT"
            left = mid + 1
        else:
            action = f"{nums[mid]} > {target}, go LEFT"
            right = mid - 1
        print(f"  {step:>4} | {left:>2} {mid:>2} {right:>2} | {nums[mid]:>7} | {action:>30} | {result}")

    print(f"\n  First occurrence of {target}: index {result}")
    print()

    # Compare standard vs first
    print("--- Standard vs First Occurrence ---")
    print()
    print(f"  Array: {nums}")
    print(f"  Standard binary search might return index 2 (any '2')")
    print(f"  First occurrence search returns index {first_occurrence(nums, target)} (leftmost '2') ✓")
    print(f"  Last occurrence search returns index {last_occurrence(nums, target)} (rightmost '2')")
    print(f"  Count of {target}: {count_occurrences(nums, target)}")
    print()

    # The key difference
    print("--- Key Difference ---")
    print()
    print("  Standard:  if nums[mid] == target: return mid  ← stops immediately")
    print("  First:     if nums[mid] == target:")
    print("               result = mid        ← record it")
    print("               right = mid - 1     ← keep searching LEFT ★")
    print("  Last:      if nums[mid] == target:")
    print("               result = mid        ← record it")
    print("               left = mid + 1      ← keep searching RIGHT ★")
    print()

    # Test cases
    print("--- Test Cases ---\n")
    tests = [
        ([1,2,2,2,3,4], 2, 1, 3),
        ([1,1,1,1,1], 1, 0, 4),
        ([1,2,3,4,5], 3, 2, 2),
        ([1,2,3,4,5], 6, -1, -1),
        ([2,2,2,2], 2, 0, 3),
        ([1,3,3,5,5,5,7], 5, 3, 5),
    ]

    print(f"  {'Array':>22} | {'Target':>6} | {'First':>5} | {'Last':>4} | {'Count':>5}")
    print(f"  {'-'*22} | {'-'*6} | {'-'*5} | {'-'*4} | {'-'*5}")
    for nums, t, exp_f, exp_l in tests:
        f = first_occurrence(nums, t)
        l = last_occurrence(nums, t)
        cnt = count_occurrences(nums, t)
        ok = f == exp_f and l == exp_l
        print(f"  {str(nums):>22} | {t:>6} | {f:>5} | {l:>4} | {cnt:>5}  {'✓' if ok else '✗'}")

    print()
    print("  Time: O(log n) | Space: O(1)")


if __name__ == "__main__":
    demonstrate()
