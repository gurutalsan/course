"""
Q5. Write a function that uses a stack to convert an infix expression
    like '3 + 4 * 2' to postfix '3 4 2 * +'.

Answer:
    Use the SHUNTING-YARD algorithm (by Dijkstra):

    1. If token is a NUMBER → add to output.
    2. If token is an OPERATOR → pop operators with higher/equal precedence
       from the stack to output, then push current operator.
    3. If token is '(' → push to stack.
    4. If token is ')' → pop to output until '(' is found.
    5. At end → pop all remaining operators to output.

    Time:  O(n)
    Space: O(n)
"""


def infix_to_postfix(expression: str) -> str:
    """
    Convert infix expression to postfix using the Shunting-Yard algorithm.

    Time:  O(n)
    Space: O(n)

    Example:
        >>> infix_to_postfix('3 + 4 * 2')
        '3 4 2 * +'
    """
    # Operator precedence and associativity
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    right_associative = {'^'}  # Only ^ is right-associative

    output = []
    operator_stack = []

    tokens = tokenize(expression)

    for token in tokens:
        if token.isdigit() or (token[0].isdigit()):
            # Number → straight to output
            output.append(token)

        elif token == '(':
            operator_stack.append(token)

        elif token == ')':
            # Pop until '(' is found
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()  # Remove the '('

        elif token in precedence:
            # Operator: pop higher/equal precedence operators
            while (operator_stack and
                   operator_stack[-1] != '(' and
                   operator_stack[-1] in precedence and
                   (precedence[operator_stack[-1]] > precedence[token] or
                    (precedence[operator_stack[-1]] == precedence[token] and
                     token not in right_associative))):
                output.append(operator_stack.pop())
            operator_stack.append(token)

    # Pop remaining operators
    while operator_stack:
        output.append(operator_stack.pop())

    return ' '.join(output)


def tokenize(expression: str) -> list:
    """Split expression into tokens."""
    tokens = []
    current_num = ''

    for char in expression:
        if char.isdigit() or char == '.':
            current_num += char
        elif char == ' ':
            if current_num:
                tokens.append(current_num)
                current_num = ''
        else:
            if current_num:
                tokens.append(current_num)
                current_num = ''
            tokens.append(char)

    if current_num:
        tokens.append(current_num)

    return tokens


def demonstrate():
    print("=" * 70)
    print("Q5: Infix to Postfix Conversion (Shunting-Yard Algorithm)")
    print("=" * 70)
    print()

    # --- The Problem ---
    print("--- The Problem ---")
    print()
    print("  Infix:   3 + 4 * 2     (humans read this)")
    print("  Postfix: 3 4 2 * +     (computers evaluate this easily)")
    print()
    print("  We need to handle OPERATOR PRECEDENCE:")
    print("    * and / have HIGHER precedence than + and -")
    print("    So '3 + 4 * 2' means '3 + (4 * 2)' = 11, not '(3 + 4) * 2' = 14")
    print()

    # --- Shunting-Yard Rules ---
    print("--- Shunting-Yard Algorithm Rules ---")
    print()
    print("  Token       | Action")
    print("  ------------|-----------------------------------------------")
    print("  Number      | Send directly to OUTPUT")
    print("  (           | Push onto STACK")
    print("  )           | Pop stack to output until '(' found")
    print("  Operator    | Pop higher/equal precedence ops to output,")
    print("              | then push current operator onto stack")
    print("  End         | Pop all remaining operators to output")
    print()
    print("  Precedence: ^ (3) > * / (2) > + - (1)")
    print()

    # --- Step-by-Step: '3 + 4 * 2' ---
    print("=" * 70)
    print("TRACE: '3 + 4 * 2' → '3 4 2 * +'")
    print("=" * 70)
    print()

    expr = '3 + 4 * 2'
    tokens = tokenize(expr)

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    op_stack = []

    print(f"  {'Step':>4} | {'Token':>6} | {'Action':>35} | {'Output':>15} | {'Stack':>10}")
    print(f"  {'-'*4} | {'-'*6} | {'-'*35} | {'-'*15} | {'-'*10}")

    step = 0
    for token in tokens:
        step += 1
        if token.isdigit():
            output.append(token)
            action = f"Number → to output"
        elif token in precedence:
            while (op_stack and op_stack[-1] in precedence and
                   precedence[op_stack[-1]] >= precedence[token]):
                output.append(op_stack.pop())
            op_stack.append(token)
            action = f"Op '{token}' (prec={precedence[token]}) → push"
        else:
            action = f"Unknown token"

        print(f"  {step:>4} | {token:>6} | {action:>35} | {' '.join(output):>15} | {str(op_stack):>10}")

    # Pop remaining
    while op_stack:
        step += 1
        op = op_stack.pop()
        output.append(op)
        print(f"  {step:>4} | {'END':>6} | {'Pop remaining → output':>35} | {' '.join(output):>15} | {str(op_stack):>10}")

    print()
    print(f"  Result: {' '.join(output)}")
    print()

    # --- Trace with Parentheses ---
    print("=" * 70)
    print("TRACE: '( 3 + 4 ) * 2' → '3 4 + 2 *'")
    print("=" * 70)
    print()

    expr2 = '( 3 + 4 ) * 2'
    tokens2 = tokenize(expr2)
    output2 = []
    op_stack2 = []

    print(f"  {'Step':>4} | {'Token':>6} | {'Action':>35} | {'Output':>15} | {'Stack':>10}")
    print(f"  {'-'*4} | {'-'*6} | {'-'*35} | {'-'*15} | {'-'*10}")

    step = 0
    for token in tokens2:
        step += 1
        if token.isdigit():
            output2.append(token)
            action = "Number → output"
        elif token == '(':
            op_stack2.append(token)
            action = "'(' → push to stack"
        elif token == ')':
            while op_stack2 and op_stack2[-1] != '(':
                output2.append(op_stack2.pop())
            if op_stack2:
                op_stack2.pop()
            action = "')' → pop until '('"
        elif token in precedence:
            while (op_stack2 and op_stack2[-1] in precedence and
                   precedence[op_stack2[-1]] >= precedence[token]):
                output2.append(op_stack2.pop())
            op_stack2.append(token)
            action = f"Op '{token}' → push"
        print(f"  {step:>4} | {token:>6} | {action:>35} | {' '.join(output2):>15} | {str(op_stack2):>10}")

    while op_stack2:
        step += 1
        output2.append(op_stack2.pop())
        print(f"  {step:>4} | {'END':>6} | {'Pop remaining':>35} | {' '.join(output2):>15} | {str(op_stack2):>10}")

    print()
    print(f"  Result: {' '.join(output2)}")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ("3 + 4 * 2", "3 4 2 * +", "Precedence"),
        ("( 3 + 4 ) * 2", "3 4 + 2 *", "Parentheses"),
        ("1 + 2 + 3", "1 2 + 3 +", "Left associative"),
        ("2 * 3 + 4", "2 3 * 4 +", "Higher prec first"),
        ("( 1 + 2 ) * ( 3 + 4 )", "1 2 + 3 4 + *", "Two groups"),
        ("5", "5", "Single number"),
        ("10 + 20", "10 20 +", "Multi-digit"),
        ("3 + 4 * 2 / ( 1 - 5 )", "3 4 2 * 1 5 - / +", "Complex"),
    ]

    print(f"  {'Infix':>30} | {'Expected Postfix':>25} | {'Got':>25} | {'✓/✗':>3}")
    print(f"  {'-'*30} | {'-'*25} | {'-'*25} | {'-'*3}")

    all_pass = True
    for infix, expected, desc in test_cases:
        got = infix_to_postfix(infix)
        status = "✓" if got == expected else "✗"
        if got != expected: all_pass = False
        print(f"  {infix:>30} | {expected:>25} | {got:>25} | {status:>3}")

    print(f"\n  All passed: {'✓' if all_pass else '✗'}")
    print()

    # --- Precedence Table ---
    print("--- Operator Precedence ---")
    print()
    print("  Operator | Precedence | Associativity | Example")
    print("  ---------|------------|---------------|------------------")
    print("  ^        | 3 (high)   | Right         | 2^3^4 = 2^(3^4)")
    print("  * /      | 2          | Left          | 6/3*2 = (6/3)*2")
    print("  + -      | 1 (low)    | Left          | 5-3+2 = (5-3)+2")
    print()

    print("ANSWER: Shunting-Yard algorithm uses a stack for operators.")
    print("Numbers go directly to output; operators are managed by precedence.")
    print("'3 + 4 * 2' → '3 4 2 * +' (multiplication first due to precedence).")


if __name__ == "__main__":
    demonstrate()
