"""
Q8. Write a function that, given a string of parentheses and brackets,
    checks if it is balanced. Example: '([])' → True, '([)]' → False.

Answer:
    Use a STACK (Last-In, First-Out). For each character:
    - Opening bracket → push onto stack.
    - Closing bracket → pop from stack and check if it matches.
    - If stack is empty at end and all brackets matched → balanced!

    Time Complexity:  O(n) — single pass through the string.
    Space Complexity: O(n) — stack can hold up to n/2 opening brackets.
"""


def is_balanced(s: str) -> bool:
    """
    Check if a string of brackets/parentheses is balanced using a stack.

    Rules:
    1. Every opening bracket must have a matching closing bracket.
    2. Brackets must be properly nested (no interleaving).
    3. Closing bracket must match the most recent unmatched opening bracket.

    Time:  O(n) — single pass.
    Space: O(n) — stack holds opening brackets.

    Examples:
        >>> is_balanced('([])')
        True
        >>> is_balanced('([)]')
        False
    """
    stack = []

    # Mapping: closing → opening
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    opening = set(bracket_map.values())  # {'(', '[', '{'}
    closing = set(bracket_map.keys())    # {')', ']', '}'}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False  # Closing bracket with no matching opening
            if stack[-1] != bracket_map[char]:
                return False  # Mismatched bracket types
            stack.pop()
        # Ignore non-bracket characters

    return len(stack) == 0  # Stack must be empty for balanced


# ============================================================
# Extended: Return details about the mismatch
# ============================================================
def check_balanced_detailed(s: str) -> dict:
    """
    Check if balanced and return detailed information.

    Returns:
        {
            'balanced': bool,
            'error': str or None,
            'error_position': int or None,
            'stack_state': list
        }
    """
    stack = []  # Stores (char, index)
    bracket_map = {')': '(', ']': '[', '}': '{'}
    opening = set(bracket_map.values())
    closing = set(bracket_map.keys())

    for i, char in enumerate(s):
        if char in opening:
            stack.append((char, i))
        elif char in closing:
            if not stack:
                return {
                    'balanced': False,
                    'error': f"Closing '{char}' at position {i} has no matching opening",
                    'error_position': i,
                    'stack_state': []
                }
            top_char, top_pos = stack[-1]
            if top_char != bracket_map[char]:
                return {
                    'balanced': False,
                    'error': f"Closing '{char}' at position {i} doesn't match opening '{top_char}' at position {top_pos}",
                    'error_position': i,
                    'stack_state': [c for c, _ in stack]
                }
            stack.pop()

    if stack:
        unclosed = [(c, i) for c, i in stack]
        return {
            'balanced': False,
            'error': f"Unclosed brackets: {unclosed}",
            'error_position': stack[-1][1],
            'stack_state': [c for c, _ in stack]
        }

    return {
        'balanced': True,
        'error': None,
        'error_position': None,
        'stack_state': []
    }


def demonstrate():
    print("=" * 70)
    print("Q8: Balanced Parentheses and Brackets Checker")
    print("=" * 70)
    print()

    # --- How Stack Works ---
    print("--- How the Stack Approach Works ---")
    print()
    print("  A STACK is Last-In, First-Out (LIFO).")
    print("  Perfect for matching brackets because the most recent")
    print("  opening bracket must be closed first.")
    print()
    print("  Rules:")
    print("    1. Opening bracket ( [ { → PUSH onto stack")
    print("    2. Closing bracket ) ] } → POP from stack and CHECK match")
    print("    3. At end: stack must be EMPTY for balanced string")
    print()

    # --- Step-by-Step: Balanced Example ---
    print("--- Walkthrough 1: '([])' → True ---")
    print()
    s = "([])"
    print(f"  Input: '{s}'")
    print()

    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    print(f"  {'Step':>4} | {'Char':>4} | {'Action':>25} | {'Stack':>15} | {'Status'}")
    print(f"  {'-'*4} | {'-'*4} | {'-'*25} | {'-'*15} | {'-'*12}")

    for i, char in enumerate(s):
        if char in '([{':
            stack.append(char)
            action = f"PUSH '{char}'"
            status = "OK"
        elif char in ')]}':
            if stack and stack[-1] == bracket_map[char]:
                popped = stack.pop()
                action = f"POP '{popped}' matches '{char}'"
                status = "✓ Match"
            else:
                action = f"MISMATCH!"
                status = "✗ Error"

        print(f"  {i+1:>4} | {char:>4} | {action:>25} | {str(stack):>15} | {status}")

    final = "✓ BALANCED" if not stack else "✗ UNBALANCED"
    print(f"  {'':>4} | {'':>4} | {'Stack empty?':>25} | {str(stack):>15} | {final}")
    print()

    # --- Step-by-Step: Unbalanced Example ---
    print("--- Walkthrough 2: '([)]' → False ---")
    print()
    s = "([)]"
    print(f"  Input: '{s}'")
    print()

    stack = []

    print(f"  {'Step':>4} | {'Char':>4} | {'Action':>30} | {'Stack':>15} | {'Status'}")
    print(f"  {'-'*4} | {'-'*4} | {'-'*30} | {'-'*15} | {'-'*12}")

    for i, char in enumerate(s):
        if char in '([{':
            stack.append(char)
            action = f"PUSH '{char}'"
            status = "OK"
        elif char in ')]}':
            if stack and stack[-1] == bracket_map[char]:
                popped = stack.pop()
                action = f"POP '{popped}' matches '{char}'"
                status = "✓ Match"
            elif stack:
                action = f"Top is '{stack[-1]}', need '{bracket_map[char]}'"
                status = "✗ MISMATCH!"
            else:
                action = f"Stack empty! No match for '{char}'"
                status = "✗ ERROR"

        print(f"  {i+1:>4} | {char:>4} | {action:>30} | {str(stack):>15} | {status}")

        if "MISMATCH" in status or "ERROR" in status:
            print()
            print(f"  → STOPPED: '{s}' is NOT balanced!")
            break

    print()

    # --- Visual: Why '([)]' Fails ---
    print("--- Visual: Why '([)]' is Invalid ---")
    print()
    print("  Valid nesting:   ( [ ] )      Brackets properly nested")
    print("                   ( [   ]  )   Inner pair closed before outer")
    print()
    print("  Invalid nesting: ( [ ) ]      Brackets interleaved!")
    print("                   ( [   ) ]    ']' should come before ')'")
    print("                       ↑ ')' expects '(' but finds '['")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ("()", True, "Simple parens"),
        ("([])", True, "Nested mixed"),
        ("{[()]}", True, "Triple nested"),
        ("([)]", False, "Interleaved"),
        ("(", False, "Unclosed"),
        (")", False, "No opening"),
        ("", True, "Empty string"),
        ("((()))", True, "Deep nesting"),
        ("{[}", False, "Missing close"),
        ("()[]{}", True, "Sequential pairs"),
        ("((())(()))", True, "Complex valid"),
        ("({[()]})", True, "All three types"),
        ("]", False, "Single closing"),
        ("[(])", False, "Wrong order"),
        ("(((((((((())))))))))", True, "Very deep"),
    ]

    print(f"  {'Input':>25}  | {'Expected':>8} | {'Got':>5} | {'✓/✗':>3}")
    print(f"  {'-'*25}  | {'-'*8} | {'-'*5} | {'-'*3}")

    all_pass = True
    for s, expected, desc in test_cases:
        result = is_balanced(s)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_pass = False
        print(f"  {repr(s):>25}  | {str(expected):>8} | {str(result):>5} | {status:>3}")

    print()
    print(f"  All tests passed: {'✓ YES' if all_pass else '✗ NO'}")
    print()

    # --- Detailed Error Messages ---
    print("--- Detailed Error Reports ---")
    print()

    error_cases = [
        "([)]",
        "(()",
        "())",
        "{[}",
        "((())(",
    ]

    for s in error_cases:
        result = check_balanced_detailed(s)
        print(f"  '{s}':")
        if result['balanced']:
            print(f"    ✓ Balanced")
        else:
            print(f"    ✗ {result['error']}")

            # Visual pointer to error
            if result['error_position'] is not None:
                pointer = "    " + " " * (result['error_position']) + "↑"
                print(f"    {s}")
                print(pointer)
        print()

    # --- The Code ---
    print("--- The Implementation ---")
    print()
    print("  def is_balanced(s):")
    print("      stack = []")
    print("      bracket_map = {')':'(', ']':'[', '}':'{'}")
    print()
    print("      for char in s:")
    print("          if char in '([{':          # Opening")
    print("              stack.append(char)       #   → push")
    print("          elif char in ')]}':         # Closing")
    print("              if not stack:            #   → empty stack = error")
    print("                  return False")
    print("              if stack[-1] != bracket_map[char]:  # mismatch")
    print("                  return False")
    print("              stack.pop()              #   → match! pop it")
    print()
    print("      return len(stack) == 0           # Must be empty at end")
    print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Time:  O(n) — single pass through the string")
    print("  Space: O(n) — stack holds up to n/2 opening brackets")
    print()
    print("ANSWER:")
    print("  Use a STACK. Push opening brackets, pop and match on closing.")
    print("  '([])' → True (properly nested)")
    print("  '([)]' → False (interleaved, ')' doesn't match '[')")


if __name__ == "__main__":
    demonstrate()
