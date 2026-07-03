"""
Q6. Generate all valid combinations of n pairs of parentheses.
    n=3 → ['((()))','(()())','(())()','()(())','()()()']

Answer:
    Backtracking with two counters: open_count and close_count.
    Rules:
    - Can add '(' if open_count < n
    - Can add ')' if close_count < open_count

    Time: O(4^n / sqrt(n)) — Catalan number.
    Space: O(n) recursion depth.
"""


def generate_parentheses(n):
    """Generate all valid parentheses combinations."""
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(''.join(current))
            return

        if open_count < n:
            current.append('(')
            backtrack(current, open_count + 1, close_count)
            current.pop()

        if close_count < open_count:
            current.append(')')
            backtrack(current, open_count, close_count + 1)
            current.pop()

    backtrack([], 0, 0)
    return result


def demonstrate():
    print("=" * 70)
    print("Q6: Generate Valid Parentheses")
    print("=" * 70)
    print()

    for n in range(1, 5):
        result = generate_parentheses(n)
        print(f"  n={n}: {result} ({len(result)} combinations)")
    print()

    # --- Rules ---
    print("--- Rules for Valid Parentheses ---")
    print()
    print("  1. Add '(' if open_count < n     (don't exceed n opens)")
    print("  2. Add ')' if close_count < open  (can't close without open)")
    print()
    print("  These two rules guarantee EVERY generated string is valid!")
    print()

    # --- Recursion Tree for n=3 ---
    print("--- Recursion Tree for n=3 ---")
    print()
    print("                              ''")
    print("                              |")
    print("                             '('")
    print("                          /        \\")
    print("                       '(('        '()'")
    print("                      /    \\         |")
    print("                   '((('   '(()'   '()('")
    print("                    |      / \\      |")
    print("                '((()'  '(()(' '(())'  '()(('")
    print("                  |       |      |       |")
    print("               '((())'  ...    ...     ...")
    print("                  ↓")
    print("               '((()))' ✓")
    print()

    # --- Trace ---
    print("--- Trace for n=2 ---")
    print()

    def backtrack_trace(current, o, c, n, depth=0):
        indent = "    " * depth
        state = ''.join(current)
        print(f"  {indent}'{state}' (open={o}, close={c})")

        if len(current) == 2 * n:
            print(f"  {indent}  → VALID: '{state}' ✓")
            return

        if o < n:
            print(f"  {indent}  Add '(' (open {o}→{o+1})")
            current.append('(')
            backtrack_trace(current, o + 1, c, n, depth + 1)
            current.pop()

        if c < o:
            print(f"  {indent}  Add ')' (close {c}→{c+1})")
            current.append(')')
            backtrack_trace(current, o, c + 1, n, depth + 1)
            current.pop()

    backtrack_trace([], 0, 0, 2)
    print()

    # --- Why it works ---
    print("--- Why Only Valid Strings Are Generated ---")
    print()
    print("  Invalid: '())' → close_count (2) > open_count (1) → blocked by rule 2")
    print("  Invalid: '(((' for n=2 → open_count (3) > n (2) → blocked by rule 1")
    print()
    print("  At every point in construction:")
    print("    close_count ≤ open_count ≤ n")
    print("  This is the definition of valid parentheses!")
    print()

    # Catalan numbers
    print("--- Count = Catalan Numbers ---")
    print()
    import math
    print("  | n | Count | Catalan(n) |")
    print("  |---|-------|------------|")
    for n in range(1, 8):
        count = len(generate_parentheses(n))
        catalan = math.comb(2*n, n) // (n + 1)
        print(f"  | {n} | {count:>5} | {catalan:>10} |")

    print()
    print("  Catalan(n) = C(2n,n)/(n+1)")
    print("  Time: O(4^n/√n) | Space: O(n)")


if __name__ == "__main__":
    demonstrate()
