"""
Q5. Longest Increasing Subsequence (LIS) of [10,9,2,5,3,7,101,18].
    Show DP array at each step. Time complexity?

Answer:
    dp[i] = length of LIS ending at index i.
    For each i, check all j < i: if nums[j] < nums[i], dp[i] = max(dp[i], dp[j]+1).

    O(n²) DP approach. O(n log n) with patience sorting (binary search).
"""

import bisect


def lis_dp(nums):
    """
    LIS using O(n²) DP.
    dp[i] = length of longest increasing subsequence ending at nums[i].
    """
    if not nums:
        return 0, []

    n = len(nums)
    dp = [1] * n
    parent = [-1] * n  # For reconstruction

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    # Find max and reconstruct
    max_len = max(dp)
    idx = dp.index(max_len)

    # Reconstruct
    lis = []
    while idx != -1:
        lis.append(nums[idx])
        idx = parent[idx]
    lis.reverse()

    return max_len, lis, dp


def lis_binary_search(nums):
    """LIS using O(n log n) patience sorting with binary search."""
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)


def demonstrate():
    print("=" * 70)
    print("Q5: Longest Increasing Subsequence (LIS)")
    print("=" * 70)
    print()

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    max_len, lis, dp = lis_dp(nums)

    print(f"  Input: {nums}")
    print(f"  LIS length: {max_len}")
    print(f"  One LIS: {lis}")
    print()

    # --- DP Array at Each Step ---
    print("--- DP Array at Each Step ---")
    print()
    print(f"  {'i':>3} | {'nums[i]':>7} | {'Check j<i':>30} | {'dp':>25}")
    print(f"  {'-'*3} | {'-'*7} | {'-'*30} | {'-'*25}")

    n = len(nums)
    dp_trace = [1] * n

    for i in range(n):
        updates = []
        for j in range(i):
            if nums[j] < nums[i]:
                if dp_trace[j] + 1 > dp_trace[i]:
                    dp_trace[i] = dp_trace[j] + 1
                    updates.append(f"{nums[j]}<{nums[i]}→dp[{j}]+1={dp_trace[i]}")

        upd_str = "; ".join(updates) if updates else "no update"
        print(f"  {i:>3} | {nums[i]:>7} | {upd_str:>30} | {dp_trace[:i+1]}")

    print()
    print(f"  Final dp: {dp_trace}")
    print(f"  Max = {max(dp_trace)} at index {dp_trace.index(max(dp_trace))}")
    print()

    # --- Reconstruction ---
    print("--- Reconstructing the LIS ---")
    print()
    print(f"  dp =   {dp_trace}")
    print(f"  nums = {nums}")
    print(f"  Max dp = {max_len} at index {dp_trace.index(max_len)}")
    print(f"  Backtrack: 101(dp=4) ← 7(dp=3) ← 5(dp=2) ← 2(dp=1)")
    print(f"  LIS = {lis}")
    print()

    # --- O(n log n) approach ---
    print("--- O(n log n) Approach: Patience Sorting ---")
    print()
    print("  Maintain 'tails' array: tails[i] = smallest tail of IS of length i+1")
    print()
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
            action = f"append {num}"
        else:
            old = tails[pos]
            tails[pos] = num
            action = f"replace tails[{pos}]={old} with {num}"
        print(f"  num={num:>4}: {action:>30} → tails={tails}")

    print(f"\n  LIS length = len(tails) = {len(tails)}")
    print()

    # --- Test cases ---
    print("--- Test Cases ---\n")
    tests = [
        ([10,9,2,5,3,7,101,18], 4),
        ([0,1,0,3,2,3], 4),
        ([7,7,7,7,7], 1),
        ([1,2,3,4,5], 5),
        ([5,4,3,2,1], 1),
    ]
    for nums, expected in tests:
        got_dp, _, _ = lis_dp(nums)
        got_bs = lis_binary_search(nums)
        print(f"  {str(nums):>25} → dp={got_dp}, bs={got_bs} (exp {expected}) {'✓' if got_dp==got_bs==expected else '✗'}")

    print()
    print("  O(n²) DP approach | O(n log n) binary search approach")


if __name__ == "__main__":
    demonstrate()
