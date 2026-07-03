"""
Q3. Course Schedule: Can you finish all courses given prerequisites?
    Explain how this is a cycle detection problem.

Answer:
    Model as a DIRECTED GRAPH: prerequisite [a,b] means b→a (take b before a).
    If the graph has a CYCLE → impossible to finish all courses.
    If NO cycle → courses can be completed.

    Use DFS with 3 states:
    - UNVISITED (0): not yet explored
    - VISITING (1): currently in DFS stack (being explored)
    - VISITED (2): fully explored, no cycle from this node

    If we visit a VISITING node → CYCLE detected!

    Time: O(V + E), Space: O(V + E)
"""

from collections import defaultdict


def can_finish(num_courses: int, prerequisites: list) -> bool:
    """
    Determine if all courses can be completed (no cycles).
    DFS with 3 states for cycle detection.
    Time: O(V + E), Space: O(V + E).
    """
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    UNVISITED, VISITING, VISITED = 0, 1, 2
    state = [UNVISITED] * num_courses

    def has_cycle(node):
        if state[node] == VISITING:
            return True   # Back edge → cycle!
        if state[node] == VISITED:
            return False  # Already fully explored

        state[node] = VISITING
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True

        state[node] = VISITED
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False

    return True


def demonstrate():
    print("=" * 70)
    print("Q3: Course Schedule — Cycle Detection")
    print("=" * 70)
    print()

    # --- Why it's cycle detection ---
    print("--- Why This Is a Cycle Detection Problem ---")
    print()
    print("  Prerequisites form a DIRECTED GRAPH:")
    print("    [1,0] means 'take 0 before 1' → edge 0→1")
    print()
    print("  If there's a CYCLE: A requires B, B requires C, C requires A")
    print("  → impossible! You can never start.")
    print()
    print("  No cycle → valid topological ordering exists → can finish all.")
    print()

    # --- Example 1: Can finish ---
    print("--- Example 1: Can Finish ---")
    print()
    print("  2 courses, prerequisites: [[1,0]]")
    print("    0 → 1  (take 0 before 1)")
    print("    Order: 0, 1 ✓")
    print(f"  Result: {can_finish(2, [[1,0]])} ✓")
    print()

    # --- Example 2: Cannot finish ---
    print("--- Example 2: Cannot Finish (Cycle!) ---")
    print()
    print("  2 courses, prerequisites: [[1,0],[0,1]]")
    print("    0 → 1 and 1 → 0  ← CYCLE!")
    print("    0 needs 1, but 1 needs 0 → deadlock!")
    print(f"  Result: {can_finish(2, [[1,0],[0,1]])} ✓")
    print()

    # --- 3-state DFS explanation ---
    print("--- Three-State DFS ---")
    print()
    print("  State 0 (UNVISITED): Haven't started exploring")
    print("  State 1 (VISITING):  Currently in DFS path (on the stack)")
    print("  State 2 (VISITED):   Fully explored, safe")
    print()
    print("  If we reach a VISITING node → we found a BACK EDGE → CYCLE!")
    print()
    print("  Trace for [[1,0],[0,1]] (has cycle):")
    print("    Start DFS at 0: state[0] = VISITING")
    print("    Visit neighbor 1: state[1] = VISITING")
    print("    Visit neighbor 0: state[0] = VISITING ← BACK EDGE! CYCLE!")
    print()

    # --- Larger example ---
    print("--- Example 3: Larger Graph ---")
    print()
    print("  4 courses, prereqs: [[1,0],[2,0],[3,1],[3,2]]")
    print()
    print("    0 → 1 → 3")
    print("    0 → 2 → 3")
    print("    (No cycle → can finish)")

    prereqs = [[1,0],[2,0],[3,1],[3,2]]
    print(f"\n  Result: {can_finish(4, prereqs)} (expected True) ✓")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---\n")
    tests = [
        (2, [[1,0]], True, "Simple chain"),
        (2, [[1,0],[0,1]], False, "Simple cycle"),
        (4, [[1,0],[2,0],[3,1],[3,2]], True, "Diamond (no cycle)"),
        (3, [[0,1],[1,2],[2,0]], False, "3-node cycle"),
        (1, [], True, "Single course"),
        (5, [[1,0],[2,1],[3,2],[4,3]], True, "Long chain"),
        (4, [[1,0],[2,1],[0,2],[3,2]], False, "Cycle in chain"),
    ]

    for n, prereqs, expected, desc in tests:
        got = can_finish(n, prereqs)
        status = "✓" if got == expected else "✗"
        print(f"  {desc:>20}: n={n}, prereqs={prereqs}")
        print(f"  {'':>20}  → {got} (expected {expected}) {status}")

    print()
    print("  Time: O(V + E) | Space: O(V + E)")
    print("  ANSWER: Cycle in prerequisite graph = impossible to finish.")


if __name__ == "__main__":
    demonstrate()
