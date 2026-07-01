"""
Q7. Write a function that detects the node where a cycle begins in a
    linked list (not just whether a cycle exists). Explain the math.

Answer:
    Phase 1: Floyd's detection — find where slow and fast meet.
    Phase 2: Move one pointer to HEAD, keep the other at meeting point.
             Advance both one step at a time. Where they meet = cycle start!

    THE MATH:
    Let:
        F = distance from head to cycle start
        C = cycle length
        a = distance from cycle start to meeting point

    When slow and fast meet:
        slow traveled: F + a
        fast traveled: F + a + kC  (fast looped k extra times)
        fast = 2 × slow: F + a + kC = 2(F + a)
        Solving: kC = F + a  →  F = kC - a  →  F = (k-1)C + (C - a)

    This means: distance from HEAD to cycle start (F) equals
    distance from MEETING POINT to cycle start (C - a), mod C.

    So moving one pointer from HEAD and one from MEETING POINT
    at the same speed — they meet at the CYCLE START!

    Time: O(n), Space: O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


def build_list_with_cycle(values, cycle_pos=-1):
    if not values:
        return None, None
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    cycle_node = None
    if 0 <= cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]
        cycle_node = nodes[cycle_pos]
    return nodes[0], cycle_node


def detect_cycle_start(head: Node) -> Node:
    """
    Find the node where the cycle begins.

    Phase 1: Floyd's detection (tortoise & hare).
    Phase 2: One pointer at head, one at meeting point.
             Both move 1 step → they meet at cycle start.

    Time:  O(n)
    Space: O(1)

    Returns:
        The node where the cycle starts, or None if no cycle.
    """
    if not head or not head.next:
        return None

    # --- Phase 1: Detect if cycle exists and find meeting point ---
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Cycle detected! Proceed to Phase 2.
            break
    else:
        return None  # No cycle (fast reached end)

    # --- Phase 2: Find the cycle start ---
    # Move one pointer to head, keep the other at meeting point.
    # Advance both one step at a time.
    pointer1 = head
    pointer2 = slow  # Meeting point

    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1  # This is the cycle start!


def demonstrate():
    print("=" * 70)
    print("Q7: Detect Cycle Start Node — The Math Explained")
    print("=" * 70)
    print()

    # --- Problem ---
    print("--- Problem ---")
    print()
    print("  Not just 'is there a cycle?' but 'WHERE does it start?'")
    print()
    print("  Example:")
    print("    [1] → [2] → [3] → [4] → [5] → [6]")
    print("                  ↑                   |")
    print("                  └───────────────────┘")
    print("    Cycle starts at node 3")
    print()

    # --- The Two-Phase Algorithm ---
    print("=" * 70)
    print("THE TWO-PHASE ALGORITHM")
    print("=" * 70)
    print()

    print("  PHASE 1: Floyd's Detection (find meeting point)")
    print("    slow moves 1 step, fast moves 2 steps.")
    print("    They meet somewhere INSIDE the cycle.")
    print()

    print("  PHASE 2: Find Cycle Start")
    print("    Move pointer1 to HEAD.")
    print("    Keep pointer2 at MEETING POINT.")
    print("    Both move 1 step at a time.")
    print("    Where they meet = CYCLE START!")
    print()

    # --- The Math ---
    print("=" * 70)
    print("THE MATH: Why Phase 2 Works")
    print("=" * 70)
    print()

    print("  Define distances:")
    print("    F = head to cycle start")
    print("    C = cycle length")
    print("    a = cycle start to meeting point")
    print()
    print("    ┌──── F ────┐ ┌── a ──┐")
    print("    HEAD ------→ START ---→ MEET")
    print("                  ↑         |")
    print("                  └── C-a ──┘")
    print("                  ←── C ────→ (total cycle)")
    print()

    print("  When slow and fast MEET:")
    print("    slow's distance:  F + a")
    print("    fast's distance:  F + a + k×C   (fast went around k extra times)")
    print("    fast = 2 × slow:  F + a + kC = 2(F + a)")
    print()
    print("  Solving:")
    print("    F + a + kC = 2F + 2a")
    print("    kC = F + a")
    print("    F = kC - a")
    print("    F = (k-1)×C + (C - a)")
    print()
    print("  Key Insight:")
    print("    F ≡ C - a  (mod C)")
    print()
    print("    Distance from HEAD to CYCLE START (F)")
    print("    = Distance from MEETING POINT to CYCLE START (C - a)")
    print("    ... plus some full loops of the cycle (which don't matter)")
    print()
    print("    So if we start one pointer at HEAD and one at MEETING POINT,")
    print("    both moving 1 step at a time, they meet at CYCLE START!")
    print()

    # --- Step-by-Step Trace ---
    print("=" * 70)
    print("TRACE: [1,2,3,4,5,6] with cycle at node 3 (index 2)")
    print("=" * 70)
    print()
    print("    F=2 (head to cycle start)")
    print("    C=4 (cycle length: 3→4→5→6→3)")
    print()
    print("    [1] → [2] → [3] → [4] → [5] → [6]")
    print("                  ↑                   |")
    print("                  └───────────────────┘")
    print()

    print("  PHASE 1: Floyd's Detection")
    print("  ─────────────────────────────")

    phase1_steps = [
        (0, 1, 1, "Both at head"),
        (1, 2, 3, "slow+1, fast+2"),
        (2, 3, 5, "slow+1, fast+2"),
        (3, 4, 3, "slow+1, fast+2 (6→3→4, wraps!)"),
        (4, 5, 5, "slow+1, fast+2 — THEY MEET at 5!"),
    ]

    print(f"    {'Step':>4} | {'Slow':>5} | {'Fast':>5} | {'Note'}")
    print(f"    {'-'*4} | {'-'*5} | {'-'*5} | {'-'*35}")
    for step, s, f, note in phase1_steps:
        met = " ★" if s == f and step > 0 else ""
        print(f"    {step:>4} | {s:>5} | {f:>5} | {note}{met}")

    print()
    print("    Meeting point: Node 5")
    print("    a = 2 (distance from cycle start [3] to meeting point [5])")
    print()

    print("  PHASE 2: Find Cycle Start")
    print("  ─────────────────────────────")
    print("    pointer1 = HEAD (node 1)")
    print("    pointer2 = MEETING POINT (node 5)")
    print()

    phase2_steps = [
        (0, 1, 5, "Start positions"),
        (1, 2, 6, "Both move 1 step"),
        (2, 3, 3, "Both move 1 step — THEY MEET at 3! ★"),
    ]

    print(f"    {'Step':>4} | {'ptr1':>5} | {'ptr2':>5} | {'Note'}")
    print(f"    {'-'*4} | {'-'*5} | {'-'*5} | {'-'*35}")
    for step, p1, p2, note in phase2_steps:
        print(f"    {step:>4} | {p1:>5} | {p2:>5} | {note}")

    print()
    print("    ★ Cycle starts at Node 3!")
    print()
    print("    Verify: F = 2, C-a = 4-2 = 2. Both travel 2 steps → meet at start! ✓")
    print()

    # --- Code Verification ---
    print("--- Code Verification ---")
    print()

    test_cases = [
        ([1, 2, 3, 4, 5, 6], 2, 3, "Cycle at index 2 (node 3)"),
        ([1, 2, 3, 4, 5], 0, 1, "Cycle at index 0 (node 1)"),
        ([1, 2, 3, 4, 5], 4, 5, "Self-loop at last node"),
        ([1, 2, 3, 4, 5], -1, None, "No cycle"),
        ([1, 2], 0, 1, "Small cycle"),
        ([1], 0, 1, "Single node self-loop"),
    ]

    print(f"  {'Values':>20} | {'Cycle At':>8} | {'Expected':>8} | {'Got':>8} | {'✓/✗':>3}")
    print(f"  {'-'*20} | {'-'*8} | {'-'*8} | {'-'*8} | {'-'*3}")

    for values, cycle_pos, expected_data, desc in test_cases:
        head, _ = build_list_with_cycle(values, cycle_pos)
        result = detect_cycle_start(head)
        got = result.data if result else None
        status = "✓" if got == expected_data else "✗"
        cp = str(cycle_pos) if cycle_pos >= 0 else "None"
        got_str = str(got) if got else "None"
        exp_str = str(expected_data) if expected_data else "None"
        print(f"  {str(values):>20} | {cp:>8} | {exp_str:>8} | {got_str:>8} | {status:>3}")

    print()

    # --- Summary ---
    print("--- Complexity ---")
    print()
    print("  Phase 1 (detect): O(n) time, O(1) space")
    print("  Phase 2 (find start): O(n) time, O(1) space")
    print("  Total: O(n) time, O(1) space")
    print()
    print("ANSWER:")
    print("  Phase 1: Floyd's to find meeting point.")
    print("  Phase 2: One pointer from HEAD, one from MEETING POINT,")
    print("  both move 1 step → meet at CYCLE START.")
    print("  Math: F = kC - a, so both travel the same distance to cycle start.")


if __name__ == "__main__":
    demonstrate()
