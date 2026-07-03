"""
Q7. Difference between recursion and backtracking.
    When does a recursive problem become a backtracking problem?

Answer:
    RECURSION: A function that calls itself to break a problem into
    smaller subproblems. Goal: compute a result.

    BACKTRACKING: Recursion + UNDO step. Explores choices, and when a
    choice fails, UNDOES it and tries the next option.
    Goal: find ALL solutions (or one valid solution) in a search space.

    A problem becomes backtracking when:
    1. There are multiple CHOICES at each step
    2. Some choices lead to DEAD ENDS (constraints)
    3. You need to UNDO choices and try alternatives
"""


def factorial(n):
    """Pure RECURSION: compute n! No choices, no backtracking."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Pure RECURSION: compute nth Fibonacci. No choices."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def find_subsets(nums):
    """BACKTRACKING: explore include/exclude choices, undo each."""
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])
            return

        # Choice 1: skip
        backtrack(index + 1, current)

        # Choice 2: include → make choice, explore, UNDO
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()  # ← THE BACKTRACK STEP

    backtrack(0, [])
    return result


def find_path(maze, start, end):
    """BACKTRACKING: find path in maze, undo visited on dead ends."""
    rows, cols = len(maze), len(maze[0])
    path = []

    def backtrack(r, c):
        if (r, c) == end:
            path.append((r, c))
            return True
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                maze[r][c] != 0):
            return False

        # Mark visited
        maze[r][c] = 2
        path.append((r, c))

        # Try all 4 directions
        if (backtrack(r+1, c) or backtrack(r-1, c) or
                backtrack(r, c+1) or backtrack(r, c-1)):
            return True

        # BACKTRACK: undo visit
        path.pop()
        maze[r][c] = 0
        return False

    backtrack(start[0], start[1])
    return path


def demonstrate():
    print("=" * 70)
    print("Q7: Recursion vs Backtracking")
    print("=" * 70)
    print()

    # --- Comparison ---
    print("--- Side-by-Side Comparison ---")
    print()
    print("  Feature        | Recursion           | Backtracking")
    print("  ---------------|---------------------|--------------------")
    print("  Definition     | Function calls self | Recursion + UNDO")
    print("  Goal           | Compute a result    | Find solutions")
    print("  Choices        | One clear path      | Multiple options")
    print("  Undo step      | No                  | Yes (pop, restore)")
    print("  Dead ends      | N/A                 | Prune & backtrack")
    print("  Examples       | Factorial, Fib,     | N-Queens, Sudoku,")
    print("                 | merge sort, tree DFS| subsets, permutations")
    print()

    # --- Pure Recursion ---
    print("--- Example: Pure Recursion (Factorial) ---")
    print()
    print("  def factorial(n):")
    print("      if n <= 1: return 1")
    print("      return n * factorial(n - 1)")
    print()
    print("  factorial(5):")
    print("    5 × factorial(4)")
    print("    5 × 4 × factorial(3)")
    print("    5 × 4 × 3 × factorial(2)")
    print("    5 × 4 × 3 × 2 × factorial(1)")
    print("    5 × 4 × 3 × 2 × 1 = 120")
    print()
    print(f"  Result: {factorial(5)}")
    print("  → No choices, no undoing, just compute.")
    print()

    # --- Backtracking ---
    print("--- Example: Backtracking (Subsets) ---")
    print()
    print("  def backtrack(index, current):")
    print("      if index == len(nums):")
    print("          result.append(current[:])")
    print("          return")
    print("      backtrack(index + 1, current)    # Skip")
    print("      current.append(nums[index])       # ← CHOOSE")
    print("      backtrack(index + 1, current)     # ← EXPLORE")
    print("      current.pop()                     # ← UNDO ★")
    print()
    print("  The CHOOSE → EXPLORE → UNDO pattern IS backtracking.")
    print()

    # --- When does recursion become backtracking? ---
    print("--- When Recursion Becomes Backtracking ---")
    print()
    print("  Recursion becomes backtracking when:")
    print()
    print("  1. MULTIPLE CHOICES at each step")
    print("     → 'Should I include this element or not?'")
    print("     → 'Which column should I place the queen in?'")
    print()
    print("  2. CONSTRAINTS that make some choices invalid")
    print("     → Queens can't attack each other")
    print("     → Parentheses must be balanced")
    print()
    print("  3. Need to UNDO a choice to try another")
    print("     → current.pop()")
    print("     → board[r][c] = '.' (remove queen)")
    print("     → visited.remove(node)")
    print()

    # --- Maze example ---
    print("--- Backtracking in Action: Maze ---")
    print()
    maze = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
    ]
    print("  Maze (0=open, 1=wall):")
    for row in maze:
        print(f"    {row}")
    print()

    path = find_path([r[:] for r in maze], (0, 0), (3, 3))
    print(f"  Path found: {path}")
    print()
    print("  The solver TRIES a direction, and if it hits a dead end,")
    print("  it BACKTRACKS (undoes the move) and tries another direction.")
    print()

    # Summary
    print("--- Template: Backtracking Pattern ---")
    print()
    print("  def backtrack(state):")
    print("      if is_solution(state):")
    print("          record(state)")
    print("          return")
    print("      for choice in get_choices(state):")
    print("          if is_valid(choice):        # Pruning")
    print("              make_choice(choice)     # Choose")
    print("              backtrack(new_state)     # Explore")
    print("              undo_choice(choice)      # Backtrack ★")


if __name__ == "__main__":
    demonstrate()
