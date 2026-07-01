"""
Q8. Design a MaxStack that supports push, pop, top, peekMax, and popMax.
    What tradeoffs do you encounter?

Answer:
    Approach 1 (Two Stacks): Similar to MinStack but for max.
        push/pop/top/peekMax: O(1)
        popMax: O(n) — must find and remove the max, then rebuild.

    Approach 2 (Stack + Sorted Structure): Use a doubly-linked list + TreeMap
        All operations: O(log n) using balanced BST.

    The KEY TRADEOFF:
    peekMax in O(1) is easy (parallel stack), but
    popMax (removing the max from anywhere) is hard:
    - With a stack alone: O(n) to find and remove.
    - With a heap: O(n) for lazy deletion.
    - With a balanced BST + doubly-linked list: O(log n) but complex.
"""


# ============================================================
# Approach 1: Two Stacks (Simple — peekMax O(1), popMax O(n))
# ============================================================
class MaxStack:
    """
    MaxStack using two stacks.

    push/pop/top/peekMax: O(1)
    popMax: O(n) — must find and remove max, then rebuild.

    This is the simplest approach with a clear tradeoff.
    """

    def __init__(self):
        self.main_stack = []
        self.max_stack = []   # Tracks current max at each level

    def push(self, val: int) -> None:
        """Push value. O(1)."""
        self.main_stack.append(val)
        if not self.max_stack:
            self.max_stack.append(val)
        else:
            self.max_stack.append(max(val, self.max_stack[-1]))

    def pop(self) -> int:
        """Remove and return top. O(1)."""
        self.max_stack.pop()
        return self.main_stack.pop()

    def top(self) -> int:
        """Return top without removing. O(1)."""
        return self.main_stack[-1]

    def peekMax(self) -> int:
        """Return the maximum value in the stack. O(1)."""
        return self.max_stack[-1]

    def popMax(self) -> int:
        """
        Remove and return the maximum value. O(n).

        Strategy: Pop elements into a temp buffer until we find the max,
        remove it, then push the buffer elements back.
        """
        max_val = self.peekMax()

        # Pop elements into buffer until we find the max
        buffer = []
        while self.top() != max_val:
            buffer.append(self.pop())

        # Remove the max
        self.pop()

        # Push buffer elements back
        while buffer:
            self.push(buffer.pop())

        return max_val

    def __len__(self):
        return len(self.main_stack)

    def __repr__(self):
        return f"MaxStack(main={self.main_stack}, max={self.max_stack})"


# ============================================================
# Approach 2: Stack + Heap with Lazy Deletion
# ============================================================
import heapq


class MaxStackHeap:
    """
    MaxStack using a stack + max-heap with lazy deletion.

    push: O(log n)
    pop: O(log n) amortized
    top: O(1)
    peekMax: O(1) amortized
    popMax: O(log n) amortized

    Uses a counter (ID) to handle duplicates and track deletion.
    """

    def __init__(self):
        self.stack = []        # (value, id)
        self.heap = []         # (-value, -id) for max-heap via min-heap
        self.deleted = set()   # Set of deleted IDs
        self.counter = 0       # Unique ID for each push

    def push(self, val: int) -> None:
        self.counter += 1
        self.stack.append((val, self.counter))
        heapq.heappush(self.heap, (-val, -self.counter))

    def pop(self) -> int:
        # Remove from stack (skip deleted entries)
        while self.stack and self.stack[-1][1] in self.deleted:
            self.stack.pop()

        val, uid = self.stack.pop()
        self.deleted.add(uid)
        return val

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.deleted:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        # Clean up deleted entries from heap top
        while self.heap and -self.heap[0][1] in self.deleted:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.deleted:
            heapq.heappop(self.heap)
        neg_val, neg_id = heapq.heappop(self.heap)
        self.deleted.add(-neg_id)
        return -neg_val


def demonstrate():
    print("=" * 70)
    print("Q8: MaxStack Design — Push, Pop, Top, PeekMax, PopMax")
    print("=" * 70)
    print()

    # --- The Challenge ---
    print("--- The Challenge ---")
    print()
    print("  Regular stack: push, pop, top → all O(1). Easy!")
    print("  MinStack: add getMin() → O(1) with parallel stack. Still easy!")
    print()
    print("  MaxStack with popMax() is HARDER because:")
    print("  The maximum might be ANYWHERE in the stack, not just the top.")
    print("  Removing it from the middle breaks the stack structure.")
    print()

    # --- Approach 1 Demo ---
    print("=" * 70)
    print("APPROACH 1: Two Stacks (Simple)")
    print("=" * 70)
    print()

    ms = MaxStack()
    ops = [
        ("push", 5), ("push", 1), ("push", 5),
        ("top", None), ("popMax", None),
        ("top", None), ("peekMax", None),
        ("pop", None), ("top", None),
    ]

    print(f"  {'Operation':>12} | {'main_stack':>15} | {'max_stack':>15} | {'Result':>8}")
    print(f"  {'-'*12} | {'-'*15} | {'-'*15} | {'-'*8}")

    for op, val in ops:
        if op == "push":
            ms.push(val)
            print(f"  {'push('+str(val)+')':>12} | {str(ms.main_stack):>15} | {str(ms.max_stack):>15} | {'—':>8}")
        elif op == "pop":
            result = ms.pop()
            print(f"  {'pop()':>12} | {str(ms.main_stack):>15} | {str(ms.max_stack):>15} | {result:>8}")
        elif op == "top":
            result = ms.top()
            print(f"  {'top()':>12} | {str(ms.main_stack):>15} | {str(ms.max_stack):>15} | {result:>8}")
        elif op == "peekMax":
            result = ms.peekMax()
            print(f"  {'peekMax()':>12} | {str(ms.main_stack):>15} | {str(ms.max_stack):>15} | {result:>8}")
        elif op == "popMax":
            result = ms.popMax()
            print(f"  {'popMax()':>12} | {str(ms.main_stack):>15} | {str(ms.max_stack):>15} | {result:>8}")

    print()

    # --- How popMax works ---
    print("--- How popMax() Works (The Hard Part) ---")
    print()
    print("  Stack: [5, 1, 5, 3, 7, 2]   Max = 7 (in the middle!)")
    print()
    print("  Step 1: Pop elements into buffer until we find 7:")
    print("    Pop 2 → buffer: [2]        Stack: [5, 1, 5, 3, 7]")
    print("    top=7! Found the max!")
    print()
    print("  Step 2: Pop the max (7):")
    print("    Pop 7 → removed!           Stack: [5, 1, 5, 3]")
    print()
    print("  Step 3: Push buffer back (reverse order):")
    print("    Push 2                      Stack: [5, 1, 5, 3, 2]")
    print()
    print("  Cost: O(n) — had to move n elements to find and remove max")
    print()

    # --- Tradeoffs ---
    print("=" * 70)
    print("TRADEOFFS ANALYSIS")
    print("=" * 70)
    print()

    print("  ┌──────────────────┬──────────┬──────────┬──────────┬──────────┬──────────┐")
    print("  │ Approach         │ push     │ pop      │ top      │ peekMax  │ popMax   │")
    print("  ├──────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┤")
    print("  │ Two Stacks       │ O(1)     │ O(1)     │ O(1)     │ O(1)    │ O(n) ★  │")
    print("  │ Stack + Heap     │ O(log n) │ O(log n)*│ O(1)*    │ O(1)*   │ O(log n)*│")
    print("  │ DLL + TreeMap    │ O(log n) │ O(log n) │ O(1)     │ O(log n)│ O(log n) │")
    print("  └──────────────────┴──────────┴──────────┴──────────┴──────────┴──────────┘")
    print("  * amortized")
    print()

    print("  THE CORE TRADEOFF:")
    print("  ─────────────────")
    print()
    print("  1. Simplicity vs Performance")
    print("     Two stacks is simple but popMax is O(n).")
    print("     Heap/TreeMap approaches are O(log n) but much more complex.")
    print()
    print("  2. peekMax (easy) vs popMax (hard)")
    print("     peekMax = 'what is the max?' → just track it → O(1)")
    print("     popMax = 'remove the max' → need to find it in the stack")
    print("     and remove from the middle → breaks stack invariant!")
    print()
    print("  3. Time vs Space")
    print("     Heap approach uses extra space for deleted set.")
    print("     TreeMap uses balanced tree overhead.")
    print()

    # --- Comprehensive Test ---
    print("--- Comprehensive Test ---")
    print()

    ms2 = MaxStack()
    test_ops = [
        ("push", 5, None),
        ("push", 1, None),
        ("push", 5, None),
        ("top", None, 5),
        ("popMax", None, 5),
        ("top", None, 1),
        ("peekMax", None, 5),
        ("pop", None, 1),
        ("top", None, 5),
    ]

    all_pass = True
    for op, val, expected in test_ops:
        if op == "push":
            ms2.push(val)
            print(f"  push({val})")
        elif op == "pop":
            result = ms2.pop()
            ok = result == expected
            if not ok: all_pass = False
            print(f"  pop() → {result} (expected {expected}) {'✓' if ok else '✗'}")
        elif op == "top":
            result = ms2.top()
            ok = result == expected
            if not ok: all_pass = False
            print(f"  top() → {result} (expected {expected}) {'✓' if ok else '✗'}")
        elif op == "peekMax":
            result = ms2.peekMax()
            ok = result == expected
            if not ok: all_pass = False
            print(f"  peekMax() → {result} (expected {expected}) {'✓' if ok else '✗'}")
        elif op == "popMax":
            result = ms2.popMax()
            ok = result == expected
            if not ok: all_pass = False
            print(f"  popMax() → {result} (expected {expected}) {'✓' if ok else '✗'}")

    print(f"\n  All tests passed: {'✓' if all_pass else '✗'}")
    print()

    # --- When to use which ---
    print("--- When to Use Which Approach ---")
    print()
    print("  Two Stacks (Approach 1):")
    print("    ✓ Simple to implement and understand")
    print("    ✓ popMax is rare in your use case")
    print("    ✗ popMax is O(n) — bad if called frequently")
    print()
    print("  Stack + Heap (Approach 2):")
    print("    ✓ All operations O(log n) amortized")
    print("    ✓ Good when popMax is called frequently")
    print("    ✗ More complex, lazy deletion overhead")
    print()
    print("ANSWER: Use two stacks for simplicity (peekMax=O(1), popMax=O(n)).")
    print("The key tradeoff is that popMax requires finding and removing the")
    print("maximum from the MIDDLE of the stack, which breaks LIFO order.")
    print("Better approaches use heap/TreeMap for O(log n) but add complexity.")


if __name__ == "__main__":
    demonstrate()
