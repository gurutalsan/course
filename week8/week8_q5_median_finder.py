"""
Q5. Implement a MedianFinder class using two heaps (max-heap + min-heap).
    Supports addNum(num) and findMedian(). Explain balancing logic.

Answer:
    Split numbers into two halves:
    - max_heap: stores the SMALLER half (top = largest of small half)
    - min_heap: stores the LARGER half  (top = smallest of large half)

    Balancing rule: max_heap can have at most 1 more element than min_heap.
    Median = max_heap top (if odd) or average of both tops (if even).

    addNum:  O(log n) — heap push/pop.
    findMedian: O(1) — peek at heap tops.
"""

import heapq


class MedianFinder:
    """
    Find median from a data stream using two heaps.

    max_heap (negated): smaller half, top = max of smaller half
    min_heap:           larger half,  top = min of larger half

    Invariant: len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1

    addNum:     O(log n)
    findMedian: O(1)
    """

    def __init__(self):
        self.max_heap = []  # Stores negated values (Python only has min-heap)
        self.min_heap = []

    def addNum(self, num: int) -> None:
        """Add a number while maintaining the two-heap balance."""
        # Step 1: Push to max_heap (negate for max-heap behavior)
        heapq.heappush(self.max_heap, -num)

        # Step 2: Ensure max_heap's top ≤ min_heap's top
        if self.min_heap and (-self.max_heap[0]) > self.min_heap[0]:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # Step 3: Balance sizes (max_heap can be at most 1 larger)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        """Return the current median. O(1)."""
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0

    def _state(self):
        """Show internal state for debugging."""
        max_vals = sorted([-x for x in self.max_heap])
        min_vals = sorted(self.min_heap)
        return max_vals, min_vals


def demonstrate():
    print("=" * 70)
    print("Q5: MedianFinder — Two Heaps")
    print("=" * 70)
    print()

    # --- How it works ---
    print("--- Two-Heap Design ---")
    print()
    print("  max_heap (smaller half)     min_heap (larger half)")
    print("  ┌─────────────────┐         ┌─────────────────┐")
    print("  │  1, 2, [3] ←top │         │ [4]→ top, 5, 6  │")
    print("  └─────────────────┘         └─────────────────┘")
    print("           ↑                            ↑")
    print("    max of small half            min of large half")
    print()
    print("  Odd count:  median = max_heap top")
    print("  Even count: median = (max_heap top + min_heap top) / 2")
    print()

    # --- Step-by-step ---
    print("--- Step-by-Step: Adding [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0] ---")
    print()

    mf = MedianFinder()
    numbers = [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0]

    print(f"  {'Add':>4} | {'max_heap (small)':>20} | {'min_heap (large)':>20} | {'Median':>7}")
    print(f"  {'-'*4} | {'-'*20} | {'-'*20} | {'-'*7}")

    for num in numbers:
        mf.addNum(num)
        small, large = mf._state()
        median = mf.findMedian()
        print(f"  {num:>4} | {str(small):>20} | {str(large):>20} | {median:>7.1f}")

    print()

    # --- Balancing Logic ---
    print("--- Balancing Logic ---")
    print()
    print("  After adding each number:")
    print("    1. Push to max_heap first")
    print("    2. If max_heap top > min_heap top → move it to min_heap")
    print("    3. If max_heap has 2+ more elements → move one to min_heap")
    print("    4. If min_heap has more elements → move one to max_heap")
    print()
    print("  This ensures:")
    print("    • max_heap top ≤ min_heap top (correct ordering)")
    print("    • |max_heap| = |min_heap| or |max_heap| = |min_heap| + 1")
    print()

    # --- LeetCode test ---
    print("--- LeetCode Test ---")
    print()
    mf2 = MedianFinder()
    ops = [
        ("addNum", 1, None), ("addNum", 2, None), ("findMedian", None, 1.5),
        ("addNum", 3, None), ("findMedian", None, 2.0),
    ]

    all_pass = True
    for op, val, expected in ops:
        if op == "addNum":
            mf2.addNum(val)
            print(f"  addNum({val})")
        else:
            result = mf2.findMedian()
            ok = abs(result - expected) < 1e-9
            if not ok: all_pass = False
            print(f"  findMedian() → {result} (expected {expected}) {'✓' if ok else '✗'}")

    print(f"\n  All passed: {'✓' if all_pass else '✗'}")
    print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Operation   | Time     | Space")
    print("  ------------|----------|------")
    print("  addNum(n)   | O(log n) | O(n) total")
    print("  findMedian()| O(1)     | —")
    print()
    print("  Why two heaps? Sorted array insert is O(n). Heaps give O(log n).")
    print("  Single heap can't efficiently track both halves simultaneously.")


if __name__ == "__main__":
    demonstrate()
