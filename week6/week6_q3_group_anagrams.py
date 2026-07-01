"""
Q3. Write a function that groups anagrams together from a list of strings.
    Example: ['eat','tea','tan','ate','nat','bat']
           → [['eat','tea','ate'], ['tan','nat'], ['bat']]

Answer:
    Key Insight: Anagrams have the same SORTED characters.
    sorted("eat") = sorted("tea") = sorted("ate") = "aet"

    Use a hash map: sorted_word → [list of original words]

    Time:  O(n × k log k) where n = number of words, k = max word length
    Space: O(n × k) — storing all words in the map
"""

from collections import defaultdict


def group_anagrams(strs: list) -> list:
    """
    Group anagrams together using sorted string as hash key.

    Time:  O(n × k log k) — sort each word of length k.
    Space: O(n × k)
    """
    groups = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))  # Anagrams produce the same sorted key
        groups[key].append(word)

    return list(groups.values())


def group_anagrams_count(strs: list) -> list:
    """
    Alternative: Use character COUNT as key instead of sorting.
    This is O(n × k) — avoids the k log k sorting cost.

    Time:  O(n × k)
    Space: O(n × k)
    """
    groups = defaultdict(list)

    for word in strs:
        # Create a count tuple: (count_a, count_b, ..., count_z)
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)  # Tuples are hashable
        groups[key].append(word)

    return list(groups.values())


def demonstrate():
    print("=" * 70)
    print("Q3: Group Anagrams Together")
    print("=" * 70)
    print()

    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print(f"  Input: {strs}")
    print()

    result = group_anagrams(strs)
    print(f"  Output: {result}")
    print()

    # --- How it works ---
    print("--- How It Works ---")
    print()
    print("  Anagrams share the same characters → same SORTED string!")
    print()

    groups = defaultdict(list)
    print(f"  {'Word':>6} | {'sorted()':>10} | {'Groups so far'}")
    print(f"  {'-'*6} | {'-'*10} | {'-'*40}")

    for word in strs:
        key = ''.join(sorted(word))
        groups[key].append(word)
        print(f"  {word:>6} | {key:>10} | {dict(groups)}")

    print()
    print(f"  Final groups: {list(groups.values())}")
    print()

    # --- Alternative approach ---
    print("--- Alternative: Character Count as Key ---")
    print()
    print("  Instead of sorting (O(k log k)), count characters (O(k)):")
    print()

    for word in ['eat', 'tea', 'ate']:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        non_zero = {chr(i + ord('a')): v for i, v in enumerate(count) if v > 0}
        print(f"    '{word}' → {non_zero} → same key!")

    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        (['eat', 'tea', 'tan', 'ate', 'nat', 'bat'], "Standard"),
        ([''], "Empty string"),
        (['a'], "Single char"),
        (['abc', 'bca', 'cab', 'xyz', 'zyx'], "Two groups"),
        (['listen', 'silent', 'hello', 'world', 'enlist'], "Longer words"),
        (['', ''], "Two empty strings"),
        (['ab', 'ba', 'abc', 'bca', 'a', 'a'], "Mixed lengths"),
    ]

    for strs, desc in test_cases:
        r1 = group_anagrams(strs)
        r2 = group_anagrams_count(strs)
        # Sort inner lists for comparison
        r1_sorted = sorted([sorted(g) for g in r1])
        r2_sorted = sorted([sorted(g) for g in r2])
        match = r1_sorted == r2_sorted
        print(f"  {desc:>20}: {strs}")
        print(f"  {'':>20}  → {r1}  {'✓' if match else '✗'}")
        print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Method          | Time         | Space   | Key Type")
    print("  ----------------|-------------|---------|------------------")
    print("  Sort-based      | O(n·k·logk) | O(n·k)  | Sorted string")
    print("  Count-based ★   | O(n·k)      | O(n·k)  | Character count tuple")
    print()
    print("  n = number of strings, k = max string length")
    print()
    print("ANSWER: Use sorted string (or char count) as hash key to group anagrams.")
    print("All anagrams map to the same key. O(n × k log k) or O(n × k) time.")


if __name__ == "__main__":
    demonstrate()
