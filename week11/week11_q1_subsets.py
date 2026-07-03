"""
Q1. Generate all subsets of [1,2,3]. Draw recursion tree.
    How many subsets does a set of n elements have?

Answer:
    A set of n elements has 2^n subsets (each element: include or exclude).
    [1,2,3] → 2³ = 8 subsets.

    Approach: For each element, make two choices — INCLUDE or EXCLUDE.
    This creates a binary recursion tree of depth n.

    Time: O(n × 2^n) — 2^n subsets, each up to n elements to copy.
    Space: O(n) recursion depth.
"""


def subsets(nums):
    """Generate all subsets using include/exclude backtracking."""
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])  # Copy current subset
            return

        # Choice 1: EXCLUDE nums[index]
        backtrack(index + 1, current)

        # Choice 2: INCLUDE nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()  # Backtrack!

    backtrack(0, [])
    return result


def subsets_iterative(nums):
    """Build subsets iteratively: start with [[]], add each num to all existing."""
    result = [[]]
    for num in nums:
        result += [subset + [num] for subset in result]
    return result


def demonstrate():
    print("=" * 70)
    print("Q1: All Subsets (Power Set)")
    print("=" * 70)
    print()

    nums = [1, 2, 3]
    result = subsets(nums)
    print(f"  Input: {nums}")
    print(f"  Subsets ({len(result)} total): {result}")
    print(f"  2^{len(nums)} = {2**len(nums)} ✓")
    print()

    # --- Recursion Tree ---
    print("--- Complete Recursion Tree ---")
    print()
    print("  Each level: decide to INCLUDE or EXCLUDE that element")
    print()
    print("                            []")
    print("                    /                \\")
    print("               exclude 1          include 1")
    print("                  []                 [1]")
    print("              /       \\          /        \\")
    print("          excl 2    incl 2   excl 2    incl 2")
    print("           []        [2]      [1]       [1,2]")
    print("          / \\       / \\      / \\       / \\")
    print("        e3  i3   e3  i3   e3  i3    e3  i3")
    print("        []  [3] [2] [2,3] [1] [1,3] [1,2] [1,2,3]")
    print()
    print("  Leaf nodes (depth = n) = all 8 subsets ✓")
    print()

    # --- Traced execution ---
    print("--- Traced Execution ---")
    print()
    trace_result = []

    def backtrack_trace(index, current, depth=0):
        indent = "    " * depth
        if index == len(nums):
            trace_result.append(current[:])
            print(f"  {indent}→ LEAF: add {current}")
            return

        print(f"  {indent}index={index} (element {nums[index]})")
        print(f"  {indent}  Skip {nums[index]}:")
        backtrack_trace(index + 1, current, depth + 1)

        current.append(nums[index])
        print(f"  {indent}  Take {nums[index]}: current={current}")
        backtrack_trace(index + 1, current, depth + 1)
        current.pop()

    backtrack_trace(0, [])
    print()

    # --- Iterative approach ---
    print("--- Iterative Build ---")
    print()
    result_iter = [[]]
    print(f"  Start: {result_iter}")
    for num in nums:
        new = [s + [num] for s in result_iter]
        result_iter += new
        print(f"  Add {num}: {result_iter}")
    print()

    # Formula
    print("--- Formula ---")
    print()
    print("  A set of n elements has 2^n subsets.")
    print("  Why? Each element has 2 choices: IN or OUT.")
    print("  n elements → 2 × 2 × ... × 2 (n times) = 2^n")
    print()
    print("  | n | Subsets |")
    print("  |---|--------|")
    for n in range(6):
        print(f"  | {n} | {2**n:>6} |")

    print()
    print(f"  Time: O(n × 2^n) | Space: O(n) recursion depth")


if __name__ == "__main__":
    demonstrate()
