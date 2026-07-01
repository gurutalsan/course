"""
Q3. Implement Floyd's Cycle Detection algorithm. Explain why the fast
    pointer moves 2 steps and the slow pointer moves 1 step.

Answer:
    Floyd's Cycle Detection (Tortoise and Hare Algorithm):
    - SLOW pointer moves 1 step at a time.
    - FAST pointer moves 2 steps at a time.
    - If there's a cycle, they WILL meet inside the cycle.
    - If there's no cycle, fast pointer reaches None.

    WHY 2 steps and 1 step?
    The relative speed difference is 1. In each iteration, the fast
    pointer CLOSES THE GAP by exactly 1 node. This guarantees they
    meet within one full traversal of the cycle, giving O(n) time.

    If fast moved 3 steps (gap closes by 2), it could SKIP over slow
    in cycles with odd length, requiring more complex analysis.

    Time Complexity:  O(n)
    Space Complexity: O(1) — only two pointers!
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


def has_cycle(head: Node) -> bool:
    """
    Floyd's Cycle Detection Algorithm (Tortoise and Hare).

    Two pointers:
    - slow: moves 1 step per iteration
    - fast: moves 2 steps per iteration

    If they meet → cycle exists.
    If fast reaches None → no cycle.

    Time:  O(n) — fast traverses at most 2n nodes.
    Space: O(1) — only two pointer variables.
    """
    if head is None or head.next is None:
        return False

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next          # Move 1 step
        fast = fast.next.next     # Move 2 steps

        if slow == fast:          # They met → cycle!
            return True

    return False  # fast reached end → no cycle


def has_cycle_with_trace(head: Node) -> tuple:
    """
    Floyd's algorithm with step-by-step trace for visualization.
    Returns (has_cycle, steps_log).
    """
    if head is None or head.next is None:
        return False, []

    slow = head
    fast = head
    steps = []
    step_num = 0

    while fast is not None and fast.next is not None:
        step_num += 1
        slow = slow.next
        fast = fast.next.next

        steps.append({
            'step': step_num,
            'slow': slow.data if slow else None,
            'fast': fast.data if fast else None,
            'met': slow == fast
        })

        if slow == fast:
            return True, steps

    return False, steps


# ============================================================
# Alternative: Hash Set method (for comparison)
# ============================================================
def has_cycle_hashset(head: Node) -> bool:
    """
    Detect cycle using a hash set — stores visited nodes.

    Time:  O(n)
    Space: O(n) — stores all visited nodes.
    """
    visited = set()
    current = head

    while current:
        if id(current) in visited:
            return True
        visited.add(id(current))
        current = current.next

    return False


def build_list_with_cycle(values: list, cycle_pos: int = -1) -> Node:
    """
    Build a linked list, optionally with a cycle.

    Args:
        values: List of values for nodes.
        cycle_pos: Index of node where tail connects back to.
                   -1 means no cycle.
    """
    if not values:
        return None

    nodes = []
    for val in values:
        nodes.append(Node(val))

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if cycle_pos >= 0 and cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]  # Create cycle

    return nodes[0]


def demonstrate():
    print("=" * 70)
    print("Q3: Floyd's Cycle Detection Algorithm")
    print("=" * 70)
    print()

    # --- What is a Cycle? ---
    print("--- What is a Cycle in a Linked List? ---")
    print()
    print("  Normal list (no cycle):")
    print("    [1] → [2] → [3] → [4] → [5] → None")
    print()
    print("  List WITH a cycle:")
    print("    [1] → [2] → [3] → [4] → [5]")
    print("                 ↑               |")
    print("                 └───────────────┘")
    print("    Node 5's next points back to Node 3!")
    print("    Traversing this list would loop forever.")
    print()

    # --- The Algorithm ---
    print("--- Floyd's Tortoise and Hare Algorithm ---")
    print()
    print("  Two pointers start at the head:")
    print("    🐢 Slow (tortoise): moves 1 step at a time")
    print("    🐇 Fast (hare):     moves 2 steps at a time")
    print()
    print("  If there's a cycle:")
    print("    Both pointers enter the cycle.")
    print("    Fast gains 1 node per step on slow.")
    print("    Eventually, fast catches up → they MEET → cycle detected!")
    print()
    print("  If there's NO cycle:")
    print("    Fast pointer reaches None → no cycle.")
    print()

    # --- Step-by-Step Trace WITH Cycle ---
    print("=" * 70)
    print("TRACE 1: List with Cycle — [1,2,3,4,5] cycle at node 3 (index 2)")
    print("=" * 70)
    print()
    print("    [1] → [2] → [3] → [4] → [5]")
    print("                 ↑               |")
    print("                 └───────────────┘")
    print()

    head_cycle = build_list_with_cycle([1, 2, 3, 4, 5], cycle_pos=2)
    has_c, steps = has_cycle_with_trace(head_cycle)

    print(f"  {'Step':>4} | {'Slow (🐢)':>10} | {'Fast (🐇)':>10} | {'Met?':>5}")
    print(f"  {'-'*4} | {'-'*10} | {'-'*10} | {'-'*5}")
    print(f"  {'init':>4} | {'1':>10} | {'1':>10} | {'—':>5}")

    for s in steps:
        met = "✓ YES!" if s['met'] else "No"
        print(f"  {s['step']:>4} | {s['slow']:>10} | {str(s['fast']):>10} | {met:>5}")

    print()
    print(f"  Cycle detected: {has_c}")
    print()

    # --- Detailed movement trace ---
    print("  Detailed pointer movement:")
    print()
    print("  Init:   🐢=1, 🐇=1")
    print("    [🐢🐇1] → [2] → [3] → [4] → [5] ─┐")
    print("                      ↑                  |")
    print("                      └──────────────────┘")
    print()
    print("  Step 1: 🐢→2 (1 hop), 🐇→3 (2 hops)")
    print("    [1] → [🐢2] → [🐇3] → [4] → [5] ─┐")
    print("                    ↑                    |")
    print("                    └────────────────────┘")
    print()
    print("  Step 2: 🐢→3, 🐇→5")
    print("    [1] → [2] → [🐢3] → [4] → [🐇5] ─┐")
    print("                  ↑                      |")
    print("                  └──────────────────────┘")
    print()
    print("  Step 3: 🐢→4, 🐇→4  (🐇 wraps: 5→3→4)")
    print("    [1] → [2] → [3] → [🐢🐇4] → [5] ─┐")
    print("                  ↑                      |")
    print("                  └──────────────────────┘")
    print("    THEY MET at node 4! → Cycle confirmed! ✓")
    print()

    # --- Trace WITHOUT Cycle ---
    print("=" * 70)
    print("TRACE 2: List without Cycle — [1,2,3,4,5]")
    print("=" * 70)
    print()
    print("    [1] → [2] → [3] → [4] → [5] → None")
    print()

    head_no_cycle = build_list_with_cycle([1, 2, 3, 4, 5], cycle_pos=-1)
    has_c, steps = has_cycle_with_trace(head_no_cycle)

    print(f"  {'Step':>4} | {'Slow (🐢)':>10} | {'Fast (🐇)':>10} | {'Met?':>5}")
    print(f"  {'-'*4} | {'-'*10} | {'-'*10} | {'-'*5}")

    for s in steps:
        fast_str = str(s['fast']) if s['fast'] is not None else "None"
        print(f"  {s['step']:>4} | {s['slow']:>10} | {fast_str:>10} | {'No':>5}")

    print()
    print(f"  Fast reached None → No cycle! ({has_c})")
    print()

    # --- WHY 2 Steps and 1 Step? ---
    print("=" * 70)
    print("WHY does fast move 2 steps and slow move 1 step?")
    print("=" * 70)
    print()
    print("  1. RELATIVE SPEED = 1")
    print("     Fast moves 2, slow moves 1 → gap closes by 1 each step.")
    print("     No matter the cycle size, they WILL meet.")
    print()
    print("  2. GUARANTEED MEETING")
    print("     If cycle has length C, once both are in the cycle,")
    print("     the gap between them decreases by 1 each step.")
    print("     After at most C steps, gap = 0 → they meet!")
    print()
    print("  3. WHY NOT 3 STEPS?")
    print("     If fast moves 3, relative speed = 2.")
    print("     Fast could SKIP over slow in odd-length cycles.")
    print("     Example: cycle of 3, fast jumps from position behind")
    print("     slow to position ahead of slow without meeting.")
    print()
    print("     With speed difference = 1, this can NEVER happen.")
    print()
    print("  4. MATHEMATICAL PROOF:")
    print("     Let's say slow has traveled distance d when it enters cycle.")
    print("     At that point, fast has traveled 2d.")
    print("     Both are in the cycle. Distance between them = (2d - d) mod C.")
    print("     Each step reduces this distance by 1.")
    print("     After at most C steps → distance = 0 → they meet!")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([1, 2, 3, 4, 5], 2, True, "Cycle to node at index 2"),
        ([1, 2, 3, 4, 5], -1, False, "No cycle"),
        ([1, 2], 0, True, "Cycle: 2→1 (small cycle)"),
        ([1], 0, True, "Self-loop"),
        ([1], -1, False, "Single node, no cycle"),
        ([], -1, False, "Empty list"),
        ([1, 2, 3, 4, 5, 6], 3, True, "Cycle to node at index 3"),
    ]

    print(f"  {'Values':>20}  | {'Cycle At':>8} | {'Expected':>8} | {'Floyd':>6} | {'Hash':>5} | {'✓/✗':>3}")
    print(f"  {'-'*20}  | {'-'*8} | {'-'*8} | {'-'*6} | {'-'*5} | {'-'*3}")

    for values, cycle_pos, expected, desc in test_cases:
        head = build_list_with_cycle(values, cycle_pos)
        result_floyd = has_cycle(head)
        result_hash = has_cycle_hashset(head)
        status = "✓" if result_floyd == expected else "✗"
        cp = str(cycle_pos) if cycle_pos >= 0 else "None"
        print(f"  {str(values):>20}  | {cp:>8} | {str(expected):>8} | {str(result_floyd):>6} | {str(result_hash):>5} | {status:>3}")

    print()

    # --- Comparison ---
    print("--- Method Comparison ---")
    print()
    print("  Method             | Time | Space | Notes")
    print("  -------------------|------|-------|---------------------------")
    print("  Floyd's (2-ptr) ★  | O(n) | O(1)  | No extra memory!")
    print("  Hash Set           | O(n) | O(n)  | Stores visited nodes")
    print()
    print("ANSWER:")
    print("  Floyd's uses O(1) space with slow (1-step) and fast (2-step) pointers.")
    print("  Speed difference of 1 guarantees meeting within the cycle.")
    print("  Fast moves 2 steps because it creates a relative speed of exactly 1,")
    print("  ensuring the gap closes by 1 each iteration — no skipping possible.")


if __name__ == "__main__":
    demonstrate()
