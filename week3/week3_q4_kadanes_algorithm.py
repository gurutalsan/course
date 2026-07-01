"""
Q4. Given an array [1,-2,3,4,-1,2,1,-5,4], find the contiguous subarray
    with the largest sum (Kadane's algorithm). What is the time complexity?

Answer:
    Kadane's Algorithm finds the maximum subarray sum in O(n).

    For [1, -2, 3, 4, -1, 2, 1, -5, 4]:
        Maximum subarray sum = 9
        Subarray = [3, 4, -1, 2, 1]

    Core Idea:
    At each position, decide: Is it better to
    (a) extend the previous subarray by adding current element, OR
    (b) start a new subarray from the current element?

    current_sum = max(num, current_sum + num)

    Time Complexity:  O(n) — single pass.
    Space Complexity: O(1) — only tracking two variables.
"""


# ============================================================
# Kadane's Algorithm ★ OPTIMAL ★
# ============================================================
def max_subarray_kadane(nums: list) -> tuple:
    """
    Find the contiguous subarray with the largest sum using Kadane's algorithm.

    Time:  O(n) — single pass.
    Space: O(1) — two variables only.

    Returns:
        (max_sum, start_index, end_index)
    """
    if not nums:
        return 0, -1, -1

    max_sum = nums[0]
    current_sum = nums[0]
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        # Key decision: extend current subarray or start fresh?
        if current_sum + nums[i] < nums[i]:
            current_sum = nums[i]
            temp_start = i  # New subarray starts here
        else:
            current_sum += nums[i]

        # Update global max
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, start, end


# ============================================================
# Brute Force — O(n²) for comparison
# ============================================================
def max_subarray_brute(nums: list) -> tuple:
    """
    Brute force: check every possible subarray.

    Time:  O(n²) — two nested loops.
    Space: O(1)
    """
    if not nums:
        return 0, -1, -1

    max_sum = float('-inf')
    start = end = 0

    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start, end = i, j

    return max_sum, start, end


# ============================================================
# Divide and Conquer — O(n log n)
# ============================================================
def max_subarray_divide_conquer(nums: list) -> int:
    """
    Divide and conquer approach.

    Time:  O(n log n) — split in half, merge results.
    Space: O(log n)   — recursion stack.
    """
    def helper(left, right):
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        # Max sum in left half
        left_max = helper(left, mid)
        # Max sum in right half
        right_max = helper(mid + 1, right)

        # Max sum crossing the midpoint
        left_cross = float('-inf')
        total = 0
        for i in range(mid, left - 1, -1):
            total += nums[i]
            left_cross = max(left_cross, total)

        right_cross = float('-inf')
        total = 0
        for i in range(mid + 1, right + 1):
            total += nums[i]
            right_cross = max(right_cross, total)

        cross_max = left_cross + right_cross

        return max(left_max, right_max, cross_max)

    if not nums:
        return 0
    return helper(0, len(nums) - 1)


def demonstrate():
    print("=" * 70)
    print("Q4: Maximum Subarray Sum — Kadane's Algorithm")
    print("=" * 70)
    print()

    # --- Problem ---
    nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]
    print(f"  Array: {nums}")
    print()

    # --- Result ---
    max_sum, start, end = max_subarray_kadane(nums)
    subarray = nums[start:end + 1]
    print(f"  Maximum subarray sum: {max_sum}")
    print(f"  Subarray: {subarray} (indices {start} to {end})")
    print()

    # --- Kadane's Algorithm Explanation ---
    print("--- Kadane's Algorithm: Core Idea ---")
    print()
    print("  At each position i, make ONE decision:")
    print()
    print("    current_sum = max(nums[i], current_sum + nums[i])")
    print()
    print("    Option A: current_sum + nums[i]  → extend the subarray")
    print("    Option B: nums[i] alone          → start a NEW subarray")
    print()
    print("  Choose whichever is LARGER. If extending makes the sum")
    print("  worse than starting fresh, abandon the old subarray.")
    print()

    # --- Step-by-Step Walkthrough ---
    print("--- Step-by-Step Walkthrough ---")
    print()
    print(f"  Array: {nums}")
    print(f"  Index:  {list(range(len(nums)))}")
    print()

    current_sum = nums[0]
    max_sum_step = nums[0]

    print(f"  {'i':>3} | {'nums[i]':>7} | {'Extend':>10} | {'Fresh':>7} | {'Decision':>10} | {'cur_sum':>7} | {'max_sum':>7} | {'Subarray'}")
    print(f"  {'-'*3} | {'-'*7} | {'-'*10} | {'-'*7} | {'-'*10} | {'-'*7} | {'-'*7} | {'-'*15}")

    temp_start = 0
    start = 0
    end = 0

    print(f"  {0:>3} | {nums[0]:>7} | {'—':>10} | {'—':>7} | {'start':>10} | {current_sum:>7} | {max_sum_step:>7} | {nums[0:1]}")

    for i in range(1, len(nums)):
        extend = current_sum + nums[i]
        fresh = nums[i]

        if extend < fresh:
            decision = "★ FRESH"
            current_sum = fresh
            temp_start = i
        else:
            decision = "extend"
            current_sum = extend

        if current_sum > max_sum_step:
            max_sum_step = current_sum
            start = temp_start
            end = i

        subarray_str = str(nums[temp_start:i + 1])
        print(f"  {i:>3} | {nums[i]:>7} | {extend:>10} | {fresh:>7} | {decision:>10} | {current_sum:>7} | {max_sum_step:>7} | {subarray_str}")

    print()
    print(f"  Final answer: max_sum = {max_sum_step}")
    print(f"  Subarray: {nums[start:end+1]}")
    print()

    # --- Visual Subarray Highlight ---
    print("--- Visual: Highlighting the Maximum Subarray ---")
    print()
    nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]
    max_sum, start, end = max_subarray_kadane(nums)

    visual = "  "
    for i, n in enumerate(nums):
        if start <= i <= end:
            visual += f"[{n:>2}]"
        else:
            visual += f" {n:>2} "
    print(visual)

    marker = "  "
    for i in range(len(nums)):
        if i == start:
            marker += " ↑──"
        elif i == end:
            marker += "──↑ "
        elif start < i < end:
            marker += "────"
        else:
            marker += "    "
    print(marker)
    print(f"  {'':>{start*4+2}}Sum = {max_sum}")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([1, -2, 3, 4, -1, 2, 1, -5, 4], 9, "Given example"),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "LeetCode example"),
        ([1], 1, "Single element"),
        ([-1], -1, "Single negative"),
        ([-2, -1, -3], -1, "All negatives"),
        ([5, 4, -1, 7, 8], 23, "All positive-ish"),
        ([1, 2, 3, 4, 5], 15, "All positive"),
    ]

    print(f"  {'Input':>40}  | {'Expected':>8} | {'Got':>5} | {'Subarray':>20} | {'✓/✗':>3}")
    print(f"  {'-'*40}  | {'-'*8} | {'-'*5} | {'-'*20} | {'-'*3}")

    for nums, expected, desc in test_cases:
        max_s, s, e = max_subarray_kadane(nums)
        sub = nums[s:e+1]
        status = "✓" if max_s == expected else "✗"
        nums_str = str(nums) if len(str(nums)) <= 38 else str(nums)[:35] + "..."
        print(f"  {nums_str:>40}  | {expected:>8} | {max_s:>5} | {str(sub):>20} | {status:>3}")

    print()

    # --- Complexity ---
    print("--- Complexity Comparison ---")
    print()
    print("  Algorithm            | Time       | Space    | Notes")
    print("  ---------------------|------------|----------|-------------------")
    print("  Brute Force          | O(n²)      | O(1)     | Try all subarrays")
    print("  Divide & Conquer     | O(n log n) | O(log n) | Split & merge")
    print("  Kadane's Algorithm ★ | O(n)       | O(1)     | Single pass!")
    print()
    print("ANSWER:")
    print("  Kadane's Algorithm: O(n) time, O(1) space.")
    print("  For [1,-2,3,4,-1,2,1,-5,4]: max sum = 9, subarray = [3,4,-1,2,1]")


if __name__ == "__main__":
    demonstrate()
