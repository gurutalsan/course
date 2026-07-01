"""
Q1. Implement a complete LinkedList class with: append, prepend,
    delete_by_value, search, and print_list methods. Test each method.

Answer:
    A singly linked list stores data in NODES. Each node has:
    - data: the value stored
    - next: a pointer/reference to the next node

    Head → [data|next] → [data|next] → [data|next] → None

    Key Operations:
    - append:          O(n) — traverse to end, add node
    - prepend:         O(1) — add node before head
    - delete_by_value: O(n) — find and remove node
    - search:          O(n) — traverse until found
    - print_list:      O(n) — traverse and print all
"""


class Node:
    """A single node in the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """
    Singly Linked List implementation with full CRUD operations.

    Structure:
        head → [data|next] → [data|next] → ... → None

    Time Complexities:
        append:          O(n) — must traverse to find the end
        prepend:         O(1) — insert at head
        delete_by_value: O(n) — must search for the value
        search:          O(n) — linear scan
        print_list:      O(n) — visit every node
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def append(self, data) -> None:
        """
        Add a node at the END of the list.

        Time:  O(n) — traverse to the last node.
        Space: O(1) — create one new node.
        """
        new_node = Node(data)

        # If list is empty, new node becomes head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head
        while current.next is not None:
            current = current.next

        # Link the last node to the new node
        current.next = new_node

    def prepend(self, data) -> None:
        """
        Add a node at the BEGINNING of the list.

        Time:  O(1) — just update head pointer.
        Space: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head  # Point new node to current head
        self.head = new_node       # Update head to new node

    def delete_by_value(self, value) -> bool:
        """
        Delete the FIRST node with the given value.

        Time:  O(n) — may need to traverse entire list.
        Space: O(1)

        Returns:
            True if node was found and deleted, False otherwise.
        """
        if self.head is None:
            return False

        # Special case: head node has the target value
        if self.head.data == value:
            self.head = self.head.next
            return True

        # Traverse to find the node BEFORE the target
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                # Skip over the target node (unlink it)
                current.next = current.next.next
                return True
            current = current.next

        return False  # Value not found

    def search(self, value) -> tuple:
        """
        Search for a value in the list.

        Time:  O(n)
        Space: O(1)

        Returns:
            (found: bool, position: int) — position is 0-indexed, -1 if not found.
        """
        current = self.head
        position = 0

        while current is not None:
            if current.data == value:
                return True, position
            current = current.next
            position += 1

        return False, -1

    def print_list(self) -> str:
        """
        Print the linked list in a visual format.

        Time:  O(n) — visit every node.
        Space: O(n) — build string representation.

        Returns:
            String representation like "1 → 2 → 3 → None"
        """
        elements = []
        current = self.head

        while current is not None:
            elements.append(str(current.data))
            current = current.next

        result = " → ".join(elements) + " → None"
        return result

    def to_list(self) -> list:
        """Convert linked list to Python list for easy comparison."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        return self.print_list()


def demonstrate():
    print("=" * 70)
    print("Q1: Complete LinkedList Class Implementation")
    print("=" * 70)
    print()

    # --- Structure Explanation ---
    print("--- Linked List Structure ---")
    print()
    print("  Node: [data | next] → points to the next node (or None)")
    print()
    print("  LinkedList:")
    print("    head → [10|→] → [20|→] → [30|→] → None")
    print()
    print("  Each node is an independent object in memory.")
    print("  Unlike arrays, nodes are NOT stored contiguously.")
    print()

    # ==========================================
    # TEST: append()
    # ==========================================
    print("=" * 70)
    print("TEST 1: append() — Add to end")
    print("=" * 70)
    print()

    ll = LinkedList()
    print(f"  Empty list:  {ll.print_list()}")
    print(f"  Length: {len(ll)}")
    print()

    for val in [10, 20, 30, 40, 50]:
        ll.append(val)
        print(f"  append({val}):  {ll.print_list()}")

    print()
    print(f"  Final length: {len(ll)}")
    print(f"  As Python list: {ll.to_list()}")
    print()

    # ==========================================
    # TEST: prepend()
    # ==========================================
    print("=" * 70)
    print("TEST 2: prepend() — Add to beginning")
    print("=" * 70)
    print()

    ll2 = LinkedList()
    for val in [30, 20, 10]:
        ll2.prepend(val)
        print(f"  prepend({val}): {ll2.print_list()}")

    print()
    print("  Notice: prepend inserts at the HEAD, so the order is reversed!")
    print()

    # Prepend to existing list
    print("  Prepending 5 to existing list [10, 20, 30, 40, 50]:")
    ll.prepend(5)
    print(f"  prepend(5): {ll.print_list()}")
    print()

    # ==========================================
    # TEST: search()
    # ==========================================
    print("=" * 70)
    print("TEST 3: search() — Find a value")
    print("=" * 70)
    print()

    print(f"  List: {ll.print_list()}")
    print()

    search_tests = [10, 30, 50, 99, 5]
    print(f"  {'Value':>7} | {'Found':>5} | {'Position':>8} | {'Note'}")
    print(f"  {'-'*7} | {'-'*5} | {'-'*8} | {'-'*20}")

    for val in search_tests:
        found, pos = ll.search(val)
        note = f"At index {pos}" if found else "Not in list"
        print(f"  {val:>7} | {str(found):>5} | {pos:>8} | {note}")

    print()

    # ==========================================
    # TEST: delete_by_value()
    # ==========================================
    print("=" * 70)
    print("TEST 4: delete_by_value() — Remove a node")
    print("=" * 70)
    print()

    print(f"  Before: {ll.print_list()}")
    print()

    delete_tests = [
        (30, "Delete middle node (30)"),
        (5, "Delete head node (5)"),
        (50, "Delete tail node (50)"),
        (99, "Delete non-existent (99)"),
    ]

    for val, desc in delete_tests:
        success = ll.delete_by_value(val)
        status = "✓ Deleted" if success else "✗ Not found"
        print(f"  {desc}")
        print(f"    delete({val}): {status}")
        print(f"    List now: {ll.print_list()}")
        print()

    # ==========================================
    # TEST: Edge Cases
    # ==========================================
    print("=" * 70)
    print("TEST 5: Edge Cases")
    print("=" * 70)
    print()

    # Empty list operations
    empty = LinkedList()
    print(f"  Empty list: {empty.print_list()}")
    print(f"  search(1): {empty.search(1)}")
    print(f"  delete(1): {empty.delete_by_value(1)}")
    print()

    # Single element
    single = LinkedList()
    single.append(42)
    print(f"  Single element: {single.print_list()}")
    print(f"  search(42): {single.search(42)}")
    print(f"  delete(42): {single.delete_by_value(42)}")
    print(f"  After delete: {single.print_list()}")
    print()

    # --- How Each Operation Works (Visual) ---
    print("=" * 70)
    print("HOW EACH OPERATION WORKS (Visual)")
    print("=" * 70)
    print()

    print("  APPEND(40):")
    print("    head → [10|→] → [20|→] → [30|→] → None")
    print("                                 ↓")
    print("    head → [10|→] → [20|→] → [30|→] → [40|→] → None")
    print()

    print("  PREPEND(5):")
    print("    head → [10|→] → [20|→] → [30|→] → None")
    print("      ↓")
    print("    head → [5|→] → [10|→] → [20|→] → [30|→] → None")
    print()

    print("  DELETE(20):")
    print("    head → [10|→] → [20|→] → [30|→] → None")
    print("                      ↓ skip")
    print("    head → [10|→] ─────────→ [30|→] → None")
    print("                    [20|→] (orphaned, garbage collected)")
    print()

    print("  SEARCH(30):")
    print("    head → [10|→] → [20|→] → [30|→] → None")
    print("            ✗ 10     ✗ 20     ✓ 30! (pos=2)")
    print()

    # --- Complexity Summary ---
    print("--- Complexity Summary ---")
    print()
    print("  Operation       | Time  | Space | Notes")
    print("  ----------------|-------|-------|------------------------")
    print("  append(val)     | O(n)  | O(1)  | Traverse to end")
    print("  prepend(val)    | O(1)  | O(1)  | Update head pointer")
    print("  delete(val)     | O(n)  | O(1)  | Find + unlink node")
    print("  search(val)     | O(n)  | O(1)  | Linear scan")
    print("  print_list()    | O(n)  | O(n)  | Visit all nodes")
    print()
    print("  Note: append can be made O(1) by maintaining a 'tail' pointer.")


if __name__ == "__main__":
    demonstrate()
