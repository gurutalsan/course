"""
Q3. Combination Sum: Find all combos of [2,3,6,7] summing to 7.
    Elements can be reused. Trace the backtracking.

Answer:
    Backtrack: at each step, choose a candidate (can reuse), subtract
    from remaining target. If target==0 → found. If target<0 → prune.

    Results: [[2,2,3], [7]]

    Time: O(n^(T/M)) where T=target, M=min candidate.
    Space: O(T/M) recursion depth.
"""


def combination_sum(candidates, target):
    """
    Find all unique combinations summing to target.
    Each number can be used UNLIMITED times.
    """
    result = []
    candidates.sort()

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # Prune: sorted, so all after are too large

            current.append(candidates[i])
            # Pass i (not i+1) to allow reuse
            backtrack(i, current, remaining - candidates[i])
            current.pop()  # Backtrack!

    backtrack(0, [], target)
    return result


def demonstrate():
    print("=" * 70)
    print("Q3: Combination Sum — Backtracking")
    print("=" * 70)
    print()

    candidates = [2, 3, 6, 7]
    target = 7
    result = combination_sum(candidates, target)
    print(f"  Candidates: {candidates}")
    print(f"  Target: {target}")
    print(f"  Result: {result}")
    print()

    # --- Full Trace ---
    print("--- Backtracking Trace ---")
    print()

    def backtrack_trace(start, current, remaining, depth=0):
        indent = "    " * depth
        if remaining == 0:
            print(f"  {indent}✓ SUM={target}! Found: {current}")
            return
        if remaining < 0:
            print(f"  {indent}✗ Sum exceeds target, backtrack")
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                print(f"  {indent}✗ {candidates[i]} > remaining {remaining}, prune rest")
                break

            current.append(candidates[i])
            print(f"  {indent}Try {candidates[i]}: current={current}, remaining={remaining - candidates[i]}")
            backtrack_trace(i, current, remaining - candidates[i], depth + 1)
            current.pop()
            print(f"  {indent}Undo {candidates[i]}: current={current}")

    backtrack_trace(0, [], target)
    print()

    # --- Recursion Tree ---
    print("--- Recursion Tree (simplified) ---")
    print()
    print("  target=7, candidates=[2,3,6,7]")
    print()
    print("                          rem=7")
    print("               /      /      \\      \\")
    print("            +2      +3       +6     +7")
    print("          rem=5    rem=4   rem=1   rem=0 ✓ [7]")
    print("         / | \\     / \\      ✗")
    print("       +2 +3 +6  +3  +6")
    print("      r=3 r=2 ✗  r=1  ✗")
    print("      / \\   |")
    print("    +2  +3  +2")
    print("   r=1 r=0✓ r=0 ✓")
    print("    ✗  [2,2,3] [3,2,2]←pruned (start prevents duplicates)")
    print()
    print("  Using 'start' index prevents duplicate combinations")
    print("  e.g., [2,2,3] found but [3,2,2] not explored")
    print()

    # --- Key concepts ---
    print("--- Key Backtracking Concepts ---")
    print()
    print("  1. CHOOSE:    current.append(candidates[i])")
    print("  2. EXPLORE:   backtrack(i, current, remaining - candidates[i])")
    print("  3. UNCHOOSE:  current.pop()  ← BACKTRACK!")
    print()
    print("  Pruning: if candidates[i] > remaining → break (sorted order)")
    print("  Reuse:   pass i (not i+1) to allow same element again")
    print("  No dups: 'start' parameter ensures combinations, not permutations")
    print()

    # --- Test cases ---
    print("--- Test Cases ---\n")
    tests = [
        ([2, 3, 6, 7], 7, [[2,2,3], [7]]),
        ([2, 3, 5], 8, [[2,2,2,2], [2,3,3], [3,5]]),
        ([2], 1, []),
        ([1], 3, [[1,1,1]]),
    ]

    for cands, tgt, expected in tests:
        got = combination_sum(cands, tgt)
        ok = got == expected
        print(f"  candidates={cands}, target={tgt}")
        print(f"    → {got} {'✓' if ok else '✗'}")


if __name__ == "__main__":
    demonstrate()
