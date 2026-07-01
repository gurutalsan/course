"""
Q5. Write a function to determine if two strings are anagrams of each other.
    Provide two different approaches and compare their complexities.

Answer:
    Two strings are anagrams if they contain the same characters with
    the same frequencies, just rearranged.

    Approach 1: Sorting — O(n log n) time, O(n) space
    Approach 2: Counting (Counter/dict) — O(n) time, O(1) space*

    * O(1) space because the character set is bounded (e.g., 26 letters).
"""

from collections import Counter


# ============================================================
# Approach 1: Sorting — O(n log n)
# ============================================================
def is_anagram_sort(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams by sorting both.

    If sorted versions are equal → anagram.

    Time:  O(n log n) — dominated by sorting.
    Space: O(n) — sorted copies of both strings.
    """
    if len(s1) != len(s2):
        return False

    return sorted(s1.lower()) == sorted(s2.lower())


# ============================================================
# Approach 2: Character Counting — O(n) ★ OPTIMAL ★
# ============================================================
def is_anagram_counter(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams using character frequency counting.

    Time:  O(n) — single pass to count each string.
    Space: O(1) — bounded by alphabet size (26 for lowercase).

    Using collections.Counter for concise code.
    """
    if len(s1) != len(s2):
        return False

    return Counter(s1.lower()) == Counter(s2.lower())


# ============================================================
# Approach 2b: Manual counting with dictionary
# ============================================================
def is_anagram_dict(s1: str, s2: str) -> bool:
    """
    Manual character counting using a dictionary.

    Increment for s1 chars, decrement for s2 chars.
    If all counts are 0 at the end → anagram.

    Time:  O(n)
    Space: O(1) — bounded by character set size.
    """
    if len(s1) != len(s2):
        return False

    char_count = {}

    for char in s1.lower():
        char_count[char] = char_count.get(char, 0) + 1

    for char in s2.lower():
        char_count[char] = char_count.get(char, 0) - 1

    return all(count == 0 for count in char_count.values())


# ============================================================
# Approach 2c: Fixed-size array (if only lowercase a-z)
# ============================================================
def is_anagram_array(s1: str, s2: str) -> bool:
    """
    Using a fixed-size array of 26 counters (only lowercase a-z).

    Time:  O(n)
    Space: O(1) — exactly 26 integers.
    """
    if len(s1) != len(s2):
        return False

    counts = [0] * 26  # One slot for each letter a-z

    for char in s1.lower():
        counts[ord(char) - ord('a')] += 1

    for char in s2.lower():
        counts[ord(char) - ord('a')] -= 1

    return all(c == 0 for c in counts)


def demonstrate():
    import time

    print("=" * 70)
    print("Q5: Anagram Checker — Two Approaches Compared")
    print("=" * 70)
    print()

    # --- What is an Anagram? ---
    print("--- What is an Anagram? ---")
    print()
    print("  Two strings are anagrams if they contain exactly the same")
    print("  characters with the same frequencies, just rearranged.")
    print()
    print('  "listen"  ↔  "silent"     ✓ Anagram')
    print('  "hello"   ↔  "world"      ✗ Not anagram')
    print('  "anagram" ↔  "nagaram"    ✓ Anagram')
    print()

    # --- Approach 1: Sorting ---
    print("=" * 70)
    print("Approach 1: SORTING — O(n log n)")
    print("=" * 70)
    print()
    print("  Idea: If two strings are anagrams, their sorted forms are identical.")
    print()
    print('  sorted("listen") → [\'e\', \'i\', \'l\', \'n\', \'s\', \'t\']')
    print('  sorted("silent") → [\'e\', \'i\', \'l\', \'n\', \'s\', \'t\']')
    print("  Equal? → ✓ Anagram!")
    print()
    print("  Code:")
    print("    def is_anagram_sort(s1, s2):")
    print("        return sorted(s1) == sorted(s2)")
    print()

    # --- Approach 2: Counting ---
    print("=" * 70)
    print("Approach 2: CHARACTER COUNTING — O(n) ★ OPTIMAL ★")
    print("=" * 70)
    print()
    print("  Idea: Count character frequencies. If counts match → anagram.")
    print()

    s1, s2 = "listen", "silent"
    c1 = Counter(s1)
    c2 = Counter(s2)
    print(f'  Counter("listen") → {dict(c1)}')
    print(f'  Counter("silent") → {dict(c2)}')
    print(f"  Equal? → ✓ Anagram!")
    print()
    print("  Code:")
    print("    from collections import Counter")
    print("    def is_anagram_counter(s1, s2):")
    print("        return Counter(s1) == Counter(s2)")
    print()

    # --- Step-by-Step: Manual Dict Approach ---
    print("--- Step-by-Step: Manual Dictionary Counting ---")
    print()
    s1, s2 = "anagram", "nagaram"
    print(f'  s1 = "{s1}", s2 = "{s2}"')
    print()

    char_count = {}
    print("  Phase 1: Count s1 characters (increment):")
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
        print(f"    '{char}' → counts = {char_count}")

    print()
    print("  Phase 2: Count s2 characters (decrement):")
    for char in s2:
        char_count[char] = char_count.get(char, 0) - 1
        print(f"    '{char}' → counts = {char_count}")

    all_zero = all(v == 0 for v in char_count.values())
    print()
    print(f"  All counts zero? {all_zero} → {'✓ Anagram!' if all_zero else '✗ Not anagram'}")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ("listen", "silent", True),
        ("anagram", "nagaram", True),
        ("hello", "world", False),
        ("", "", True),
        ("a", "a", True),
        ("ab", "ba", True),
        ("ab", "abc", False),
        ("rat", "car", False),
        ("Astronomer", "Moon starer", False),  # Has space difference
        ("aabbcc", "abcabc", True),
        ("aaaa", "aaab", False),
    ]

    print(f"  {'s1':>15}  | {'s2':>15} | {'Expected':>8} | {'Sort':>5} | {'Counter':>7} | {'Dict':>5} | {'✓/✗':>3}")
    print(f"  {'-'*15}  | {'-'*15} | {'-'*8} | {'-'*5} | {'-'*7} | {'-'*5} | {'-'*3}")

    for s1, s2, expected in test_cases:
        r_sort = is_anagram_sort(s1, s2)
        r_counter = is_anagram_counter(s1, s2)
        r_dict = is_anagram_dict(s1, s2)
        status = "✓" if r_sort == r_counter == r_dict == expected else "✗"
        print(
            f"  {repr(s1):>15}  | {repr(s2):>15} | "
            f"{str(expected):>8} | {str(r_sort):>5} | "
            f"{str(r_counter):>7} | {str(r_dict):>5} | {status:>3}"
        )

    print()

    # --- Complexity Comparison ---
    print("--- Complexity Comparison ---")
    print()
    print("  Approach            | Time       | Space        | Method")
    print("  --------------------|------------|--------------|------------------")
    print("  Sorting             | O(n log n) | O(n)         | Sort both, compare")
    print("  Counter ★           | O(n)       | O(1)*        | Count frequencies")
    print("  Manual Dict         | O(n)       | O(1)*        | Increment/decrement")
    print("  Fixed Array (a-z)   | O(n)       | O(1)         | 26-element array")
    print()
    print("  * O(1) because character set is bounded (e.g., 26 letters)")
    print()

    # --- Performance ---
    print("--- Performance Benchmark ---")
    print()

    import random
    import string

    sizes = [100, 1_000, 10_000, 100_000, 500_000]

    print(f"  {'n':>8}  |  {'Sort O(nlogn)':>14}  |  {'Counter O(n)':>14}  |  {'Speedup':>8}")
    print(f"  {'-'*8}  |  {'-'*14}  |  {'-'*14}  |  {'-'*8}")

    for n in sizes:
        chars = list(random.choices(string.ascii_lowercase, k=n))
        s1 = ''.join(chars)
        random.shuffle(chars)
        s2 = ''.join(chars)

        start = time.perf_counter()
        _ = is_anagram_sort(s1, s2)
        sort_time = (time.perf_counter() - start) * 1000

        start = time.perf_counter()
        _ = is_anagram_counter(s1, s2)
        counter_time = (time.perf_counter() - start) * 1000

        speedup = sort_time / counter_time if counter_time > 0 else 0

        print(
            f"  {n:>8,}  |  "
            f"{sort_time:>11.3f} ms  |  "
            f"{counter_time:>11.3f} ms  |  "
            f"{speedup:>7.1f}x"
        )

    print()
    print("ANSWER:")
    print("  Approach 1 (Sorting):   O(n log n) time, O(n) space")
    print("  Approach 2 (Counting):  O(n) time, O(1) space ★ Better")
    print("  Counting is faster because it avoids the cost of sorting.")


if __name__ == "__main__":
    demonstrate()
