"""
Q5. Word Search: Does a word exist in a 2D grid? Backtracking with visited cells.

Answer:
    For each cell matching the first character, DFS in 4 directions.
    Mark cells as visited (modify in-place), then UN-mark on backtrack.

    Time:  O(M × N × 4^L) where L = word length.
    Space: O(L) recursion depth.
"""


def word_search(board, word):
    """
    Check if word exists in the grid via adjacent cells.
    Backtracking DFS with in-place visited marking.
    """
    if not board or not word:
        return False

    rows, cols = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word):
            return True  # All characters matched!

        if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[idx]):
            return False

        # Mark visited
        temp = board[r][c]
        board[r][c] = '#'

        # Explore 4 directions
        found = (dfs(r + 1, c, idx + 1) or
                 dfs(r - 1, c, idx + 1) or
                 dfs(r, c + 1, idx + 1) or
                 dfs(r, c - 1, idx + 1))

        # Backtrack: restore cell
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    return False


def demonstrate():
    print("=" * 70)
    print("Q5: Word Search — Backtracking in 2D Grid")
    print("=" * 70)
    print()

    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E'],
    ]

    print("  Board:")
    for row in board:
        print(f"    {row}")
    print()

    tests = ["ABCCED", "SEE", "ABCB", "ABFS"]
    for word in tests:
        b = [row[:] for row in board]
        result = word_search(b, word)
        print(f"  '{word}': {result}")
    print()

    # --- Trace ---
    print("--- Trace: Searching for 'SEE' ---")
    print()
    print("  Start: Find 'S' in grid → found at (1,3)")
    print()
    print("    A  B  C  E         A  B  C  E")
    print("    S  F  C [S]←start  S  F  C [#]")
    print("    A  D  E  E         A  D  E [E]←match 'E'")
    print()
    print("    A  B  C  E")
    print("    S  F  C [#]")
    print("    A  D [E][#]←match 'E', word complete!")
    print()
    print("  Path: (1,3)→(2,3)→(2,2) = 'S'→'E'→'E' ✓")
    print()

    print("--- Trace: Searching for 'ABCB' (should fail) ---")
    print()
    print("  Start at (0,0)='A', then (0,1)='B', then (0,2)='C'")
    print("  Need 'B' next → (0,1) is 'B' BUT already visited! (#)")
    print("  No other neighbor is 'B' → backtrack → False")
    print()
    print("  The visited constraint prevents reusing cells!")
    print()

    # --- How backtracking handles visited ---
    print("--- Visited Cell Handling ---")
    print()
    print("  1. MARK:     board[r][c] = '#'   (before exploring)")
    print("  2. EXPLORE:  DFS in 4 directions")
    print("  3. RESTORE:  board[r][c] = temp   (after exploring)")
    print()
    print("  Why modify in-place instead of a visited set?")
    print("  → O(1) space per cell vs O(L) for a set")
    print("  → Simpler to implement")
    print("  → Automatically handles the constraint")
    print()

    # More test cases
    print("--- More Test Cases ---\n")
    tests2 = [
        ([['A','B'],['C','D']], "ABDC", True),
        ([['A','B'],['C','D']], "ABCD", False),
        ([['A']], "A", True),
        ([['A']], "B", False),
        ([['A','A']], "AA", True),
    ]

    for b, w, expected in tests2:
        got = word_search([r[:] for r in b], w)
        print(f"  board={b}, word='{w}' → {got} {'✓' if got==expected else '✗'}")

    print()
    print("  Time: O(M×N×4^L) worst case | Space: O(L) recursion")


if __name__ == "__main__":
    demonstrate()
