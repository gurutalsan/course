"""
Q6. Compare arrays vs linked lists: When would you choose a linked list
    over a Python list? Give specific scenarios.

Answer:
    Choose a LINKED LIST when:
    1. Frequent insertions/deletions at the BEGINNING or MIDDLE.
    2. You don't need random access by index.
    3. You need constant-time splicing (joining/splitting lists).
    4. Memory is fragmented (nodes don't need contiguous blocks).

    Choose an ARRAY (Python list) when:
    1. You need fast random access by index — O(1).
    2. You mainly add/remove from the END.
    3. Memory locality matters for cache performance.
    4. You need slicing or sorting.
"""

import time
import sys


class Node:
    """Linked list node for demonstration."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Simple linked list for benchmarking."""
    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def insert_after_node(self, node, data):
        """Insert after a given node reference — O(1)."""
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def delete_head(self):
        if self.head:
            self.head = self.head.next
            self.size -= 1

    def get_nth(self, index):
        curr = self.head
        for _ in range(index):
            if curr is None:
                return None
            curr = curr.next
        return curr


def demonstrate():
    print("=" * 70)
    print("Q6: Arrays vs Linked Lists — When to Choose Each")
    print("=" * 70)
    print()

    # --- Comprehensive Comparison ---
    print("--- Complete Comparison Table ---")
    print()
    print("  Operation              | Array (list)  | Linked List    | Winner")
    print("  -----------------------|---------------|----------------|--------")
    print("  Access by index [i]    | O(1) ★        | O(n)           | Array")
    print("  Search (unsorted)      | O(n)          | O(n)           | Tie")
    print("  Insert at beginning    | O(n)          | O(1) ★         | LL")
    print("  Insert at end          | O(1)*         | O(n) or O(1)** | Array")
    print("  Insert at middle       | O(n)          | O(1)***        | LL")
    print("  Delete from beginning  | O(n)          | O(1) ★         | LL")
    print("  Delete from end        | O(1)          | O(n)           | Array")
    print("  Delete from middle     | O(n)          | O(1)***        | LL")
    print("  Memory per element     | ~8 bytes      | ~48 bytes      | Array")
    print("  Cache performance      | Excellent ★   | Poor           | Array")
    print("  Memory allocation      | Contiguous    | Fragmented     | Depends")
    print("  Resize behavior        | Amortized     | Per-node       | Depends")
    print()
    print("  *  Amortized O(1) for Python list (occasional O(n) resize)")
    print("  ** O(1) if tail pointer is maintained")
    print("  *** O(1) if you have a reference to the insertion point")
    print()

    # --- Performance Benchmarks ---
    print("=" * 70)
    print("BENCHMARK 1: Insert at BEGINNING (n=50,000)")
    print("=" * 70)
    print()

    n = 50_000

    # Array: insert at beginning
    arr = []
    start = time.perf_counter()
    for i in range(n):
        arr.insert(0, i)  # O(n) — shifts all elements
    array_time = (time.perf_counter() - start) * 1000

    # Linked List: insert at beginning
    ll = LinkedList()
    start = time.perf_counter()
    for i in range(n):
        ll.prepend(i)  # O(1) — just update head
    ll_time = (time.perf_counter() - start) * 1000

    print(f"  Array  list.insert(0, x):  {array_time:>10.3f} ms")
    print(f"  LL     prepend(x):         {ll_time:>10.3f} ms")
    print(f"  Winner: {'Linked List' if ll_time < array_time else 'Array'} ({max(array_time, ll_time)/min(array_time, ll_time):.0f}x faster)")
    print()

    print("  Why? Array insert(0) shifts ALL existing elements right — O(n)")
    print("        LL prepend() just creates a node and updates head — O(1)")
    print()

    # --- Benchmark 2: Access by index ---
    print("=" * 70)
    print("BENCHMARK 2: Access by INDEX (n=10,000)")
    print("=" * 70)
    print()

    n = 10_000
    arr = list(range(n))

    ll = LinkedList()
    for i in range(n):
        ll.prepend(n - 1 - i)

    # Array access
    start = time.perf_counter()
    for _ in range(1000):
        _ = arr[n // 2]  # O(1)
    array_time = (time.perf_counter() - start) * 1000

    # LL access
    start = time.perf_counter()
    for _ in range(1000):
        _ = ll.get_nth(n // 2)  # O(n)
    ll_time = (time.perf_counter() - start) * 1000

    print(f"  Array  arr[{n//2}]:      {array_time:>10.3f} ms (1000 accesses)")
    print(f"  LL     get_nth({n//2}):  {ll_time:>10.3f} ms (1000 accesses)")
    print(f"  Winner: {'Array' if array_time < ll_time else 'Linked List'} ({max(array_time, ll_time)/max(min(array_time, ll_time), 0.001):.0f}x faster)")
    print()

    print("  Why? Array[i] = base_address + i × size → O(1) direct jump")
    print("        LL must traverse from head, counting nodes → O(n)")
    print()

    # --- Benchmark 3: Delete from beginning ---
    print("=" * 70)
    print("BENCHMARK 3: Delete from BEGINNING (n=50,000)")
    print("=" * 70)
    print()

    n = 50_000

    # Array
    arr = list(range(n))
    start = time.perf_counter()
    for _ in range(n):
        arr.pop(0)  # O(n) shift
    array_time = (time.perf_counter() - start) * 1000

    # LL
    ll = LinkedList()
    for i in range(n):
        ll.prepend(i)
    start = time.perf_counter()
    for _ in range(n):
        ll.delete_head()  # O(1)
    ll_time = (time.perf_counter() - start) * 1000

    print(f"  Array  pop(0):        {array_time:>10.3f} ms")
    print(f"  LL     delete_head(): {ll_time:>10.3f} ms")
    print(f"  Winner: {'Linked List' if ll_time < array_time else 'Array'}")
    print()

    # --- Memory Comparison ---
    print("=" * 70)
    print("MEMORY COMPARISON")
    print("=" * 70)
    print()

    n = 1000
    arr = list(range(n))
    arr_size = sys.getsizeof(arr) + sum(sys.getsizeof(x) for x in arr)

    node_size = sys.getsizeof(Node(0))
    ll_size = node_size * n

    print(f"  Storing {n} integers:")
    print(f"    Array (Python list): ~{arr_size:,} bytes ({arr_size/n:.1f} bytes/element)")
    print(f"    Linked List:        ~{ll_size:,} bytes ({node_size} bytes/node)")
    print()
    print("  Arrays are MORE memory efficient due to:")
    print("    - No per-element pointer overhead")
    print("    - Contiguous memory (better cache utilization)")
    print()

    # --- Specific Scenarios ---
    print("=" * 70)
    print("WHEN TO CHOOSE EACH")
    print("=" * 70)
    print()

    print("  ╔═══════════════════════════════════════════════════════════════╗")
    print("  ║                  CHOOSE LINKED LIST WHEN:                    ║")
    print("  ╠═══════════════════════════════════════════════════════════════╣")
    print("  ║                                                             ║")
    print("  ║  1. QUEUE Implementation (FIFO)                             ║")
    print("  ║     → Frequent add-to-back + remove-from-front              ║")
    print("  ║     → LL with tail pointer: both O(1)                       ║")
    print("  ║                                                             ║")
    print("  ║  2. Undo/Redo Systems                                       ║")
    print("  ║     → Insert/delete operations in the middle of history     ║")
    print("  ║     → Don't need random access to steps                     ║")
    print("  ║                                                             ║")
    print("  ║  3. Music Playlist / Image Viewer                           ║")
    print("  ║     → Navigate next/previous (doubly linked list)           ║")
    print("  ║     → Easy insert/remove songs without shifting             ║")
    print("  ║                                                             ║")
    print("  ║  4. Memory Allocators                                       ║")
    print("  ║     → Free list management in OS memory management          ║")
    print("  ║     → Blocks scattered in memory, can't use contiguous      ║")
    print("  ║                                                             ║")
    print("  ║  5. Polynomial Math / Sparse Matrices                       ║")
    print("  ║     → Each term is a node; easy to insert/merge terms       ║")
    print("  ║                                                             ║")
    print("  ╚═══════════════════════════════════════════════════════════════╝")
    print()
    print("  ╔═══════════════════════════════════════════════════════════════╗")
    print("  ║                  CHOOSE ARRAY (list) WHEN:                  ║")
    print("  ╠═══════════════════════════════════════════════════════════════╣")
    print("  ║                                                             ║")
    print("  ║  1. Random Access Needed                                    ║")
    print("  ║     → Accessing elements by index: arr[i]                   ║")
    print("  ║     → Binary search, sorting algorithms                     ║")
    print("  ║                                                             ║")
    print("  ║  2. Stack Implementation (LIFO)                             ║")
    print("  ║     → push/pop from end are both O(1)                       ║")
    print("  ║                                                             ║")
    print("  ║  3. Numerical Computation                                   ║")
    print("  ║     → Matrix operations, data processing                    ║")
    print("  ║     → Cache-friendly memory layout = faster iteration       ║")
    print("  ║                                                             ║")
    print("  ║  4. Most General-Purpose Use Cases                          ║")
    print("  ║     → In Python, list is almost always the right choice     ║")
    print("  ║     → Use deque for queue needs                             ║")
    print("  ║                                                             ║")
    print("  ╚═══════════════════════════════════════════════════════════════╝")
    print()

    # --- Summary ---
    print("--- Practical Advice for Python ---")
    print()
    print("  In Python, you almost NEVER need to implement a linked list.")
    print("  Python's built-in list and collections.deque cover most needs.")
    print()
    print("  However, understanding linked lists is crucial because:")
    print("  • They appear in coding interviews constantly")
    print("  • They teach pointer manipulation and memory concepts")
    print("  • They're the foundation for trees, graphs, hash chains")
    print("  • Other languages (C, C++, Java) use them more extensively")
    print()
    print("ANSWER:")
    print("  Choose linked list for frequent beginning/middle insertions,")
    print("  queue implementations, and when you don't need random access.")
    print("  Choose array for index access, cache performance, and sorting.")


if __name__ == "__main__":
    demonstrate()
