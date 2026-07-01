"""
Q6. Explain the difference between LIFO and FIFO with real-world examples.
    When would you choose a stack over a queue?

Answer:
    LIFO (Last In, First Out) — STACK
      The MOST RECENTLY added item is removed first.
      Like a stack of plates: you take the top plate off first.

    FIFO (First In, First Out) — QUEUE
      The OLDEST item is removed first.
      Like a line at a store: first person in line gets served first.
"""


from collections import deque


class Stack:
    """LIFO: Last In, First Out."""
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __repr__(self):
        return f"Stack({self._data}) ← top"


class Queue:
    """FIFO: First In, First Out."""
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        return self._data.popleft()

    def peek(self):
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __repr__(self):
        return f"Queue({list(self._data)}) → front"


def demonstrate():
    print("=" * 70)
    print("Q6: LIFO vs FIFO — Stacks vs Queues")
    print("=" * 70)
    print()

    # --- Core Definitions ---
    print("--- Core Definitions ---")
    print()
    print("  STACK (LIFO — Last In, First Out)")
    print("  ═══════════════════════════════════")
    print("  The LAST item added is the FIRST to be removed.")
    print()
    print("       ┌───┐")
    print("       │ C │ ← top (last in, first out)")
    print("       │ B │")
    print("       │ A │ ← bottom (first in, last out)")
    print("       └───┘")
    print("    push(C) → pop() returns C")
    print()
    print("  QUEUE (FIFO — First In, First Out)")
    print("  ═══════════════════════════════════")
    print("  The FIRST item added is the FIRST to be removed.")
    print()
    print("    front → ┌───┬───┬───┐ ← back")
    print("            │ A │ B │ C │")
    print("            └───┴───┴───┘")
    print("    enqueue(C) → dequeue() returns A")
    print()

    # --- Side-by-Side Demo ---
    print("=" * 70)
    print("SIDE-BY-SIDE DEMONSTRATION")
    print("=" * 70)
    print()

    s = Stack()
    q = Queue()

    print("  Adding A, B, C to both:")
    print()
    for item in ['A', 'B', 'C']:
        s.push(item)
        q.enqueue(item)
        print(f"  Add '{item}':  {s}  |  {q}")

    print()
    print("  Removing items:")
    print()

    for _ in range(3):
        s_item = s.pop()
        q_item = q.dequeue()
        print(f"  Remove:  Stack→'{s_item}' (LIFO)  |  Queue→'{q_item}' (FIFO)")

    print()
    print("  Stack removed: C, B, A  (reverse order — LIFO)")
    print("  Queue removed: A, B, C  (original order — FIFO)")
    print()

    # --- Real-World Examples ---
    print("=" * 70)
    print("REAL-WORLD EXAMPLES")
    print("=" * 70)
    print()

    print("  ╔═══════════════════════════════════════════════════════════════╗")
    print("  ║                    STACK (LIFO) Examples                     ║")
    print("  ╠═══════════════════════════════════════════════════════════════╣")
    print("  ║                                                             ║")
    print("  ║  1. UNDO/REDO in text editors                              ║")
    print("  ║     → Last action is undone first                           ║")
    print("  ║                                                             ║")
    print("  ║  2. Browser BACK button                                     ║")
    print("  ║     → Last page visited is the first to go back to          ║")
    print("  ║                                                             ║")
    print("  ║  3. Stack of PLATES in a cafeteria                          ║")
    print("  ║     → Top plate is taken first                              ║")
    print("  ║                                                             ║")
    print("  ║  4. FUNCTION CALL STACK in programming                      ║")
    print("  ║     → Most recent function returns first                    ║")
    print("  ║                                                             ║")
    print("  ║  5. Matching PARENTHESES in code                            ║")
    print("  ║     → Most recent '(' matches the next ')'                  ║")
    print("  ║                                                             ║")
    print("  ╚═══════════════════════════════════════════════════════════════╝")
    print()
    print("  ╔═══════════════════════════════════════════════════════════════╗")
    print("  ║                    QUEUE (FIFO) Examples                     ║")
    print("  ╠═══════════════════════════════════════════════════════════════╣")
    print("  ║                                                             ║")
    print("  ║  1. CHECKOUT LINE at a supermarket                          ║")
    print("  ║     → First person in line is served first                  ║")
    print("  ║                                                             ║")
    print("  ║  2. PRINT QUEUE                                             ║")
    print("  ║     → First document sent is printed first                  ║")
    print("  ║                                                             ║")
    print("  ║  3. CPU TASK SCHEDULING                                     ║")
    print("  ║     → Processes are handled in arrival order                ║")
    print("  ║                                                             ║")
    print("  ║  4. BFS (Breadth-First Search) in graphs                    ║")
    print("  ║     → Explore nodes level by level                          ║")
    print("  ║                                                             ║")
    print("  ║  5. MESSAGE QUEUES (Kafka, RabbitMQ)                        ║")
    print("  ║     → Messages processed in order received                  ║")
    print("  ║                                                             ║")
    print("  ╚═══════════════════════════════════════════════════════════════╝")
    print()

    # --- When to Choose Which ---
    print("=" * 70)
    print("WHEN TO CHOOSE STACK vs QUEUE")
    print("=" * 70)
    print()

    print("  Choose STACK when:                     Choose QUEUE when:")
    print("  ─────────────────────────              ─────────────────────────")
    print("  • Most recent first matters             • Order of arrival matters")
    print("  • Undo/redo operations                  • Fair processing (FCFS)")
    print("  • Backtracking (maze, DFS)              • Level-by-level (BFS)")
    print("  • Expression evaluation                 • Task scheduling")
    print("  • Balanced brackets                     • Buffer/stream processing")
    print("  • Recursion simulation                  • Producer-consumer pattern")
    print()

    # --- Comparison Table ---
    print("--- Complete Comparison ---")
    print()
    print("  Feature          | Stack (LIFO)        | Queue (FIFO)")
    print("  -----------------|--------------------|-----------------")
    print("  Order            | Last In, First Out  | First In, First Out")
    print("  Add operation    | push (to top)       | enqueue (to back)")
    print("  Remove operation | pop (from top)      | dequeue (from front)")
    print("  Peek             | top element         | front element")
    print("  Python impl.     | list (append/pop)   | deque (append/popleft)")
    print("  Graph traversal  | DFS                 | BFS")
    print("  Real-world       | Plates, Undo        | Lines, Printers")
    print()

    # --- Code Examples ---
    print("--- Practical Code Examples ---")
    print()

    # Stack: Undo system
    print("  STACK Example: Simple Undo System")
    undo_stack = Stack()
    actions = ["type 'H'", "type 'e'", "type 'l'", "type 'l'", "type 'o'"]
    for action in actions:
        undo_stack.push(action)
        print(f"    Do: {action}")

    print()
    for _ in range(2):
        undone = undo_stack.pop()
        print(f"    Undo: {undone}")

    print()

    # Queue: Task processor
    print("  QUEUE Example: Print Job Queue")
    print_queue = Queue()
    jobs = ["Report.pdf", "Photo.jpg", "Invoice.docx"]
    for job in jobs:
        print_queue.enqueue(job)
        print(f"    Submit: {job}")

    print()
    while not print_queue.is_empty():
        job = print_queue.dequeue()
        print(f"    Printing: {job}")

    print()
    print("ANSWER:")
    print("  LIFO (Stack): Last added = first removed. Use for undo, DFS, brackets.")
    print("  FIFO (Queue): First added = first removed. Use for scheduling, BFS, buffers.")
    print("  Choose stack when recency matters; choose queue when fairness matters.")


if __name__ == "__main__":
    demonstrate()
