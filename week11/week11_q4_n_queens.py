"""
Q4. Solve N-Queens for n=4. Draw all valid boards.
    Explain is_safe() diagonal check.

Answer:
    Place queens row by row. For each row, try each column.
    Check: no two queens share same column, or diagonal.

    Diagonal check:
    - Same diagonal (\\): row - col is constant
    - Same anti-diagonal (/): row + col is constant

    n=4 has exactly 2 solutions.
    Time: O(n!), Space: O(n).
"""


def solve_n_queens(n):
    """Solve N-Queens using backtracking."""
    result = []
    cols = set()
    diag = set()       # row - col (same for \\ diagonal)
    anti_diag = set()   # row + col (same for / diagonal)

    board = [['.' for _ in range(n)] for _ in range(n)]

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row - col) in diag or (row + col) in anti_diag:
                continue  # Not safe!

            # Place queen
            board[row][col] = 'Q'
            cols.add(col)
            diag.add(row - col)
            anti_diag.add(row + col)

            backtrack(row + 1)

            # Remove queen (backtrack)
            board[row][col] = '.'
            cols.remove(col)
            diag.discard(row - col)
            anti_diag.discard(row + col)

    backtrack(0)
    return result


def print_board(board, title=""):
    if title:
        print(f"  {title}")
    n = len(board)
    print(f"    +{'---+' * n}")
    for row in board:
        cells = '|'.join(f' {c} ' for c in row)
        print(f"    |{cells}|")
        print(f"    +{'---+' * n}")


def demonstrate():
    print("=" * 70)
    print("Q4: N-Queens Problem (n=4)")
    print("=" * 70)
    print()

    solutions = solve_n_queens(4)
    print(f"  n=4 → {len(solutions)} solutions")
    print()

    for i, sol in enumerate(solutions):
        print_board(sol, f"Solution {i+1}:")
        print()

    # --- Diagonal Check ---
    print("--- is_safe() Diagonal Explanation ---")
    print()
    print("  Two queens attack each other if:")
    print("    1. Same ROW      → handled by placing one per row")
    print("    2. Same COLUMN   → track used columns in a set")
    print("    3. Same DIAGONAL → two types:")
    print()
    print("    \\ diagonal: row - col is CONSTANT")
    print("      (0,0)=0  (1,1)=0  (2,2)=0  ← same \\ diagonal")
    print("      (0,1)=-1 (1,2)=-1           ← same \\ diagonal")
    print()
    print("    / anti-diagonal: row + col is CONSTANT")
    print("      (0,2)=2  (1,1)=2  (2,0)=2  ← same / diagonal")
    print("      (0,3)=3  (1,2)=3            ← same / diagonal")
    print()
    print("    Visual for 4×4:")
    print("         col→  0    1    2    3")
    print("    row 0:   r-c=0  -1   -2   -3     \\ diagonals")
    print("    row 1:       1   0   -1   -2")
    print("    row 2:       2   1    0   -1")
    print("    row 3:       3   2    1    0")
    print()
    print("         col→  0    1    2    3")
    print("    row 0:   r+c=0   1    2    3     / diagonals")
    print("    row 1:       1   2    3    4")
    print("    row 2:       2   3    4    5")
    print("    row 3:       3   4    5    6")
    print()

    # --- Backtracking trace ---
    print("--- Backtracking Trace (first solution) ---")
    print()
    print("  Row 0: Try col 0 → place Q at (0,0)")
    print("  Row 1: col 0 (col conflict), col 1 (diag conflict)")
    print("         col 2 → place Q at (1,2)")
    print("  Row 2: col 0 (diag), col 1-3 conflicts → BACKTRACK")
    print("  Back to Row 1: try col 3 → Q at (1,3)")
    print("  Row 2: col 0 (diag), col 1 → place Q at (2,1)")
    print("  Row 3: all columns conflict → BACKTRACK")
    print("  ... eventually finds (0,1),(1,3),(2,0),(3,2) ✓")
    print()

    # N-Queens count
    print("--- Solution Counts ---")
    print()
    print("  | n | Solutions |")
    print("  |---|-----------|")
    for n in range(1, 9):
        sols = solve_n_queens(n)
        print(f"  | {n} | {len(sols):>9} |")

    print()
    print("  Time: O(n!) | Space: O(n)")


if __name__ == "__main__":
    demonstrate()
