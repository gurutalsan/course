"""
Q4. Using Python's heapq, find the kth largest element in an unsorted array.
    Explain why a min-heap of size k works.

Answer:
    Maintain a MIN-HEAP of size k. The heap's root (smallest of the k
    elements) is the kth largest overall.

    Why? The heap always holds the k largest elements seen so far.
    The smallest among those k elements = the kth largest.

    Time:  O(n log k) — each insert/pop is O(log k), done n times.
    Space: O(k) — heap holds exactly k elements.
"""

import heapq


def kth_largest_heap(nums: list, k: int) -> int:
    """
    Find kth largest using a min-heap of size k.

    Strategy:
    1. Push first k elements into min-heap.
    2. For remaining elements: if element > heap root, replace root.
    3. Heap root = kth largest.

    Time:  O(n log k)
    Space: O(k)
    """
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # Remove smallest, keeping k largest

    return heap[0]  # Root = smallest of k largest = kth largest


def kth_largest_sort(nums: list, k: int) -> int:
    """Comparison: sorting approach O(n log n)."""
    return sorted(nums, reverse=True)[k - 1]


def kth_largest_quickselect(nums: list, k: int) -> int:
    """Comparison: quickselect O(n) average."""
    import random
    target = len(nums) - k

    def quickselect(left, right):
        pivot_idx = random.randint(left, right)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        pivot = nums[right]
        store = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]
        if store == target:
            return nums[store]
        elif store < target:
            return quickselect(store + 1, right)
        else:
            return quickselect(left, store - 1)

    return quickselect(0, len(nums) - 1)


def demonstrate():
    print("=" * 70)
    print("Q4: Kth Largest Element Using Min-Heap")
    print("=" * 70)
    print()

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"  Array: {nums},  k = {k}")
    print(f"  Sorted descending: {sorted(nums, reverse=True)}")
    print(f"  kth largest = {kth_largest_heap(nums, k)}")
    print()

    # --- Why min-heap of size k works ---
    print("--- Why a Min-Heap of Size k Works ---")
    print()
    print("  The heap holds the k LARGEST elements seen so far.")
    print("  The ROOT of a min-heap is the SMALLEST in the heap.")
    print("  So the root = smallest of the k largest = kth largest!")
    print()
    print("  Visual (k=3, processing [3,2,1,5,6,4]):")
    print()

    heap = []
    print(f"  {'Step':>4} | {'Num':>4} | {'Action':>25} | {'Heap':>15} | {'Root (kth)'}")
    print(f"  {'-'*4} | {'-'*4} | {'-'*25} | {'-'*15} | {'-'*10}")

    for i, num in enumerate([3, 2, 1, 5, 6, 4]):
        heapq.heappush(heap, num)
        if len(heap) > 3:
            popped = heapq.heappop(heap)
            action = f"Push {num}, pop {popped}"
        else:
            action = f"Push {num}"
        root = heap[0] if heap else "—"
        print(f"  {i+1:>4} | {num:>4} | {action:>25} | {str(sorted(heap)):>15} | {root}")

    print()
    print(f"  Final heap: {sorted(heap)} → root = {heap[0]} = 3rd largest ✓")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---\n")
    tests = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([7, 6, 5, 4, 3, 2, 1], 3, 5),
        ([1, 2, 3, 4, 5, 6, 7], 1, 7),
        ([3, 2, 1, 5, 6, 4], 6, 1),
    ]

    for nums, k, expected in tests:
        got = kth_largest_heap(nums, k)
        status = "✓" if got == expected else "✗"
        print(f"  nums={nums}, k={k} → {got} (expected {expected}) {status}")

    print()

    # --- Comparison ---
    print("--- Method Comparison ---")
    print()
    print("  Method        | Time       | Space | Best when")
    print("  --------------|------------|-------|--------------------")
    print("  Sort           | O(n log n)| O(n)  | Simple, one-off")
    print("  Min-heap ★     | O(n log k)| O(k)  | k << n, streaming")
    print("  Quickselect    | O(n) avg  | O(1)  | Single query, avg case")
    print()
    print("  Heap advantage: works for STREAMING data (don't need all data upfront)")
    print("  and uses only O(k) memory!")


if __name__ == "__main__":
    demonstrate()
