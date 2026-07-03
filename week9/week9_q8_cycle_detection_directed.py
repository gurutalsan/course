"""
Q8. Detect if adding an edge would create a cycle in a directed graph.
    Use DFS with three states (UNVISITED, VISITING, VISITED).

Answer:
    Three-state DFS:
    - UNVISITED (0): Not yet explored.
    - VISITING (1):  Currently on the DFS path (ancestors in recursion stack).
    - VISITED (2):   Fully explored, confirmed no cycle from this node.

    If DFS reaches a VISITING node → BACK EDGE → CYCLE!

    To check if adding edge (u→v) creates a cycle:
    Temporarily add the edge, then check if a cycle exists from u.
    Or equivalently: check if v can already reach u (path v→...→u exists).

    Time: O(V + E), Space: O(V).
"""

from collections import defaultdict


class DirectedGraph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if v not in self.adj:
            self.adj[v] = []

    def has_cycle(self):
        """Three-state DFS cycle detection. O(V + E)."""
        UNVISITED, VISITING, VISITED = 0, 1, 2
        state = {node: UNVISITED for node in self.adj}

        def dfs(node):
            state[node] = VISITING
            for neighbor in self.adj[node]:
                if state.get(neighbor, UNVISITED) == VISITING:
                    return True   # Back edge → cycle!
                if state.get(neighbor, UNVISITED) == UNVISITED:
                    if dfs(neighbor):
                        return True
            state[node] = VISITED
            return False

        for node in list(self.adj.keys()):
            if state[node] == UNVISITED:
                if dfs(node):
                    return True
        return False

    def would_create_cycle(self, u, v):
        """Check if adding edge u→v would create a cycle."""
        # A cycle would exist if v can already reach u
        # (adding u→v would close the loop: u→v→...→u)
        visited = set()

        def can_reach(node, target):
            if node == target:
                return True
            visited.add(node)
            for nb in self.adj.get(node, []):
                if nb not in visited:
                    if can_reach(nb, target):
                        return True
            return False

        return can_reach(v, u)

    def has_cycle_trace(self):
        """Three-state DFS with printed trace."""
        UNVISITED, VISITING, VISITED = 0, 1, 2
        state_names = {0: "UNVISITED", 1: "VISITING", 2: "VISITED"}
        state = {node: UNVISITED for node in self.adj}

        def dfs(node, depth=0):
            indent = "    " * depth
            state[node] = VISITING
            print(f"  {indent}Enter {node} → VISITING")

            for nb in self.adj[node]:
                if state.get(nb, UNVISITED) == VISITING:
                    print(f"  {indent}  → {nb} is VISITING → CYCLE FOUND! ★")
                    return True
                if state.get(nb, UNVISITED) == UNVISITED:
                    if dfs(nb, depth + 1):
                        return True

            state[node] = VISITED
            print(f"  {indent}Leave {node} → VISITED")
            return False

        for node in sorted(self.adj.keys()):
            if state[node] == UNVISITED:
                if dfs(node):
                    return True
        return False


def demonstrate():
    print("=" * 70)
    print("Q8: Cycle Detection with Three-State DFS")
    print("=" * 70)
    print()

    # --- Three states explained ---
    print("--- Three States ---")
    print()
    print("  UNVISITED (white): Not yet explored")
    print("  VISITING  (gray):  Currently on DFS path (in recursion stack)")
    print("  VISITED   (black): Fully explored, no cycle from here")
    print()
    print("  Key insight: if DFS reaches a VISITING node, we found a")
    print("  BACK EDGE — a path from a node back to its ancestor → CYCLE!")
    print()

    # --- Graph WITHOUT cycle ---
    print("--- Example 1: No Cycle ---")
    print()
    print("    A → B → C")
    print("    ↓       ↓")
    print("    D       E")
    print()

    g1 = DirectedGraph()
    for u, v in [('A','B'), ('A','D'), ('B','C'), ('C','E')]:
        g1.add_edge(u, v)

    print("  DFS trace:")
    result1 = g1.has_cycle_trace()
    print(f"  Has cycle: {result1}")
    print()

    # --- Graph WITH cycle ---
    print("--- Example 2: Has Cycle ---")
    print()
    print("    A → B → C")
    print("    ↑       ↓")
    print("    └───────┘")
    print()

    g2 = DirectedGraph()
    for u, v in [('A','B'), ('B','C'), ('C','A')]:
        g2.add_edge(u, v)

    print("  DFS trace:")
    result2 = g2.has_cycle_trace()
    print(f"  Has cycle: {result2}")
    print()

    # --- Would adding edge create cycle? ---
    print("--- Would Adding Edge Create a Cycle? ---")
    print()
    print("    A → B → C → D")

    g3 = DirectedGraph()
    for u, v in [('A','B'), ('B','C'), ('C','D')]:
        g3.add_edge(u, v)

    tests = [
        ('D', 'A', True, "D→A creates A→B→C→D→A cycle"),
        ('D', 'B', True, "D→B creates B→C→D→B cycle"),
        ('A', 'D', False, "A→D is fine (no path D→A)"),
        ('C', 'B', True, "C→B creates B→C→B cycle"),
        ('A', 'C', False, "A→C is fine (redundant but no cycle)"),
    ]

    print()
    print(f"  {'Edge':>6} | {'Creates Cycle?':>14} | {'Expected':>8} | {'Note'}")
    print(f"  {'-'*6} | {'-'*14} | {'-'*8} | {'-'*30}")

    for u, v, expected, note in tests:
        result = g3.would_create_cycle(u, v)
        status = "✓" if result == expected else "✗"
        print(f"  {u}→{v:>3} | {str(result):>14} | {str(expected):>8} | {note} {status}")

    print()

    # --- Why 3 states not 2? ---
    print("--- Why 3 States, Not Just Visited/Unvisited? ---")
    print()
    print("  With only 2 states, we can't distinguish between:")
    print("    • A BACK edge (to ancestor) → CYCLE")
    print("    • A CROSS edge (to already-finished node) → NO CYCLE")
    print()
    print("  Example:  A → C")
    print("            B → C")
    print("  When processing B→C, C is already VISITED (not VISITING).")
    print("  With 2 states, we'd wrongly report a cycle.")
    print("  With 3 states: C is VISITED (black) → safe, not a cycle.")
    print()

    print("  Time: O(V + E) | Space: O(V)")


if __name__ == "__main__":
    demonstrate()
