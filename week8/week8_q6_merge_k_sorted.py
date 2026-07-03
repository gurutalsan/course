"""
Q6. Merge k sorted lists into one sorted list using a heap.
    Time complexity in terms of n (total elements) and k (number of lists)?

Answer:
    Use a MIN-HEAP of size k. Push the first element from each list.
    Pop the smallest, add to result, push the next element from that list.

    Time:  O(n log k) — each of n elements is pushed/popped from a k-sized heap.
    Space: O(k) for the heap + O(n) for the result.
"""

import heapq


def merge_k_sorted(lists: list) -> list:
    """
    Merge k sorted lists using a min-heap.

    Heap holds (value, list_index, element_index) tuples.
    Always pop the global minimum, then push the next from that list.

    Time:  O(n log k) — n total elements, heap of size k.
    Space: O(k) heap + O(n) result.
    """
    heap = []
    result = []

    # Initialize: push first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Push next element from the same list
        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][next_idx], list_idx, next_idx))

    return result


def merge_k_sorted_brute(lists: list) -> list:
    """Brute force: concatenate and sort. O(n log n)."""
    all_elements = []
    for lst in lists:
        all_elements.extend(lst)
    return sorted(all_elements)


def demonstrate():
    print("=" * 70)
    print("Q6: Merge K Sorted Lists Using a Heap")
    print("=" * 70)
    print()

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print(f"  Input: {lists}")
    result = merge_k_sorted(lists)
    print(f"  Merged: {result}")
    print()

    # --- Step-by-step ---
    print("--- Step-by-Step Trace ---")
    print()
    print(f"  List 0: {lists[0]}")
    print(f"  List 1: {lists[1]}")
    print(f"  List 2: {lists[2]}")
    print()

    heap = []
    res = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    print(f"  {'Step':>4} | {'Pop':>5} | {'From':>6} | {'Push Next':>12} | {'Heap':>20} | {'Result'}")
    print(f"  {'-'*4} | {'-'*5} | {'-'*6} | {'-'*12} | {'-'*20} | {'-'*25}")

    step = 0
    h_display = [(v, f"L{li}") for v, li, _ in sorted(heap)]
    print(f"  {'init':>4} | {'—':>5} | {'—':>6} | {'—':>12} | {str(h_display):>20} | {res}")

    heap2 = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap2, (lst[0], i, 0))

    while heap2:
        step += 1
        val, li, ei = heapq.heappop(heap2)
        res.append(val)

        push_str = "—"
        ni = ei + 1
        if ni < len(lists[li]):
            heapq.heappush(heap2, (lists[li][ni], li, ni))
            push_str = f"{lists[li][ni]} (L{li})"

        h_display = [(v, f"L{l}") for v, l, _ in sorted(heap2)]
        print(f"  {step:>4} | {val:>5} | {'L'+str(li):>6} | {push_str:>12} | {str(h_display):>20} | {res}")

    print()

    # --- Why O(n log k)? ---
    print("--- Why O(n log k)? ---")
    print()
    print("  • Heap always has AT MOST k elements (one per list)")
    print("  • Each push/pop on a k-sized heap = O(log k)")
    print("  • Total elements processed = n")
    print("  • Total operations = n × O(log k) = O(n log k)")
    print()
    print("  Compare: brute force sort = O(n log n)")
    print("  When k << n: O(n log k) << O(n log n)  ★ much faster!")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---\n")
    tests = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([[]], []),
        ([], []),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]], list(range(1, 13))),
    ]

    for lsts, expected in tests:
        got = merge_k_sorted(lsts)
        brute = merge_k_sorted_brute(lsts)
        ok = got == expected == brute
        print(f"  {str(lsts):>40} → {got}  {'✓' if ok else '✗'}")

    print()
    print("  Time: O(n log k) | Space: O(k) heap + O(n) result")
    print("  n = total elements across all lists, k = number of lists")


if __name__ == "__main__":
    demonstrate()
