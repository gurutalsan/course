"""
Q2. Explain what happens during a hash collision. Compare separate chaining
    vs open addressing (linear probing). Which does Python's dict use?

Answer:
    COLLISION: Two different keys hash to the SAME bucket index.
    Example: hash("apple") % 8 = 3 AND hash("grape") % 8 = 3

    SEPARATE CHAINING: Each bucket stores a linked list/list of entries.
    OPEN ADDRESSING (Linear Probing): If bucket is full, try the NEXT one.

    Python's dict uses OPEN ADDRESSING with a custom probing scheme
    (perturbed linear probing) — NOT separate chaining.
"""


def demonstrate():
    print("=" * 70)
    print("Q2: Hash Collisions — Chaining vs Open Addressing")
    print("=" * 70)
    print()

    # --- What is a Collision? ---
    print("--- What is a Hash Collision? ---")
    print()
    print("  A collision occurs when two DIFFERENT keys hash to the SAME index.")
    print()
    print("  Example with 8 buckets:")
    print('    hash("apple") % 8 = 3')
    print('    hash("grape") % 8 = 3   ← COLLISION! Same bucket!')
    print()
    print("  This is INEVITABLE when keys > buckets (Pigeonhole Principle).")
    print("  The question is: how do we HANDLE it?")
    print()

    # --- Separate Chaining ---
    print("=" * 70)
    print("METHOD 1: SEPARATE CHAINING")
    print("=" * 70)
    print()
    print("  Each bucket stores a LIST (or linked list) of entries.")
    print("  Colliding entries are simply appended to the same list.")
    print()
    print("  Insert 'apple', 'banana', 'grape', 'cherry' (8 buckets):")
    print()
    print("  Index | Bucket Contents")
    print("  ------|--------------------------------------------")
    print("    0   | → (empty)")
    print("    1   | → ('banana', 5)")
    print("    2   | → (empty)")
    print("    3   | → ('apple', 3) → ('grape', 6)  ← CHAIN!")
    print("    4   | → (empty)")
    print("    5   | → ('cherry', 7)")
    print("    6   | → (empty)")
    print("    7   | → (empty)")
    print()
    print("  Lookup 'grape':")
    print("    hash('grape') % 8 = 3 → go to bucket 3")
    print("    Scan chain: 'apple'? No → 'grape'? YES! Return 6")
    print()
    print("  Pros: Simple, never truly 'full', good with high load")
    print("  Cons: Extra memory for list/pointers, cache-unfriendly")
    print()

    # --- Open Addressing (Linear Probing) ---
    print("=" * 70)
    print("METHOD 2: OPEN ADDRESSING (Linear Probing)")
    print("=" * 70)
    print()
    print("  All entries stored IN the array itself (no chains).")
    print("  If a bucket is occupied → try the NEXT bucket.")
    print()
    print("  Insert 'apple'(→3), 'banana'(→1), 'grape'(→3), 'cherry'(→5):")
    print()
    print("  Step 1: Insert 'apple' at index 3")
    print("  Index: [ _, 'banana', _,  'apple',  _, 'cherry', _, _ ]")
    print("           0      1     2      3       4     5      6  7")
    print()
    print("  Step 2: Insert 'grape' → hash=3, OCCUPIED! Try 4... empty!")
    print("  Index: [ _, 'banana', _,  'apple', 'grape', 'cherry', _, _ ]")
    print("           0      1     2      3        4↑       5       6  7")
    print("                                        └ probed here!")
    print()
    print("  Lookup 'grape':")
    print("    hash('grape') % 8 = 3 → bucket 3 has 'apple' (not grape)")
    print("    Probe next: bucket 4 has 'grape' → Found!")
    print()
    print("  Pros: Cache-friendly (contiguous memory), no extra pointers")
    print("  Cons: Clustering problems, degrades at high load factor")
    print()

    # --- Visual Comparison ---
    print("=" * 70)
    print("VISUAL COMPARISON")
    print("=" * 70)
    print()
    print("  SEPARATE CHAINING:")
    print("  ┌───┐")
    print("  │ 0 │ → (empty)")
    print("  │ 1 │ → [banana:5]")
    print("  │ 2 │ → (empty)")
    print("  │ 3 │ → [apple:3] → [grape:6]  ← linked list")
    print("  │ 4 │ → (empty)")
    print("  │ 5 │ → [cherry:7]")
    print("  └───┘")
    print()
    print("  OPEN ADDRESSING (LINEAR PROBING):")
    print("  ┌───────────┬───────────┬───────────┬───────────┬───────────┬───────────┐")
    print("  │  (empty)  │ banana:5  │  (empty)  │ apple:3   │ grape:6   │ cherry:7  │")
    print("  │  idx 0    │  idx 1    │  idx 2    │  idx 3    │  idx 4↑   │  idx 5    │")
    print("  └───────────┴───────────┴───────────┴───────────┴───────────┴───────────┘")
    print("                                                    └ probed!")
    print()

    # --- Clustering Problem ---
    print("--- Open Addressing: The Clustering Problem ---")
    print()
    print("  When many keys hash to nearby indices, they form CLUSTERS.")
    print("  New keys that hash into a cluster must probe through it.")
    print("  This makes the cluster grow LARGER → more probing → slower!")
    print()
    print("  Example of primary clustering:")
    print("  [ _, X, X, X, X, X, _, _ ]")
    print("       ↑ cluster ↑")
    print("  Any key hashing to 1-5 must probe through the entire cluster!")
    print()

    # --- Comparison Table ---
    print("=" * 70)
    print("DETAILED COMPARISON")
    print("=" * 70)
    print()
    print("  Feature              | Separate Chaining    | Open Addressing")
    print("  ---------------------|---------------------|-----------------")
    print("  Storage              | Array + linked lists | Array only")
    print("  Collision handling   | Append to chain      | Probe next slot")
    print("  Load factor limit    | Can exceed 1.0       | Must stay < 1.0")
    print("  Cache performance    | Poor (pointer chasing)| Good (contiguous)")
    print("  Memory overhead      | Pointers per entry   | Empty slots")
    print("  Deletion             | Simple (remove node) | Complex (tombstones)")
    print("  Clustering           | No clustering        | Primary clustering")
    print("  Worst case lookup    | O(n) long chain      | O(n) long probe")
    print("  Implementation       | Simpler              | More complex")
    print("  Best load factor     | 0.75 - 1.0           | < 0.7")
    print()

    # --- What Python Uses ---
    print("=" * 70)
    print("WHAT DOES PYTHON'S dict USE?")
    print("=" * 70)
    print()
    print("  Python's dict uses OPEN ADDRESSING with PERTURBED PROBING.")
    print()
    print("  Specifically:")
    print("  1. NOT simple linear probing (avoids clustering)")
    print("  2. Uses a custom probe sequence that mixes in higher bits")
    print("     of the hash value:")
    print()
    print("     j = ((5 * j) + 1 + perturb) % table_size")
    print("     perturb >>= 5")
    print()
    print("  3. Resizes when load factor > 2/3 (~0.67)")
    print("  4. Since Python 3.6: maintains insertion order")
    print("  5. Uses compact dict (keys + hash stored separately)")
    print()
    print("  Why NOT separate chaining?")
    print("  • Open addressing has better CACHE performance")
    print("  • No pointer overhead per entry")
    print("  • Python's perturbed probing avoids clustering issues")
    print()

    # --- Demonstrate with real Python dict ---
    print("--- Python dict Internals Demo ---")
    print()

    # Show that hash values exist
    keys = ["apple", "banana", "grape", "cherry"]
    print("  Python hash values:")
    for k in keys:
        print(f"    hash('{k}') = {hash(k)}")
    print()

    # Show collision potential
    print("  With 8 buckets:")
    for k in keys:
        idx = hash(k) % 8
        print(f"    hash('{k}') % 8 = {idx}")
    print()

    collisions = {}
    for k in keys:
        idx = hash(k) % 8
        collisions.setdefault(idx, []).append(k)
    collision_count = sum(1 for v in collisions.values() if len(v) > 1)
    print(f"  Collisions: {collision_count}")
    for idx, ks in collisions.items():
        if len(ks) > 1:
            print(f"    Bucket {idx}: {ks}")
    print()

    # --- Summary ---
    print("--- Summary ---")
    print()
    print("  Separate Chaining: Simpler, handles high load, uses extra memory")
    print("  Open Addressing:   Cache-friendly, complex deletion, needs low load")
    print("  Python's dict:     Open addressing with perturbed probing")
    print()
    print("ANSWER: Collisions happen when different keys hash to the same index.")
    print("Chaining stores a list at each bucket; open addressing probes next slots.")
    print("Python's dict uses open addressing with perturbed (non-linear) probing.")


if __name__ == "__main__":
    demonstrate()
