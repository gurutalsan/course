"""
Q1. What is the time complexity of accessing the 5th element of a Python list? Explain why.

Answer: O(1) — Constant Time

Explanation:
    Python lists are implemented as dynamic arrays (contiguous blocks of memory
    containing pointers/references to objects). Each element's memory address can
    be calculated directly using:

        address = base_address + (index * pointer_size)

    This means accessing ANY element by index (whether it's the 1st or the
    1,000,000th) takes the same constant amount of time — O(1).

    This is fundamentally different from a linked list, where you'd need to
    traverse from the head node to reach the desired position — O(n).
"""

import time


def demonstrate_constant_time_access():
    """Demonstrate that list access time is constant regardless of index."""

    # Create a large list
    large_list = list(range(10_000_000))  # 10 million elements

    # --- Access the 5th element ---
    start = time.perf_counter_ns()
    _ = large_list[4]  # 0-indexed, so index 4 = 5th element
    end = time.perf_counter_ns()
    time_5th = end - start

    # --- Access the 5,000,000th element ---
    start = time.perf_counter_ns()
    _ = large_list[4_999_999]
    end = time.perf_counter_ns()
    time_5millionth = end - start

    # --- Access the last element ---
    start = time.perf_counter_ns()
    _ = large_list[-1]
    end = time.perf_counter_ns()
    time_last = end - start

    print("=" * 60)
    print("Q1: Time Complexity of Accessing the 5th Element")
    print("=" * 60)
    print()
    print("Python lists use DYNAMIC ARRAYS (contiguous memory).")
    print("Element address = base_address + (index × pointer_size)")
    print("=> ANY index access is O(1) — constant time.")
    print()
    print("--- Timing Demonstration ---")
    print(f"  Access 5th element (index 4):          {time_5th:>6} ns")
    print(f"  Access 5,000,000th element (index ~5M): {time_5millionth:>6} ns")
    print(f"  Access last element (index ~10M):        {time_last:>6} ns")
    print()
    print("All access times are roughly the same → O(1) confirmed.")
    print()

    # Comparison: List vs Linked List (simulated)
    print("--- Comparison: Array (list) vs Linked List ---")
    print()
    print("  Operation          | Array (Python list) | Linked List")
    print("  -------------------|--------------------|-----------")
    print("  Access by index    | O(1)               | O(n)")
    print("  Search (unsorted)  | O(n)               | O(n)")
    print("  Insert at end      | O(1) amortized     | O(1) if tail ref")
    print("  Insert at start    | O(n)               | O(1)")
    print()
    print("ANSWER: Accessing the 5th element of a Python list is O(1).")


if __name__ == "__main__":
    demonstrate_constant_time_access()
