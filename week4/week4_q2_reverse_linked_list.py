"""
Q2. Write a function to reverse a linked list iteratively.
    Trace through the algorithm step by step for the list 1→2→3→4.

Answer:
    Use three pointers: prev, current, next_node.
    At each step, reverse the 'next' pointer of the current node.

    Time Complexity:  O(n) — single pass through the list.
    Space Complexity: O(1) — only three pointer variables.

    Algorithm:
    1. Initialize: prev = None, current = head
    2. While current is not None:
       a. Save next_node = current.next
       b. Reverse link: current.next = prev
       c. Move forward: prev = current, current = next_node
    3. Return prev (new head)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


def build_list(values: list) -> Node:
    """Helper: Build a linked list from a Python list."""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def list_to_str(head: Node) -> str:
    """Helper: Convert linked list to string representation."""
    parts = []
    current = head
    while current:
        parts.append(str(current.data))
        current = current.next
    return " → ".join(parts) + " → None"


# ============================================================
# Iterative Reversal ★ RECOMMENDED ★
# ============================================================
def reverse_iterative(head: Node) -> Node:
    """
    Reverse a linked list iteratively using three pointers.

    Time:  O(n) — single pass.
    Space: O(1) — three pointer variables only.

    Returns:
        New head of the reversed list.
    """
    prev = None
    current = head

    while current is not None:
        next_node = current.next   # Save next
        current.next = prev        # Reverse the link
        prev = current             # Move prev forward
        current = next_node        # Move current forward

    return prev  # prev is now the new head


# ============================================================
# Recursive Reversal (for comparison)
# ============================================================
def reverse_recursive(head: Node) -> Node:
    """
    Reverse a linked list recursively.

    Time:  O(n)
    Space: O(n) — recursion call stack.
    """
    # Base case: empty list or single node
    if head is None or head.next is None:
        return head

    # Reverse the rest of the list
    new_head = reverse_recursive(head.next)

    # Make the next node point back to current
    head.next.next = head
    head.next = None

    return new_head


def demonstrate():
    print("=" * 70)
    print("Q2: Reverse a Linked List — Iterative Approach")
    print("=" * 70)
    print()

    # --- The Algorithm ---
    print("--- The Algorithm ---")
    print()
    print("  Use THREE pointers: prev, current, next_node")
    print()
    print("  At each step:")
    print("    1. Save:    next_node = current.next")
    print("    2. Reverse: current.next = prev")
    print("    3. Advance: prev = current")
    print("    4. Advance: current = next_node")
    print()

    # --- Step-by-Step Trace for 1→2→3→4 ---
    print("=" * 70)
    print("STEP-BY-STEP TRACE: 1 → 2 → 3 → 4")
    print("=" * 70)
    print()

    print("  Initial state:")
    print("    prev = None")
    print("    current → [1] → [2] → [3] → [4] → None")
    print()

    steps = [
        {
            "step": 1,
            "current_val": 1,
            "before": "  None    [1] → [2] → [3] → [4] → None",
            "markers": "    ↑      ↑",
            "labels":  "   prev  curr",
            "save":    "  next_node = current.next → [2]",
            "reverse": "  current.next = prev → None  (1 now points to None)",
            "after":   "  None ← [1]    [2] → [3] → [4] → None",
            "move":    "          ↑      ↑",
            "mlabels": "         prev  curr",
        },
        {
            "step": 2,
            "current_val": 2,
            "before": "  None ← [1]    [2] → [3] → [4] → None",
            "markers": "          ↑      ↑",
            "labels":  "         prev  curr",
            "save":    "  next_node = current.next → [3]",
            "reverse": "  current.next = prev → [1]  (2 now points to 1)",
            "after":   "  None ← [1] ← [2]    [3] → [4] → None",
            "move":    "                 ↑      ↑",
            "mlabels": "                prev  curr",
        },
        {
            "step": 3,
            "current_val": 3,
            "before": "  None ← [1] ← [2]    [3] → [4] → None",
            "markers": "                 ↑      ↑",
            "labels":  "                prev  curr",
            "save":    "  next_node = current.next → [4]",
            "reverse": "  current.next = prev → [2]  (3 now points to 2)",
            "after":   "  None ← [1] ← [2] ← [3]    [4] → None",
            "move":    "                        ↑      ↑",
            "mlabels": "                       prev  curr",
        },
        {
            "step": 4,
            "current_val": 4,
            "before": "  None ← [1] ← [2] ← [3]    [4] → None",
            "markers": "                        ↑      ↑",
            "labels":  "                       prev  curr",
            "save":    "  next_node = current.next → None",
            "reverse": "  current.next = prev → [3]  (4 now points to 3)",
            "after":   "  None ← [1] ← [2] ← [3] ← [4]    None",
            "move":    "                              ↑      ↑",
            "mlabels": "                             prev  curr",
        },
    ]

    for s in steps:
        print(f"  ─── Step {s['step']}: current = [{s['current_val']}] ───")
        print()
        print(f"    Before:   {s['before']}")
        print(f"              {s['markers']}")
        print(f"              {s['labels']}")
        print()
        print(f"    1. Save:    {s['save']}")
        print(f"    2. Reverse: {s['reverse']}")
        print()
        print(f"    After:    {s['after']}")
        print(f"    3-4 Move: {s['move']}")
        print(f"              {s['mlabels']}")
        print()

    print("  ─── Loop ends: current = None ───")
    print()
    print("  Return prev → [4] (new head)")
    print()
    print("  Final:  None ← [1] ← [2] ← [3] ← [4]")
    print("          which is: [4] → [3] → [2] → [1] → None")
    print()

    # --- Verify with actual code ---
    print("=" * 70)
    print("VERIFICATION: Running the actual code")
    print("=" * 70)
    print()

    head = build_list([1, 2, 3, 4])
    print(f"  Before: {list_to_str(head)}")

    reversed_head = reverse_iterative(head)
    print(f"  After:  {list_to_str(reversed_head)}")
    print()

    # --- More Test Cases ---
    print("--- More Test Cases ---")
    print()

    test_cases = [
        ([1, 2, 3, 4, 5], "5 elements"),
        ([1, 2], "2 elements"),
        ([1], "Single element"),
        ([], "Empty list"),
        ([10, 20, 30], "Three elements"),
        ([5, 4, 3, 2, 1], "Already 'reversed'"),
    ]

    for values, desc in test_cases:
        head = build_list(values)
        original = list_to_str(head)
        reversed_head = reverse_iterative(head)
        reversed_str = list_to_str(reversed_head)

        print(f"  {desc}:")
        print(f"    Original: {original}")
        print(f"    Reversed: {reversed_str}")
        print()

    # --- Iterative vs Recursive ---
    print("--- Iterative vs Recursive Comparison ---")
    print()
    print("  Method     | Time | Space  | Notes")
    print("  -----------|------|--------|---------------------------")
    print("  Iterative  | O(n) | O(1) ★ | Only 3 pointer variables")
    print("  Recursive  | O(n) | O(n)   | Call stack = n frames")
    print()
    print("  Iterative is preferred due to O(1) space.")
    print()

    # Verify recursive produces same result
    print("  Recursive verification:")
    head = build_list([1, 2, 3, 4])
    print(f"    Original:  {list_to_str(head)}")
    reversed_r = reverse_recursive(head)
    print(f"    Reversed:  {list_to_str(reversed_r)}")
    print()

    # --- The Code ---
    print("--- The Code ---")
    print()
    print("  def reverse_iterative(head):")
    print("      prev = None")
    print("      current = head")
    print()
    print("      while current is not None:")
    print("          next_node = current.next   # 1. Save next")
    print("          current.next = prev        # 2. Reverse link")
    print("          prev = current             # 3. Move prev →")
    print("          current = next_node        # 4. Move current →")
    print()
    print("      return prev  # New head")
    print()
    print("ANSWER: O(n) time, O(1) space. Three pointers: prev, current, next.")


if __name__ == "__main__":
    demonstrate()
