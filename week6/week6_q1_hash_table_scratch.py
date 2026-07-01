"""
Q1. Implement a hash table from scratch with put, get, delete, and resize
    methods. Use separate chaining for collision handling. Test with 20+ entries.

Answer:
    A hash table maps keys to values using a hash function.
    - Hash function converts key → index in an internal array.
    - Collisions (two keys → same index) handled by SEPARATE CHAINING:
      each bucket is a linked list of (key, value) pairs.
    - Resize (rehash) when load factor > threshold to maintain O(1) average.

    Average case: put O(1), get O(1), delete O(1)
    Worst case (all collisions): O(n)
"""


class HashTable:
    """
    Hash Table with separate chaining for collision resolution.

    Internal structure:
        buckets = [ [(k,v), (k,v)], [], [(k,v)], ... ]
        Each bucket is a list of (key, value) pairs.

    Load factor = num_entries / num_buckets
    When load_factor > 0.75, resize (double the buckets and rehash).
    """

    def __init__(self, initial_capacity: int = 8):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
        self.LOAD_FACTOR_THRESHOLD = 0.75

    def _hash(self, key) -> int:
        """Compute bucket index for a given key."""
        return hash(key) % self.capacity

    def put(self, key, value) -> None:
        """
        Insert or update a key-value pair. O(1) average.

        If key exists → update value.
        If key is new → append to bucket chain.
        If load factor exceeded → resize.
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # Check if key already exists → update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Key doesn't exist → add new entry
        bucket.append((key, value))
        self.size += 1

        # Check if resize needed
        if self.size / self.capacity > self.LOAD_FACTOR_THRESHOLD:
            self._resize()

    def get(self, key, default=None):
        """
        Retrieve value by key. O(1) average.
        Returns default if key not found.
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for k, v in bucket:
            if k == key:
                return v

        return default

    def delete(self, key) -> bool:
        """
        Remove a key-value pair. O(1) average.
        Returns True if deleted, False if not found.
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True

        return False

    def _resize(self) -> None:
        """
        Double the capacity and rehash all entries.
        Called when load factor exceeds threshold.
        """
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def contains(self, key) -> bool:
        """Check if key exists. O(1) average."""
        idx = self._hash(key)
        return any(k == key for k, _ in self.buckets[idx])

    def keys(self) -> list:
        """Return all keys."""
        return [k for bucket in self.buckets for k, _ in bucket]

    def values(self) -> list:
        """Return all values."""
        return [v for bucket in self.buckets for _, v in bucket]

    def items(self) -> list:
        """Return all (key, value) pairs."""
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    @property
    def load_factor(self) -> float:
        return self.size / self.capacity

    def __len__(self):
        return self.size

    def __repr__(self):
        items = [f"{k}: {v}" for k, v in self.items()]
        return "{" + ", ".join(items) + "}"

    def __getitem__(self, key):
        val = self.get(key)
        if val is None and not self.contains(key):
            raise KeyError(key)
        return val

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, key):
        return self.contains(key)

    def display_internals(self):
        """Show the internal bucket structure."""
        print(f"    Capacity: {self.capacity}, Size: {self.size}, "
              f"Load Factor: {self.load_factor:.2f}")
        for i, bucket in enumerate(self.buckets):
            if bucket:
                chain = " → ".join([f"({k}: {v})" for k, v in bucket])
                print(f"    Bucket [{i:>2}]: {chain}")
            else:
                print(f"    Bucket [{i:>2}]: (empty)")


def demonstrate():
    print("=" * 70)
    print("Q1: Hash Table from Scratch — Separate Chaining")
    print("=" * 70)
    print()

    # --- How it works ---
    print("--- How Separate Chaining Works ---")
    print()
    print('  put("apple", 5):')
    print("    hash('apple') % 8 = 3")
    print("    buckets[3].append(('apple', 5))")
    print()
    print("  Collision: another key also hashes to index 3:")
    print('  put("grape", 7):')
    print("    hash('grape') % 8 = 3  ← same bucket!")
    print("    buckets[3].append(('grape', 7))")
    print()
    print("    Bucket 3: ('apple', 5) → ('grape', 7)  ← chain!")
    print()

    # --- Build and test with 20+ entries ---
    print("=" * 70)
    print("TEST: Insert 25 entries")
    print("=" * 70)
    print()

    ht = HashTable(initial_capacity=8)

    test_data = [
        ("apple", 3), ("banana", 5), ("cherry", 7), ("date", 2),
        ("elderberry", 9), ("fig", 4), ("grape", 6), ("honeydew", 8),
        ("kiwi", 1), ("lemon", 10), ("mango", 12), ("nectarine", 3),
        ("orange", 15), ("papaya", 7), ("quince", 11), ("raspberry", 2),
        ("strawberry", 14), ("tangerine", 6), ("watermelon", 20),
        ("blueberry", 13), ("avocado", 9), ("coconut", 16),
        ("dragonfruit", 18), ("guava", 5), ("jackfruit", 22),
    ]

    print(f"  Initial capacity: {ht.capacity}")
    print()

    resize_points = []
    for key, val in test_data:
        old_cap = ht.capacity
        ht.put(key, val)
        if ht.capacity != old_cap:
            resize_points.append((len(ht), old_cap, ht.capacity))

    print(f"  After inserting {len(test_data)} entries:")
    print(f"    Size: {len(ht)}")
    print(f"    Capacity: {ht.capacity}")
    print(f"    Load factor: {ht.load_factor:.2f}")
    print()

    if resize_points:
        print("  Resize events:")
        for size, old, new in resize_points:
            print(f"    At size {size}: {old} → {new} buckets")
    print()

    # --- Show internal structure ---
    print("--- Internal Bucket Structure (first 16) ---")
    print()
    for i in range(min(16, ht.capacity)):
        bucket = ht.buckets[i]
        if bucket:
            chain = " → ".join([f"({k}: {v})" for k, v in bucket])
            print(f"  [{i:>2}]: {chain}")
        else:
            print(f"  [{i:>2}]: —")
    if ht.capacity > 16:
        non_empty = sum(1 for b in ht.buckets[16:] if b)
        print(f"  ... ({non_empty} more non-empty buckets)")
    print()

    # --- Test GET ---
    print("--- Test GET ---")
    print()
    get_tests = ["apple", "mango", "watermelon", "missing_key", "grape"]
    for key in get_tests:
        val = ht.get(key, "NOT FOUND")
        print(f"  get('{key}') → {val}")
    print()

    # --- Test UPDATE ---
    print("--- Test UPDATE ---")
    print()
    print(f"  Before: get('apple') = {ht.get('apple')}")
    ht.put("apple", 99)
    print(f"  After put('apple', 99): get('apple') = {ht.get('apple')}")
    print(f"  Size unchanged: {len(ht)} (update, not insert)")
    print()

    # --- Test DELETE ---
    print("--- Test DELETE ---")
    print()
    print(f"  Size before: {len(ht)}")
    print(f"  delete('banana'): {ht.delete('banana')}")
    print(f"  delete('missing'): {ht.delete('missing')}")
    print(f"  Size after: {len(ht)}")
    print(f"  get('banana'): {ht.get('banana', 'NOT FOUND')}")
    print()

    # --- Test CONTAINS ---
    print("--- Test CONTAINS ---")
    print()
    for key in ["cherry", "banana", "kiwi"]:
        print(f"  '{key}' in ht: {key in ht}")
    print()

    # --- Bracket syntax ---
    print("--- Bracket Syntax (like Python dict) ---")
    print()
    ht["new_key"] = 42
    print(f"  ht['new_key'] = 42 → get: {ht['new_key']}")
    print()

    # --- Complexity ---
    print("--- Complexity Summary ---")
    print()
    print("  Operation | Average | Worst (all collisions)")
    print("  ----------|---------|----------------------")
    print("  put       | O(1)    | O(n)")
    print("  get       | O(1)    | O(n)")
    print("  delete    | O(1)    | O(n)")
    print("  resize    | O(n)    | O(n)  (amortized O(1) per put)")
    print()
    print("ANSWER: Separate chaining stores colliding entries as a list in each")
    print("bucket. Resize doubles capacity when load factor > 0.75 to keep O(1).")


if __name__ == "__main__":
    demonstrate()
