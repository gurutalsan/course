"""
Q7. Implement a function that checks if a sequence of push/pop operations
    on a stack is valid. Given pushed=[1,2,3,4,5] and popped=[4,5,3,2,1],
    return True.

Answer:
    SIMULATE the stack operations:
    1. Iterate through the 'pushed' sequence, pushing each element.
    2. After each push, check if the top of stack matches the next
       expected pop. If so, pop it.
    3. At the end, if the stack is empty → valid sequence.

    Time:  O(n) — each element pushed and popped at most once.
    Space: O(n) — the simulation stack.
"""


def validate_stack_sequences(pushed: list, popped: list) -> bool:
    """
    Check if a push/pop sequence is valid for a stack.

    Simulate: push elements one by one. After each push, pop as many
    as possible that match the expected 'popped' order.

    Time:  O(n) — each element pushed once, popped at most once.
    Space: O(n) — simulation stack.

    Examples:
        >>> validate_stack_sequences([1,2,3,4,5], [4,5,3,2,1])
        True
        >>> validate_stack_sequences([1,2,3,4,5], [4,3,5,1,2])
        False
    """
    stack = []
    pop_idx = 0  # Index into popped sequence

    for val in pushed:
        stack.append(val)

        # Pop as many as possible that match expected sequence
        while stack and pop_idx < len(popped) and stack[-1] == popped[pop_idx]:
            stack.pop()
            pop_idx += 1

    return len(stack) == 0  # All elements must be popped


def validate_with_trace(pushed: list, popped: list) -> tuple:
    """Same as above but returns step-by-step trace."""
    stack = []
    pop_idx = 0
    steps = []

    for val in pushed:
        stack.append(val)
        steps.append(('push', val, list(stack), pop_idx))

        while stack and pop_idx < len(popped) and stack[-1] == popped[pop_idx]:
            popped_val = stack.pop()
            steps.append(('pop', popped_val, list(stack), pop_idx))
            pop_idx += 1

    return len(stack) == 0, steps


def demonstrate():
    print("=" * 70)
    print("Q7: Validate Stack Push/Pop Sequence")
    print("=" * 70)
    print()

    # --- Problem ---
    print("--- Problem ---")
    print()
    print("  Given the order elements are PUSHED and POPPED,")
    print("  determine if this is a valid stack operation sequence.")
    print()
    print("  pushed = [1, 2, 3, 4, 5]")
    print("  popped = [4, 5, 3, 2, 1]")
    print("  Is this possible? → YES ✓")
    print()

    # --- Trace: Valid sequence ---
    print("=" * 70)
    print("TRACE: pushed=[1,2,3,4,5], popped=[4,5,3,2,1] → True")
    print("=" * 70)
    print()

    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    valid, steps = validate_with_trace(pushed, popped)

    print(f"  {'Step':>4} | {'Action':>10} | {'Value':>5} | {'Stack':>15} | {'Next Expected Pop':>18}")
    print(f"  {'-'*4} | {'-'*10} | {'-'*5} | {'-'*15} | {'-'*18}")

    for i, (action, val, stack, pidx) in enumerate(steps):
        next_pop = popped[pidx] if pidx < len(popped) else "—"
        print(f"  {i+1:>4} | {action:>10} | {val:>5} | {str(stack):>15} | {str(next_pop):>18}")

    print()
    print(f"  Stack empty at end: {valid} → Valid sequence ✓")
    print()

    # --- Manual walkthrough ---
    print("  Manual walkthrough:")
    print("    Push 1 → Stack: [1]")
    print("    Push 2 → Stack: [1, 2]")
    print("    Push 3 → Stack: [1, 2, 3]")
    print("    Push 4 → Stack: [1, 2, 3, 4]  → top=4 matches popped[0]=4 → Pop!")
    print("    Pop  4 → Stack: [1, 2, 3]      → top=3 ≠ popped[1]=5 → continue")
    print("    Push 5 → Stack: [1, 2, 3, 5]  → top=5 matches popped[1]=5 → Pop!")
    print("    Pop  5 → Stack: [1, 2, 3]      → top=3 matches popped[2]=3 → Pop!")
    print("    Pop  3 → Stack: [1, 2]          → top=2 matches popped[3]=2 → Pop!")
    print("    Pop  2 → Stack: [1]             → top=1 matches popped[4]=1 → Pop!")
    print("    Pop  1 → Stack: []              → Empty! ✓")
    print()

    # --- Trace: Invalid sequence ---
    print("=" * 70)
    print("TRACE: pushed=[1,2,3,4,5], popped=[4,3,5,1,2] → False")
    print("=" * 70)
    print()

    pushed2 = [1, 2, 3, 4, 5]
    popped2 = [4, 3, 5, 1, 2]
    valid2, steps2 = validate_with_trace(pushed2, popped2)

    print(f"  {'Step':>4} | {'Action':>10} | {'Value':>5} | {'Stack':>15} | {'Next Expected Pop':>18}")
    print(f"  {'-'*4} | {'-'*10} | {'-'*5} | {'-'*15} | {'-'*18}")

    for i, (action, val, stack, pidx) in enumerate(steps2):
        next_pop = popped2[pidx] if pidx < len(popped2) else "—"
        print(f"  {i+1:>4} | {action:>10} | {val:>5} | {str(stack):>15} | {str(next_pop):>18}")

    print()
    print(f"  Stack at end: not empty → INVALID ✗")
    print()
    print("  Why invalid?")
    print("    After popping 4, 3, we need to pop 5, then 1, then 2.")
    print("    But after popping 5, stack is [1, 2].")
    print("    We need to pop 1 next, but top is 2!")
    print("    Since stack is LIFO, we can't reach 1 without popping 2 first.")
    print("    The sequence [... 1, 2] is impossible → False ✗")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---")
    print()

    test_cases = [
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True, "Standard valid"),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False, "Invalid order"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True, "Pop immediately"),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], True, "Reverse order"),
        ([1], [1], True, "Single element"),
        ([], [], True, "Empty"),
        ([1, 2, 3], [3, 2, 1], True, "Pure stack (push all, pop all)"),
        ([1, 2, 3], [1, 3, 2], True, "Interleaved"),
        ([1, 2, 3], [3, 1, 2], False, "Can't access 1 before 2"),
    ]

    print(f"  {'pushed':>20} | {'popped':>20} | {'Expected':>8} | {'Got':>5} | {'✓/✗':>3}")
    print(f"  {'-'*20} | {'-'*20} | {'-'*8} | {'-'*5} | {'-'*3}")

    all_pass = True
    for pushed, popped, expected, desc in test_cases:
        result = validate_stack_sequences(pushed, popped)
        status = "✓" if result == expected else "✗"
        if result != expected: all_pass = False
        print(f"  {str(pushed):>20} | {str(popped):>20} | {str(expected):>8} | {str(result):>5} | {status:>3}")

    print(f"\n  All passed: {'✓' if all_pass else '✗'}")
    print()

    # --- The Code ---
    print("--- The Implementation ---")
    print()
    print("  def validate_stack_sequences(pushed, popped):")
    print("      stack = []")
    print("      pop_idx = 0")
    print()
    print("      for val in pushed:")
    print("          stack.append(val)             # Push next value")
    print()
    print("          while (stack and              # While stack not empty")
    print("                 pop_idx < len(popped) and")
    print("                 stack[-1] == popped[pop_idx]):  # Top matches?")
    print("              stack.pop()               # Pop it!")
    print("              pop_idx += 1              # Move to next expected")
    print()
    print("      return len(stack) == 0            # All popped = valid")
    print()

    # --- Complexity ---
    print("--- Complexity ---")
    print()
    print("  Time:  O(n) — each element pushed once, popped at most once")
    print("  Space: O(n) — simulation stack")
    print()
    print("ANSWER: Simulate the stack. Push elements one by one, pop whenever")
    print("top matches the next expected pop. If stack is empty at end → valid.")


if __name__ == "__main__":
    demonstrate()
