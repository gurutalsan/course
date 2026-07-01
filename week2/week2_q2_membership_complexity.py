"""
Q2. What is the time complexity of checking if an element exists in:
    (a) a list, (b) a set, (c) a dictionary? Why are they different?

Answer:
    (a) List:       O(n)  — Linear scan; must check each element sequentially.
    (b) Set:        O(1)  — Hash-based; computes hash → jumps directly to bucket.
    (c) Dictionary: O(1)  — Hash-based (keys are hashed); same mechanism as sets.

    Why different?
    - Lists store elements in contiguous memory. To find an element, Python
      must iterate from the beginning until it finds a match → O(n).
    - Sets and dicts use HASH TABLES. They compute a hash of the element/key,
      which maps directly to a memory location (bucket) → O(1) average case.
"""

import time
import random


def benchmark_membership_test(n: int, target_present: bool = False):
    """
    Benchmark 'element in container' for list, set, and dict.

    Args:
        n: Number of elements in each container.
        target_present: If True, search for an element that exists.
                        If False, search for one that doesn't (worst case for list).
    """
    # Build containers with the same data
    data = list(range(n))
    data_list = data[:]
    data_set = set(data)
    data_dict = {x: True for x in data}

    # Element to search for
    if target_present:
        target = n - 1  # Last element (worst case for list even when present)
    else:
        target = n + 999  # Element that doesn't exist

    # Number of lookups to get stable timing
    repeats = 1000

    # --- List lookup ---
    start = time.perf_counter()
    for _ in range(repeats):
        _ = target in data_list
    list_time = (time.perf_counter() - start) / repeats * 1_000_000  # microseconds

    # --- Set lookup ---
    start = time.perf_counter()
    for _ in range(repeats):
        _ = target in data_set
    set_time = (time.perf_counter() - start) / repeats * 1_000_000

    # --- Dict lookup ---
    start = time.perf_counter()
    for _ in range(repeats):
        _ = target in data_dict
    dict_time = (time.perf_counter() - start) / repeats * 1_000_000

    return list_time, set_time, dict_time


def demonstrate():
    print("=" * 70)
    print("Q2: Membership Test Complexity — List vs Set vs Dictionary")
    print("=" * 70)
    print()

    # --- How each structure works internally ---
    print("--- How Each Structure Works ---")
    print()
    print("  LIST (array-based):")
    print("    [10, 25, 7, 42, 3, ...]")
    print("     ↓")
    print("    'Is 42 in the list?'")
    print("    Check index 0 (10) → no")
    print("    Check index 1 (25) → no")
    print("    Check index 2 (7)  → no")
    print("    Check index 3 (42) → YES! (had to check 4 elements)")
    print("    → LINEAR SCAN: O(n)")
    print()
    print("  SET (hash table):")
    print("    {10, 25, 7, 42, 3, ...}")
    print("     ↓")
    print("    'Is 42 in the set?'")
    print("    hash(42) → bucket index 6")
    print("    Check bucket 6 → 42 is there → YES! (1 lookup)")
    print("    → HASH LOOKUP: O(1)")
    print()
    print("  DICTIONARY (hash table for keys):")
    print("    {10: 'a', 25: 'b', 7: 'c', 42: 'd', ...}")
    print("     ↓")
    print("    'Is 42 in the dict?' (checks KEYS)")
    print("    hash(42) → bucket index 6")
    print("    Check bucket 6 → key 42 exists → YES! (1 lookup)")
    print("    → HASH LOOKUP: O(1)")
    print()

    # --- Complexity Summary ---
    print("--- Time Complexity Summary ---")
    print()
    print("  Operation: 'element in container'")
    print()
    print("  Container   | Average Case | Worst Case | Why")
    print("  ------------|-------------|------------|---------------------------")
    print("  List        | O(n)        | O(n)       | Sequential scan required")
    print("  Set         | O(1)        | O(n)*      | Hash → direct bucket lookup")
    print("  Dictionary  | O(1)        | O(n)*      | Hash → direct bucket lookup")
    print()
    print("  * Worst case O(n) for set/dict only happens with extreme hash")
    print("    collisions (all elements hash to the same bucket). In practice,")
    print("    Python's hash function makes this virtually impossible.")
    print()

    # --- Practical Benchmarks ---
    print("--- Practical Benchmarks (element NOT present — worst case for list) ---")
    print()
    print(f"  {'n':>8}  |  {'List (µs)':>12}  |  {'Set (µs)':>11}  |  {'Dict (µs)':>12}  |  {'List/Set':>9}")
    print(f"  {'-'*8}  |  {'-'*12}  |  {'-'*11}  |  {'-'*12}  |  {'-'*9}")

    for n in [100, 1_000, 10_000, 50_000, 100_000]:
        lt, st, dt = benchmark_membership_test(n, target_present=False)
        ratio = lt / st if st > 0 else 0
        print(f"  {n:>8,}  |  {lt:>10.2f}  |  {st:>9.2f}  |  {dt:>10.2f}  |  {ratio:>8.0f}x")

    print()

    # --- Element present benchmarks ---
    print("--- Benchmarks (element present — last position, worst for list) ---")
    print()
    print(f"  {'n':>8}  |  {'List (µs)':>12}  |  {'Set (µs)':>11}  |  {'Dict (µs)':>12}  |  {'List/Set':>9}")
    print(f"  {'-'*8}  |  {'-'*12}  |  {'-'*11}  |  {'-'*12}  |  {'-'*9}")

    for n in [100, 1_000, 10_000, 50_000, 100_000]:
        lt, st, dt = benchmark_membership_test(n, target_present=True)
        ratio = lt / st if st > 0 else 0
        print(f"  {n:>8,}  |  {lt:>10.2f}  |  {st:>9.2f}  |  {dt:>10.2f}  |  {ratio:>8.0f}x")

    print()

    # --- Code Demonstration ---
    print("--- Code Examples ---")
    print()

    # List
    my_list = [10, 20, 30, 40, 50]
    print(f"  my_list = {my_list}")
    print(f"  30 in my_list → {30 in my_list}  (scans: 10→20→30 found! 3 checks)")
    print(f"  99 in my_list → {99 in my_list}  (scans: 10→20→30→40→50 not found! 5 checks)")
    print()

    # Set
    my_set = {10, 20, 30, 40, 50}
    print(f"  my_set = {my_set}")
    print(f"  30 in my_set → {30 in my_set}   (hash(30) → direct lookup, 1 check)")
    print(f"  99 in my_set → {99 in my_set}  (hash(99) → empty bucket, 1 check)")
    print()

    # Dict
    my_dict = {10: "a", 20: "b", 30: "c", 40: "d", 50: "e"}
    print(f"  my_dict = {my_dict}")
    print(f"  30 in my_dict → {30 in my_dict}   (hash(30) → key found, 1 check)")
    print(f"  99 in my_dict → {99 in my_dict}  (hash(99) → no such key, 1 check)")
    print()

    # --- Hash table visual ---
    print("--- Visual: How a Hash Table Works ---")
    print()
    print("  Elements: [10, 25, 7, 42, 3, 18]")
    print("  Hash table with 8 buckets (simplified):")
    print()
    print("  Bucket | hash(x) % 8 | Contents")
    print("  -------|-------------|----------")

    elements = [10, 25, 7, 42, 3, 18]
    buckets = {i: [] for i in range(8)}
    for x in elements:
        bucket = hash(x) % 8
        buckets[bucket].append(x)

    for i in range(8):
        contents = str(buckets[i]) if buckets[i] else "empty"
        print(f"    [{i}]   |     {i}       | {contents}")

    print()
    print("  Lookup 'Is 42 here?':")
    h = hash(42) % 8
    print(f"    hash(42) % 8 = {h}")
    print(f"    Go to bucket [{h}] → found {buckets[h]} → O(1)!")
    print()

    # --- Answer ---
    print("ANSWER:")
    print("  (a) List:       O(n) — must scan elements one by one")
    print("  (b) Set:        O(1) — hash-based direct bucket lookup")
    print("  (c) Dictionary: O(1) — keys are hashed (same as set)")
    print()
    print("  They differ because lists use SEQUENTIAL storage (linear scan)")
    print("  while sets and dicts use HASH TABLES (constant-time lookup).")


if __name__ == "__main__":
    demonstrate()
