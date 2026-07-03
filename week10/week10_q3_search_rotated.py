"""
Q3. Search in rotated sorted array [4,5,6,7,0,1,2], target=0.
    Modified binary search. Key insight?

Answer:
    Key Insight: In a rotated sorted array, at least ONE half is always
    sorted. Check which half is sorted, then check if target falls in
    that sorted range. If yes, search there; otherwise search the other half.

    Time: O(log n), Space: O(1).
"""


def search_rotated(nums, target):
    """
    Modified binary search for rotated sorted array.
    At each step, one half is guaranteed sorted.
    Time: O(log n), Space: O(1).
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target in sorted left half
            else:
                left = mid + 1   # Target in right half
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Target in sorted right half
            else:
                right = mid - 1  # Target in left half

    return -1


def demonstrate():
    print("=" * 70)
    print("Q3: Search in Rotated Sorted Array")
    print("=" * 70)
    print()

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(f"  Array:  {nums}")
    print(f"  Target: {target}")
    print()

    print("--- Key Insight ---")
    print()
    print("  Original sorted: [0, 1, 2, 4, 5, 6, 7]")
    print("  Rotated at idx 4: [4, 5, 6, 7, | 0, 1, 2]")
    print("                     ← sorted →   ← sorted →")
    print()
    print("  At any mid point, ONE HALF is always sorted!")
    print("  Check if target is in the sorted half → narrow search.")
    print()

    # Trace
    print("--- Binary Search Trace ---")
    print()
    left, right = 0, len(nums) - 1

    print(f"  {'Step':>4} | {'L':>2} {'M':>2} {'R':>2} | {'nums[L..R]':>20} | {'Sorted half':>12} | {'Action'}")
    print(f"  {'-'*4} | {'-'*8} | {'-'*20} | {'-'*12} | {'-'*25}")

    step = 0
    while left <= right:
        step += 1
        mid = (left + right) // 2

        if nums[mid] == target:
            print(f"  {step:>4} | {left:>2} {mid:>2} {right:>2} | {nums[left:right+1]} | — | FOUND at index {mid}!")
            break

        if nums[left] <= nums[mid]:
            sorted_half = "Left"
            if nums[left] <= target < nums[mid]:
                action = f"{target} in [{nums[left]},{nums[mid]}) → go LEFT"
                right = mid - 1
            else:
                action = f"{target} not in [{nums[left]},{nums[mid]}) → go RIGHT"
                left = mid + 1
        else:
            sorted_half = "Right"
            if nums[mid] < target <= nums[right]:
                action = f"{target} in ({nums[mid]},{nums[right]}] → go RIGHT"
                left = mid + 1
            else:
                action = f"{target} not in ({nums[mid]},{nums[right]}] → go LEFT"
                right = mid - 1

        print(f"  {step:>4} | {left:>2} {mid:>2} {right:>2} | {str(nums[min(left,mid):max(right,mid)+1]):>20} | {sorted_half:>12} | {action}")

    print()
    print(f"  Result: index {search_rotated(nums, target)}")
    print()

    # Test cases
    print("--- Test Cases ---\n")
    tests = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([4,5,6,7,0,1,2], 6, 2),
        ([1], 1, 0),
        ([1], 0, -1),
        ([2,1], 1, 1),
        ([3,1,2], 3, 0),
        ([6,7,1,2,3,4,5], 4, 5),
    ]

    for nums, target, expected in tests:
        got = search_rotated(nums, target)
        print(f"  {str(nums):>22}, target={target} → idx={got} {'✓' if got==expected else '✗'}")

    print()
    print("  Time: O(log n) | Space: O(1)")
    print("  Key: one half is always sorted → decide which half to search.")


if __name__ == "__main__":
    demonstrate()
