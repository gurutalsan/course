"""
Q6. Shortest path in unweighted graph using BFS. Return the path, not distance.

Answer:
    BFS guarantees shortest path in UNWEIGHTED graphs because it explores
    nodes level by level (distance 1, then 2, then 3...).

    Track the parent of each node. Reconstruct path by backtracking from
    destination to source using the parent map.

    Time: O(V + E), Space: O(V).
"""

from collections import deque, defaultdict


def shortest_path(graph: dict, start, end) -> list:
    """
    BFS shortest path returning the actual path.
    Time: O(V + E), Space: O(V).
    """
    if start == end:
        return [start]

    visited = {start}
    queue = deque([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

                if neighbor == end:
                    # Reconstruct path
                    path = []
                    current = end
                    while current is not None:
                        path.append(current)
                        current = parent[current]
                    return path[::-1]

    return []  # No path exists


def all_shortest_paths_bfs(graph, start):
    """BFS from start, return distances to all reachable nodes."""
    dist = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nb in graph.get(node, []):
            if nb not in dist:
                dist[nb] = dist[node] + 1
                queue.append(nb)
    return dist


def demonstrate():
    print("=" * 70)
    print("Q6: Shortest Path in Unweighted Graph (BFS)")
    print("=" * 70)
    print()

    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F'],
    }

    print("  Graph:")
    print("    A — B — D")
    print("    |   |")
    print("    C   E")
    print("    |   |")
    print("    F———+")
    print("    |")
    print("    G")
    print()

    # Shortest paths
    pairs = [('A','G'), ('A','E'), ('D','G'), ('A','D'), ('B','F')]

    for start, end in pairs:
        path = shortest_path(graph, start, end)
        print(f"  {start} → {end}: {' → '.join(path)} (distance {len(path)-1})")

    print()

    # --- Trace ---
    print("--- BFS Trace: A → G ---")
    print()

    visited = {'A'}
    queue = deque(['A'])
    parent = {'A': None}
    found = False

    print(f"  {'Step':>4} | {'Visit':>5} | {'Level':>5} | {'Add':>12} | {'Queue':>15} | {'Parents'}")
    print(f"  {'-'*4} | {'-'*5} | {'-'*5} | {'-'*12} | {'-'*15} | {'-'*25}")

    step = 0
    level_map = {'A': 0}

    while queue and not found:
        step += 1
        node = queue.popleft()
        added = []
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                parent[nb] = node
                queue.append(nb)
                level_map[nb] = level_map[node] + 1
                added.append(nb)
                if nb == 'G':
                    found = True

        print(f"  {step:>4} | {node:>5} | {level_map[node]:>5} | {str(added):>12} | {str(list(queue)):>15} | {node}←{parent[node]}")

    # Reconstruct
    path = []
    curr = 'G'
    while curr:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    print(f"\n  Path: {' → '.join(path)}")
    print()

    # --- Why BFS gives shortest path ---
    print("--- Why BFS Guarantees Shortest Path ---")
    print()
    print("  BFS explores ALL nodes at distance d before distance d+1.")
    print("  So the FIRST time we reach a node = shortest distance!")
    print()
    print("    Distance 0: {A}")
    print("    Distance 1: {B, C}")
    print("    Distance 2: {D, E, F}")
    print("    Distance 3: {G} ← first found at distance 3")
    print()

    # Distances from A
    dists = all_shortest_paths_bfs(graph, 'A')
    print("  Distances from A:")
    for node in sorted(dists):
        print(f"    A → {node}: {dists[node]}")

    print()
    print("  Time: O(V + E) | Space: O(V)")
    print("  NOTE: BFS only works for UNWEIGHTED graphs.")
    print("  For weighted graphs, use Dijkstra's algorithm.")


if __name__ == "__main__":
    demonstrate()
