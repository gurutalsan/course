"""
Q4. Write a function that checks if a string is a palindrome.
    What is its time complexity? What is its space complexity?

Answer:
    Time Complexity:  O(n)  — We compare characters from both ends, examining
                              at most n/2 pairs, which simplifies to O(n).
    Space Complexity: O(1)  — We use only two pointer variables (constant extra space).

    Note: A naive approach using slicing (s == s[::-1]) is also O(n) time but
    O(n) space because s[::-1] creates a new reversed string.
"""


# ============================================================
# Method 1: Two-Pointer Approach (Optimal)
# Time: O(n), Space: O(1)
# ============================================================
def is_palindrome_two_pointer(s: str) -> bool:
    """
    Check if a string is a palindrome using two pointers.

    Time Complexity:  O(n) — each character is visited at most once.
    Space Complexity: O(1) — only two integer variables used.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# ============================================================
# Method 2: Slice Comparison (Pythonic but uses more space)
# Time: O(n), Space: O(n)
# ============================================================
def is_palindrome_slice(s: str) -> bool:
    """
    Check if a string is a palindrome using string slicing.

    Time Complexity:  O(n) — reversing the string takes O(n).
    Space Complexity: O(n) — s[::-1] creates a new string of length n.
    """
    return s == s[::-1]


# ============================================================
# Method 3: Recursive Approach
# Time: O(n), Space: O(n) due to call stack
# ============================================================
def is_palindrome_recursive(s: str, left: int = 0, right: int = None) -> bool:
    """
    Check if a string is a palindrome using recursion.

    Time Complexity:  O(n) — n/2 recursive calls.
    Space Complexity: O(n) — call stack depth is n/2, simplified to O(n).
    """
    if right is None:
        right = len(s) - 1

    # Base case: pointers have crossed or met
    if left >= right:
        return True

    # Check current characters
    if s[left] != s[right]:
        return False

    return is_palindrome_recursive(s, left + 1, right - 1)


# ============================================================
# Bonus: Case-insensitive, alphanumeric-only palindrome check
# ============================================================
def is_palindrome_clean(s: str) -> bool:
    """
    Check if a string is a palindrome, ignoring non-alphanumeric
    characters and case.

    Time Complexity:  O(n)
    Space Complexity: O(1) — two-pointer, no extra string created.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def demonstrate_palindrome():
    """Run all palindrome methods on test cases."""
    print("=" * 65)
    print("Q4: Palindrome Checker — Time & Space Complexity Analysis")
    print("=" * 65)
    print()

    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("madam", True),
        ("a", True),
        ("ab", False),
        ("abba", True),
        ("abcba", True),
        ("", True),
        ("Was it a car or a cat I saw", True),  # clean version only
    ]

    # --- Method Comparison ---
    print("--- Method Comparison ---")
    print()
    print("  Method              | Time  | Space | Notes")
    print("  --------------------|-------|-------|---------------------------")
    print("  Two-Pointer         | O(n)  | O(1)  | Optimal; in-place")
    print("  Slice (s[::-1])     | O(n)  | O(n)  | Creates reversed copy")
    print("  Recursive           | O(n)  | O(n)  | Call stack = O(n/2) ≈ O(n)")
    print("  Clean (alnum+lower) | O(n)  | O(1)  | Ignores punctuation/case")
    print()

    # --- Test Results ---
    print("--- Test Results (Two-Pointer Method) ---")
    print()
    print(f"  {'Input':>30}  |  {'Expected':>8}  |  {'Result':>8}  |  {'✓/✗':>3}")
    print(f"  {'-'*30}  |  {'-'*8}  |  {'-'*8}  |  {'-'*3}")

    for s, expected in test_cases[:-1]:  # Exclude the sentence test
        result = is_palindrome_two_pointer(s)
        status = "✓" if result == expected else "✗"
        print(f"  {repr(s):>30}  |  {str(expected):>8}  |  {str(result):>8}  |  {status:>3}")

    print()

    # --- Clean method for sentence ---
    print("--- Bonus: Clean Palindrome Check (ignore case & punctuation) ---")
    print()
    sentence = "Was it a car or a cat I saw"
    result = is_palindrome_clean(sentence)
    print(f'  Input:  "{sentence}"')
    print(f"  Result: {result}")
    print()

    # --- Step-by-Step Walkthrough ---
    print("--- Step-by-Step Walkthrough: 'racecar' ---")
    print()
    s = "racecar"
    left = 0
    right = len(s) - 1
    step = 0

    while left < right:
        step += 1
        match = "✓ match" if s[left] == s[right] else "✗ mismatch"
        print(f"  Step {step}: Compare s[{left}]='{s[left]}' with s[{right}]='{s[right]}'  → {match}")
        left += 1
        right -= 1

    print(f"  Step {step + 1}: Pointers crossed (left={left} >= right={right}) → Palindrome!")
    print()
    print(f"  Total comparisons: {step} (n/2 = {len(s)//2})")
    print(f"  Time Complexity: O(n) where n = {len(s)}")
    print(f"  Space Complexity: O(1) — only 'left' and 'right' variables used")
    print()
    print("ANSWER:")
    print("  Time Complexity:  O(n) — we check n/2 pairs ≈ O(n)")
    print("  Space Complexity: O(1) — two pointer variables (constant space)")


if __name__ == "__main__":
    demonstrate_palindrome()
