"""
Q1. Implement a Graph class with adjacency list representation.
    Support directed and undirected edges. Include BFS and DFS.

Answer:
    Adjacency list: dict where key=node, value=list of neighbors.
    BFS uses a queue → explores level by level.
    DFS uses a stack (or recursion) → explores depth first.

    Time:  BFS/DFS = O(V + E), V = vertices, E = edges.
    Space: O(V + E) for adjacency list, O(V) for visited set.
"""

from collections import deque, defaultdict


class Graph:
    """
    Graph with adjacency list representation.
    Supports directed and undirected edges.
    """

    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        """Add edge u→v (and v→u if undirected)."""
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)
        # Ensure both nodes exist in adj
        if v not in self.adj:
            self.adj[v] = []

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def bfs(self, start):
        """
        Breadth-First Search — explore level by level.
        Uses a QUEUE (FIFO). O(V + E).
        """
        visited = set([start])
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start):
        """
        Depth-First Search (iterative) — explore as deep as possible.
        Uses a STACK (LIFO). O(V + E).
        """
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                # Push neighbors in reverse for consistent left-to-right order
                for neighbor in reversed(self.adj[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return order

    def dfs_recursive(self, start, visited=None, order=None):
        """DFS using recursion. O(V + E)."""
        if visited is None:
            visited = set()
            order = []
        visited.add(start)
        order.append(start)
        for neighbor in self.adj[start]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited, order)
        return order

    def display(self):
        """Print the adjacency list."""
        for node in sorted(self.adj):
            neighbors = sorted(self.adj[node])
            print(f"    {node} → {neighbors}")


def demonstrate():
    print("=" * 70)
    print("Q1: Graph Class — Adjacency List, BFS, DFS")
    print("=" * 70)
    print()

    # --- Undirected Graph ---
    print("--- Undirected Graph ---")
    print()
    print("    0 ── 1 ── 2")
    print("    |    |    |")
    print("    3 ── 4    5")
    print()

    g = Graph(directed=False)
    edges = [(0, 1), (0, 3), (1, 2), (1, 4), (2, 5), (3, 4)]
    for u, v in edges:
        g.add_edge(u, v)

    print("  Adjacency List:")
    g.display()
    print()

    bfs_order = g.bfs(0)
    dfs_order = g.dfs(0)
    dfs_rec = g.dfs_recursive(0)

    print(f"  BFS from 0: {bfs_order}")
    print(f"  DFS from 0 (iterative): {dfs_order}")
    print(f"  DFS from 0 (recursive): {dfs_rec}")
    print()

    # BFS trace
    print("--- BFS Trace from node 0 ---")
    print()
    visited = set([0])
    queue = deque([0])
    print(f"  {'Step':>4} | {'Visit':>5} | {'Queue':>20} | {'Add neighbors'}")
    print(f"  {'-'*4} | {'-'*5} | {'-'*20} | {'-'*20}")

    step = 0
    while queue:
        step += 1
        node = queue.popleft()
        added = []
        for nb in g.adj[node]:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
                added.append(nb)
        print(f"  {step:>4} | {node:>5} | {str(list(queue)):>20} | {added}")

    print()

    # --- Directed Graph ---
    print("--- Directed Graph ---")
    print()
    print("    A → B → C")
    print("    ↓   ↓")
    print("    D → E")
    print()

    dg = Graph(directed=True)
    for u, v in [('A','B'), ('A','D'), ('B','C'), ('B','E'), ('D','E')]:
        dg.add_edge(u, v)

    print("  Adjacency List:")
    dg.display()
    print()
    print(f"  BFS from A: {dg.bfs('A')}")
    print(f"  DFS from A: {dg.dfs('A')}")
    print()

    # --- BFS vs DFS ---
    print("--- BFS vs DFS Comparison ---")
    print()
    print("  Feature       | BFS                | DFS")
    print("  --------------|--------------------|-----------------")
    print("  Data struct   | Queue (FIFO)       | Stack (LIFO)")
    print("  Explores      | Level by level     | Depth first")
    print("  Shortest path | ✓ (unweighted)     | ✗")
    print("  Time          | O(V + E)           | O(V + E)")
    print("  Space         | O(V)               | O(V)")
    print("  Use case      | Shortest path, BFS | Cycle detection,")
    print("                | level order        | topological sort")
    print()
    print("  Both visit every vertex and edge once → O(V + E)")


if __name__ == "__main__":
    demonstrate()
