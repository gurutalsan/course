"""
Q1. When would you use a set instead of a list? Give two real-world examples
    where sets are the better choice.

Answer:
    Use a SET when:
    1. You need UNIQUE elements only (no duplicates allowed).
    2. You need FAST membership testing — O(1) vs O(n) for lists.
    3. You need set operations — union, intersection, difference.
    4. Order does NOT matter (sets are unordered).

    Real-World Example 1: Tracking unique website visitors
    Real-World Example 2: Finding common friends between two social media users
"""


# ============================================================
# Example 1: Tracking Unique Website Visitors
# ============================================================
def track_unique_visitors_list(page_visits: list) -> list:
    """Using a list — SLOW for large datasets (O(n) lookup per check)."""
    unique = []
    for visitor in page_visits:
        if visitor not in unique:  # O(n) lookup every time!
            unique.append(visitor)
    return unique


def track_unique_visitors_set(page_visits: list) -> set:
    """Using a set — FAST, automatic deduplication (O(1) lookup)."""
    return set(page_visits)  # Duplicates removed automatically!


# ============================================================
# Example 2: Finding Common Friends (Social Media)
# ============================================================
def common_friends_list(user_a_friends: list, user_b_friends: list) -> list:
    """Using lists — O(n × m) nested comparison."""
    common = []
    for friend in user_a_friends:
        if friend in user_b_friends:  # O(m) for each of n friends
            common.append(friend)
    return common


def common_friends_set(user_a_friends: list, user_b_friends: list) -> set:
    """Using sets — O(min(n, m)) intersection operation."""
    return set(user_a_friends) & set(user_b_friends)  # Built-in intersection!


def demonstrate():
    import time

    print("=" * 70)
    print("Q1: When to Use a Set Instead of a List")
    print("=" * 70)
    print()

    # --- When to choose Set vs List ---
    print("--- Decision Guide: Set vs List ---")
    print()
    print("  Feature              | List               | Set")
    print("  ---------------------|--------------------|-----------------")
    print("  Duplicates allowed?  | ✓ Yes              | ✗ No (unique only)")
    print("  Ordered?             | ✓ Yes (insertion)  | ✗ No")
    print("  Indexable? (arr[i])  | ✓ Yes              | ✗ No")
    print("  Membership test      | O(n) — slow        | O(1) — fast")
    print("  Add element          | O(1) append        | O(1) add")
    print("  Union/Intersection   | Manual loops       | Built-in operators")
    print()

    # --- Example 1: Unique Website Visitors ---
    print("=" * 70)
    print("Example 1: Tracking Unique Website Visitors")
    print("=" * 70)
    print()

    page_visits = [
        "user_101", "user_205", "user_101", "user_330",
        "user_205", "user_442", "user_101", "user_330",
        "user_550", "user_205", "user_442", "user_101",
    ]

    print(f"  Raw page visits ({len(page_visits)} total):")
    print(f"    {page_visits}")
    print()

    # List approach
    unique_list = track_unique_visitors_list(page_visits)
    print(f"  List approach — unique visitors: {unique_list}")
    print(f"    Count: {len(unique_list)}")
    print(f"    Problem: 'if visitor not in unique' is O(n) each time → O(n²) total")
    print()

    # Set approach
    unique_set = track_unique_visitors_set(page_visits)
    print(f"  Set approach — unique visitors: {unique_set}")
    print(f"    Count: {len(unique_set)}")
    print(f"    Advantage: Automatic dedup, O(1) per insert → O(n) total")
    print()

    # Performance comparison at scale
    print("  --- Performance at Scale ---")
    print()
    import random
    large_visits = [f"user_{random.randint(1, 1000)}" for _ in range(50_000)]

    start = time.perf_counter()
    _ = track_unique_visitors_list(large_visits)
    list_time = (time.perf_counter() - start) * 1000

    start = time.perf_counter()
    _ = track_unique_visitors_set(large_visits)
    set_time = (time.perf_counter() - start) * 1000

    print(f"    50,000 visits (list): {list_time:>10.3f} ms")
    print(f"    50,000 visits (set):  {set_time:>10.3f} ms")
    print(f"    Speedup:              {list_time/set_time:>10.1f}x")
    print()

    # --- Example 2: Common Friends ---
    print("=" * 70)
    print("Example 2: Finding Common Friends (Social Media)")
    print("=" * 70)
    print()

    alice_friends = ["Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]
    bob_friends = ["Alice", "Charlie", "Eve", "Heidi", "Ivan", "Grace"]

    print(f"  Alice's friends: {alice_friends}")
    print(f"  Bob's friends:   {bob_friends}")
    print()

    common_list = common_friends_list(alice_friends, bob_friends)
    common_set = common_friends_set(alice_friends, bob_friends)

    print(f"  Common friends (list approach): {common_list}")
    print(f"  Common friends (set approach):  {common_set}")
    print()

    # Bonus: Other set operations
    a_set = set(alice_friends)
    b_set = set(bob_friends)

    print("  --- Bonus: Set Operations ---")
    print()
    print(f"    Union (all friends):        {a_set | b_set}")
    print(f"    Intersection (common):      {a_set & b_set}")
    print(f"    Alice only (difference):    {a_set - b_set}")
    print(f"    Bob only (difference):      {b_set - a_set}")
    print(f"    Exclusive (symmetric diff): {a_set ^ b_set}")
    print()

    # --- Summary ---
    print("=" * 70)
    print("ANSWER:")
    print()
    print("  Use SETS when:")
    print("    1. You need unique elements (no duplicates)")
    print("    2. You need fast O(1) membership testing")
    print("    3. You need set math (union, intersection, difference)")
    print()
    print("  Example 1: Tracking unique website visitors")
    print("    → Set automatically removes duplicate visits")
    print()
    print("  Example 2: Finding common friends on social media")
    print("    → Set intersection is O(min(n,m)) vs O(n×m) with lists")


if __name__ == "__main__":
    demonstrate()
