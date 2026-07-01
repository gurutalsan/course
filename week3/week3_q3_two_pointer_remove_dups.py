"""
Q3. Explain the two-pointer technique. Write a function that removes
    duplicates from a sorted array in-place and returns the new length.

Answer:
    TWO-POINTER TECHNIQUE:
    Use two indices (pointers) that move through the data structure,
    typically from both ends toward the center, or both from the start
    at different speeds (slow/fast pointer). This eliminates nested loops
    and reduces O(n²) to O(n).

    For removing duplicates from a SORTED array:
    - SLOW pointer: marks the position of the last unique element.
    - FAST pointer: scans ahead to find the next unique element.

    Time Complexity:  O(n) — single pass.
    Space Complexity: O(1) — in-place, no extra array.
"""


def remove_duplicates_inplace(nums: list) -> int:
    """
    Remove duplicates from a SORTED array in-place.

    Modifies the array so that unique elements are at the front.
    Returns the count of unique elements.

    Uses slow/fast two-pointer technique:
    - slow: position to place next unique element.
    - fast: scans ahead for new unique values.

    Time:  O(n) — single pass.
    Space: O(1) — in-place modification.

    Example:
        nums = [1, 1, 2, 2, 3]
        k = remove_duplicates_inplace(nums)
        # k = 3, nums[:k] = [1, 2, 3]
    """
    if not nums:
        return 0

    slow = 0  # Points to last unique element position

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1  # Length = last index + 1


def demonstrate():
    print("=" * 70)
    print("Q3: Two-Pointer Technique — Remove Duplicates In-Place")
    print("=" * 70)
    print()

    # --- Two-Pointer Technique Explanation ---
    print("--- The Two-Pointer Technique ---")
    print()
    print("  Two pointers move through data to solve problems in O(n)")
    print("  instead of O(n²) with nested loops.")
    print()
    print("  Common Patterns:")
    print()
    print("  1. OPPOSITE DIRECTION (converging):")
    print("     [1, 2, 3, 4, 5, 6, 7]")
    print("      ↑                  ↑")
    print("     left →         ← right")
    print("     Use: Pair sum in sorted array, palindrome check, container")
    print()
    print("  2. SAME DIRECTION (slow/fast):")
    print("     [1, 1, 2, 2, 3, 3, 4]")
    print("      ↑  ↑")
    print("     slow fast →→→")
    print("     Use: Remove duplicates, partition, cycle detection")
    print()
    print("  3. TWO ARRAYS:")
    print("     [1, 3, 5]    [2, 4, 6]")
    print("      ↑             ↑")
    print("      i             j")
    print("     Use: Merge sorted arrays, intersection")
    print()

    # --- Algorithm Walkthrough ---
    print("--- Step-by-Step Walkthrough ---")
    print()
    nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    print(f"  Input (sorted): {nums}")
    print()

    # Show step by step
    demo_nums = nums.copy()
    slow = 0

    print(f"  {'Step':>4} | {'fast':>4} | {'nums[fast]':>10} | {'nums[slow]':>10} | {'Action':>25} | {'Array State'}")
    print(f"  {'-'*4} | {'-'*4} | {'-'*10} | {'-'*10} | {'-'*25} | {'-'*30}")

    print(f"  init |    0 | {demo_nums[0]:>10} | {demo_nums[0]:>10} | {'slow=0, start':>25} | {demo_nums}")

    for fast in range(1, len(demo_nums)):
        if demo_nums[fast] != demo_nums[slow]:
            slow += 1
            demo_nums[slow] = demo_nums[fast]
            action = f"NEW! slow→{slow}, copy {demo_nums[fast]}"
        else:
            action = f"SKIP (same as nums[{slow}])"

        # Visual marker
        arr_str = "["
        for idx in range(len(demo_nums)):
            if idx == slow and idx == fast:
                arr_str += f"*{demo_nums[idx]}*"
            elif idx == slow:
                arr_str += f"s{demo_nums[idx]}"
            elif idx == fast:
                arr_str += f"f{demo_nums[idx]}"
            else:
                arr_str += f" {demo_nums[idx]}"
            if idx < len(demo_nums) - 1:
                arr_str += ","
        arr_str += "]"

        print(f"  {fast:>4} | {fast:>4} | {nums[fast]:>10} | {demo_nums[slow]:>10} | {action:>25} | {arr_str}")

    new_length = slow + 1
    print()
    print(f"  New length: {new_length}")
    print(f"  Result: {demo_nums[:new_length]}  (first {new_length} elements)")
    print()

    # --- Visual Diagram ---
    print("--- Visual: Slow/Fast Pointer Movement ---")
    print()
    nums_vis = [1, 1, 2, 2, 3]
    print(f"  Array: {nums_vis}")
    print()
    print("  Initial:")
    print("    [1, 1, 2, 2, 3]")
    print("     S  F              slow=0, fast=1: same → skip")
    print()
    print("    [1, 1, 2, 2, 3]")
    print("     S     F           slow=0, fast=2: different! → slow=1, copy")
    print()
    print("    [1, 2, 2, 2, 3]")
    print("        S     F        slow=1, fast=3: same → skip")
    print()
    print("    [1, 2, 2, 2, 3]")
    print("        S        F     slow=1, fast=4: different! → slow=2, copy")
    print()
    print("    [1, 2, 3, 2, 3]")
    print("           S      F    Done! Length = slow+1 = 3")
    print()
    print("    Result: [1, 2, 3]  ← first 3 elements")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([1, 1, 2], 2, "Basic"),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, "Multiple dups"),
        ([1, 1, 1, 1, 1], 1, "All same"),
        ([1, 2, 3, 4, 5], 5, "No duplicates"),
        ([], 0, "Empty"),
        ([42], 1, "Single element"),
        ([1, 1, 2, 2, 2, 3, 4, 4, 5], 5, "Mixed"),
    ]

    print(f"  {'Input':>35}  | {'Expected':>8} | {'Got':>3} | {'Result Array':>20} | {'✓/✗':>3}")
    print(f"  {'-'*35}  | {'-'*8} | {'-'*3} | {'-'*20} | {'-'*3}")

    for nums, expected, desc in test_cases:
        nums_copy = nums.copy()
        k = remove_duplicates_inplace(nums_copy)
        status = "✓" if k == expected else "✗"
        result_arr = str(nums_copy[:k])
        nums_str = str(nums) if len(str(nums)) <= 33 else str(nums)[:30] + "..."
        print(f"  {nums_str:>35}  | {expected:>8} | {k:>3} | {result_arr:>20} | {status:>3}")

    print()

    # --- More Two-Pointer Examples ---
    print("--- More Two-Pointer Applications ---")
    print()

    # Example: Two Sum in sorted array (converging pointers)
    print("  1. Two Sum in Sorted Array (converging pointers):")
    print()

    def two_sum_sorted(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            elif s < target:
                left += 1
            else:
                right -= 1
        return []

    arr = [1, 3, 5, 7, 9, 11]
    target = 12
    result = two_sum_sorted(arr, target)
    print(f"    arr={arr}, target={target}")
    print(f"    Result: {result} → {arr[result[0]]} + {arr[result[1]]} = {target}")
    print()

    # Example: Palindrome check (converging pointers)
    print("  2. Palindrome Check (converging pointers):")
    print()

    def is_palindrome(s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    for word in ["racecar", "hello", "madam"]:
        print(f"    '{word}' → {is_palindrome(word)}")

    print()

    # --- Complexity ---
    print("--- Complexity Summary ---")
    print()
    print("  Without two pointers (brute force):  O(n²)")
    print("  With two pointers:                   O(n)")
    print("  Space:                               O(1) — in-place!")
    print()
    print("ANSWER:")
    print("  Two-pointer technique uses two indices moving through data")
    print("  to avoid nested loops. For removing duplicates from a sorted")
    print("  array: slow pointer tracks unique position, fast pointer scans")
    print("  ahead. Time: O(n), Space: O(1).")


if __name__ == "__main__":
    demonstrate()
