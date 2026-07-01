"""
Q2. Write a function that evaluates a postfix expression (Reverse Polish
    Notation). Example: ['2','1','+','3','*'] → 9.

Answer:
    Use a STACK. Scan tokens left to right:
    - Number → push onto stack.
    - Operator → pop two operands, apply operator, push result.

    At the end, the stack contains exactly one element: the answer.

    Time Complexity:  O(n) — process each token once.
    Space Complexity: O(n) — stack holds operands.

    Why RPN? No parentheses needed, no precedence rules!
    Infix:   (2 + 1) * 3 = 9
    Postfix:  2 1 + 3 *   = 9
"""


def eval_postfix(tokens: list) -> float:
    """
    Evaluate a postfix (Reverse Polish Notation) expression.

    Rules:
    - Number token → push to stack.
    - Operator token → pop two, compute, push result.

    Time:  O(n)
    Space: O(n)

    Example:
        >>> eval_postfix(['2', '1', '+', '3', '*'])
        9
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            # Pop two operands (note: order matters for - and /)
            b = stack.pop()  # Second operand (popped first)
            a = stack.pop()  # First operand (popped second)

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = int(a / b)  # Truncate toward zero (LeetCode style)

            stack.append(result)
        else:
            # It's a number — push onto stack
            stack.append(int(token))

    return stack[0]  # Final result


def demonstrate():
    print("=" * 70)
    print("Q2: Evaluate Postfix Expression (Reverse Polish Notation)")
    print("=" * 70)
    print()

    # --- What is Postfix? ---
    print("--- What is Postfix (RPN)? ---")
    print()
    print("  Infix (normal):   (2 + 1) * 3 = 9")
    print("  Postfix (RPN):    2 1 + 3 *    = 9")
    print()
    print("  In postfix, operators come AFTER their operands.")
    print("  No parentheses needed! No precedence ambiguity!")
    print()
    print("  Algorithm:")
    print("    - Number → push to stack")
    print("    - Operator → pop 2 values, compute, push result")
    print()

    # --- Step-by-Step: ['2','1','+','3','*'] ---
    print("=" * 70)
    print("TRACE: ['2', '1', '+', '3', '*']  →  (2 + 1) * 3 = 9")
    print("=" * 70)
    print()

    tokens = ['2', '1', '+', '3', '*']
    stack = []

    print(f"  {'Step':>4} | {'Token':>6} | {'Action':>30} | {'Stack':>15}")
    print(f"  {'-'*4} | {'-'*6} | {'-'*30} | {'-'*15}")

    step = 0
    for token in tokens:
        step += 1
        if token in {'+', '-', '*', '/'}:
            b = stack.pop()
            a = stack.pop()
            if token == '+': result = a + b
            elif token == '-': result = a - b
            elif token == '*': result = a * b
            elif token == '/': result = int(a / b)
            action = f"Pop {a},{b} → {a} {token} {b} = {result}"
            stack.append(result)
        else:
            stack.append(int(token))
            action = f"Push {token}"

        print(f"  {step:>4} | {token:>6} | {action:>30} | {str(stack):>15}")

    print()
    print(f"  Final result: {stack[0]}")
    print()

    # --- Another Example ---
    print("=" * 70)
    print("TRACE: ['4', '13', '5', '/', '+']  →  4 + (13 / 5) = 6")
    print("=" * 70)
    print()

    tokens2 = ['4', '13', '5', '/', '+']
    stack2 = []

    print(f"  {'Step':>4} | {'Token':>6} | {'Action':>30} | {'Stack':>15}")
    print(f"  {'-'*4} | {'-'*6} | {'-'*30} | {'-'*15}")

    step = 0
    for token in tokens2:
        step += 1
        if token in {'+', '-', '*', '/'}:
            b = stack2.pop()
            a = stack2.pop()
            if token == '+': result = a + b
            elif token == '-': result = a - b
            elif token == '*': result = a * b
            elif token == '/': result = int(a / b)
            action = f"Pop {a},{b} → {a} {token} {b} = {result}"
            stack2.append(result)
        else:
            stack2.append(int(token))
            action = f"Push {token}"

        print(f"  {step:>4} | {token:>6} | {action:>30} | {str(stack2):>15}")

    print()
    print(f"  Final result: {stack2[0]}")
    print()

    # --- Visual Stack Diagram ---
    print("--- Visual: Stack During ['2','1','+','3','*'] ---")
    print()
    print("  Push 2    Push 1    + (pop 2)    Push 3    * (pop 2)")
    print("                      push 3                push 9")
    print()
    print("  ┌───┐    ┌───┐    ┌───┐        ┌───┐    ┌───┐")
    print("  │   │    │ 1 │    │   │        │ 3 │    │   │")
    print("  │ 2 │    │ 2 │    │ 3 │        │ 3 │    │ 9 │")
    print("  └───┘    └───┘    └───┘        └───┘    └───┘")
    print("                    2+1=3                  3*3=9")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        (['2', '1', '+', '3', '*'], 9, "(2+1)*3"),
        (['4', '13', '5', '/', '+'], 6, "4+(13/5)"),
        (['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'],
         22, "Complex expression"),
        (['3', '4', '+'], 7, "3+4"),
        (['5', '1', '2', '+', '4', '*', '+', '3', '-'], 14, "5+((1+2)*4)-3"),
        (['2', '3', '*'], 6, "2*3"),
        (['7'], 7, "Single number"),
        (['15', '7', '1', '1', '+', '-', '/', '3', '*', '2', '1', '1', '+', '+', '-'],
         5, "LeetCode example"),
    ]

    print(f"  {'Infix':>22} | {'Postfix Tokens':>45} | {'Expected':>8} | {'Got':>5} | {'✓/✗':>3}")
    print(f"  {'-'*22} | {'-'*45} | {'-'*8} | {'-'*5} | {'-'*3}")

    for tokens, expected, infix in test_cases:
        result = eval_postfix(tokens)
        status = "✓" if result == expected else "✗"
        tok_str = str(tokens) if len(str(tokens)) <= 43 else str(tokens)[:40] + "..."
        print(f"  {infix:>22} | {tok_str:>45} | {expected:>8} | {result:>5} | {status:>3}")

    print()

    # --- Why Postfix Matters ---
    print("--- Why Postfix Matters ---")
    print()
    print("  1. CALCULATORS: HP calculators and many scientific calculators use RPN")
    print("  2. COMPILERS: Convert infix → postfix for unambiguous evaluation")
    print("  3. VIRTUAL MACHINES: JVM and Python bytecode use stack-based execution")
    print("  4. NO PRECEDENCE: No need for ( ) or * before + rules")
    print()

    # --- Infix vs Postfix vs Prefix ---
    print("--- Notation Comparison ---")
    print()
    print("  Expression      | Infix        | Postfix     | Prefix")
    print("  ----------------|--------------|-------------|----------")
    print("  (2+1)*3         | (2 + 1) * 3  | 2 1 + 3 *   | * + 2 1 3")
    print("  2+(1*3)         | 2 + 1 * 3    | 2 1 3 * +   | + 2 * 1 3")
    print("  (a+b)*(c-d)     | (a+b)*(c-d)  | a b + c d - *| * + a b - c d")
    print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Time:  O(n) — process each token exactly once")
    print("  Space: O(n) — stack holds at most n/2 operands")
    print()
    print("ANSWER: Use a stack. Numbers get pushed; operators pop two,")
    print("compute, and push the result. Final stack value = answer.")


if __name__ == "__main__":
    demonstrate()
