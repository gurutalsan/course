"""
Q4. Find the longest consecutive sequence in an unsorted array.
    Example: [100,4,200,1,3,2] → 4 (the sequence 1,2,3,4). O(n) time.

Answer:
    Use a HASH SET for O(1) lookups.

    For each number, check if it's the START of a sequence
    (i.e., num-1 is NOT in the set). If it is, count how far
    the sequence extends (num+1, num+2, ...).

    Time:  O(n) — each number is visited at most twice.
    Space: O(n) — the hash set.
"""


def longest_consecutive(nums: list) -> int:
    """
    Find the length of the longest consecutive element sequence.

    Key insight: Only start counting from the BEGINNING of a sequence
    (where num-1 doesn't exist in the set). This ensures O(n).

    Time:  O(n) — despite nested loop, each element counted at most once.
    Space: O(n)
    """
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting if this is the BEGINNING of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length


def longest_consecutive_with_sequence(nums: list) -> tuple:
    """Same but also returns the actual sequence."""
    if not nums:
        return 0, []

    num_set = set(nums)
    max_length = 0
    best_start = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            if length > max_length:
                max_length = length
                best_start = num

    return max_length, list(range(best_start, best_start + max_length))


def demonstrate():
    print("=" * 70)
    print("Q4: Longest Consecutive Sequence — O(n)")
    print("=" * 70)
    print()

    nums = [100, 4, 200, 1, 3, 2]
    length, seq = longest_consecutive_with_sequence(nums)

    print(f"  Input:    {nums}")
    print(f"  Length:   {length}")
    print(f"  Sequence: {seq}")
    print()

    # --- Why O(n)? ---
    print("--- Why O(n) Despite the While Loop? ---")
    print()
    print("  Key trick: We ONLY start counting from sequence BEGINNINGS.")
    print("  A number is a 'start' if (num - 1) is NOT in the set.")
    print()
    print(f"  Set: {set(nums)}")
    print()

    num_set = set(nums)
    for num in sorted(num_set):
        is_start = (num - 1) not in num_set
        print(f"    {num}: (num-1)={num-1} in set? "
              f"{'Yes → skip' if not is_start else 'No → START counting!'}")

    print()
    print("  Only 100, 200, and 1 trigger counting.")
    print("  Numbers 2, 3, 4 are SKIPPED (they're not sequence starts).")
    print("  Each number is counted at most ONCE → O(n) total!")
    print()

    # --- Step-by-step ---
    print("--- Step-by-Step Trace ---")
    print()
    print(f"  num_set = {num_set}")
    print()

    for num in sorted(num_set):
        if num - 1 not in num_set:
            current = num
            length = 1
            seq_build = [num]
            while current + 1 in num_set:
                current += 1
                length += 1
                seq_build.append(current)
            print(f"  Start={num}: count {seq_build} → length={length}")

    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4, "1,2,3,4"),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9, "0-8"),
        ([1, 2, 0, 1], 3, "0,1,2 (with dup)"),
        ([], 0, "Empty"),
        ([1], 1, "Single element"),
        ([5, 5, 5, 5], 1, "All same"),
        ([10, 30, 20], 1, "No consecutive"),
        ([1, 3, 5, 2, 4], 5, "1-5"),
        ([-2, -1, 0, 1, 2], 5, "Negative numbers"),
    ]

    print(f"  {'Input':>35} | {'Expected':>8} | {'Got':>5} | {'Sequence':>15} | {'✓/✗':>3}")
    print(f"  {'-'*35} | {'-'*8} | {'-'*5} | {'-'*15} | {'-'*3}")

    for nums, expected, desc in test_cases:
        length, seq = longest_consecutive_with_sequence(nums)
        status = "✓" if length == expected else "✗"
        nums_str = str(nums) if len(str(nums)) <= 33 else str(nums)[:30] + "..."
        seq_str = str(seq) if len(str(seq)) <= 13 else str(seq)[:10] + "..."
        print(f"  {nums_str:>35} | {expected:>8} | {length:>5} | {seq_str:>15} | {status:>3}")

    print()

    # --- Complexity ---
    print("--- Why NOT Sorting? ---")
    print()
    print("  Sorting approach: O(n log n) — sort, then scan for consecutive")
    print("  Hash set approach: O(n) — no sorting needed!")
    print()
    print("  The set gives us O(1) lookup for 'is num+1 present?'")
    print("  Combined with the 'start-only' trick → O(n) total.")
    print()
    print("ANSWER: Use a hash set. Only count from sequence starts (num-1 not in set).")
    print("For [100,4,200,1,3,2]: longest = 4 (sequence 1,2,3,4). Time: O(n).")


if __name__ == "__main__":
    demonstrate()
