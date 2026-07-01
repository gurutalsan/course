"""
Q5. Given a linked list 1→2→3→4→5, write a function that removes the
    2nd node from the end (node 4). Use the two-pointer technique.

Answer:
    Use two pointers with a GAP of n between them:
    1. Move the FAST pointer n steps ahead.
    2. Move BOTH pointers one step at a time.
    3. When fast reaches the end, slow is at the node BEFORE the target.
    4. Delete the target by skipping it: slow.next = slow.next.next

    Time Complexity:  O(L) — single pass, where L is list length.
    Space Complexity: O(1) — only two pointers.
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


def remove_nth_from_end(head: Node, n: int) -> Node:
    """
    Remove the nth node from the END of the linked list.

    Two-pointer technique:
    1. Create a dummy node before head (handles edge case of removing head).
    2. Move fast pointer n+1 steps from dummy.
    3. Move both until fast reaches None.
    4. slow.next is the target — skip it.

    Time:  O(L) — single pass, L = list length.
    Space: O(1) — two pointers only.

    Args:
        head: Head of the linked list.
        n: Position from the end (1-indexed). n=1 removes last node.

    Returns:
        New head of the modified list.
    """
    # Dummy node handles the edge case of removing the head
    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    # Move fast n+1 steps ahead (to create a gap of n)
    for _ in range(n + 1):
        if fast is None:
            return head  # n is larger than list length
        fast = fast.next

    # Move both until fast reaches the end
    while fast is not None:
        fast = fast.next
        slow = slow.next

    # slow.next is the node to remove — skip it
    removed = slow.next
    slow.next = slow.next.next

    return dummy.next


def demonstrate():
    print("=" * 70)
    print("Q5: Remove Nth Node from End — Two-Pointer Technique")
    print("=" * 70)
    print()

    # --- Problem ---
    print("--- Problem ---")
    print()
    print("  List: 1 → 2 → 3 → 4 → 5 → None")
    print("  Remove the 2nd node from the end → node 4")
    print("  Result: 1 → 2 → 3 → 5 → None")
    print()
    print("  Counting from end: 5(1st), 4(2nd), 3(3rd), 2(4th), 1(5th)")
    print()

    # --- Algorithm ---
    print("--- Algorithm: Two Pointers with Gap ---")
    print()
    print("  Key Insight: If fast is n steps ahead of slow, when fast")
    print("  reaches the end, slow is at the node BEFORE the target.")
    print()
    print("  Steps:")
    print("    1. Create dummy → head (handles removing head node)")
    print("    2. Move fast n+1 steps from dummy")
    print("    3. Move both one step at a time until fast = None")
    print("    4. slow.next is the target → skip it")
    print()

    # --- Step-by-Step Trace ---
    print("=" * 70)
    print("TRACE: Remove 2nd from end in [1,2,3,4,5]")
    print("=" * 70)
    print()

    print("  Setup: n = 2")
    print()
    print("  Step 0: Create dummy node")
    print("    [D] → [1] → [2] → [3] → [4] → [5] → None")
    print("     ↑")
    print("    fast")
    print("    slow")
    print()

    print("  Step 1: Move fast n+1 = 3 steps ahead")
    print("    [D] → [1] → [2] → [3] → [4] → [5] → None")
    print("     ↑                  ↑")
    print("    slow               fast")
    print()
    print("    Gap between slow and fast = 3 positions")
    print()

    print("  Step 2: Move both until fast = None")
    print()

    positions = [
        ("Move 1", "[D] → [1] → [2] → [3] → [4] → [5] → None",
         "          ↑                         ↑",
         "         slow                      fast"),
        ("Move 2", "[D] → [1] → [2] → [3] → [4] → [5] → None",
         "                 ↑                         ↑",
         "                slow                      fast"),
        ("Move 3", "[D] → [1] → [2] → [3] → [4] → [5] → None",
         "                        ↑                        ↑",
         "                       slow                     fast(None)"),
    ]

    for label, diagram, markers, labels in positions:
        print(f"    {label}:")
        print(f"    {diagram}")
        print(f"    {markers}")
        print(f"    {labels}")
        print()

    print("  Step 3: fast = None → STOP!")
    print("    slow is at node [3]")
    print("    slow.next = [4] ← THIS is the node to remove")
    print()

    print("  Step 4: Skip the target node")
    print("    slow.next = slow.next.next")
    print("    [3].next = [5] (skip over [4])")
    print()
    print("    Before: [D] → [1] → [2] → [3] → [4] → [5] → None")
    print("    After:  [D] → [1] → [2] → [3] ─────→ [5] → None")
    print()
    print("    Result: 1 → 2 → 3 → 5 → None ✓")
    print()

    # --- Verify with code ---
    print("--- Code Verification ---")
    print()

    head = build_list([1, 2, 3, 4, 5])
    print(f"  Before:  {to_str(head)}")
    head = remove_nth_from_end(head, 2)
    print(f"  Remove 2nd from end:")
    print(f"  After:   {to_str(head)}")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5], "Remove 2nd from end (4)"),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4], "Remove last (5)"),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5], "Remove first (1)"),
        ([1, 2], 1, [1], "Remove last of two"),
        ([1, 2], 2, [2], "Remove first of two"),
        ([1], 1, [], "Remove only node"),
        ([1, 2, 3], 3, [2, 3], "Remove head"),
        ([10, 20, 30, 40], 2, [10, 20, 40], "Remove 30"),
    ]

    print(f"  {'Input':>20}  | {'n':>2} | {'Expected':>20} | {'Got':>20} | {'✓/✗':>3}")
    print(f"  {'-'*20}  | {'-'*2} | {'-'*20} | {'-'*20} | {'-'*3}")

    for values, n, expected, desc in test_cases:
        head = build_list(values)
        head = remove_nth_from_end(head, n)
        got = to_list(head)
        status = "✓" if got == expected else "✗"
        print(f"  {str(values):>20}  | {n:>2} | {str(expected):>20} | {str(got):>20} | {status:>3}")

    print()

    # --- Why Dummy Node? ---
    print("--- Why Use a Dummy Node? ---")
    print()
    print("  Without dummy, removing the HEAD node is a special case:")
    print("    If n equals list length → we need to remove head")
    print("    But there's no node BEFORE head to update!")
    print()
    print("  With dummy:")
    print("    [dummy] → [1] → [2] → ...")
    print("    Now even head has a predecessor (dummy)")
    print("    All cases handled uniformly!")
    print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Time:  O(L)  — single pass (fast travels L, slow travels L-n)")
    print("  Space: O(1)  — only two pointers + dummy node")
    print()
    print("ANSWER:")
    print("  Use two pointers with a gap of n+1. When fast reaches None,")
    print("  slow is right before the target. Skip the target node.")
    print("  For [1,2,3,4,5] with n=2: removes node 4 → [1,2,3,5]")


if __name__ == "__main__":
    demonstrate()
