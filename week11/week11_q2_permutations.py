"""
Q2. Generate all permutations of [1,2,3]. How many? Time complexity?

Answer:
    n elements → n! permutations.  3! = 6.
    At each position, choose from remaining unused elements.

    Time:  O(n × n!) — n! permutations, each takes O(n) to copy.
    Space: O(n) recursion depth + O(n) for used tracking.
"""


def permutations(nums):
    """Generate all permutations using backtracking."""
    result = []

    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return

        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()  # Backtrack!

    backtrack([], nums)
    return result


def permutations_swap(nums):
    """In-place permutations using swaps."""
    result = []
    nums = nums[:]

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Swap back

    backtrack(0)
    return result


def demonstrate():
    print("=" * 70)
    print("Q2: All Permutations")
    print("=" * 70)
    print()

    nums = [1, 2, 3]
    result = permutations(nums)
    print(f"  Input: {nums}")
    print(f"  Permutations ({len(result)} total):")
    for p in result:
        print(f"    {p}")
    print(f"  3! = {3*2*1} ✓")
    print()

    # --- Recursion Tree ---
    print("--- Recursion Tree ---")
    print()
    print("  Level 0: Choose 1st element from {1,2,3}")
    print("  Level 1: Choose 2nd from remaining")
    print("  Level 2: Choose 3rd from remaining")
    print()
    print("                      []")
    print("              /       |       \\")
    print("            [1]      [2]      [3]")
    print("           / \\      / \\      / \\")
    print("        [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]")
    print("         |     |     |     |     |     |")
    print("       [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]")
    print()

    # --- Trace ---
    print("--- Trace (first few calls) ---")
    print()

    def backtrack_trace(current, remaining, depth=0, limit=[0]):
        indent = "    " * depth
        if limit[0] > 12:
            return
        limit[0] += 1

        if not remaining:
            print(f"  {indent}→ RESULT: {current}")
            return

        for i in range(len(remaining)):
            elem = remaining[i]
            print(f"  {indent}Pick {elem} from {remaining}")
            current.append(elem)
            backtrack_trace(current, remaining[:i] + remaining[i+1:], depth + 1, limit)
            current.pop()
            if limit[0] > 12:
                print(f"  {indent}... (truncated)")
                return

    backtrack_trace([], [1, 2, 3])
    print()

    # Verify swap approach
    result2 = permutations_swap(nums)
    print(f"  Swap approach also gives {len(result2)} permutations ✓")
    print()

    # --- Formula ---
    print("--- Permutation Count Formula ---")
    print()
    print("  n elements → n! permutations")
    print("  Why? 1st position: n choices")
    print("       2nd position: n-1 choices")
    print("       ...")
    print("       nth position: 1 choice")
    print("       Total = n × (n-1) × ... × 1 = n!")
    print()

    import math
    print("  | n  | n!         |")
    print("  |----|------------|")
    for n in range(1, 9):
        print(f"  | {n:>2} | {math.factorial(n):>10,} |")

    print()
    print(f"  Time: O(n × n!) | Space: O(n)")
    print(f"  n! grows VERY fast — 10! = 3,628,800")


if __name__ == "__main__":
    demonstrate()
