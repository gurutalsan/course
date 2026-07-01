"""
Q1. Implement the Two Sum problem: Given nums=[2,7,11,15] and target=9,
    return indices of two numbers that add up to target.
    What is your solution's time and space complexity?

Answer:
    Optimal approach: Use a HASH MAP (dictionary) to store complements.

    Time Complexity:  O(n) — single pass through the array.
    Space Complexity: O(n) — hash map stores up to n elements.

    How it works:
    For each number, calculate complement = target - num.
    Check if complement is already in the hash map.
    If yes → found the pair! Return both indices.
    If no  → store current num and its index in the map.
"""


# ============================================================
# Method 1: Brute Force — O(n²)
# ============================================================
def two_sum_brute(nums: list, target: int) -> list:
    """
    Brute force: check every pair.

    Time:  O(n²) — nested loops.
    Space: O(1)  — no extra data structures.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# ============================================================
# Method 2: Hash Map (Optimal) ★ RECOMMENDED ★
# ============================================================
def two_sum(nums: list, target: int) -> list:
    """
    Optimal: Use a hash map to find complements in O(1).

    Time:  O(n) — single pass through the array.
    Space: O(n) — hash map stores visited numbers.

    Algorithm:
        For each num at index i:
            complement = target - num
            If complement is in hash_map → return [hash_map[complement], i]
            Else → store num: i in hash_map
    """
    hash_map = {}  # value → index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hash_map:
            return [hash_map[complement], i]

        hash_map[num] = i

    return []  # No solution found


# ============================================================
# Method 3: Two Pointer (only works on SORTED arrays)
# ============================================================
def two_sum_sorted(nums: list, target: int) -> list:
    """
    Two-pointer approach for SORTED arrays.
    Returns indices in the original (sorted) array.

    Time:  O(n log n) if sorting needed, O(n) if pre-sorted.
    Space: O(n) — for storing original indices.
    """
    indexed = sorted(enumerate(nums), key=lambda x: x[1])
    left, right = 0, len(indexed) - 1

    while left < right:
        current_sum = indexed[left][1] + indexed[right][1]
        if current_sum == target:
            return sorted([indexed[left][0], indexed[right][0]])
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


def demonstrate():
    print("=" * 70)
    print("Q1: Two Sum Problem")
    print("=" * 70)
    print()

    # --- Problem Statement ---
    print("--- Problem ---")
    print()
    print("  Given: nums = [2, 7, 11, 15], target = 9")
    print("  Find:  Two indices whose values add up to target")
    print("  Answer: [0, 1]  because nums[0] + nums[1] = 2 + 7 = 9")
    print()

    # --- Hash Map Algorithm Walkthrough ---
    print("--- Hash Map Algorithm (Step-by-Step) ---")
    print()
    nums = [2, 7, 11, 15]
    target = 9

    print(f"  nums = {nums}, target = {target}")
    print()

    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        found = complement in hash_map

        print(f"  Step {i+1}: num={num}, complement={target}-{num}={complement}")
        print(f"    hash_map = {hash_map}")
        print(f"    Is {complement} in hash_map? {'✓ YES!' if found else '✗ No'}")

        if found:
            result = [hash_map[complement], i]
            print(f"    → FOUND! Return [{hash_map[complement]}, {i}]")
            print(f"    → nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {target}")
            break
        else:
            hash_map[num] = i
            print(f"    → Store {{{num}: {i}}} in hash_map")

        print()

    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([2, 7, 11, 15], 9, "Basic example"),
        ([3, 2, 4], 6, "Non-adjacent pair"),
        ([3, 3], 6, "Duplicate values"),
        ([1, 5, 3, 7, 8, 2], 10, "Multiple possibilities"),
        ([-1, -2, -3, -4, -5], -8, "Negative numbers"),
        ([0, 4, 3, 0], 0, "Zero sum"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 17, "Larger array"),
    ]

    print(f"  {'nums':>30}  | {'target':>6} | {'Indices':>9} | {'Values':>12} | {'Check':>8}")
    print(f"  {'-'*30}  | {'-'*6} | {'-'*9} | {'-'*12} | {'-'*8}")

    for nums, target, desc in test_cases:
        result = two_sum(nums, target)
        if result:
            values = f"{nums[result[0]]}+{nums[result[1]]}={nums[result[0]]+nums[result[1]]}"
            check = "✓" if nums[result[0]] + nums[result[1]] == target else "✗"
        else:
            values = "N/A"
            check = "—"

        nums_str = str(nums) if len(str(nums)) <= 28 else str(nums)[:25] + "..."
        print(f"  {nums_str:>30}  | {target:>6} | {str(result):>9} | {values:>12} | {check:>8}")

    print()

    # --- Complexity Comparison ---
    print("--- Method Comparison ---")
    print()
    print("  Method        | Time       | Space | How It Works")
    print("  --------------|------------|-------|---------------------------------")
    print("  Brute Force   | O(n²)      | O(1)  | Check every pair")
    print("  Hash Map ★    | O(n)       | O(n)  | Store complements in dict")
    print("  Two Pointer   | O(n log n) | O(n)  | Sort first, then converge")
    print()

    # --- Performance Benchmark ---
    import time
    import random

    print("--- Performance Benchmark ---")
    print()
    print(f"  {'n':>8}  |  {'Brute O(n²)':>14}  |  {'HashMap O(n)':>14}  |  {'Speedup':>8}")
    print(f"  {'-'*8}  |  {'-'*14}  |  {'-'*14}  |  {'-'*8}")

    for n in [100, 1_000, 5_000, 10_000, 50_000]:
        nums = random.sample(range(n * 10), n)
        target = nums[-1] + nums[-2]  # Guarantee a solution at the end

        if n <= 10_000:
            start = time.perf_counter()
            _ = two_sum_brute(nums, target)
            brute_time = (time.perf_counter() - start) * 1000
            brute_str = f"{brute_time:>11.3f} ms"
        else:
            brute_str = "    (skipped)"

        start = time.perf_counter()
        _ = two_sum(nums, target)
        hash_time = (time.perf_counter() - start) * 1000

        speedup = brute_time / hash_time if n <= 10_000 and hash_time > 0 else 0
        speedup_str = f"{speedup:>7.0f}x" if speedup > 0 else "     N/A"

        print(f"  {n:>8,}  |  {brute_str:>14}  |  {hash_time:>11.3f} ms  |  {speedup_str:>8}")

    print()
    print("ANSWER:")
    print("  Use a hash map for O(n) time, O(n) space.")
    print("  For each number, check if (target - num) was already seen.")


if __name__ == "__main__":
    demonstrate()
