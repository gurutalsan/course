"""
Q7. Search a 2D matrix where each row and column is sorted. O(m+n).
    Example: search for 5 in [[1,4,7],[2,5,8],[3,6,9]].

Answer:
    Start from TOP-RIGHT corner (or bottom-left).
    - If current == target → found!
    - If current > target → move LEFT (eliminate column)
    - If current < target → move DOWN (eliminate row)

    Each step eliminates a row or column → O(m + n).
"""


def search_matrix(matrix, target):
    """
    Search in row-sorted and column-sorted matrix.
    Start from top-right corner.
    Time: O(m + n), Space: O(1).
    """
    if not matrix or not matrix[0]:
        return False, (-1, -1)

    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, cols - 1  # Start at top-right

    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return True, (r, c)
        elif matrix[r][c] > target:
            c -= 1  # Too big → go left
        else:
            r += 1  # Too small → go down

    return False, (-1, -1)


def demonstrate():
    print("=" * 70)
    print("Q7: Search 2D Sorted Matrix — O(m + n)")
    print("=" * 70)
    print()

    matrix = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16],
        [10, 13, 14, 17],
    ]

    print("  Matrix (each row and column sorted):")
    for row in matrix:
        print(f"    {row}")
    print()

    # --- Algorithm ---
    print("--- Algorithm: Start from Top-Right ---")
    print()
    print("  Start at top-right corner (0, cols-1)")
    print("  • current > target → move LEFT  (eliminate this column)")
    print("  • current < target → move DOWN  (eliminate this row)")
    print("  • current == target → FOUND!")
    print()
    print("  Why top-right? It's a 'decision point':")
    print("    Going LEFT  → smaller values")
    print("    Going DOWN  → larger values")
    print()

    # --- Trace ---
    target = 5
    print(f"--- Trace: Search for {target} ---")
    print()
    r, c = 0, len(matrix[0]) - 1
    step = 0

    print(f"  {'Step':>4} | {'(r,c)':>6} | {'Value':>5} | {'Action':>20}")
    print(f"  {'-'*4} | {'-'*6} | {'-'*5} | {'-'*20}")

    while r < len(matrix) and c >= 0:
        step += 1
        val = matrix[r][c]
        if val == target:
            print(f"  {step:>4} | ({r},{c}) | {val:>5} | FOUND! ★")
            break
        elif val > target:
            print(f"  {step:>4} | ({r},{c}) | {val:>5} | {val}>{target} → go LEFT")
            c -= 1
        else:
            print(f"  {step:>4} | ({r},{c}) | {val:>5} | {val}<{target} → go DOWN")
            r += 1

    print()

    # Visual path
    print("  Visual path (searching for 5):")
    print("    [1   4   7  *11*]  ← start at 11, 11>5 → left")
    print("    [2   5   8  *12*]")
    print("    [3   6   9   16 ]")
    print("    [10  13  14  17 ]")
    print()
    print("    [1   4  *7*  — ]  ← at 7, 7>5 → left")
    print("    [1  *4*  —   — ]  ← at 4, 4<5 → down")
    print("    [2  *5*  —   — ]  ← at 5, FOUND at (1,1)! ★")
    print()

    # Test cases
    print("--- Test Cases ---\n")
    tests = [5, 1, 17, 14, 15, 10, 0]
    for t in tests:
        found, pos = search_matrix(matrix, t)
        status = f"at {pos}" if found else "not found"
        print(f"  Search {t:>3}: {str(found):>5} {status}")

    print()

    # Smaller example from question
    print("--- Example from Question ---")
    m2 = [[1,4,7],[2,5,8],[3,6,9]]
    print(f"  Matrix: {m2}")
    found, pos = search_matrix(m2, 5)
    print(f"  Search 5: found={found} at {pos}")
    print()

    print("  Time: O(m + n) — at most m+n steps (one row or column eliminated each)")
    print("  Space: O(1)")


if __name__ == "__main__":
    demonstrate()
