"""
Q6. Write a function that groups a list of words by their first letter
    using defaultdict.

    Example: ['apple','avocado','banana'] → {'a':['apple','avocado'], 'b':['banana']}

Answer:
    defaultdict(list) automatically creates an empty list for any new key,
    eliminating the need to check if a key exists before appending.

    Time Complexity:  O(n) — single pass through the word list.
    Space Complexity: O(n) — storing all n words in the dictionary.
"""

from collections import defaultdict


def group_by_first_letter(words: list) -> dict:
    """
    Group words by their first letter using defaultdict.

    Args:
        words: List of words to group.

    Returns:
        Dictionary mapping first letter → list of words.

    Time:  O(n) — one pass through the list.
    Space: O(n) — all words stored in result.

    Example:
        >>> group_by_first_letter(['apple', 'avocado', 'banana'])
        {'a': ['apple', 'avocado'], 'b': ['banana']}
    """
    groups = defaultdict(list)

    for word in words:
        if word:  # Skip empty strings
            first_letter = word[0].lower()  # Case-insensitive grouping
            groups[first_letter].append(word)

    return dict(groups)  # Convert to regular dict for clean output


# ============================================================
# Comparison: Without defaultdict (manual approach)
# ============================================================
def group_by_first_letter_manual(words: list) -> dict:
    """
    Same functionality WITHOUT defaultdict — requires key-existence checks.

    This is more verbose and error-prone.
    """
    groups = {}

    for word in words:
        if word:
            first_letter = word[0].lower()
            # Must check if key exists before appending!
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(word)

    return groups


# ============================================================
# Alternative: Using setdefault() (built-in dict method)
# ============================================================
def group_by_first_letter_setdefault(words: list) -> dict:
    """
    Using dict.setdefault() — slightly less readable than defaultdict.
    """
    groups = {}

    for word in words:
        if word:
            first_letter = word[0].lower()
            groups.setdefault(first_letter, []).append(word)

    return groups


def demonstrate():
    print("=" * 70)
    print("Q6: Group Words by First Letter Using defaultdict")
    print("=" * 70)
    print()

    # --- How defaultdict Works ---
    print("--- How defaultdict Works ---")
    print()
    print("  Regular dict:   accessing a missing key → KeyError!")
    print("  defaultdict:    accessing a missing key → creates default value")
    print()
    print("  from collections import defaultdict")
    print()
    print("  # Regular dict:")
    print("  d = {}")
    print("  d['a'].append('apple')    # ← KeyError! 'a' doesn't exist")
    print()
    print("  # defaultdict(list):")
    print("  d = defaultdict(list)")
    print("  d['a'].append('apple')    # ← Works! Creates [] first, then appends")
    print()

    # --- The Function ---
    print("--- Implementation ---")
    print()
    print("  def group_by_first_letter(words):")
    print("      groups = defaultdict(list)")
    print("      for word in words:")
    print("          first_letter = word[0].lower()")
    print("          groups[first_letter].append(word)")
    print("      return dict(groups)")
    print()

    # --- Main Example ---
    print("--- Main Example ---")
    print()

    words = ['apple', 'avocado', 'banana', 'blueberry', 'cherry',
             'coconut', 'apricot', 'blackberry', 'cantaloupe']

    result = group_by_first_letter(words)

    print(f"  Input:  {words}")
    print()
    print("  Output:")
    for letter in sorted(result.keys()):
        print(f"    '{letter}' → {result[letter]}")
    print()

    # --- Step-by-Step Walkthrough ---
    print("--- Step-by-Step Walkthrough ---")
    print()
    small_words = ['apple', 'avocado', 'banana']
    print(f"  Input: {small_words}")
    print()

    groups = defaultdict(list)
    for i, word in enumerate(small_words):
        first = word[0].lower()
        print(f"  Step {i+1}: word='{word}', first_letter='{first}'")
        print(f"    Before: dict = {dict(groups)}")
        groups[first].append(word)
        print(f"    groups['{first}'].append('{word}')")
        print(f"    After:  dict = {dict(groups)}")
        print()

    print(f"  Final result: {dict(groups)}")
    print()

    # --- Code Comparison ---
    print("--- Code Comparison: 3 Approaches ---")
    print()
    print("  1. defaultdict (CLEANEST — recommended):")
    print("     groups = defaultdict(list)")
    print("     for word in words:")
    print("         groups[word[0]].append(word)     # No check needed!")
    print()
    print("  2. Manual check (VERBOSE):")
    print("     groups = {}")
    print("     for word in words:")
    print("         if word[0] not in groups:        # Must check!")
    print("             groups[word[0]] = []         # Must initialize!")
    print("         groups[word[0]].append(word)")
    print()
    print("  3. setdefault (COMPACT but less readable):")
    print("     groups = {}")
    print("     for word in words:")
    print("         groups.setdefault(word[0], []).append(word)")
    print()

    # --- Verify all three produce the same result ---
    print("--- Verification: All 3 methods produce same output ---")
    print()
    r1 = group_by_first_letter(words)
    r2 = group_by_first_letter_manual(words)
    r3 = group_by_first_letter_setdefault(words)

    print(f"  defaultdict:  {r1 == r2 == r3}")
    print()

    # --- More Examples with defaultdict ---
    print("--- More defaultdict Use Cases ---")
    print()

    # Example: Counting
    print("  1. Counting (defaultdict(int)):")
    counter = defaultdict(int)
    for char in "mississippi":
        counter[char] += 1
    print(f"     'mississippi' → {dict(counter)}")
    print()

    # Example: Grouping students by grade
    print("  2. Grouping students by grade:")
    students = [("Alice", "A"), ("Bob", "B"), ("Charlie", "A"),
                ("Diana", "B"), ("Eve", "A"), ("Frank", "C")]
    by_grade = defaultdict(list)
    for name, grade in students:
        by_grade[grade].append(name)
    print(f"     Students: {students}")
    for grade in sorted(by_grade):
        print(f"       Grade {grade}: {by_grade[grade]}")
    print()

    # Example: Adjacency list (graph)
    print("  3. Building a graph (adjacency list):")
    edges = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")]
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Undirected
    print(f"     Edges: {edges}")
    for node in sorted(graph):
        print(f"       {node} → {graph[node]}")
    print()

    # --- Edge Cases ---
    print("--- Edge Cases ---")
    print()
    edge_cases = [
        ([], "Empty list"),
        (["apple"], "Single word"),
        (["Apple", "avocado", "APRICOT"], "Mixed case"),
        (["123abc", "456def"], "Starting with numbers"),
    ]

    for words_ec, desc in edge_cases:
        result_ec = group_by_first_letter(words_ec)
        print(f"  {desc:>25}: {words_ec}")
        print(f"  {'':>25}  → {result_ec}")
        print()

    print("ANSWER:")
    print("  defaultdict(list) auto-creates empty lists for new keys,")
    print("  making grouping clean and Pythonic with O(n) time complexity.")


if __name__ == "__main__":
    demonstrate()
