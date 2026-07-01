"""
Q3. Implement a Queue using two Stacks only. Explain the amortized
    time complexity of the dequeue operation.

Answer:
    Use two stacks: stack_in (for enqueue) and stack_out (for dequeue).

    Enqueue: Always push to stack_in → O(1).
    Dequeue: Pop from stack_out. If stack_out is empty, transfer ALL
             elements from stack_in to stack_out (reverses order!).

    Amortized Analysis:
    Each element is pushed at most TWICE (once to stack_in, once to
    stack_out) and popped at most TWICE. So across n operations,
    total work = O(n). Per operation = O(n)/n = O(1) amortized.

    Worst case single dequeue: O(n) (when transfer happens).
    Amortized per dequeue: O(1).
"""


class QueueWithTwoStacks:
    """
    Queue (FIFO) implemented using two stacks (LIFO).

    stack_in:  receives all enqueue operations.
    stack_out: serves all dequeue operations.

    When stack_out is empty and dequeue is called, we transfer
    ALL elements from stack_in to stack_out. This reversal
    converts LIFO order to FIFO order!

    Amortized Time:
        enqueue: O(1)
        dequeue: O(1) amortized (O(n) worst case for transfer)
    """

    def __init__(self):
        self.stack_in = []   # For enqueue
        self.stack_out = []  # For dequeue

    def enqueue(self, val) -> None:
        """Add element to back of queue. Always O(1)."""
        self.stack_in.append(val)

    def dequeue(self):
        """
        Remove element from front of queue.

        O(1) amortized:
        - If stack_out has elements: just pop → O(1)
        - If stack_out is empty: transfer all from stack_in → O(n)
          But each element is transferred at most once!
        """
        if not self.stack_out:
            if not self.stack_in:
                raise IndexError("Queue is empty")
            # Transfer ALL elements from stack_in to stack_out
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        """Look at front element without removing."""
        if not self.stack_out:
            if not self.stack_in:
                raise IndexError("Queue is empty")
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def is_empty(self) -> bool:
        return len(self.stack_in) == 0 and len(self.stack_out) == 0

    def __len__(self):
        return len(self.stack_in) + len(self.stack_out)

    def __repr__(self):
        return f"Queue(in={self.stack_in}, out={self.stack_out})"


def demonstrate():
    print("=" * 70)
    print("Q3: Queue Using Two Stacks")
    print("=" * 70)
    print()

    # --- The Problem ---
    print("--- The Challenge ---")
    print()
    print("  Stack = LIFO (Last In, First Out):  push/pop from TOP")
    print("  Queue = FIFO (First In, First Out):  enqueue BACK, dequeue FRONT")
    print()
    print("  How to get FIFO behavior from LIFO stacks?")
    print("  Answer: Use TWO stacks! Transferring reverses the order.")
    print()

    # --- How It Works ---
    print("--- How It Works ---")
    print()
    print("  stack_in:  receives enqueue (push) operations")
    print("  stack_out: serves dequeue (pop) operations")
    print()
    print("  Enqueue: push to stack_in (always)")
    print("  Dequeue: pop from stack_out")
    print("           If stack_out is empty → transfer all from stack_in")
    print()
    print("  The TRANSFER reverses the order!")
    print("  stack_in  (LIFO): [1, 2, 3]  (3 on top)")
    print("  After transfer:")
    print("  stack_out (LIFO): [3, 2, 1]  (1 on top → first in, first out!)")
    print()

    # --- Step-by-Step Demo ---
    print("=" * 70)
    print("STEP-BY-STEP DEMONSTRATION")
    print("=" * 70)
    print()

    q = QueueWithTwoStacks()

    operations = [
        ("enqueue", 1), ("enqueue", 2), ("enqueue", 3),
        ("dequeue", None), ("dequeue", None),
        ("enqueue", 4), ("enqueue", 5),
        ("dequeue", None), ("dequeue", None), ("dequeue", None),
    ]

    print(f"  {'Operation':>14} | {'stack_in':>15} | {'stack_out':>15} | {'Result':>8} | {'Note'}")
    print(f"  {'-'*14} | {'-'*15} | {'-'*15} | {'-'*8} | {'-'*25}")

    for op, val in operations:
        if op == "enqueue":
            q.enqueue(val)
            note = f"Push {val} to stack_in"
            print(f"  {'enqueue('+str(val)+')':>14} | {str(q.stack_in):>15} | {str(q.stack_out):>15} | {'—':>8} | {note}")
        else:
            # Check if transfer happens
            if not q.stack_out:
                note = "Transfer! Reverse order"
            else:
                note = "Pop from stack_out"
            result = q.dequeue()
            print(f"  {'dequeue()':>14} | {str(q.stack_in):>15} | {str(q.stack_out):>15} | {result:>8} | {note}")

    print()

    # --- Visual: The Transfer ---
    print("--- Visual: The Transfer (Key Insight) ---")
    print()
    print("  After enqueue(1), enqueue(2), enqueue(3):")
    print()
    print("    stack_in          stack_out")
    print("    ┌───┐             ┌───┐")
    print("    │ 3 │ ← top      │   │ empty")
    print("    │ 2 │             │   │")
    print("    │ 1 │             │   │")
    print("    └───┘             └───┘")
    print()
    print("  dequeue() → stack_out is empty → TRANSFER!")
    print()
    print("    Pop 3 from stack_in, push to stack_out")
    print("    Pop 2 from stack_in, push to stack_out")
    print("    Pop 1 from stack_in, push to stack_out")
    print()
    print("    stack_in          stack_out")
    print("    ┌───┐             ┌───┐")
    print("    │   │ empty       │ 1 │ ← top (FIRST IN!)")
    print("    │   │             │ 2 │")
    print("    │   │             │ 3 │")
    print("    └───┘             └───┘")
    print()
    print("  Now pop from stack_out → 1 (first in, first out!) ✓")
    print()

    # --- Amortized Analysis ---
    print("=" * 70)
    print("AMORTIZED TIME COMPLEXITY ANALYSIS")
    print("=" * 70)
    print()
    print("  Worst case for single dequeue: O(n)")
    print("    When stack_out is empty, we transfer n elements.")
    print()
    print("  But this is RARE! Amortized per operation: O(1)")
    print()
    print("  Proof (Accounting Method):")
    print("  ──────────────────────────")
    print("  Each element goes through at most 4 operations:")
    print("    1. Push to stack_in     (during enqueue)  — O(1)")
    print("    2. Pop from stack_in    (during transfer) — O(1)")
    print("    3. Push to stack_out    (during transfer) — O(1)")
    print("    4. Pop from stack_out   (during dequeue)  — O(1)")
    print()
    print("  Total cost per element = 4 × O(1) = O(1)")
    print("  Total cost for n elements = O(n)")
    print("  Amortized cost per operation = O(n) / n = O(1) ✓")
    print()
    print("  Think of it like a PREPAID CARD:")
    print("    When you enqueue, you 'prepay' for the future transfer.")
    print("    The transfer is expensive, but it's already paid for!")
    print()

    # --- Timing Example ---
    print("--- Timing: Individual Operation Costs ---")
    print()

    q2 = QueueWithTwoStacks()
    print(f"  {'Op #':>5} | {'Operation':>12} | {'Cost':>6} | {'Note'}")
    print(f"  {'-'*5} | {'-'*12} | {'-'*6} | {'-'*30}")

    ops = [
        ("enqueue(1)", 1, "O(1)", "Push to stack_in"),
        ("enqueue(2)", 1, "O(1)", "Push to stack_in"),
        ("enqueue(3)", 1, "O(1)", "Push to stack_in"),
        ("dequeue()", 4, "O(n)", "Transfer 3 + pop 1 = 4 ops ★"),
        ("dequeue()", 1, "O(1)", "Pop from stack_out (no transfer)"),
        ("dequeue()", 1, "O(1)", "Pop from stack_out (no transfer)"),
    ]

    total_cost = 0
    for i, (op, cost, big_o, note) in enumerate(ops, 1):
        total_cost += cost
        print(f"  {i:>5} | {op:>12} | {big_o:>6} | {note}")

    print()
    print(f"  Total operations: {len(ops)}")
    print(f"  Total cost: {total_cost}")
    print(f"  Amortized: {total_cost}/{len(ops)} = {total_cost/len(ops):.1f} per operation → O(1)")
    print()

    # --- Comparison ---
    print("--- Queue Implementation Comparison ---")
    print()
    print("  Method            | Enqueue | Dequeue   | Space | Notes")
    print("  ------------------|---------|-----------|-------|---------------------")
    print("  Two Stacks ★      | O(1)    | O(1) amtz | O(n)  | This solution!")
    print("  collections.deque | O(1)    | O(1)      | O(n)  | Python built-in")
    print("  List + pop(0)     | O(1)    | O(n)      | O(n)  | DON'T do this!")
    print("  Linked List       | O(1)    | O(1)      | O(n)  | With tail pointer")
    print()

    # --- Full Correctness Test ---
    print("--- Correctness Test: FIFO Order ---")
    print()
    q3 = QueueWithTwoStacks()
    for i in range(1, 8):
        q3.enqueue(i)

    dequeued = []
    while not q3.is_empty():
        dequeued.append(q3.dequeue())

    print(f"  Enqueued: [1, 2, 3, 4, 5, 6, 7]")
    print(f"  Dequeued: {dequeued}")
    print(f"  FIFO order maintained: {dequeued == list(range(1, 8))}")
    print()

    print("ANSWER: Two stacks with lazy transfer. Enqueue always O(1).")
    print("Dequeue O(1) amortized because each element is transferred at most once.")


if __name__ == "__main__":
    demonstrate()
