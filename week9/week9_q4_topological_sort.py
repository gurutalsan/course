"""
Q4. Topological sort using Kahn's algorithm (BFS with in-degree).
    Find valid ordering for: 4 courses, prereqs [[1,0],[2,0],[3,1],[3,2]].

Answer:
    Kahn's Algorithm:
    1. Compute in-degree for all nodes.
    2. Add all nodes with in-degree 0 to a queue.
    3. Pop from queue, add to result, decrease neighbors' in-degrees.
    4. If neighbor's in-degree becomes 0, add to queue.
    5. If result has all nodes → valid ordering. Else → cycle exists.

    Time: O(V + E), Space: O(V + E).
"""

from collections import defaultdict, deque


def topological_sort(num_courses: int, prerequisites: list) -> list:
    """
    Kahn's algorithm: BFS-based topological sort.
    Returns valid course ordering, or empty list if cycle exists.
    """
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Start with nodes that have no prerequisites
    queue = deque()
    for i in range(num_courses):
        if in_degree[i] == 0:
            queue.append(i)

    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all courses included → valid ordering
    return order if len(order) == num_courses else []


def demonstrate():
    print("=" * 70)
    print("Q4: Topological Sort — Kahn's Algorithm")
    print("=" * 70)
    print()

    prereqs = [[1,0],[2,0],[3,1],[3,2]]

    print("  4 courses, prerequisites:", prereqs)
    print()
    print("    0 → 1 → 3")
    print("    0 → 2 → 3")
    print()

    # --- Step-by-step trace ---
    print("--- Step-by-Step Trace ---")
    print()

    graph = defaultdict(list)
    in_deg = [0] * 4
    for c, p in prereqs:
        graph[p].append(c)
        in_deg[c] += 1

    print(f"  In-degrees: {in_deg}")
    print(f"  Nodes with in-degree 0: {[i for i,d in enumerate(in_deg) if d==0]}")
    print()

    queue = deque([i for i,d in enumerate(in_deg) if d==0])
    order = []

    print(f"  {'Step':>4} | {'Process':>7} | {'Reduce':>15} | {'In-degree':>15} | {'Queue':>10} | {'Order'}")
    print(f"  {'-'*4} | {'-'*7} | {'-'*15} | {'-'*15} | {'-'*10} | {'-'*15}")

    step = 0
    while queue:
        step += 1
        node = queue.popleft()
        order.append(node)
        reduced = []
        for nb in graph[node]:
            in_deg[nb] -= 1
            reduced.append(f"{nb}→{in_deg[nb]}")
            if in_deg[nb] == 0:
                queue.append(nb)
        red_str = ", ".join(reduced) if reduced else "—"
        print(f"  {step:>4} | {node:>7} | {red_str:>15} | {str(in_deg):>15} | {str(list(queue)):>10} | {order}")

    print()
    print(f"  Result: {order}")
    print(f"  Valid: {len(order) == 4} ✓")
    print()

    # --- How Kahn's works ---
    print("--- Kahn's Algorithm Summary ---")
    print()
    print("  1. Compute in-degree (number of incoming edges) for each node")
    print("  2. Enqueue all nodes with in-degree = 0 (no prerequisites)")
    print("  3. While queue not empty:")
    print("     a. Dequeue node → add to result")
    print("     b. For each neighbor: decrease in-degree by 1")
    print("     c. If neighbor's in-degree = 0 → enqueue it")
    print("  4. If result has all nodes → valid topological order")
    print("     If not → cycle exists (some nodes never reached in-degree 0)")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---\n")
    tests = [
        (4, [[1,0],[2,0],[3,1],[3,2]], True, "Diamond"),
        (2, [[1,0],[0,1]], False, "Cycle"),
        (2, [[1,0]], True, "Simple"),
        (1, [], True, "Single"),
        (6, [[1,0],[2,1],[3,1],[4,2],[4,3],[5,4]], True, "Complex DAG"),
    ]

    for n, prereqs, should_work, desc in tests:
        result = topological_sort(n, prereqs)
        has_order = len(result) == n
        status = "✓" if has_order == should_work else "✗"
        print(f"  {desc:>15}: n={n} → {result if result else 'CYCLE!'} {status}")

    print()
    print("  Time: O(V + E) | Space: O(V + E)")


if __name__ == "__main__":
    demonstrate()
