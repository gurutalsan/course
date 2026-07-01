"""
Q3. Given a sorted array of 1 million elements, how many steps (maximum)
    does binary search need? Show your calculation.

Answer: 20 steps (maximum)

Calculation:
    Binary search halves the search space with each step.
    Maximum steps = ⌊log₂(n)⌋ + 1

    For n = 1,000,000:
        log₂(1,000,000) = ln(1,000,000) / ln(2)
                         = 13.8155... / 0.6931...
                         = 19.9316...

        ⌊19.9316⌋ + 1 = 19 + 1 = 20

    Maximum steps = 20

    Verification: 2^19 = 524,288 < 1,000,000 < 1,048,576 = 2^20
"""

import math


def binary_search(arr, target):
    """
    Standard binary search implementation.
    Returns (index, steps_taken) or (-1, steps_taken) if not found.
    """
    left, right = 0, len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, steps  # Not found


def show_binary_search_steps():
    """Show the halving process step by step."""
    print("=" * 60)
    print("Q3: Binary Search Steps for 1,000,000 Elements")
    print("=" * 60)
    print()

    n = 1_000_000

    # --- Mathematical Calculation ---
    print("--- Mathematical Calculation ---")
    print()
    print(f"  n = {n:,}")
    print(f"  log₂({n:,}) = {math.log2(n):.4f}")
    print(f"  ⌊log₂({n:,})⌋ + 1 = {int(math.log2(n))} + 1 = {int(math.log2(n)) + 1}")
    print()
    print(f"  Maximum steps = {int(math.log2(n)) + 1}")
    print()

    # --- Step-by-step halving ---
    print("--- Step-by-Step Halving of Search Space ---")
    print()
    print(f"  {'Step':>4}  |  {'Search Space Size':>20}  |  {'Remaining':>15}")
    print(f"  {'-'*4}  |  {'-'*20}  |  {'-'*15}")

    remaining = n
    step = 0
    while remaining > 0:
        step += 1
        print(f"  {step:>4}  |  {remaining:>20,}  |  ", end="")
        remaining = remaining // 2
        if remaining > 0:
            print(f"{remaining:>15,}")
        else:
            print(f"{'Found or exhausted':>15}")

    print()
    print(f"  Total steps to exhaust search space: {step}")
    print()

    # --- Practical Demonstration ---
    print("--- Practical Demonstration ---")
    print()

    # Create sorted array of 1 million elements
    arr = list(range(1, n + 1))  # [1, 2, 3, ..., 1,000,000]

    # Test: search for an element that requires maximum steps
    # Worst case is typically a missing element or element at the boundary
    test_cases = [
        (1, "First element"),
        (500_000, "Middle element"),
        (1_000_000, "Last element"),
        (999_999, "Near-last element"),
        (1_000_001, "Non-existent (beyond range)"),
    ]

    print(f"  {'Target':>12}  |  {'Description':>22}  |  {'Found?':>7}  |  {'Steps':>5}")
    print(f"  {'-'*12}  |  {'-'*22}  |  {'-'*7}  |  {'-'*5}")

    max_steps = 0
    for target, desc in test_cases:
        idx, steps = binary_search(arr, target)
        found = "Yes" if idx != -1 else "No"
        max_steps = max(max_steps, steps)
        print(f"  {target:>12,}  |  {desc:>22}  |  {found:>7}  |  {steps:>5}")

    print()
    print(f"  Maximum steps observed: {max_steps}")
    print()

    # --- Verification ---
    print("--- Verification ---")
    print()
    print(f"  2^19 = {2**19:>12,}  <  1,000,000")
    print(f"  2^20 = {2**20:>12,}  >= 1,000,000")
    print()
    print("  Since 2^19 < 1,000,000 ≤ 2^20, we need at most 20 comparisons.")
    print()

    # --- Comparison table for different sizes ---
    print("--- Binary Search: Steps for Various Array Sizes ---")
    print()
    print(f"  {'Array Size':>15}  |  {'Max Steps (⌊log₂n⌋+1)':>22}")
    print(f"  {'-'*15}  |  {'-'*22}")

    for size in [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 1_000_000_000]:
        steps = int(math.log2(size)) + 1 if size > 0 else 0
        print(f"  {size:>15,}  |  {steps:>22}")

    print()
    print("ANSWER: Binary search needs at most 20 steps for 1,000,000 elements.")


if __name__ == "__main__":
    show_binary_search_steps()
