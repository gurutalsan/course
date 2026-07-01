"""
Q7. What happens when you use a mutable object (like a list) as a
    dictionary key? Why?

Answer:
    Python raises a TypeError: unhashable type: 'list'

    WHY:
    Dictionary keys MUST be hashable. An object is hashable if:
    1. It has a hash value (via __hash__) that NEVER CHANGES during its lifetime.
    2. It can be compared to other objects (via __eq__).

    Mutable objects (list, dict, set) CANNOT be dictionary keys because:
    - Their contents can change after creation.
    - If contents change, their hash value would need to change too.
    - But if the hash changes, the dict can't find the key anymore!
    - This would break the fundamental guarantee of hash tables.

    Immutable objects (int, float, str, tuple, frozenset) CAN be keys
    because their values never change → stable hash → reliable lookup.
"""


def demonstrate():
    print("=" * 70)
    print("Q7: Mutable Objects as Dictionary Keys")
    print("=" * 70)
    print()

    # --- The Error ---
    print("--- What Happens: TypeError ---")
    print()

    print("  Attempting: my_dict = {[1, 2, 3]: 'value'}")
    print()

    try:
        my_dict = {[1, 2, 3]: "value"}
    except TypeError as e:
        print(f"  ❌ TypeError: {e}")

    print()

    try:
        my_dict = {}
        my_list = [1, 2, 3]
        my_dict[my_list] = "value"
    except TypeError as e:
        print(f"  Attempting: my_dict[my_list] = 'value'")
        print(f"  ❌ TypeError: {e}")

    print()

    # Other mutable types
    print("  Other mutable types that FAIL as keys:")
    print()

    mutable_tests = [
        ([1, 2, 3], "list"),
        ({"a": 1}, "dict"),
        ({1, 2, 3}, "set"),
    ]

    for obj, name in mutable_tests:
        try:
            d = {obj: "test"}
            print(f"    {name:>6} {str(obj):>20}  →  ✓ (unexpected)")
        except TypeError as e:
            print(f"    {name:>6} {str(obj):>20}  →  ❌ {e}")

    print()

    # --- WHY: The Hash Table Problem ---
    print("--- WHY: The Hash Table Problem ---")
    print()
    print("  Dictionaries use HASH TABLES internally.")
    print("  To store/retrieve a key-value pair:")
    print()
    print("    1. Compute hash(key) → bucket index")
    print("    2. Store/find the value in that bucket")
    print()
    print("  If the key is MUTABLE and changes after insertion:")
    print()
    print("    Step 1: key = [1, 2, 3]")
    print("            hash([1, 2, 3]) → bucket 42")
    print("            Store ('value') in bucket 42")
    print()
    print("    Step 2: key.append(4)  ← key is now [1, 2, 3, 4]")
    print("            hash([1, 2, 3, 4]) → bucket 87  ← DIFFERENT bucket!")
    print()
    print("    Step 3: Looking up key [1, 2, 3, 4]")
    print("            Goes to bucket 87 → EMPTY!")
    print("            The value is lost in bucket 42! 💥")
    print()
    print("  Python PREVENTS this by requiring keys to be IMMUTABLE (hashable).")
    print()

    # --- What IS Hashable? ---
    print("--- What IS Hashable? ---")
    print()
    print("  Type          | Mutable? | Hashable? | Can be dict key?")
    print("  --------------|----------|-----------|------------------")

    hashable_tests = [
        (42, "int", False),
        (3.14, "float", False),
        ("hello", "str", False),
        (True, "bool", False),
        ((1, 2, 3), "tuple", False),
        (frozenset({1, 2}), "frozenset", False),
        (None, "NoneType", False),
    ]

    for obj, type_name, is_mutable in hashable_tests:
        try:
            h = hash(obj)
            hashable = "✓ Yes"
            can_be_key = "✓ Yes"
        except TypeError:
            hashable = "✗ No"
            can_be_key = "✗ No"

        mutable_str = "✓ Yes" if is_mutable else "✗ No"
        print(f"  {type_name:>14} | {mutable_str:>8} | {hashable:>9} | {can_be_key}")

    print(f"  {'list':>14} | {'✓ Yes':>8} | {'✗ No':>9} | {'✗ No'}")
    print(f"  {'dict':>14} | {'✓ Yes':>8} | {'✗ No':>9} | {'✗ No'}")
    print(f"  {'set':>14} | {'✓ Yes':>8} | {'✗ No':>9} | {'✗ No'}")
    print()

    # --- Hash values demonstration ---
    print("--- Hash Values of Immutable Types ---")
    print()

    hash_examples = [42, 3.14, "hello", True, (1, 2, 3), frozenset({1, 2}), None]
    for obj in hash_examples:
        print(f"  hash({str(obj):>20}) = {hash(obj)}")

    print()

    # --- Workarounds ---
    print("--- Workarounds: How to Use List-Like Data as Keys ---")
    print()

    # Workaround 1: Convert to tuple
    print("  1. Convert list to TUPLE (immutable version of list):")
    print()
    my_list = [1, 2, 3]
    my_tuple = tuple(my_list)
    my_dict = {my_tuple: "value"}
    print(f"     my_list = {my_list}")
    print(f"     my_dict = {{tuple(my_list): 'value'}}")
    print(f"     my_dict = {my_dict}")
    print(f"     my_dict[(1, 2, 3)] = '{my_dict[(1, 2, 3)]}'  ✓")
    print()

    # Workaround 2: Convert set to frozenset
    print("  2. Convert set to FROZENSET (immutable version of set):")
    print()
    my_set = {1, 2, 3}
    my_dict = {frozenset(my_set): "value"}
    print(f"     my_set = {my_set}")
    print(f"     my_dict = {{frozenset(my_set): 'value'}}")
    print(f"     my_dict = {my_dict}")
    print()

    # Workaround 3: Convert to string
    print("  3. Convert to STRING representation:")
    print()
    my_list = [1, 2, 3]
    my_dict = {str(my_list): "value"}
    print(f"     my_dict = {{str([1, 2, 3]): 'value'}}")
    print(f"     my_dict = {my_dict}")
    print()

    # --- Tuple with mutable elements ---
    print("--- Gotcha: Tuple Containing Mutable Elements ---")
    print()

    print("  A tuple of immutable elements IS hashable:")
    t1 = (1, 2, 3)
    print(f"    hash((1, 2, 3)) = {hash(t1)}  ✓")
    print()

    print("  A tuple CONTAINING a list is NOT hashable:")
    t2 = (1, [2, 3])
    try:
        h = hash(t2)
        print(f"    hash((1, [2, 3])) = {h}")
    except TypeError as e:
        print(f"    hash((1, [2, 3])) → ❌ TypeError: {e}")

    print()
    print("  The tuple itself is immutable, but if it CONTAINS a mutable")
    print("  element, the overall hash can't be stable → unhashable.")
    print()

    # --- Custom class example ---
    print("--- Bonus: Custom Objects as Keys ---")
    print()

    class Point:
        """Immutable point — safe to use as dict key."""
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __hash__(self):
            return hash((self.x, self.y))

        def __eq__(self, other):
            return isinstance(other, Point) and self.x == other.x and self.y == other.y

        def __repr__(self):
            return f"Point({self.x}, {self.y})"

    p1 = Point(1, 2)
    p2 = Point(3, 4)
    locations = {p1: "Home", p2: "Office"}
    print(f"  class Point with __hash__ and __eq__:")
    print(f"    locations = {locations}")
    print(f"    locations[Point(1, 2)] = '{locations[Point(1, 2)]}'  ✓")
    print()

    print("ANSWER:")
    print("  Using a mutable object (list, dict, set) as a dictionary key")
    print("  raises TypeError: unhashable type.")
    print()
    print("  WHY: Dict keys must be hashable (stable hash value). Mutable")
    print("  objects can change, which would change their hash, making")
    print("  the key unfindable in the hash table. Python prevents this.")


if __name__ == "__main__":
    demonstrate()
