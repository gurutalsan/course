"""
Q4. Write a function to merge two sorted linked lists into one sorted list.
    What is the time and space complexity?

Answer:
    Use a dummy head and a tail pointer. Compare the front nodes of
    both lists, attach the smaller one to the merged list, advance
    that pointer. When one list is exhausted, attach the rest.

    Time Complexity:  O(n + m) — visit each node exactly once.
    Space Complexity: O(1) — only rearranging existing node pointers.
                      (No new nodes created!)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for v in values[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head


def to_str(head):
    parts = []
    curr = head
    while curr:
        parts.append(str(curr.data))
        curr = curr.next
    return " → ".join(parts) + " → None" if parts else "None"


def to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result


# ============================================================
# Iterative Merge ★ RECOMMENDED ★
# ============================================================
def merge_sorted_lists(l1: Node, l2: Node) -> Node:
    """
    Merge two sorted linked lists into one sorted list.

    Uses a dummy node as the starting point and a tail pointer
    to build the merged list by comparing front nodes.

    Time:  O(n + m) — each node visited once.
    Space: O(1)     — reuses existing nodes, no new nodes created.

    Returns:
        Head of the merged sorted list.
    """
    dummy = Node(0)   # Dummy node to simplify edge cases
    tail = dummy      # Tail of the merged list

    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Attach remaining nodes (one list might not be exhausted)
    tail.next = l1 if l1 is not None else l2

    return dummy.next  # Skip the dummy node


# ============================================================
# Recursive Merge (for comparison)
# ============================================================
def merge_sorted_recursive(l1: Node, l2: Node) -> Node:
    """
    Merge two sorted lists recursively.

    Time:  O(n + m)
    Space: O(n + m) — recursion call stack.
    """
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.data <= l2.data:
        l1.next = merge_sorted_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted_recursive(l1, l2.next)
        return l2


def demonstrate():
    print("=" * 70)
    print("Q4: Merge Two Sorted Linked Lists")
    print("=" * 70)
    print()

    # --- Problem ---
    print("--- Problem ---")
    print()
    print("  List 1: 1 → 3 → 5 → 7 → None")
    print("  List 2: 2 → 4 → 6 → 8 → None")
    print("  Merged: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → None")
    print()

    # --- Algorithm ---
    print("--- Algorithm: Dummy Node + Comparison ---")
    print()
    print("  1. Create a dummy node as the anchor.")
    print("  2. Compare front nodes of both lists.")
    print("  3. Attach the SMALLER one to the merged list.")
    print("  4. Advance the pointer of the list we took from.")
    print("  5. When one list is empty, attach the rest of the other.")
    print()

    # --- Step-by-Step Walkthrough ---
    print("=" * 70)
    print("STEP-BY-STEP: Merge [1,3,5] and [2,4,6]")
    print("=" * 70)
    print()

    steps = [
        ("Init", "L1: [1]→[3]→[5]→None\n            L2: [2]→[4]→[6]→None\n            Merged: [dummy]", "Create dummy node"),
        ("Step 1", "L1: [1]→[3]→[5]  vs  L2: [2]→[4]→[6]\n            1 ≤ 2 → take 1 from L1\n            Merged: [dummy]→[1]", "Compare 1 vs 2"),
        ("Step 2", "L1: [3]→[5]  vs  L2: [2]→[4]→[6]\n            3 > 2 → take 2 from L2\n            Merged: [dummy]→[1]→[2]", "Compare 3 vs 2"),
        ("Step 3", "L1: [3]→[5]  vs  L2: [4]→[6]\n            3 ≤ 4 → take 3 from L1\n            Merged: [dummy]→[1]→[2]→[3]", "Compare 3 vs 4"),
        ("Step 4", "L1: [5]  vs  L2: [4]→[6]\n            5 > 4 → take 4 from L2\n            Merged: [dummy]→[1]→[2]→[3]→[4]", "Compare 5 vs 4"),
        ("Step 5", "L1: [5]  vs  L2: [6]\n            5 ≤ 6 → take 5 from L1\n            Merged: [dummy]→[1]→[2]→[3]→[4]→[5]", "Compare 5 vs 6"),
        ("Step 6", "L1: None  →  L2: [6] remaining\n            Attach rest of L2\n            Merged: [dummy]→[1]→[2]→[3]→[4]→[5]→[6]", "L1 exhausted"),
    ]

    for label, diagram, action in steps:
        print(f"  {label}: {action}")
        for line in diagram.split('\n'):
            print(f"            {line.strip()}")
        print()

    print("  Return dummy.next → [1]→[2]→[3]→[4]→[5]→[6]→None ✓")
    print()

    # --- Verify with code ---
    print("--- Verification ---")
    print()

    l1 = build_list([1, 3, 5, 7])
    l2 = build_list([2, 4, 6, 8])
    print(f"  L1:     {to_str(l1)}")
    print(f"  L2:     {to_str(l2)}")
    merged = merge_sorted_lists(l1, l2)
    print(f"  Merged: {to_str(merged)}")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([1, 3, 5], [2, 4, 6], "Same length"),
        ([1, 2, 3], [4, 5, 6, 7, 8], "L2 longer"),
        ([1, 5, 10], [2, 3], "L1 longer"),
        ([], [1, 2, 3], "L1 empty"),
        ([1, 2, 3], [], "L2 empty"),
        ([], [], "Both empty"),
        ([1], [2], "Single elements"),
        ([1, 1, 1], [1, 1, 1], "All same values"),
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], "Interleaved"),
    ]

    for v1, v2, desc in test_cases:
        l1 = build_list(v1)
        l2 = build_list(v2)
        merged = merge_sorted_lists(l1, l2)
        merged_list = to_list(merged)
        is_sorted = merged_list == sorted(v1 + v2)
        status = "✓" if is_sorted else "✗"

        print(f"  {desc:>20}: {v1} + {v2}")
        print(f"  {'':>20}  → {merged_list}  {status}")
        print()

    # --- Why Dummy Node? ---
    print("--- Why Use a Dummy Node? ---")
    print()
    print("  Without dummy: need special handling for the first node")
    print("    if l1.data <= l2.data:")
    print("        head = l1; l1 = l1.next    ← special case for head!")
    print("    else:")
    print("        head = l2; l2 = l2.next")
    print("    tail = head")
    print("    # ... then the loop")
    print()
    print("  With dummy: no special cases! Clean, uniform logic")
    print("    dummy = Node(0)")
    print("    tail = dummy")
    print("    # ... loop attaches to tail.next")
    print("    return dummy.next    ← skip the dummy")
    print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Method     | Time     | Space    | Notes")
    print("  -----------|----------|----------|---------------------------")
    print("  Iterative★ | O(n + m) | O(1)     | Rearranges existing nodes")
    print("  Recursive  | O(n + m) | O(n + m) | Call stack depth")
    print()
    print("ANSWER:")
    print("  Time:  O(n + m) — each node from both lists visited exactly once.")
    print("  Space: O(1) — no new nodes created, only pointer rearrangement.")


if __name__ == "__main__":
    demonstrate()
