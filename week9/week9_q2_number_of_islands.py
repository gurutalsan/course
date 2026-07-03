"""
Q2. Number of Islands: Given a 2D grid of '1's (land) and '0's (water),
    count the number of islands using DFS.

Answer:
    Scan the grid. When a '1' is found, increment count and DFS to
    mark all connected '1's as visited (sink the island).

    Time:  O(M × N) — visit each cell once.
    Space: O(M × N) — recursion stack in worst case (all land).
"""


def num_islands(grid: list) -> int:
    """
    Count islands using DFS flood-fill.
    Time: O(M×N), Space: O(M×N) worst case.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '#'  # Mark visited
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)  # Sink the island

    return count


def num_islands_bfs(grid: list) -> int:
    """BFS alternative."""
    from collections import deque
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                queue = deque([(r, c)])
                grid[r][c] = '#'
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '#'
                            queue.append((nr, nc))
    return count


def print_grid(grid, title=""):
    if title:
        print(f"  {title}")
    for row in grid:
        print("    " + " ".join(row))
    print()


def demonstrate():
    print("=" * 70)
    print("Q2: Number of Islands — DFS Flood Fill")
    print("=" * 70)
    print()

    grid1 = [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0'],
    ]

    print_grid(grid1, "Grid 1:")
    g1_copy = [row[:] for row in grid1]
    print(f"  Islands: {num_islands(g1_copy)} (expected 1)")
    print()

    grid2 = [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1'],
    ]

    print_grid(grid2, "Grid 2:")
    g2_copy = [row[:] for row in grid2]
    print(f"  Islands: {num_islands(g2_copy)} (expected 3)")
    print()

    # --- Step-by-step trace ---
    print("--- Trace: Grid 2 ---")
    print()
    g2_trace = [row[:] for row in grid2]
    rows, cols = len(g2_trace), len(g2_trace[0])
    count = 0

    def dfs_trace(r, c, island_id):
        if r < 0 or r >= rows or c < 0 or c >= cols or g2_trace[r][c] != '1':
            return
        g2_trace[r][c] = str(island_id)
        dfs_trace(r+1, c, island_id)
        dfs_trace(r-1, c, island_id)
        dfs_trace(r, c+1, island_id)
        dfs_trace(r, c-1, island_id)

    for r in range(rows):
        for c in range(cols):
            if g2_trace[r][c] == '1':
                count += 1
                print(f"  Found '1' at ({r},{c}) → Island #{count}")
                dfs_trace(r, c, count)
                print_grid(g2_trace, f"  After marking island #{count}:")

    print(f"  Total islands: {count}")
    print()

    # --- Visual ---
    print("--- Visual: DFS Flood Fill ---")
    print()
    print("  When we find a '1', DFS spreads in 4 directions")
    print("  marking all connected land as visited:")
    print()
    print("  1 1 0      # # 0      Island 1 found & sunk")
    print("  1 1 0  →   # # 0")
    print("  0 0 1      0 0 1      ← Island 2 not yet found")
    print()
    print("  Continue scanning... find '1' at (2,2)")
    print("  # # 0      # # 0")
    print("  # # 0  →   # # 0      Island 2 found & sunk")
    print("  0 0 #      0 0 #")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---\n")
    tests = [
        ([['1','1','1','1','0'],['1','1','0','1','0'],
          ['1','1','0','0','0'],['0','0','0','0','0']], 1),
        ([['1','1','0','0','0'],['1','1','0','0','0'],
          ['0','0','1','0','0'],['0','0','0','1','1']], 3),
        ([['1','0','1','0','1']], 3),
        ([['0','0','0']], 0),
        ([['1']], 1),
    ]

    for grid, expected in tests:
        g = [row[:] for row in grid]
        got = num_islands(g)
        print(f"  {str(grid):>55} → {got} {'✓' if got==expected else '✗'}")

    print()
    print("  Time: O(M×N) — each cell visited once")
    print("  Space: O(M×N) — recursion stack worst case")


if __name__ == "__main__":
    demonstrate()
