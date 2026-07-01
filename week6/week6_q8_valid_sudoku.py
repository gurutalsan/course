"""
Q8. Given a sudoku board (9×9), write a function to check if it is valid
    using hash sets for rows, columns, and 3×3 boxes.

Answer:
    Use 9 sets for rows, 9 sets for columns, and 9 sets for 3×3 boxes.
    Scan every cell once. For each non-empty cell, check if the number
    already exists in its row/column/box set. If yes → invalid.

    Box index formula: box_idx = (row // 3) * 3 + (col // 3)

    Time:  O(1) — board is always 9×9 = 81 cells (constant).
    Space: O(1) — at most 27 sets of at most 9 elements each.
"""


def is_valid_sudoku(board: list) -> bool:
    """
    Check if a 9×9 Sudoku board is valid.

    Rules:
    1. Each row must contain digits 1-9 without repetition.
    2. Each column must contain digits 1-9 without repetition.
    3. Each of the 9 3×3 sub-boxes must contain 1-9 without repetition.

    '.' represents an empty cell. Only filled cells are validated.

    Time:  O(81) = O(1) — fixed board size.
    Space: O(27 × 9) = O(1)
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]

            if num == '.':
                continue

            # Compute which 3×3 box this cell belongs to
            box_idx = (r // 3) * 3 + (c // 3)

            # Check for duplicates
            if num in rows[r]:
                return False
            if num in cols[c]:
                return False
            if num in boxes[box_idx]:
                return False

            # Add to sets
            rows[r].add(num)
            cols[c].add(num)
            boxes[box_idx].add(num)

    return True


def is_valid_sudoku_detailed(board: list) -> tuple:
    """Same as above but returns details about the first violation."""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == '.':
                continue

            box_idx = (r // 3) * 3 + (c // 3)

            if num in rows[r]:
                return False, f"Duplicate '{num}' in row {r}"
            if num in cols[c]:
                return False, f"Duplicate '{num}' in column {c}"
            if num in boxes[box_idx]:
                return False, f"Duplicate '{num}' in box {box_idx} (row {r}, col {c})"

            rows[r].add(num)
            cols[c].add(num)
            boxes[box_idx].add(num)

    return True, "Valid board"


def demonstrate():
    print("=" * 70)
    print("Q8: Valid Sudoku Checker Using Hash Sets")
    print("=" * 70)
    print()

    # --- Box Index Formula ---
    print("--- Box Index Formula ---")
    print()
    print("  The 9×9 board has 9 boxes (3×3 each):")
    print()
    print("    ┌─────────┬─────────┬─────────┐")
    print("    │ Box 0   │ Box 1   │ Box 2   │")
    print("    │ (0,0)   │ (0,1)   │ (0,2)   │")
    print("    ├─────────┼─────────┼─────────┤")
    print("    │ Box 3   │ Box 4   │ Box 5   │")
    print("    │ (1,0)   │ (1,1)   │ (1,2)   │")
    print("    ├─────────┼─────────┼─────────┤")
    print("    │ Box 6   │ Box 7   │ Box 8   │")
    print("    │ (2,0)   │ (2,1)   │ (2,2)   │")
    print("    └─────────┴─────────┴─────────┘")
    print()
    print("  Formula: box_idx = (row // 3) * 3 + (col // 3)")
    print()
    print("  Examples:")
    print("    Cell (0,0) → box (0//3)*3 + (0//3) = 0")
    print("    Cell (1,4) → box (1//3)*3 + (4//3) = 0*3 + 1 = 1")
    print("    Cell (5,7) → box (5//3)*3 + (7//3) = 1*3 + 2 = 5")
    print("    Cell (8,8) → box (8//3)*3 + (8//3) = 2*3 + 2 = 8")
    print()

    # --- Valid Board ---
    valid_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]

    print("--- Valid Board ---")
    print()
    print_board(valid_board)
    is_valid, msg = is_valid_sudoku_detailed(valid_board)
    print(f"  Result: {is_valid} — {msg}")
    print()

    # --- Invalid Board ---
    invalid_board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],  # ← Duplicate 8 in column 0!
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]

    print("--- Invalid Board ---")
    print()
    print_board(invalid_board)
    is_valid, msg = is_valid_sudoku_detailed(invalid_board)
    print(f"  Result: {is_valid} — {msg}")
    print()

    # --- Algorithm Trace ---
    print("--- Algorithm: Three Sets Per Unit ---")
    print()
    print("  We maintain:")
    print("    9 row sets:    rows[0..8]")
    print("    9 column sets: cols[0..8]")
    print("    9 box sets:    boxes[0..8]")
    print()
    print("  For each non-empty cell (r, c) with value num:")
    print("    1. Check: num in rows[r]?    → duplicate in row!")
    print("    2. Check: num in cols[c]?    → duplicate in column!")
    print("    3. Check: num in boxes[idx]? → duplicate in box!")
    print("    4. If all clear: add num to all three sets.")
    print()

    # --- Trace first few cells ---
    print("--- Trace: First Row of Valid Board ---")
    print()
    print(f"  Row 0: {valid_board[0]}")
    print()

    rows_trace = [set() for _ in range(9)]
    cols_trace = [set() for _ in range(9)]
    boxes_trace = [set() for _ in range(9)]

    print(f"  {'Cell':>6} | {'Num':>3} | {'Box':>3} | {'rows[0]':>12} | {'cols[c]':>10} | {'boxes[b]':>10} | {'Valid?':>6}")
    print(f"  {'-'*6} | {'-'*3} | {'-'*3} | {'-'*12} | {'-'*10} | {'-'*10} | {'-'*6}")

    for c in range(9):
        num = valid_board[0][c]
        if num == '.':
            print(f"  (0,{c}) | {'·':>3} | {'—':>3} | {'—':>12} | {'—':>10} | {'—':>10} | {'skip':>6}")
            continue

        box_idx = (0 // 3) * 3 + (c // 3)
        valid = num not in rows_trace[0] and num not in cols_trace[c] and num not in boxes_trace[box_idx]

        rows_trace[0].add(num)
        cols_trace[c].add(num)
        boxes_trace[box_idx].add(num)

        print(f"  (0,{c}) | {num:>3} | {box_idx:>3} | {str(rows_trace[0]):>12} | {str(cols_trace[c]):>10} | {str(boxes_trace[box_idx]):>10} | {'✓' if valid else '✗':>6}")

    print()

    # --- Test with box duplicate ---
    print("--- Test: Box Duplicate ---")
    print()
    box_dup_board = [
        ["1","2","3",".",".",".",".",".","."],
        ["4","5","6",".",".",".",".",".","."],
        ["7","8","1",".",".",".",".",".","."],  # 1 duplicated in box 0!
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
    ]
    is_valid, msg = is_valid_sudoku_detailed(box_dup_board)
    print(f"  Box duplicate: {is_valid} — {msg}")
    print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Time:  O(81) = O(1) — board size is fixed at 9×9")
    print("  Space: O(27 × 9) = O(1) — 27 sets, each ≤ 9 elements")
    print()
    print("  (Technically O(1) because the input size is constant,")
    print("   but conceptually O(n²) for an n×n board)")
    print()
    print("ANSWER: Use 9 row sets + 9 column sets + 9 box sets.")
    print("For each cell, check membership in all three sets → O(1) per cell.")
    print("Box index = (row // 3) * 3 + (col // 3).")


def print_board(board):
    """Pretty-print a sudoku board."""
    for i, row in enumerate(board):
        if i % 3 == 0 and i > 0:
            print("  ───────┼───────┼───────")
        line = "  "
        for j, cell in enumerate(row):
            if j % 3 == 0 and j > 0:
                line += "│ "
            display = cell if cell != '.' else '·'
            line += display + " "
        print(line)
    print()


if __name__ == "__main__":
    demonstrate()
