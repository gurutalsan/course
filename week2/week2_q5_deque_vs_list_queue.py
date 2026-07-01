"""
Q5. Why is deque preferred over list for implementing a queue?
    What specific operation makes the difference?

Answer:
    deque (double-ended queue) is preferred because it supports O(1)
    operations at BOTH ends, while list has O(n) for left-side operations.

    The specific operation that makes the difference:
        ★ Removing from the front (popleft / pop(0)) ★

    - list.pop(0):       O(n) — must shift ALL remaining elements left by one.
    - deque.popleft():   O(1) — directly removes from the front, no shifting.

    For a queue (FIFO: First-In, First-Out):
        Enqueue (add to back):    list.append() = O(1)  ≈ deque.append() = O(1)
        Dequeue (remove from front): list.pop(0) = O(n) ≪ deque.popleft() = O(1)
                                                     ↑ THIS is the bottleneck!
"""

from collections import deque
import time


# ============================================================
# Queue using List (SLOW dequeue)
# ============================================================
class ListQueue:
    """Queue implementation using a list — O(n) dequeue."""

    def __init__(self):
        self._data = []

    def enqueue(self, item):
        """Add to the back — O(1)."""
        self._data.append(item)

    def dequeue(self):
        """Remove from the front — O(n)! Must shift all elements."""
        if not self._data:
            raise IndexError("Queue is empty")
        return self._data.pop(0)  # ← O(n) operation!

    def peek(self):
        if not self._data:
            raise IndexError("Queue is empty")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"ListQueue({self._data})"


# ============================================================
# Queue using Deque (FAST dequeue) ★ PREFERRED ★
# ============================================================
class DequeQueue:
    """Queue implementation using deque — O(1) dequeue."""

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """Add to the back — O(1)."""
        self._data.append(item)

    def dequeue(self):
        """Remove from the front — O(1)! No shifting needed."""
        if not self._data:
            raise IndexError("Queue is empty")
        return self._data.popleft()  # ← O(1) operation!

    def peek(self):
        if not self._data:
            raise IndexError("Queue is empty")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"DequeQueue({list(self._data)})"


def demonstrate():
    print("=" * 70)
    print("Q5: Why Deque Is Preferred Over List for Queues")
    print("=" * 70)
    print()

    # --- The Problem with Lists ---
    print("--- The Problem: list.pop(0) is O(n) ---")
    print()
    print("  Queue = FIFO (First-In, First-Out)")
    print("  Two operations: enqueue (add back) + dequeue (remove front)")
    print()
    print("  Using a list:")
    print()
    print("    Before pop(0):  [A, B, C, D, E]    ← 'A' is at front")
    print("                     ↑ remove this")
    print()
    print("    After pop(0):   [B, C, D, E]")
    print("                     ↑  ↑  ↑  ↑")
    print("                     ALL elements shift left by 1 → O(n)!")
    print()
    print("  Using a deque:")
    print()
    print("    Before popleft(): A ↔ B ↔ C ↔ D ↔ E   (doubly-linked)")
    print("                      ↑ remove this")
    print()
    print("    After popleft():  B ↔ C ↔ D ↔ E")
    print("                      ↑ just update pointer → O(1)!")
    print()

    # --- Operation Comparison ---
    print("--- Operation Complexity Comparison ---")
    print()
    print("  Operation         | list          | deque         | Winner")
    print("  ------------------|---------------|---------------|---------")
    print("  Append (right)    | O(1)          | O(1)          | Tie")
    print("  Pop (right)       | O(1)          | O(1)          | Tie")
    print("  ★ Pop (left)      | O(n) ← SLOW  | O(1) ← FAST  | deque ★")
    print("  ★ Insert (left)   | O(n) ← SLOW  | O(1) ← FAST  | deque ★")
    print("  Access by index   | O(1) ← FAST  | O(n) ← SLOW  | list")
    print("  Slice             | O(k)          | Not supported | list")
    print()
    print("  ★ = Critical for queue operations")
    print()

    # --- Functional Demo ---
    print("--- Queue Operations Demo ---")
    print()

    q_list = ListQueue()
    q_deque = DequeQueue()

    operations = [
        ("enqueue", "Alice"),
        ("enqueue", "Bob"),
        ("enqueue", "Charlie"),
        ("dequeue", None),
        ("enqueue", "Diana"),
        ("dequeue", None),
    ]

    print("  Step  | Operation          | ListQueue                | DequeQueue")
    print("  ------|--------------------|--------------------------|--------------------------")

    for op, val in operations:
        if op == "enqueue":
            q_list.enqueue(val)
            q_deque.enqueue(val)
            print(f"  {op:>5}  | enqueue('{val}')   | {str(q_list):>24} | {str(q_deque):>24}")
        else:
            result_list = q_list.dequeue()
            result_deque = q_deque.dequeue()
            print(f"  {op:>5}  | dequeue() → '{result_list}'  | {str(q_list):>24} | {str(q_deque):>24}")

    print()

    # --- Performance Benchmarks ---
    print("--- Performance Benchmark: Enqueue + Dequeue n Items ---")
    print()
    print(f"  {'n':>8}  |  {'list.pop(0)':>14}  |  {'deque.popleft()':>16}  |  {'Speedup':>8}")
    print(f"  {'-'*8}  |  {'-'*14}  |  {'-'*16}  |  {'-'*8}")

    for n in [1_000, 5_000, 10_000, 50_000, 100_000]:
        # List-based queue
        q = []
        for i in range(n):
            q.append(i)

        start = time.perf_counter()
        while q:
            q.pop(0)
        list_time = (time.perf_counter() - start) * 1000

        # Deque-based queue
        q = deque()
        for i in range(n):
            q.append(i)

        start = time.perf_counter()
        while q:
            q.popleft()
        deque_time = (time.perf_counter() - start) * 1000

        speedup = list_time / deque_time if deque_time > 0 else 0

        print(
            f"  {n:>8,}  |  "
            f"{list_time:>11.3f} ms  |  "
            f"{deque_time:>13.3f} ms  |  "
            f"{speedup:>7.0f}x"
        )

    print()

    # --- Visual: Why shifting is expensive ---
    print("--- Visual: Why list.pop(0) Is Expensive ---")
    print()
    print("  list = [10, 20, 30, 40, 50]    (5 elements)")
    print()
    print("  pop(0) removes 10:")
    print("    Memory: [10] [20] [30] [40] [50]")
    print("             ×    ←    ←    ←    ←     ← shift 4 elements")
    print("    Result: [20] [30] [40] [50]")
    print()
    print("  For n elements → n-1 shifts → O(n)")
    print()
    print("  deque uses a DOUBLY-LINKED LIST internally:")
    print("    head → [10] ↔ [20] ↔ [30] ↔ [40] ↔ [50] ← tail")
    print()
    print("  popleft() removes 10:")
    print("    Just update: head → [20] ↔ [30] ↔ [40] ↔ [50] ← tail")
    print("    No shifting! → O(1)")
    print()

    # --- When to use each ---
    print("--- When to Use Each ---")
    print()
    print("  Use list when:")
    print("    • You need random access by index: arr[i]")
    print("    • You mainly add/remove from the END (stack behavior)")
    print("    • You need slicing: arr[2:5]")
    print()
    print("  Use deque when:")
    print("    • You need a QUEUE (FIFO): add back, remove front")
    print("    • You need a DOUBLE-ENDED QUEUE: add/remove from both ends")
    print("    • You need a SLIDING WINDOW (maxlen parameter)")
    print()

    # --- Bonus: deque with maxlen ---
    print("--- Bonus: deque with maxlen (Sliding Window) ---")
    print()
    window = deque(maxlen=3)
    print(f"  window = deque(maxlen=3)")
    for val in [1, 2, 3, 4, 5]:
        window.append(val)
        print(f"  append({val}) → {list(window)}")

    print()
    print("  deque automatically drops the oldest element when full!")
    print()

    print("ANSWER:")
    print("  deque is preferred because deque.popleft() is O(1),")
    print("  while list.pop(0) is O(n) due to element shifting.")
    print("  This makes deque dramatically faster for queue operations.")


if __name__ == "__main__":
    demonstrate()
