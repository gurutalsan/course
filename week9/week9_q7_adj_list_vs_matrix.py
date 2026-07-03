"""
Q7. Compare adjacency list vs adjacency matrix. When is each preferred?

Answer:
    Adjacency LIST: dict/array of lists. Space O(V + E).
      → Best for SPARSE graphs (few edges relative to vertices).

    Adjacency MATRIX: 2D array of size V×V. Space O(V²).
      → Best for DENSE graphs or when edge lookup must be O(1).
"""


class GraphAdjList:
    """Graph using adjacency list."""
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def has_edge(self, u, v):
        return v in self.adj[u]  # O(degree)

    def neighbors(self, u):
        return self.adj[u]  # O(1)

    def space(self):
        return sum(len(v) for v in self.adj.values()) + self.V


class GraphAdjMatrix:
    """Graph using adjacency matrix."""
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def has_edge(self, u, v):
        return self.matrix[u][v] == 1  # O(1)!

    def neighbors(self, u):
        return [v for v in range(self.V) if self.matrix[u][v]]  # O(V)

    def space(self):
        return self.V * self.V


def demonstrate():
    print("=" * 70)
    print("Q7: Adjacency List vs Adjacency Matrix")
    print("=" * 70)
    print()

    # Build same graph both ways
    print("  Graph: 5 vertices, 4 edges")
    print("    0 — 1 — 2")
    print("    |       |")
    print("    3       4")
    print()

    edges = [(0,1), (1,2), (0,3), (2,4)]

    g_list = GraphAdjList(5)
    g_matrix = GraphAdjMatrix(5)
    for u, v in edges:
        g_list.add_edge(u, v)
        g_matrix.add_edge(u, v)

    # Adjacency List
    print("  Adjacency LIST:")
    for v in range(5):
        print(f"    {v}: {g_list.adj[v]}")
    print()

    # Adjacency Matrix
    print("  Adjacency MATRIX:")
    print("      " + "  ".join(str(i) for i in range(5)))
    for i in range(5):
        row = "  ".join(str(x) for x in g_matrix.matrix[i])
        print(f"    {i} [{row}]")
    print()

    # --- Comparison ---
    print("--- Comparison Table ---")
    print()
    print("  Operation          | Adj List        | Adj Matrix")
    print("  -------------------|-----------------|------------------")
    print("  Space              | O(V + E)        | O(V²)")
    print("  Add edge           | O(1)            | O(1)")
    print("  Remove edge        | O(E)            | O(1)")
    print("  Check edge (u,v)   | O(degree(u))    | O(1) ★")
    print("  Get all neighbors  | O(1) return list| O(V) scan row")
    print("  Iterate all edges  | O(V + E)        | O(V²)")
    print()

    # Space comparison
    print("--- Space Comparison ---")
    print()
    cases = [(10, 15), (100, 200), (1000, 5000), (1000, 500000)]
    print(f"  {'V':>6} | {'E':>8} | {'Density':>7} | {'List O(V+E)':>12} | {'Matrix O(V²)':>13} | {'Winner'}")
    print(f"  {'-'*6} | {'-'*8} | {'-'*7} | {'-'*12} | {'-'*13} | {'-'*8}")

    for v, e in cases:
        density = e / (v * (v-1) / 2) * 100
        list_space = v + 2 * e
        matrix_space = v * v
        winner = "List" if list_space < matrix_space else "Matrix"
        print(f"  {v:>6} | {e:>8} | {density:>6.1f}% | {list_space:>12,} | {matrix_space:>13,} | {winner}")

    print()

    # --- When to use which ---
    print("--- When to Choose Each ---")
    print()
    print("  ADJACENCY LIST (usually preferred):")
    print("    ✓ Sparse graphs (social networks, web graphs)")
    print("    ✓ Memory-constrained applications")
    print("    ✓ Most graph algorithms (BFS, DFS, Dijkstra)")
    print("    ✓ When you iterate neighbors frequently")
    print()
    print("  ADJACENCY MATRIX:")
    print("    ✓ Dense graphs (E ≈ V²)")
    print("    ✓ Need O(1) edge existence check")
    print("    ✓ Matrix operations (graph powers, Floyd-Warshall)")
    print("    ✓ Small fixed-size graphs")
    print()

    # Edge checks
    print("--- Edge Check Performance ---")
    print(f"  has_edge(0, 2) — List: {g_list.has_edge(0, 2)} (scans neighbors)")
    print(f"  has_edge(0, 2) — Matrix: {g_matrix.has_edge(0, 2)} (direct lookup)")
    print(f"  has_edge(0, 1) — List: {g_list.has_edge(0, 1)}")
    print(f"  has_edge(0, 1) — Matrix: {g_matrix.has_edge(0, 1)}")
    print()

    print("ANSWER: List for sparse graphs O(V+E) space; Matrix for dense O(V²).")
    print("Most real-world graphs are sparse → adjacency list is standard.")


if __name__ == "__main__":
    demonstrate()
