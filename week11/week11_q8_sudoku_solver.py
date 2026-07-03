"""
Q8. Sudoku solver using backtracking. Try digits 1-9, check validity.

Answer:
    For each empty cell, try digits 1-9. Check row, column, and 3×3 box.
    If valid → place and recurse. If stuck → undo and try next digit.

    Validation: digit must not appear in same row, column, or 3×3 box.
    Time: O(9^(empty cells)), Space: O(empty cells) recursion.
"""


def solve_sudoku(board):
    """
    Solve Sudoku in-place using backtracking.
    Returns True if solved, False if no solution.
    """

    def is_valid(board, row, col, num):
        """Check if placing num at (row, col) is valid."""
        num_str = str(num)

        # Check row
        if num_str in board[row]:
            return False

        # Check column
        for r in range(9):
            if board[r][col] == num_str:
                return False

        # Check 3×3 box
        box_r, box_c = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_r, box_r + 3):
            for c in range(box_c, box_c + 3):
                if board[r][c] == num_str:
                    return False

        return True

    def backtrack():
        # Find next empty cell
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    # Try digits 1-9
                    for num in range(1, 10):
                        if is_valid(board, r, c, num):
                            board[r][c] = str(num)  # Place

                            if backtrack():
                                return True

                            board[r][c] = '.'  # Undo (backtrack!)

                    return False  # No valid digit → dead end
        return True  # No empty cells → solved!

    return backtrack()


def print_board(board, title=""):
    if title:
        print(f"  {title}")
    print("  ╔═══════╦═══════╦═══════╗")
    for i, row in enumerate(board):
        if i > 0 and i % 3 == 0:
            print("  ╠═══════╬═══════╬═══════╣")
        line = "  ║"
        for j, val in enumerate(row):
            if j > 0 and j % 3 == 0:
                line += "║"
            v = val if val != '.' else ' '
            line += f" {v}"
        line += "║"
        print(line)
    print("  ╚═══════╩═══════╩═══════╝")


def demonstrate():
    print("=" * 70)
    print("Q8: Sudoku Solver — Backtracking")
    print("=" * 70)
    print()

    board = [
        ['5','3','.','.','7','.','.','.','.'],
        ['6','.','.','1','9','5','.','.','.'],
        ['.','9','8','.','.','.','.','6','.'],
        ['8','.','.','.','6','.','.','.','3'],
        ['4','.','.','8','.','3','.','.','1'],
        ['7','.','.','.','2','.','.','.','6'],
        ['.','6','.','.','.','.','2','8','.'],
        ['.','.','.','4','1','9','.','.','5'],
        ['.','.','.','.','8','.','.','7','9'],
    ]

    print_board(board, "Input Puzzle:")
    print()

    # Count empty cells
    empties = sum(row.count('.') for row in board)
    print(f"  Empty cells: {empties}")
    print()

    # Solve
    board_copy = [row[:] for row in board]
    solved = solve_sudoku(board_copy)

    if solved:
        print_board(board_copy, "Solved:")
    else:
        print("  No solution exists!")
    print()

    # --- Validation Logic ---
    print("--- Validation: is_valid(row, col, num) ---")
    print()
    print("  Three checks for placing digit d at position (r, c):")
    print()
    print("  1. ROW CHECK: d not in board[r]")
    print("     → Scan all 9 columns in row r")
    print()
    print("  2. COLUMN CHECK: d not in any board[i][c]")
    print("     → Scan all 9 rows in column c")
    print()
    print("  3. 3×3 BOX CHECK:")
    print("     box_row = 3 × (r // 3)")
    print("     box_col = 3 × (c // 3)")
    print("     → Scan all 9 cells in the box")
    print()
    print("  Example: placing '4' at (0, 2):")
    print("    Row 0: [5,3,_,_,7,_,_,_,_] → no 4 ✓")
    print("    Col 2: [_,_,8,_,_,_,_,_,_] → no 4 ✓")
    print("    Box (0,0)-(2,2): [5,3,_,6,_,_,_,9,8] → no 4 ✓")
    print()

    # --- How backtracking works ---
    print("--- Backtracking Flow ---")
    print()
    print("  1. Find next empty cell ('.')")
    print("  2. Try digits 1 through 9:")
    print("     a. Check if digit is valid (row, col, box)")
    print("     b. If valid → place digit, recurse to next empty")
    print("     c. If recursion succeeds → puzzle solved!")
    print("     d. If recursion fails → UNDO (set back to '.')")
    print("  3. If no digit works → return False (backtrack to prev cell)")
    print("  4. If no empty cells remain → return True (solved!)")
    print()

    # --- Visual backtracking example ---
    print("--- Visual: Backtracking at Cell (0,2) ---")
    print()
    print("  Try 1: is_valid? No (1 in col 2 at row 1)")
    print("  Try 2: is_valid? No (2 in row 0? No, in col? No, in box? No)")
    print("         → Place 2, recurse... eventually fails, UNDO")
    print("  Try 3: is_valid? No (3 in row 0)")
    print("  Try 4: is_valid? Yes → Place 4, recurse → SUCCESS!")
    print()

    print("  Time: O(9^E) where E = empty cells (worst case)")
    print("  Space: O(E) recursion depth")
    print("  Pruning (is_valid) eliminates most branches → fast in practice")


if __name__ == "__main__":
    demonstrate()
