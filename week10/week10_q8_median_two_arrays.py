"""
Q8. Median of two sorted arrays in O(log(min(m,n))).

Answer:
    Binary search on the SHORTER array to find the correct partition.
    Partition both arrays such that:
      left_part has (m+n+1)//2 elements,
      max(left_part) ≤ min(right_part).

    Binary search adjusts the partition of the shorter array.
    Time: O(log(min(m,n))), Space: O(1).

    This is LeetCode Hard #4.
"""


def find_median(nums1, nums2):
    """
    Find median of two sorted arrays.
    Binary search on the shorter array.
    Time: O(log(min(m,n))), Space: O(1).
    """
    # Ensure nums1 is the shorter array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    low, high = 0, m
    half = (m + n + 1) // 2

    while low <= high:
        i = (low + high) // 2   # Partition index in nums1
        j = half - i             # Partition index in nums2

        # Edge values (use -inf/inf for out-of-bounds)
        left1 = nums1[i - 1] if i > 0 else float('-inf')
        right1 = nums1[i] if i < m else float('inf')
        left2 = nums2[j - 1] if j > 0 else float('-inf')
        right2 = nums2[j] if j < n else float('inf')

        # Check if partition is correct
        if left1 <= right2 and left2 <= right1:
            # Found the correct partition!
            if (m + n) % 2 == 1:
                return max(left1, left2)  # Odd total: median is max of left
            else:
                return (max(left1, left2) + min(right1, right2)) / 2.0
        elif left1 > right2:
            high = i - 1  # Move partition left in nums1
        else:
            low = i + 1   # Move partition right in nums1

    return 0.0


def find_median_simple(nums1, nums2):
    """Simple O(m+n) merge approach for verification."""
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]
    return (merged[n // 2 - 1] + merged[n // 2]) / 2.0


def demonstrate():
    print("=" * 70)
    print("Q8: Median of Two Sorted Arrays — O(log(min(m,n)))")
    print("=" * 70)
    print()

    nums1 = [1, 3, 8]
    nums2 = [2, 4, 5, 6, 7]
    print(f"  nums1: {nums1}")
    print(f"  nums2: {nums2}")
    print(f"  Merged: {sorted(nums1 + nums2)}")
    print(f"  Median: {find_median(nums1, nums2)}")
    print()

    # --- The Approach ---
    print("--- Binary Search Partition Approach ---")
    print()
    print("  Goal: Partition BOTH arrays into left_part and right_part")
    print("  such that:")
    print("    1. |left_part| = (m + n + 1) // 2")
    print("    2. max(left_part) ≤ min(right_part)")
    print()
    print("  Binary search on shorter array to find partition point 'i'.")
    print("  Then j = half - i (partition in longer array).")
    print()
    print("  nums1:  [... left1 | right1 ...]")
    print("  nums2:  [... left2 | right2 ...]")
    print("  Valid if: left1 ≤ right2 AND left2 ≤ right1")
    print()

    # --- Trace ---
    print("--- Trace: nums1=[1,3,8], nums2=[2,4,5,6,7] ---")
    print()

    a, b = nums1, nums2
    if len(a) > len(b):
        a, b = b, a

    m, n = len(a), len(b)
    half = (m + n + 1) // 2
    low, high = 0, m

    print(f"  Shorter array: {a} (m={m})")
    print(f"  Longer array:  {b} (n={n})")
    print(f"  Half = {half}")
    print()

    step = 0
    print(f"  {'Step':>4} | {'i':>2} {'j':>2} | {'L1':>4} {'R1':>4} {'L2':>4} {'R2':>4} | {'Valid?':>6} | {'Action'}")
    print(f"  {'-'*4} | {'-'*5} | {'-'*19} | {'-'*6} | {'-'*20}")

    while low <= high:
        step += 1
        i = (low + high) // 2
        j = half - i

        l1 = a[i-1] if i > 0 else float('-inf')
        r1 = a[i] if i < m else float('inf')
        l2 = b[j-1] if j > 0 else float('-inf')
        r2 = b[j] if j < n else float('inf')

        l1s = str(l1) if l1 != float('-inf') else "-∞"
        r1s = str(r1) if r1 != float('inf') else "+∞"
        l2s = str(l2) if l2 != float('-inf') else "-∞"
        r2s = str(r2) if r2 != float('inf') else "+∞"

        if l1 <= r2 and l2 <= r1:
            if (m + n) % 2 == 1:
                med = max(l1, l2)
            else:
                med = (max(l1, l2) + min(r1, r2)) / 2.0
            print(f"  {step:>4} | {i:>2} {j:>2} | {l1s:>4} {r1s:>4} {l2s:>4} {r2s:>4} | {'YES':>6} | Median = {med} ★")
            break
        elif l1 > r2:
            print(f"  {step:>4} | {i:>2} {j:>2} | {l1s:>4} {r1s:>4} {l2s:>4} {r2s:>4} | {'NO':>6} | L1>R2 → move i LEFT")
            high = i - 1
        else:
            print(f"  {step:>4} | {i:>2} {j:>2} | {l1s:>4} {r1s:>4} {l2s:>4} {r2s:>4} | {'NO':>6} | L2>R1 → move i RIGHT")
            low = i + 1

    print()

    # Visual partition
    print("--- Visual: Correct Partition ---")
    print()
    print("  nums1: [1, 3 | 8]        i=2")
    print("  nums2: [2, 4 | 5, 6, 7]  j=3")
    print()
    print("  Left part:  [1, 2, 3, 4]  (max = 4)")
    print("  Right part: [5, 6, 7, 8]  (min = 5)")
    print("  4 ≤ 5 ✓")
    print("  Median = (4 + 5) / 2 = 4.5")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---\n")
    tests = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([1, 3, 8], [2, 4, 5, 6, 7], 4.5),
        ([1], [2, 3, 4], 2.5),
        ([], [1], 1.0),
        ([], [1, 2], 1.5),
        ([1, 2, 3], [4, 5, 6], 3.5),
        ([3], [-2, -1], -1.0),
    ]

    all_pass = True
    for a, b, expected in tests:
        got = find_median(a, b)
        verify = find_median_simple(a, b)
        ok = abs(got - expected) < 1e-9 and abs(got - verify) < 1e-9
        if not ok: all_pass = False
        print(f"  {str(a):>12} + {str(b):>15} → {got:>5} (expected {expected}) {'✓' if ok else '✗'}")

    print(f"\n  All passed: {'✓' if all_pass else '✗'}")
    print()
    print("  Time: O(log(min(m,n))) — binary search on shorter array")
    print("  Space: O(1)")
    print("  This is LeetCode Hard #4!")


if __name__ == "__main__":
    demonstrate()
