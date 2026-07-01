"""
Q2. Write a function that finds the longest substring without repeating
    characters. Example: 'abcabcbb' → 3 ('abc'). Use the sliding window technique.

Answer:
    Use the SLIDING WINDOW technique with two pointers (left, right) and a
    set/dict to track characters in the current window.

    Time Complexity:  O(n) — each character is visited at most twice
                             (once by right, once by left).
    Space Complexity: O(min(n, m)) — where m is the size of the character set.

    Algorithm:
    1. Expand window by moving `right` pointer.
    2. If duplicate found → shrink window by moving `left` pointer.
    3. Track the maximum window size.
"""


# ============================================================
# Method 1: Sliding Window with Set ★ RECOMMENDED ★
# ============================================================
def longest_unique_substring(s: str) -> tuple:
    """
    Find the longest substring without repeating characters.

    Uses a sliding window with a set to track characters in the window.

    Time:  O(n) — each pointer moves at most n times.
    Space: O(min(n, m)) — set holds unique chars in the window.

    Returns:
        (length, substring) — length and the actual substring.
    """
    char_set = set()
    left = 0
    max_len = 0
    max_start = 0

    for right in range(len(s)):
        # Shrink window while duplicate exists
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add current character to window
        char_set.add(s[right])

        # Update max if current window is larger
        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_start = left

    return max_len, s[max_start:max_start + max_len]


# ============================================================
# Method 2: Sliding Window with Dict (optimized — jump left pointer)
# ============================================================
def longest_unique_substring_optimized(s: str) -> tuple:
    """
    Optimized sliding window using a dict to store last-seen indices.
    Instead of shrinking one by one, jump `left` directly past the duplicate.

    Time:  O(n) — single pass.
    Space: O(min(n, m))
    """
    last_seen = {}  # char → last index
    left = 0
    max_len = 0
    max_start = 0

    for right in range(len(s)):
        char = s[right]

        # If char was seen and is within current window
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1  # Jump past the duplicate

        last_seen[char] = right

        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_start = left

    return max_len, s[max_start:max_start + max_len]


# ============================================================
# Method 3: Brute Force (for comparison) — O(n³)
# ============================================================
def longest_unique_substring_brute(s: str) -> tuple:
    """
    Brute force: check every substring for uniqueness.
    Time:  O(n³)
    Space: O(n)
    """
    max_len = 0
    max_sub = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(substring) == len(set(substring)):  # All unique
                if len(substring) > max_len:
                    max_len = len(substring)
                    max_sub = substring

    return max_len, max_sub


def demonstrate():
    print("=" * 70)
    print("Q2: Longest Substring Without Repeating Characters")
    print("=" * 70)
    print()

    # --- Sliding Window Concept ---
    print("--- Sliding Window Technique ---")
    print()
    print("  The 'window' is a range [left, right] that expands and contracts.")
    print()
    print("  Rule: The window must NEVER contain duplicate characters.")
    print()
    print("  1. Move RIGHT to expand the window (add new character).")
    print("  2. If a duplicate is found → move LEFT to shrink (remove chars).")
    print("  3. Track the maximum window size seen.")
    print()

    # --- Step-by-Step Walkthrough ---
    print("--- Step-by-Step Walkthrough: 'abcabcbb' ---")
    print()
    s = "abcabcbb"
    print(f"  String: '{s}'")
    print()

    char_set = set()
    left = 0
    max_len = 0

    print(f"  {'Step':>4} | {'right':>5} | {'char':>4} | {'Action':>30} | {'Window':>12} | {'Set':>15} | {'Max':>3}")
    print(f"  {'-'*4} | {'-'*5} | {'-'*4} | {'-'*30} | {'-'*12} | {'-'*15} | {'-'*3}")

    step = 0
    for right in range(len(s)):
        step += 1
        char = s[right]

        if char in char_set:
            # Need to shrink
            action = f"'{char}' duplicate! Shrink left"
            while s[left] != char:
                char_set.remove(s[left])
                left += 1
            char_set.remove(s[left])
            left += 1

        char_set.add(char)
        window_len = right - left + 1
        max_len = max(max_len, window_len)
        window_str = s[left:right + 1]

        if char not in s[left:right]:
            action = f"Add '{char}' to window"

        print(f"  {step:>4} | {right:>5} | {char:>4} | {action:>30} | {window_str:>12} | {str(sorted(char_set)):>15} | {max_len:>3}")

    print()
    print(f"  Answer: {max_len} (substring: '{s[0:max_len]}')")
    print()

    # --- Visual Window Diagram ---
    print("--- Visual: Sliding Window on 'abcabcbb' ---")
    print()
    s = "abcabcbb"

    windows = [
        (0, 0, "a"),
        (0, 1, "ab"),
        (0, 2, "abc"),
        (1, 3, "bca"),
        (2, 4, "cab"),
        (3, 5, "abc"),
        (5, 6, "cb"),
        (6, 7, "b"),
    ]

    for left, right, window in windows:
        visual = ""
        for i, c in enumerate(s):
            if left <= i <= right:
                visual += f"[{c}]"
            else:
                visual += f" {c} "
        max_mark = " ★ MAX" if len(window) == 3 else ""
        print(f"    {visual}  window='{window}' len={len(window)}{max_mark}")

    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ("abcabcbb", 3, "Standard case"),
        ("bbbbb", 1, "All same characters"),
        ("pwwkew", 3, "Middle substring"),
        ("", 0, "Empty string"),
        ("a", 1, "Single char"),
        ("abcdef", 6, "All unique"),
        ("dvdf", 3, "Tricky overlap"),
        ("anviaj", 5, "Near-end duplicate"),
        ("abba", 2, "Palindrome-like"),
    ]

    print(f"  {'Input':>15}  |  {'Expected':>8}  |  {'Got':>3}  |  {'Substring':>12}  |  {'✓/✗':>3}")
    print(f"  {'-'*15}  |  {'-'*8}  |  {'-'*3}  |  {'-'*12}  |  {'-'*3}")

    all_pass = True
    for s, expected, desc in test_cases:
        length, substr = longest_unique_substring(s)
        status = "✓" if length == expected else "✗"
        if length != expected:
            all_pass = False
        print(f"  {repr(s):>15}  |  {expected:>8}  |  {length:>3}  |  {repr(substr):>12}  |  {status:>3}")

    print()
    print(f"  All tests passed: {'✓ YES' if all_pass else '✗ NO'}")
    print()

    # --- Verify both methods agree ---
    print("--- Method Comparison ---")
    print()
    for s, _, desc in test_cases:
        l1, s1 = longest_unique_substring(s)
        l2, s2 = longest_unique_substring_optimized(s)
        match = "✓" if l1 == l2 else "✗"
        print(f"  {repr(s):>15}  |  Set: {l1} ({repr(s1)})  |  Dict: {l2} ({repr(s2)})  |  {match}")

    print()

    # --- Complexity Comparison ---
    print("--- Complexity Comparison ---")
    print()
    print("  Method                  | Time   | Space          | Notes")
    print("  ------------------------|--------|----------------|---------------------")
    print("  Brute Force             | O(n³)  | O(n)           | Check every substring")
    print("  Sliding Window + Set ★  | O(n)   | O(min(n, m))   | Shrink one-by-one")
    print("  Sliding Window + Dict   | O(n)   | O(min(n, m))   | Jump past duplicate")
    print()

    # --- Performance ---
    import time

    print("--- Performance Benchmark ---")
    print()

    import random
    import string

    sizes = [100, 1_000, 10_000, 100_000]

    print(f"  {'n':>8}  |  {'Set Window':>12}  |  {'Dict Window':>13}")
    print(f"  {'-'*8}  |  {'-'*12}  |  {'-'*13}")

    for n in sizes:
        s = ''.join(random.choices(string.ascii_lowercase, k=n))

        start = time.perf_counter()
        _ = longest_unique_substring(s)
        set_time = (time.perf_counter() - start) * 1000

        start = time.perf_counter()
        _ = longest_unique_substring_optimized(s)
        dict_time = (time.perf_counter() - start) * 1000

        print(f"  {n:>8,}  |  {set_time:>9.3f} ms  |  {dict_time:>10.3f} ms")

    print()
    print("ANSWER:")
    print("  Use sliding window: expand right, shrink left on duplicates.")
    print("  Time: O(n), Space: O(min(n, m))")
    print("  For 'abcabcbb' → longest unique substring is 'abc', length 3.")


if __name__ == "__main__":
    demonstrate()
