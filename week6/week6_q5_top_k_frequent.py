"""
Q5. Given an array of integers, return the top k most frequent elements
    using a bucket sort approach (not heap). Explain why this is O(n).

Answer:
    BUCKET SORT approach:
    1. Count frequencies with a hash map → O(n)
    2. Create buckets where index = frequency, value = list of elements → O(n)
    3. Iterate buckets from highest frequency → collect top k → O(n)

    Total: O(n) — no sorting or heap needed!

    Why O(n)? The max frequency is at most n, so bucket array has n+1 slots.
    Each step iterates at most n elements.
"""

from collections import Counter


def top_k_frequent_bucket(nums: list, k: int) -> list:
    """
    Find top k most frequent elements using bucket sort.

    Step 1: Count frequencies → O(n)
    Step 2: Bucket by frequency → O(n)
    Step 3: Collect from highest bucket → O(n)

    Time:  O(n) — three linear passes, no sorting!
    Space: O(n) — frequency map + bucket array.
    """
    # Step 1: Count frequencies
    freq = Counter(nums)

    # Step 2: Create frequency buckets
    # Index = frequency, Value = list of numbers with that frequency
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]

    for num, count in freq.items():
        buckets[count].append(num)

    # Step 3: Collect top k from highest frequency down
    result = []
    for i in range(n, 0, -1):  # Highest frequency first
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result

    return result


def top_k_frequent_heap(nums: list, k: int) -> list:
    """Comparison: Using heap — O(n log k)."""
    import heapq
    freq = Counter(nums)
    return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]


def demonstrate():
    print("=" * 70)
    print("Q5: Top K Frequent Elements — Bucket Sort (O(n))")
    print("=" * 70)
    print()

    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"  Input: nums = {nums}, k = {k}")
    result = top_k_frequent_bucket(nums, k)
    print(f"  Output: {result}")
    print()

    # --- Step-by-step ---
    print("--- Step-by-Step Walkthrough ---")
    print()
    print(f"  Input: {nums}")
    print()

    # Step 1
    freq = Counter(nums)
    print(f"  Step 1: Count frequencies")
    print(f"    Counter: {dict(freq)}")
    print()

    # Step 2
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    print(f"  Step 2: Create frequency buckets (index = frequency)")
    for i in range(n, -1, -1):
        if buckets[i]:
            print(f"    Frequency {i}: {buckets[i]}")

    print()

    # Step 3
    print(f"  Step 3: Collect top {k} from highest frequency")
    result = []
    for i in range(n, 0, -1):
        for num in buckets[i]:
            result.append(num)
            print(f"    Freq {i} → add {num}, collected: {result}")
            if len(result) == k:
                break
        if len(result) == k:
            break

    print()
    print(f"  Result: {result}")
    print()

    # --- Visual Bucket Diagram ---
    print("--- Visual: Frequency Buckets ---")
    print()
    nums2 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    freq2 = Counter(nums2)
    n2 = len(nums2)
    buckets2 = [[] for _ in range(n2 + 1)]
    for num, count in freq2.items():
        buckets2[count].append(num)

    print(f"  nums = {nums2}")
    print(f"  Frequencies: {dict(freq2)}")
    print()
    print("  Bucket Index (frequency) | Elements")
    print("  -------------------------|----------")
    for i in range(n2, -1, -1):
        bar = "█" * (len(buckets2[i]) * 5) if buckets2[i] else ""
        elements = str(buckets2[i]) if buckets2[i] else "—"
        if buckets2[i]:
            print(f"  Freq = {i:>2}                 | {elements:>10}  {bar}")

    print()
    print("  Top 2: Read from highest frequency → [3, 1]")
    print()

    # --- Why O(n) ---
    print("--- Why Is This O(n)? ---")
    print()
    print("  Step 1: Counter(nums) → O(n)")
    print("    One pass through the array to count.")
    print()
    print("  Step 2: Fill buckets → O(unique_elements) ≤ O(n)")
    print("    One pass through the frequency map.")
    print()
    print("  Step 3: Collect top k → O(n)")
    print("    Iterate buckets (at most n+1 slots).")
    print("    Collect at most k elements.")
    print()
    print("  Total: O(n) + O(n) + O(n) = O(n) ✓")
    print()
    print("  Key insight: Max frequency ≤ n, so bucket array is O(n) sized.")
    print("  No sorting needed! This is essentially a COUNTING SORT by frequency.")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([1, 2], 2, {1, 2}),
        ([4, 1, -1, 2, -1, 2, 3], 2, {-1, 2}),
        ([3, 3, 3, 3, 3], 1, {3}),
        ([1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1], 3, {1, 2, 3}),
    ]

    print(f"  {'Input':>35} | {'k':>2} | {'Expected':>12} | {'Got':>12} | {'✓/✗':>3}")
    print(f"  {'-'*35} | {'-'*2} | {'-'*12} | {'-'*12} | {'-'*3}")

    for nums, k, expected_set in test_cases:
        got = top_k_frequent_bucket(nums, k)
        status = "✓" if set(got) == expected_set else "✗"
        nums_str = str(nums) if len(str(nums)) <= 33 else str(nums)[:30] + "..."
        print(f"  {nums_str:>35} | {k:>2} | {str(expected_set):>12} | {str(set(got)):>12} | {status:>3}")

    print()

    # --- Comparison ---
    print("--- Method Comparison ---")
    print()
    print("  Method             | Time       | Space | Notes")
    print("  -------------------|------------|-------|------------------")
    print("  Sort by freq       | O(n log n) | O(n)  | Sort all frequencies")
    print("  Min-heap of size k | O(n log k) | O(n)  | Maintain k-size heap")
    print("  Bucket sort ★      | O(n)       | O(n)  | No sorting at all!")
    print()
    print("ANSWER: Bucket sort is O(n) because max frequency ≤ n.")
    print("Count → bucket by frequency → collect from highest. No sorting needed.")


if __name__ == "__main__":
    demonstrate()
