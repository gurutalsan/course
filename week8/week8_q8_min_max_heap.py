"""
Q8. Explain min-heap vs max-heap. Why does Python's heapq only provide
    min-heap? How do you simulate a max-heap?

Answer:
    Min-heap: parent ≤ children. Root = minimum. heappop gives smallest.
    Max-heap: parent ≥ children. Root = maximum. heappop gives largest.

    Python only provides min-heap because:
    1. Simplicity — one implementation covers both (negate values for max-heap).
    2. Min-heap is more commonly needed (Dijkstra, merge k sorted, etc.).

    Max-heap trick: NEGATE values before push, negate again after pop.
    heappush(heap, -val)  →  val = -heappop(heap)
"""

import heapq


def demonstrate():
    print("=" * 70)
    print("Q8: Min-Heap vs Max-Heap — Python's heapq")
    print("=" * 70)
    print()

    # --- Definitions ---
    print("--- Definitions ---")
    print()
    print("  MIN-HEAP: Parent ≤ Children        MAX-HEAP: Parent ≥ Children")
    print()
    print("       1  (min at root)                   9  (max at root)")
    print("      / \\                                / \\")
    print("     3   5                              7   8")
    print("    / \\                                / \\")
    print("   7   9                              3   5")
    print()
    print("  heappop → 1 (smallest)             heappop → 9 (largest)")
    print()

    # --- Min-Heap Demo ---
    print("--- Min-Heap (Python's heapq) ---")
    print()

    min_heap = []
    values = [5, 3, 8, 1, 9, 2, 7]
    print(f"  Inserting: {values}")
    print()

    for v in values:
        heapq.heappush(min_heap, v)
        print(f"  push({v}): heap = {min_heap}")

    print()
    print("  Popping (always gives smallest):")
    order = []
    while min_heap:
        val = heapq.heappop(min_heap)
        order.append(val)
        print(f"  pop → {val}")
    print(f"  Order: {order} (ascending ✓)")
    print()

    # --- Max-Heap Simulation ---
    print("--- Max-Heap Simulation (NEGATE trick) ---")
    print()
    print("  Python has NO built-in max-heap.")
    print("  Trick: push(-val), pop and negate → -heappop()")
    print()

    max_heap = []
    print(f"  Inserting: {values}")
    print()

    for v in values:
        heapq.heappush(max_heap, -v)  # Negate!
        display = [-x for x in sorted(max_heap)]
        print(f"  push(-{v}): internal={max_heap}, logical={display}")

    print()
    print("  Popping (gives largest due to negation):")
    order2 = []
    while max_heap:
        val = -heapq.heappop(max_heap)  # Negate back!
        order2.append(val)
        print(f"  -pop → {val}")
    print(f"  Order: {order2} (descending ✓)")
    print()

    # --- Comparison ---
    print("--- Comparison Table ---")
    print()
    print("  Property      | Min-Heap         | Max-Heap")
    print("  --------------|------------------|------------------")
    print("  Parent rule   | parent ≤ children| parent ≥ children")
    print("  Root          | Minimum element  | Maximum element")
    print("  heappop       | Returns smallest | Returns largest")
    print("  Python        | heapq (native)   | Negate values")
    print("  Use case      | Kth largest,     | Kth smallest,")
    print("                | Dijkstra, merge k| median (left half)")
    print()

    # --- Common Operations ---
    print("--- heapq Operations ---")
    print()
    print("  import heapq")
    print()
    print("  # Min-heap (default)")
    print("  heapq.heappush(heap, val)       # Push O(log n)")
    print("  heapq.heappop(heap)             # Pop min O(log n)")
    print("  heap[0]                          # Peek min O(1)")
    print("  heapq.heapify(list)             # Build heap O(n)")
    print("  heapq.nsmallest(k, iterable)    # K smallest O(n log k)")
    print("  heapq.nlargest(k, iterable)     # K largest O(n log k)")
    print()
    print("  # Max-heap (negation trick)")
    print("  heapq.heappush(heap, -val)      # Push negated")
    print("  -heapq.heappop(heap)            # Pop and negate back")
    print("  -heap[0]                         # Peek max")
    print()

    # --- Why only min-heap? ---
    print("--- Why Python Only Provides Min-Heap ---")
    print()
    print("  1. SIMPLICITY: One implementation, negate for max-heap")
    print("  2. CONVENTION: Min-heap is more common in algorithms:")
    print("     - Dijkstra's shortest path")
    print("     - Merge k sorted lists")
    print("     - Task scheduling (lowest priority first)")
    print("  3. FLEXIBILITY: Tuples work naturally for (priority, value)")
    print()

    # --- Practical examples ---
    print("--- Practical Examples ---")
    print()

    # Priority queue
    print("  1. Priority Queue (min-heap):")
    pq = []
    tasks = [(3, "Low"), (1, "Critical"), (2, "Medium")]
    for priority, task in tasks:
        heapq.heappush(pq, (priority, task))
    print(f"     Tasks: {tasks}")
    while pq:
        p, t = heapq.heappop(pq)
        print(f"     Process: priority={p}, task='{t}'")
    print()

    # Top 3 largest
    print("  2. Find top 3 largest from stream:")
    data = [10, 4, 3, 8, 2, 7, 1, 9, 5, 6]
    top3 = heapq.nlargest(3, data)
    print(f"     Data: {data}")
    print(f"     Top 3: {top3}")
    print()

    # Heap sort
    print("  3. Heap sort (ascending):")
    arr = [5, 3, 8, 1, 9]
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    print(f"     Sorted: {sorted_arr}")
    print()

    print("  Time complexities:")
    print("    push:    O(log n)")
    print("    pop:     O(log n)")
    print("    peek:    O(1)")
    print("    heapify: O(n)")
    print()
    print("ANSWER: Min-heap has smallest at root, max-heap has largest.")
    print("Python's heapq is min-heap only; negate values to simulate max-heap.")


if __name__ == "__main__":
    demonstrate()
