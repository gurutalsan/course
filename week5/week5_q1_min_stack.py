"""
Q1. Implement a MinStack that supports push, pop, top, and getMin,
    all in O(1) time. Explain your approach.

Answer:
    Use TWO stacks:
    - main_stack: stores all pushed values normally.
    - min_stack:  stores the current minimum at each level.

    Every time we push, we also push the current minimum onto min_stack.
    Every time we pop, we pop from both stacks.
    getMin() simply peeks at the top of min_stack → O(1)!

    All operations: O(1) time, O(n) space (two stacks of size n).
"""


class MinStack:
    """
    A stack that supports push, pop, top, and getMin — ALL in O(1).

    Approach: Maintain a parallel 'min_stack' that tracks the minimum
    value at every depth of the main stack.

    When we push(x):
        main_stack gets x.
        min_stack gets min(x, current_minimum).

    When we pop():
        Pop from BOTH stacks.

    getMin():
        Just peek at min_stack's top → O(1)!

    Time:  O(1) for ALL operations.
    Space: O(n) — two stacks of equal size.
    """

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """Push value onto the stack. O(1)."""
        self.main_stack.append(val)

        # Push current minimum onto min_stack
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> int:
        """Remove and return top element. O(1)."""
        if not self.main_stack:
            raise IndexError("Stack is empty")
        self.min_stack.pop()
        return self.main_stack.pop()

    def top(self) -> int:
        """Return top element without removing. O(1)."""
        if not self.main_stack:
            raise IndexError("Stack is empty")
        return self.main_stack[-1]

    def getMin(self) -> int:
        """Return the minimum element in the stack. O(1)."""
        if not self.min_stack:
            raise IndexError("Stack is empty")
        return self.min_stack[-1]

    def __len__(self):
        return len(self.main_stack)

    def __repr__(self):
        return f"MinStack(main={self.main_stack}, min={self.min_stack})"


# ============================================================
# Space-Optimized MinStack (only push to min_stack when new min)
# ============================================================
class MinStackOptimized:
    """
    Space-optimized: only push to min_stack when value <= current min.

    Saves space when many values are larger than the minimum.
    """

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> int:
        if not self.main_stack:
            raise IndexError("Stack is empty")
        val = self.main_stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def demonstrate():
    print("=" * 70)
    print("Q1: MinStack — All Operations in O(1)")
    print("=" * 70)
    print()

    # --- Approach ---
    print("--- Approach: Two Parallel Stacks ---")
    print()
    print("  main_stack:  stores values normally")
    print("  min_stack:   stores the minimum at each level")
    print()
    print("  push(x): main pushes x, min pushes min(x, current_min)")
    print("  pop():   pop from BOTH stacks")
    print("  getMin(): peek at min_stack → O(1)!")
    print()

    # --- Step-by-Step Demo ---
    print("=" * 70)
    print("STEP-BY-STEP DEMONSTRATION")
    print("=" * 70)
    print()

    ms = MinStack()
    operations = [
        ("push", 5), ("push", 3), ("push", 7), ("push", 2),
        ("push", 8), ("getMin", None), ("pop", None), ("pop", None),
        ("getMin", None), ("push", 1), ("getMin", None), ("top", None),
    ]

    print(f"  {'Op':>12} | {'main_stack':>20} | {'min_stack':>20} | {'Result':>8} | {'Min':>5}")
    print(f"  {'-'*12} | {'-'*20} | {'-'*20} | {'-'*8} | {'-'*5}")

    for op, val in operations:
        if op == "push":
            ms.push(val)
            result = f"push({val})"
            print(f"  {result:>12} | {str(ms.main_stack):>20} | {str(ms.min_stack):>20} | {'—':>8} | {ms.getMin():>5}")
        elif op == "pop":
            popped = ms.pop()
            print(f"  {'pop()':>12} | {str(ms.main_stack):>20} | {str(ms.min_stack):>20} | {popped:>8} | {ms.getMin():>5}")
        elif op == "getMin":
            m = ms.getMin()
            print(f"  {'getMin()':>12} | {str(ms.main_stack):>20} | {str(ms.min_stack):>20} | {m:>8} | {m:>5}")
        elif op == "top":
            t = ms.top()
            print(f"  {'top()':>12} | {str(ms.main_stack):>20} | {str(ms.min_stack):>20} | {t:>8} | {ms.getMin():>5}")

    print()

    # --- Visual ---
    print("--- Visual: How Min Tracks at Each Level ---")
    print()
    print("  After pushing 5, 3, 7, 2, 8:")
    print()
    print("    Index | main_stack | min_stack | Explanation")
    print("    ------|------------|-----------|---------------------------")
    print("      4   |     8      |     2     | min(8, 2) = 2")
    print("      3   |     2      |     2     | min(2, 3) = 2  ← new min!")
    print("      2   |     7      |     3     | min(7, 3) = 3")
    print("      1   |     3      |     3     | min(3, 5) = 3  ← new min!")
    print("      0   |     5      |     5     | first element = 5")
    print()
    print("  getMin() = min_stack[-1] = 2  → O(1) peek!")
    print()
    print("  After popping 8 and 2:")
    print()
    print("    Index | main_stack | min_stack")
    print("    ------|------------|----------")
    print("      2   |     7      |     3")
    print("      1   |     3      |     3")
    print("      0   |     5      |     5")
    print()
    print("  getMin() = min_stack[-1] = 3  → Correct! 2 is gone.")
    print()

    # --- Why not just track a single min variable? ---
    print("--- Why Not Just a Single 'min' Variable? ---")
    print()
    print("  Problem: When you pop the current minimum, what's the NEW min?")
    print("  You'd need O(n) to scan the entire stack!")
    print()
    print("  With min_stack: just pop it → previous min is revealed → O(1)!")
    print()

    # --- Test Comprehensive ---
    print("--- Comprehensive Test ---")
    print()
    ms2 = MinStack()
    test_ops = [
        ("push", -2), ("push", 0), ("push", -3),
        ("getMin", None, -3), ("pop", None, -3),
        ("top", None, 0), ("getMin", None, -2),
    ]

    all_pass = True
    for item in test_ops:
        op = item[0]
        val = item[1]
        expected = item[2] if len(item) > 2 else None

        if op == "push":
            ms2.push(val)
            print(f"  push({val})")
        elif op == "pop":
            result = ms2.pop()
            ok = result == expected
            print(f"  pop() → {result} (expected {expected}) {'✓' if ok else '✗'}")
            if not ok: all_pass = False
        elif op == "getMin":
            result = ms2.getMin()
            ok = result == expected
            print(f"  getMin() → {result} (expected {expected}) {'✓' if ok else '✗'}")
            if not ok: all_pass = False
        elif op == "top":
            result = ms2.top()
            ok = result == expected
            print(f"  top() → {result} (expected {expected}) {'✓' if ok else '✗'}")
            if not ok: all_pass = False

    print(f"\n  All tests passed: {'✓' if all_pass else '✗'}")
    print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Operation | Time | Space")
    print("  ----------|------|------")
    print("  push(x)   | O(1) | O(1) per push")
    print("  pop()     | O(1) | —")
    print("  top()     | O(1) | —")
    print("  getMin()  | O(1) | —")
    print("  Overall   | O(1) | O(n) total (two stacks)")
    print()
    print("ANSWER: Use a parallel min_stack that tracks the minimum at each level.")
    print("All operations are O(1) because getMin() is just a peek at min_stack top.")


if __name__ == "__main__":
    demonstrate()
