"""
Q7. Implement an LRU Cache with O(1) get and put operations.
    Hint: combine a hash map with a doubly linked list.

Answer:
    LRU (Least Recently Used) Cache evicts the least recently accessed
    item when the cache is full.

    Data Structures:
    - Hash map: key → node (for O(1) lookup)
    - Doubly linked list: maintains access order (most recent at head)

    get(key): O(1) — look up in map, move node to head.
    put(key, value): O(1) — insert at head, evict tail if over capacity.
"""


class DLLNode:
    """Doubly linked list node for LRU Cache."""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache: O(1) get and put.

    Structure:
        HashMap: key → DLLNode
        DLL:     HEAD ↔ [most recent] ↔ ... ↔ [least recent] ↔ TAIL
                 (dummy)                                        (dummy)

    On access: move node to right after HEAD (most recent).
    On eviction: remove node right before TAIL (least recent).
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key → DLLNode

        # Dummy head and tail (simplifies edge cases)
        self.head = DLLNode()  # Most recently used end
        self.tail = DLLNode()  # Least recently used end
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DLLNode):
        """Remove a node from the DLL. O(1)."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: DLLNode):
        """Add node right after HEAD (most recently used). O(1)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node: DLLNode):
        """Move existing node to front (mark as most recently used)."""
        self._remove(node)
        self._add_to_front(node)

    def get(self, key: int) -> int:
        """
        Get value by key. Returns -1 if not found.
        Moves accessed node to front (most recently used). O(1).
        """
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair. O(1).
        If cache is full, evict the least recently used item (tail end).
        """
        if key in self.cache:
            # Update existing
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            # Insert new
            if len(self.cache) >= self.capacity:
                # Evict LRU (right before tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            new_node = DLLNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

    def _get_order(self) -> list:
        """Get current order from most to least recently used."""
        order = []
        curr = self.head.next
        while curr != self.tail:
            order.append((curr.key, curr.value))
            curr = curr.next
        return order

    def __repr__(self):
        order = self._get_order()
        items = [f"{k}:{v}" for k, v in order]
        return f"LRU[{' → '.join(items)}] (left=MRU, right=LRU)"


def demonstrate():
    print("=" * 70)
    print("Q7: LRU Cache — O(1) Get and Put")
    print("=" * 70)
    print()

    # --- How it works ---
    print("--- Structure: HashMap + Doubly Linked List ---")
    print()
    print("  HashMap: key → Node (O(1) lookup)")
    print("  DLL:     HEAD ↔ MRU ↔ ... ↔ LRU ↔ TAIL")
    print()
    print("  On GET:  Move accessed node to front")
    print("  On PUT:  Add new node to front; evict from back if full")
    print()

    # --- Step-by-Step Demo ---
    print("=" * 70)
    print("STEP-BY-STEP: LRU Cache with capacity=3")
    print("=" * 70)
    print()

    cache = LRUCache(3)

    operations = [
        ("put", 1, 10, None),
        ("put", 2, 20, None),
        ("put", 3, 30, None),
        ("get", 2, None, 20),
        ("put", 4, 40, None),
        ("get", 1, None, -1),
        ("get", 3, None, 30),
        ("put", 5, 50, None),
        ("get", 2, None, -1),
        ("get", 4, None, 40),
    ]

    print(f"  {'Op':>12} | {'Result':>7} | {'Cache State (MRU → LRU)':>35} | {'Note'}")
    print(f"  {'-'*12} | {'-'*7} | {'-'*35} | {'-'*25}")

    for op, key, val, expected in operations:
        if op == "put":
            cache.put(key, val)
            state = str(cache._get_order())
            evicted = len(cache.cache) < len(cache._get_order()) + 1
            note = ""
            if len(cache._get_order()) == cache.capacity:
                note = "Cache full"
            print(f"  {'put('+str(key)+','+str(val)+')':>12} | {'—':>7} | {state:>35} | {note}")
        else:
            result = cache.get(key)
            state = str(cache._get_order())
            status = "✓" if result == expected else "✗"
            note = "MISS (evicted)" if result == -1 else "HIT → moved to front"
            print(f"  {'get('+str(key)+')':>12} | {result:>7} | {state:>35} | {note} {status}")

    print()

    # --- Visual ---
    print("--- Visual: Eviction Process ---")
    print()
    print("  Capacity = 3. After put(1,10), put(2,20), put(3,30):")
    print()
    print("    HEAD ↔ [3:30] ↔ [2:20] ↔ [1:10] ↔ TAIL")
    print("            MRU                 LRU")
    print()
    print("  get(2): Move 2 to front:")
    print("    HEAD ↔ [2:20] ↔ [3:30] ↔ [1:10] ↔ TAIL")
    print("            MRU                 LRU")
    print()
    print("  put(4,40): Cache full! Evict LRU (key=1):")
    print("    HEAD ↔ [4:40] ↔ [2:20] ↔ [3:30] ↔ TAIL")
    print("            MRU                 LRU")
    print("    Key 1 evicted! get(1) now returns -1.")
    print()

    # --- Why this design? ---
    print("--- Why HashMap + Doubly Linked List? ---")
    print()
    print("  HashMap alone:  O(1) lookup, but can't track access order")
    print("  DLL alone:      O(n) lookup (must traverse to find key)")
    print("  Combined:       O(1) lookup + O(1) order updates!")
    print()
    print("  The DLL node removal/insertion are O(1) because we have")
    print("  DIRECT references to the node (from the HashMap).")
    print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Operation | Time | Why")
    print("  ----------|------|------------------------------------")
    print("  get(key)  | O(1) | HashMap lookup + DLL move-to-front")
    print("  put(k,v)  | O(1) | HashMap insert + DLL add + DLL evict")
    print()
    print("  Space: O(capacity) — bounded by cache size")
    print()

    # --- Test comprehensive ---
    print("--- LeetCode-Style Test ---")
    print()
    lru = LRUCache(2)
    test_ops = [
        ("put", 1, 1, None),
        ("put", 2, 2, None),
        ("get", 1, None, 1),
        ("put", 3, 3, None),    # Evicts key 2
        ("get", 2, None, -1),   # 2 was evicted
        ("put", 4, 4, None),    # Evicts key 1
        ("get", 1, None, -1),   # 1 was evicted
        ("get", 3, None, 3),
        ("get", 4, None, 4),
    ]

    all_pass = True
    for op, key, val, expected in test_ops:
        if op == "put":
            lru.put(key, val)
            print(f"  put({key}, {val})")
        else:
            result = lru.get(key)
            ok = result == expected
            if not ok: all_pass = False
            print(f"  get({key}) → {result} (expected {expected}) {'✓' if ok else '✗'}")

    print(f"\n  All passed: {'✓' if all_pass else '✗'}")
    print()
    print("ANSWER: Combine HashMap (O(1) lookup) + Doubly Linked List (O(1) reorder).")
    print("Access moves node to front. Eviction removes from back. Both O(1).")


if __name__ == "__main__":
    demonstrate()
