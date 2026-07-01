"""
Q6. Implement a function that rotates an array by k positions to the right.
    Example: [1,2,3,4,5] rotated by 2 → [4,5,1,2,3].
    Can you do it in O(1) extra space?

Answer:
    Yes! The THREE REVERSALS method does it in O(1) extra space.

    Algorithm:
    1. Reverse the entire array.
    2. Reverse the first k elements.
    3. Reverse the remaining n-k elements.

    Example: [1,2,3,4,5], k=2
        Step 1 — Reverse all:     [5,4,3,2,1]
        Step 2 — Reverse [0:k]:   [4,5,3,2,1]
        Step 3 — Reverse [k:n]:   [4,5,1,2,3] ✓

    Time Complexity:  O(n)
    Space Complexity: O(1) — in-place swaps only!
"""


# ============================================================
# Method 1: Slicing (Pythonic but O(n) space)
# ============================================================
def rotate_slice(nums: list, k: int) -> list:
    """
    Rotate using Python slicing — simple but uses O(n) extra space.

    Time:  O(n)
    Space: O(n) — creates new list
    """
    n = len(nums)
    k = k % n  # Handle k > n
    return nums[-k:] + nums[:-k]


# ============================================================
# Method 2: Extra Array (straightforward but O(n) space)
# ============================================================
def rotate_extra_array(nums: list, k: int) -> list:
    """
    Rotate by placing each element at its new position in a new array.

    Time:  O(n)
    Space: O(n) — extra array
    """
    n = len(nums)
    k = k % n
    result = [0] * n

    for i in range(n):
        result[(i + k) % n] = nums[i]

    return result


# ============================================================
# Method 3: Three Reversals (Optimal — O(1) space) ★ BEST ★
# ============================================================
def rotate_reverse(nums: list, k: int) -> None:
    """
    Rotate in-place using the three reversals technique.

    Steps:
    1. Reverse entire array.
    2. Reverse first k elements.
    3. Reverse remaining n-k elements.

    Time:  O(n) — three O(n) passes.
    Space: O(1) — in-place swaps only!

    Modifies the array in-place.
    """
    n = len(nums)
    k = k % n  # Handle k > n

    if k == 0:
        return

    def reverse(arr, start, end):
        """Reverse arr[start:end+1] in-place."""
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Step 1: Reverse entire array
    reverse(nums, 0, n - 1)
    # Step 2: Reverse first k elements
    reverse(nums, 0, k - 1)
    # Step 3: Reverse remaining elements
    reverse(nums, k, n - 1)


# ============================================================
# Method 4: Cyclic Replacements (O(1) space, single pass)
# ============================================================
def rotate_cyclic(nums: list, k: int) -> None:
    """
    Rotate using cyclic replacements.
    Place each element directly at its final position.

    Time:  O(n) — each element moved exactly once.
    Space: O(1)
    """
    from math import gcd

    n = len(nums)
    k = k % n

    if k == 0:
        return

    count = 0  # Number of elements placed correctly

    for start in range(gcd(n, k)):
        current = start
        prev = nums[start]

        while True:
            next_pos = (current + k) % n
            nums[next_pos], prev = prev, nums[next_pos]
            current = next_pos
            count += 1

            if current == start:
                break

        if count >= n:
            break


def demonstrate():
    print("=" * 70)
    print("Q6: Rotate Array by K Positions")
    print("=" * 70)
    print()

    # --- Problem ---
    print("--- Problem ---")
    print()
    print("  Input:  [1, 2, 3, 4, 5], k = 2")
    print("  Output: [4, 5, 1, 2, 3]")
    print()
    print("  Each element moves k positions to the RIGHT.")
    print("  Elements at the end wrap around to the beginning.")
    print()

    # --- Visual: What rotation looks like ---
    print("--- Visual: Step-by-Step Rotation ---")
    print()
    arr = [1, 2, 3, 4, 5]
    print(f"  Original:     {arr}")
    print(f"  Rotate by 1:  {rotate_slice(arr, 1)}  (5 wraps to front)")
    print(f"  Rotate by 2:  {rotate_slice(arr, 2)}  (4,5 wrap to front)")
    print(f"  Rotate by 3:  {rotate_slice(arr, 3)}")
    print(f"  Rotate by 4:  {rotate_slice(arr, 4)}")
    print(f"  Rotate by 5:  {rotate_slice(arr, 5)}  (full rotation = original)")
    print()

    # --- Three Reversals Walkthrough ---
    print("--- Three Reversals Method (O(1) Space) ---")
    print()
    print("  The KEY insight: Rotation = Three Reversals!")
    print()

    arr = [1, 2, 3, 4, 5]
    k = 2
    print(f"  Input: {arr}, k = {k}")
    print()

    # Step 1
    step1 = arr[::-1]
    print(f"  Step 1: Reverse ALL      → {step1}")

    # Step 2
    step2 = step1.copy()
    step2[:k] = step2[:k][::-1]
    print(f"  Step 2: Reverse [0:{k}]    → {step2}")

    # Step 3
    step3 = step2.copy()
    step3[k:] = step3[k:][::-1]
    print(f"  Step 3: Reverse [{k}:{len(arr)}]    → {step3}  ✓")
    print()

    # --- Why it works ---
    print("--- Why Three Reversals Works ---")
    print()
    print("  Original:        [1  2  3 | 4  5]   (split at n-k=3)")
    print("                    ←part1→   ←p2→")
    print()
    print("  We want:         [4  5 | 1  2  3]   (swap the two parts)")
    print()
    print("  Reverse all:     [5  4  3  2  1]")
    print("  Reverse [0:2]:   [4  5  3  2  1]     ← part2 is correct!")
    print("  Reverse [2:5]:   [4  5  1  2  3]     ← part1 is correct! ✓")
    print()
    print("  It's like: reverse(reverse(A) + reverse(B)) = B + A")
    print()

    # --- Detailed step-by-step with another example ---
    print("--- Another Example: [1,2,3,4,5,6,7], k=3 ---")
    print()

    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    print(f"  Original: {arr}")
    arr_demo = arr.copy()

    # Reverse all
    arr_demo.reverse()
    print(f"  Reverse all:     {arr_demo}")

    # Reverse first k
    arr_demo[:k] = arr_demo[:k][::-1]
    print(f"  Reverse [0:{k}]:   {arr_demo}")

    # Reverse rest
    arr_demo[k:] = arr_demo[k:][::-1]
    print(f"  Reverse [{k}:{len(arr)}]:   {arr_demo}")

    # Verify
    expected = rotate_slice(arr, k)
    print(f"  Expected:        {expected}")
    print(f"  Match: {'✓' if arr_demo == expected else '✗'}")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([1, 2, 3, 4, 5], 2, "Basic"),
        ([1, 2, 3, 4, 5, 6, 7], 3, "7 elements"),
        ([1, 2], 1, "Two elements"),
        ([1], 0, "Single element"),
        ([1, 2, 3], 0, "k=0 (no rotation)"),
        ([1, 2, 3], 3, "k=n (full rotation)"),
        ([1, 2, 3], 5, "k > n"),
        ([-1, -100, 3, 99], 2, "Negative numbers"),
    ]

    print(f"  {'Input':>25}  | {'k':>2} | {'Expected':>25} | {'Reverse':>25} | {'✓/✗':>3}")
    print(f"  {'-'*25}  | {'-'*2} | {'-'*25} | {'-'*25} | {'-'*3}")

    for arr, k, desc in test_cases:
        expected = rotate_slice(arr, k)
        arr_test = arr.copy()
        rotate_reverse(arr_test, k)
        status = "✓" if arr_test == expected else "✗"

        print(f"  {str(arr):>25}  | {k:>2} | {str(expected):>25} | {str(arr_test):>25} | {status:>3}")

    print()

    # --- Method Comparison ---
    print("--- Method Comparison ---")
    print()
    print("  Method              | Time  | Space | In-Place? | Notes")
    print("  --------------------|-------|-------|-----------|---------------------")
    print("  Slicing             | O(n)  | O(n)  | No        | Pythonic, simple")
    print("  Extra Array         | O(n)  | O(n)  | No        | Straightforward")
    print("  Three Reversals ★   | O(n)  | O(1)  | Yes       | Optimal space!")
    print("  Cyclic Replacement  | O(n)  | O(1)  | Yes       | Complex but elegant")
    print()

    # --- Performance ---
    import time
    import random

    print("--- Performance Benchmark ---")
    print()

    sizes = [1_000, 10_000, 100_000, 1_000_000]

    print(f"  {'n':>10}  |  {'Slice O(n)sp':>14}  |  {'Reverse O(1)sp':>16}  |  {'Speedup':>8}")
    print(f"  {'-'*10}  |  {'-'*14}  |  {'-'*16}  |  {'-'*8}")

    for n in sizes:
        arr = list(range(n))
        k = n // 3

        # Slice
        start = time.perf_counter()
        _ = rotate_slice(arr, k)
        slice_time = (time.perf_counter() - start) * 1000

        # Reverse in-place
        arr_test = arr.copy()
        start = time.perf_counter()
        rotate_reverse(arr_test, k)
        reverse_time = (time.perf_counter() - start) * 1000

        speedup = slice_time / reverse_time if reverse_time > 0 else 0

        print(
            f"  {n:>10,}  |  "
            f"{slice_time:>11.3f} ms  |  "
            f"{reverse_time:>13.3f} ms  |  "
            f"{speedup:>7.1f}x"
        )

    print()
    print("ANSWER:")
    print("  Yes, O(1) extra space is achievable using the THREE REVERSALS method.")
    print("  1. Reverse entire array  2. Reverse first k  3. Reverse rest")
    print("  Time: O(n), Space: O(1)")


if __name__ == "__main__":
    demonstrate()
