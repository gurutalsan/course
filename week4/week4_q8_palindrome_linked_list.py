"""
Q8. Implement a function that checks if a linked list is a palindrome
    using O(n) time and O(1) extra space. Hint: reverse the second half.

Answer:
    Algorithm:
    1. Find the middle of the list using slow/fast pointers.
    2. Reverse the second half in-place.
    3. Compare the first half with the reversed second half.
    4. (Optional) Restore the list by reversing the second half again.

    Time Complexity:  O(n) — three O(n) passes: find middle + reverse + compare.
    Space Complexity: O(1) — only pointer variables, no extra data structures!
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
    count = 0
    while curr and count < 20:
        parts.append(str(curr.data))
        curr = curr.next
        count += 1
    return " → ".join(parts) + " → None"


def to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result


def reverse_list(head: Node) -> Node:
    """Reverse a linked list in-place. Returns new head."""
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


# ============================================================
# Optimal: O(n) time, O(1) space ★
# ============================================================
def is_palindrome(head: Node) -> bool:
    """
    Check if a linked list is a palindrome.

    Algorithm:
    1. Find middle using slow/fast pointers.
    2. Reverse the second half.
    3. Compare first half with reversed second half.
    4. Restore the list (optional but good practice).

    Time:  O(n) — three linear passes.
    Space: O(1) — only pointer variables!
    """
    if not head or not head.next:
        return True

    # --- Step 1: Find the middle ---
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # slow is now at the middle (or left-middle for even length)

    # --- Step 2: Reverse the second half ---
    second_half_start = slow.next
    slow.next = None  # Split the list
    reversed_second = reverse_list(second_half_start)

    # --- Step 3: Compare both halves ---
    p1 = head
    p2 = reversed_second
    is_palin = True

    while p1 and p2:
        if p1.data != p2.data:
            is_palin = False
            break
        p1 = p1.next
        p2 = p2.next

    # --- Step 4: Restore the list (optional) ---
    slow.next = reverse_list(reversed_second)

    return is_palin


# ============================================================
# For comparison: O(n) time, O(n) space
# ============================================================
def is_palindrome_extra_space(head: Node) -> bool:
    """
    Check palindrome using a Python list — O(n) space.
    Simple but uses extra memory.
    """
    values = to_list(head)
    return values == values[::-1]


# ============================================================
# For comparison: Stack-based — O(n) space
# ============================================================
def is_palindrome_stack(head: Node) -> bool:
    """
    Check palindrome using a stack to compare against first half.
    Time: O(n), Space: O(n).
    """
    # Push all values onto stack
    stack = []
    curr = head
    while curr:
        stack.append(curr.data)
        curr = curr.next

    # Compare from head with stack (LIFO = reversed order)
    curr = head
    while curr:
        if curr.data != stack.pop():
            return False
        curr = curr.next

    return True


def demonstrate():
    print("=" * 70)
    print("Q8: Linked List Palindrome Check — O(1) Space")
    print("=" * 70)
    print()

    # --- Problem ---
    print("--- Problem ---")
    print()
    print("  Palindrome: reads the same forward and backward.")
    print()
    print("  1 → 2 → 3 → 2 → 1 → None   ← Palindrome ✓")
    print("  1 → 2 → 3 → 4 → 5 → None   ← NOT palindrome ✗")
    print()
    print("  Challenge: Do it in O(1) extra space (no arrays/stacks)!")
    print()

    # --- Algorithm Overview ---
    print("--- Algorithm: Reverse Second Half ---")
    print()
    print("  Step 1: Find the middle (slow/fast pointers)")
    print("  Step 2: Reverse the second half in-place")
    print("  Step 3: Compare first half with reversed second half")
    print("  Step 4: Restore the list (optional)")
    print()

    # --- Detailed Trace: Odd Length ---
    print("=" * 70)
    print("TRACE: 1 → 2 → 3 → 2 → 1 (Palindrome, odd length)")
    print("=" * 70)
    print()

    print("  Step 1: Find Middle (slow/fast)")
    print()
    print("    Init:    [1] → [2] → [3] → [2] → [1] → None")
    print("              S                              ")
    print("              F                              ")
    print()
    print("    Move 1:  [1] → [2] → [3] → [2] → [1] → None")
    print("                    S                        ")
    print("                          F                  ")
    print()
    print("    Move 2:  [1] → [2] → [3] → [2] → [1] → None")
    print("                          S                  ")
    print("                                       F     ")
    print()
    print("    fast.next.next = None → STOP. Middle = node [3]")
    print()

    print("  Step 2: Split and Reverse Second Half")
    print()
    print("    Split at middle:")
    print("      First half:  [1] → [2] → [3] → None")
    print("      Second half: [2] → [1] → None")
    print()
    print("    Reverse second half:")
    print("      Reversed:    [1] → [2] → None")
    print()

    print("  Step 3: Compare")
    print()
    print("    p1: [1] → [2] → [3] → None")
    print("    p2: [1] → [2] → None")
    print()
    print("    Compare 1 == 1? ✓")
    print("    Compare 2 == 2? ✓")
    print("    p2 = None → DONE! Palindrome ✓")
    print()
    print("    (Middle element [3] doesn't need comparison — it's the center)")
    print()

    # --- Trace: Even Length ---
    print("=" * 70)
    print("TRACE: 1 → 2 → 2 → 1 (Palindrome, even length)")
    print("=" * 70)
    print()

    print("  Step 1: Find Middle")
    print("    [1] → [2] → [2] → [1] → None")
    print("           S")
    print("                  F")
    print("    fast.next.next = None → STOP. Middle = node [2] (left-middle)")
    print()

    print("  Step 2: Split and Reverse")
    print("    First:    [1] → [2] → None")
    print("    Second:   [2] → [1] → None  → reversed → [1] → [2] → None")
    print()

    print("  Step 3: Compare")
    print("    [1] == [1]? ✓    [2] == [2]? ✓   → Palindrome ✓")
    print()

    # --- Trace: NOT palindrome ---
    print("=" * 70)
    print("TRACE: 1 → 2 → 3 (NOT a palindrome)")
    print("=" * 70)
    print()
    print("  Middle = [2]")
    print("  First half:    [1] → [2] → None")
    print("  Second half:   [3] → None → reversed → [3] → None")
    print("  Compare: 1 != 3 → NOT palindrome ✗")
    print()

    # --- Code Verification ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([1, 2, 3, 2, 1], True, "Odd palindrome"),
        ([1, 2, 2, 1], True, "Even palindrome"),
        ([1, 2, 3], False, "Not palindrome"),
        ([1], True, "Single element"),
        ([1, 1], True, "Two same"),
        ([1, 2], False, "Two different"),
        ([], True, "Empty list"),
        ([1, 2, 3, 4, 3, 2, 1], True, "Longer palindrome"),
        ([1, 2, 3, 4, 5, 6], False, "Longer non-palindrome"),
        ([5, 5, 5, 5, 5], True, "All same"),
        ([1, 0, 0, 1], True, "With zeros"),
    ]

    print(f"  {'Input':>25}  | {'Expected':>8} | {'O(1) sp':>7} | {'O(n) sp':>7} | {'Stack':>5} | {'✓/✗':>3}")
    print(f"  {'-'*25}  | {'-'*8} | {'-'*7} | {'-'*7} | {'-'*5} | {'-'*3}")

    all_pass = True
    for values, expected, desc in test_cases:
        head1 = build_list(values)
        head2 = build_list(values)
        head3 = build_list(values)

        r1 = is_palindrome(head1)
        r2 = is_palindrome_extra_space(head2)
        r3 = is_palindrome_stack(head3)

        status = "✓" if r1 == r2 == r3 == expected else "✗"
        if r1 != expected:
            all_pass = False

        vals_str = str(values) if len(str(values)) <= 23 else str(values)[:20] + "..."
        print(f"  {vals_str:>25}  | {str(expected):>8} | {str(r1):>7} | {str(r2):>7} | {str(r3):>5} | {status:>3}")

    print()
    print(f"  All tests passed: {'✓ YES' if all_pass else '✗ NO'}")
    print()

    # Verify list restoration
    print("--- Verify List Restoration ---")
    print()
    values = [1, 2, 3, 2, 1]
    head = build_list(values)
    print(f"  Before: {to_str(head)}")
    result = is_palindrome(head)
    print(f"  After:  {to_str(head)}")
    print(f"  Restored correctly: {to_list(head) == values}")
    print()

    # --- Method Comparison ---
    print("--- Method Comparison ---")
    print()
    print("  Method              | Time | Space | Technique")
    print("  --------------------|------|-------|---------------------------")
    print("  Reverse 2nd half ★  | O(n) | O(1)  | Split + reverse + compare")
    print("  Copy to array       | O(n) | O(n)  | list == list[::-1]")
    print("  Stack               | O(n) | O(n)  | Push all, compare LIFO")
    print("  Recursive           | O(n) | O(n)  | Compare via call stack")
    print()
    print("ANSWER:")
    print("  1. Find middle with slow/fast pointers.")
    print("  2. Reverse second half in-place.")
    print("  3. Compare first half with reversed second half.")
    print("  O(n) time, O(1) space — no extra data structures needed!")


if __name__ == "__main__":
    demonstrate()
