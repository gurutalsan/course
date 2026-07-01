"""
Q3. Write a function using Counter that finds the most common character
    in a string and returns it with its count.

Answer:
    Use collections.Counter which builds a frequency dictionary in O(n),
    then call .most_common(1) to get the top character in O(1).

    Time Complexity:  O(n) — single pass to count all characters.
    Space Complexity: O(k) — where k is the number of unique characters.
"""

from collections import Counter


def most_common_char(s: str) -> tuple:
    """
    Find the most common character in a string using Counter.

    Args:
        s: Input string.

    Returns:
        Tuple of (character, count). Returns ('', 0) for empty strings.

    Time Complexity:  O(n) — Counter iterates through the string once.
    Space Complexity: O(k) — stores count for each unique character.

    Examples:
        >>> most_common_char("hello")
        ('l', 2)
        >>> most_common_char("aabbbcccc")
        ('c', 4)
    """
    if not s:
        return ('', 0)

    counter = Counter(s)
    # most_common(1) returns a list of [(element, count)] — take the first
    char, count = counter.most_common(1)[0]
    return (char, count)


# ============================================================
# Alternative: Without Counter (manual approach for comparison)
# ============================================================
def most_common_char_manual(s: str) -> tuple:
    """
    Find the most common character without Counter — using a dict.

    Time Complexity:  O(n)
    Space Complexity: O(k)
    """
    if not s:
        return ('', 0)

    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    max_char = max(freq, key=freq.get)
    return (max_char, freq[max_char])


# ============================================================
# Bonus: Top N most common characters
# ============================================================
def top_n_common_chars(s: str, n: int = 3) -> list:
    """
    Find the top N most common characters.

    Returns:
        List of (character, count) tuples, sorted by frequency.
    """
    if not s:
        return []

    counter = Counter(s)
    return counter.most_common(n)


def demonstrate():
    print("=" * 65)
    print("Q3: Most Common Character Using Counter")
    print("=" * 65)
    print()

    # --- How Counter Works ---
    print("--- How collections.Counter Works ---")
    print()
    example = "programming"
    counter = Counter(example)
    print(f"  Input string: '{example}'")
    print(f"  Counter('{example}') →")
    print(f"    {dict(counter)}")
    print()
    print("  Counter builds a frequency dictionary in O(n) — one pass.")
    print("  .most_common(k) returns the k most frequent elements.")
    print()

    # --- The Function ---
    print("--- Function Implementation ---")
    print()
    print("  from collections import Counter")
    print()
    print("  def most_common_char(s):")
    print("      if not s:")
    print("          return ('', 0)")
    print("      counter = Counter(s)")
    print("      char, count = counter.most_common(1)[0]")
    print("      return (char, count)")
    print()

    # --- Test Cases ---
    print("--- Test Results ---")
    print()

    test_cases = [
        ("hello", "Simple word"),
        ("aabbbcccc", "Increasing frequency"),
        ("mississippi", "Classic example"),
        ("programming", "Double letters"),
        ("a", "Single character"),
        ("aabb", "Tied frequency (first counted wins)"),
        ("The quick brown fox jumps over the lazy dog", "Full sentence"),
        ("", "Empty string"),
        ("121212333", "Numeric characters"),
    ]

    print(f"  {'Input':>45}  |  {'Result':>12}  |  {'Count':>5}")
    print(f"  {'-'*45}  |  {'-'*12}  |  {'-'*5}")

    for s, desc in test_cases:
        char, count = most_common_char(s)
        display = repr(s) if len(s) <= 35 else repr(s[:32] + "...")
        char_display = repr(char) if char else "''"
        print(f"  {display:>45}  |  {char_display:>12}  |  {count:>5}")

    print()

    # --- Detailed Walkthrough ---
    print("--- Step-by-Step Walkthrough: 'mississippi' ---")
    print()
    s = "mississippi"
    print(f"  Input: '{s}'")
    print()

    # Build counter step by step
    running_count = {}
    print("  Building frequency counts:")
    for i, char in enumerate(s):
        running_count[char] = running_count.get(char, 0) + 1
        print(f"    Step {i+1:>2}: char='{char}' → counts = {dict(running_count)}")

    print()
    counter = Counter(s)
    print(f"  Final Counter: {dict(counter)}")
    print(f"  most_common(1): {counter.most_common(1)}")
    char, count = most_common_char(s)
    print(f"  Result: ('{char}', {count})")
    print()

    # --- Top N demonstration ---
    print("--- Bonus: Top N Most Common Characters ---")
    print()
    s = "the quick brown fox jumps over the lazy dog"
    print(f"  Input: '{s}'")
    print()

    top = top_n_common_chars(s, n=5)
    print("  Top 5 most common characters:")
    for rank, (char, count) in enumerate(top, 1):
        bar = "█" * count
        char_display = "' '" if char == ' ' else f"'{char}'"
        print(f"    #{rank}  {char_display:>4}  → {count:>2} times  {bar}")

    print()

    # --- Full frequency visualization ---
    print("--- Full Frequency Distribution: 'mississippi' ---")
    print()
    s = "mississippi"
    counter = Counter(s)

    for char, count in counter.most_common():
        bar = "█" * (count * 3)
        print(f"    '{char}' : {count:>2}  {bar}")

    print()
    print("ANSWER:")
    print("  Use Counter(s).most_common(1)[0] to get (char, count).")
    print("  Time: O(n), Space: O(k) where k = unique characters.")


if __name__ == "__main__":
    demonstrate()
