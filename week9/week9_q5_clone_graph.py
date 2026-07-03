"""
Q5. Clone a graph: deep copy of a connected undirected graph.
    Use a hash map to track visited/cloned nodes.

Answer:
    BFS or DFS. Use a hashmap: original_node → cloned_node.
    For each node, create a clone. For each neighbor, clone if not yet
    cloned, then add the cloned neighbor to the cloned node's list.

    Time: O(V + E), Space: O(V).
"""

from collections import deque


class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node({self.val})"


def clone_graph_bfs(node):
    """
    Clone graph using BFS + hashmap.
    Time: O(V + E), Space: O(V).
    """
    if not node:
        return None

    cloned = {node: GraphNode(node.val)}
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in cloned:
                cloned[neighbor] = GraphNode(neighbor.val)
                queue.append(neighbor)
            cloned[curr].neighbors.append(cloned[neighbor])

    return cloned[node]


def clone_graph_dfs(node, cloned=None):
    """Clone graph using DFS + hashmap."""
    if not node:
        return None
    if cloned is None:
        cloned = {}

    if node in cloned:
        return cloned[node]

    clone = GraphNode(node.val)
    cloned[node] = clone

    for neighbor in node.neighbors:
        clone.neighbors.append(clone_graph_dfs(neighbor, cloned))

    return clone


def build_graph(adj_list):
    """Build graph from adjacency list [[neighbors of node 1], ...]."""
    if not adj_list:
        return None
    nodes = {i+1: GraphNode(i+1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        for nb in neighbors:
            nodes[i+1].neighbors.append(nodes[nb])
    return nodes[1]


def graph_to_adj(node):
    """Convert graph to adjacency list for display."""
    if not node:
        return {}
    visited = {}
    queue = deque([node])
    visited[node.val] = node

    while queue:
        curr = queue.popleft()
        for nb in curr.neighbors:
            if nb.val not in visited:
                visited[nb.val] = nb
                queue.append(nb)

    return {v: [n.val for n in visited[v].neighbors] for v in sorted(visited)}


def demonstrate():
    print("=" * 70)
    print("Q5: Clone a Graph — Deep Copy")
    print("=" * 70)
    print()

    # Build: 1--2, 1--4, 2--3, 3--4
    adj = [[2,4], [1,3], [2,4], [1,3]]
    original = build_graph(adj)

    print("  Original graph:")
    print("    1 — 2")
    print("    |   |")
    print("    4 — 3")
    print()
    print(f"  Adjacency: {graph_to_adj(original)}")
    print()

    # Clone
    cloned_bfs = clone_graph_bfs(original)
    cloned_dfs = clone_graph_dfs(original)

    print(f"  Cloned (BFS): {graph_to_adj(cloned_bfs)}")
    print(f"  Cloned (DFS): {graph_to_adj(cloned_dfs)}")
    print()

    # Verify deep copy (different objects)
    print("--- Verify Deep Copy ---")
    print(f"  original node 1 is cloned node 1? {original is cloned_bfs}")
    print(f"  Same values? {graph_to_adj(original) == graph_to_adj(cloned_bfs)} ✓")
    print(f"  Different objects? {original is not cloned_bfs} ✓")
    print()

    # --- How it works ---
    print("--- Algorithm (BFS) ---")
    print()
    print("  1. Create clone of start node, add to hashmap")
    print("  2. BFS: for each node, clone unvisited neighbors")
    print("  3. Connect cloned node to cloned neighbors")
    print()
    print("  HashMap: {original_node → cloned_node}")
    print("  Prevents re-cloning and handles cycles!")
    print()

    # Trace
    print("--- Trace ---")
    print()
    node = build_graph(adj)
    cloned_map = {node: GraphNode(node.val)}
    q = deque([node])
    step = 0

    print(f"  {'Step':>4} | {'Process':>8} | {'Clone neighbors':>20} | {'Map size'}")
    print(f"  {'-'*4} | {'-'*8} | {'-'*20} | {'-'*8}")

    while q:
        step += 1
        curr = q.popleft()
        new_nbs = []
        for nb in curr.neighbors:
            if nb not in cloned_map:
                cloned_map[nb] = GraphNode(nb.val)
                q.append(nb)
                new_nbs.append(nb.val)
            cloned_map[curr].neighbors.append(cloned_map[nb])
        nb_str = str(new_nbs) if new_nbs else "all visited"
        print(f"  {step:>4} | Node {curr.val:>3} | {nb_str:>20} | {len(cloned_map)}")

    print()
    print("  Time: O(V + E) | Space: O(V) for the hashmap")


if __name__ == "__main__":
    demonstrate()
