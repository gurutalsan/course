"""
Q6. Write a function that finds all pairs in an array that sum to a given
    target. Handle duplicate pairs. Return unique pairs only.

Answer:
    Use a HASH SET to find complements in O(1).
    Use a second set to track pairs we've already returned → unique only.

    Time:  O(n) — single pass with O(1) lookups.
    Space: O(n) — sets for seen numbers and result pairs.
"""


def find_pairs(nums: list, target: int) -> list:
    """
    Find all UNIQUE pairs that sum to target.

    Uses a 'seen' set for O(1) complement lookup and a 'used' set
    to prevent duplicate pairs.

    Time:  O(n)
    Space: O(n)
    """
    seen = set()       # Numbers we've encountered
    result_set = set() # Pairs found (stored as sorted tuples for uniqueness)

    for num in nums:
        complement = target - num

        if complement in seen:
            # Store as sorted tuple to avoid (a,b) and (b,a) duplicates
            pair = tuple(sorted((num, complement)))
            result_set.add(pair)

        seen.add(num)

    return [list(pair) for pair in sorted(result_set)]


def find_pairs_with_indices(nums: list, target: int) -> list:
    """Find pairs with their indices (all occurrences, not just unique values)."""
    seen = {}  # num → list of indices
    pairs = []
    used = set()

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            for j in seen[complement]:
                pair_key = tuple(sorted((num, complement)))
                if pair_key not in used:
                    pairs.append((j, i, nums[j], nums[i]))
                    used.add(pair_key)

        seen.setdefault(num, []).append(i)

    return pairs


def find_pairs_brute(nums: list, target: int) -> list:
    """Brute force O(n²) for comparison."""
    result_set = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = tuple(sorted((nums[i], nums[j])))
                result_set.add(pair)
    return [list(p) for p in sorted(result_set)]


def demonstrate():
    print("=" * 70)
    print("Q6: Find All Pairs That Sum to Target (Unique Only)")
    print("=" * 70)
    print()

    nums = [1, 5, 7, -1, 5, 3, 4, 2, 6]
    target = 6
    print(f"  Array:  {nums}")
    print(f"  Target: {target}")
    print()

    result = find_pairs(nums, target)
    print(f"  Unique pairs: {result}")
    print()

    # --- Walkthrough ---
    print("--- Step-by-Step Walkthrough ---")
    print()

    seen = set()
    result_set = set()

    print(f"  {'i':>2} | {'num':>4} | {'comp':>5} | {'In seen?':>8} | {'seen set':>25} | {'Pairs found'}")
    print(f"  {'-'*2} | {'-'*4} | {'-'*5} | {'-'*8} | {'-'*25} | {'-'*20}")

    for i, num in enumerate(nums):
        comp = target - num
        found = comp in seen

        if found:
            pair = tuple(sorted((num, comp)))
            result_set.add(pair)

        seen.add(num)

        found_str = f"Yes→{[num,comp]}" if found else "No"
        print(f"  {i:>2} | {num:>4} | {comp:>5} | {found_str:>8} | {str(sorted(seen)):>25} | {sorted(result_set)}")

    print()
    print(f"  Result: {[list(p) for p in sorted(result_set)]}")
    print()

    # --- Handling Duplicates ---
    print("--- Handling Duplicates ---")
    print()
    print("  Input: [1, 5, 5, 5], target=6")
    print()

    test_nums = [1, 5, 5, 5]
    r = find_pairs(test_nums, 6)
    print(f"  Result: {r}")
    print("  Only ONE [1, 5] pair — duplicates handled by set!")
    print()

    print("  Input: [3, 3, 3], target=6")
    r2 = find_pairs([3, 3, 3], 6)
    print(f"  Result: {r2}")
    print("  Only ONE [3, 3] pair — even though multiple 3s exist.")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([1, 5, 7, -1, 5, 3, 4, 2, 6], 6, [[- 1, 7], [1, 5], [2, 4]]),
        ([1, 2, 3, 4, 5], 6, [[1, 5], [2, 4]]),
        ([3, 3, 3], 6, [[3, 3]]),
        ([1, 5, 5, 5], 6, [[1, 5]]),
        ([], 5, []),
        ([5], 5, []),
        ([0, 0, 0, 0], 0, [[0, 0]]),
        ([-2, -1, 0, 1, 2, 3], 1, [[-2, 3], [-1, 2], [0, 1]]),
    ]

    all_pass = True
    for nums, target, expected in test_cases:
        got = find_pairs(nums, target)
        brute = find_pairs_brute(nums, target)
        status = "✓" if got == expected and got == brute else "✗"
        if got != expected: all_pass = False
        print(f"  nums={nums}, target={target}")
        print(f"    → {got}  {status}")

    print(f"\n  All passed: {'✓' if all_pass else '✗'}")
    print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Method      | Time | Space | Handles Duplicates?")
    print("  ------------|------|-------|--------------------")
    print("  Brute force | O(n²)| O(n)  | With set")
    print("  Hash set ★  | O(n) | O(n)  | With sorted tuple set")
    print("  Sort+2ptr   | O(nlogn)| O(n) | With skip logic")
    print()
    print("ANSWER: Hash set for O(1) complement lookup. Store found pairs as")
    print("sorted tuples in a set to ensure uniqueness. O(n) time.")


if __name__ == "__main__":
    demonstrate()
