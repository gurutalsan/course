"""
Q2. Validate whether a binary tree is a valid BST. Explain why checking
    node.left.val < node.val < node.right.val alone is insufficient.

Answer:
    Naive check (left < node < right) only checks IMMEDIATE children.
    It misses violations deeper in the tree.

    Example of a tree that passes naive check but is NOT a valid BST:
          5
         / \\
        1   6
           / \\
          3   7    ← 3 is in the RIGHT subtree of 5 but 3 < 5! INVALID!

    Correct approach: Pass a valid RANGE (min, max) down the tree.
    Each node must satisfy: min < node.val < max.

    Time O(n), Space O(h).
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right


def build_tree(values):
    if not values: return None
    root = TreeNode(values[0])
    q = deque([root]); i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i]); q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i]); q.append(node.right)
        i += 1
    return root


# ============================================================
# WRONG: Naive check (only immediate children)
# ============================================================
def is_bst_naive(root):
    """INCORRECT! Only checks immediate children."""
    if not root:
        return True
    if root.left and root.left.val >= root.val:
        return False
    if root.right and root.right.val <= root.val:
        return False
    return is_bst_naive(root.left) and is_bst_naive(root.right)


# ============================================================
# CORRECT: Range-based validation
# ============================================================
def is_valid_bst(root):
    """
    Correct BST validation using range bounds.
    Each node must be within (min_val, max_val).
    Time O(n), Space O(h).
    """
    def validate(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))


# ============================================================
# Alternative: Inorder traversal check (must be strictly increasing)
# ============================================================
def is_valid_bst_inorder(root):
    """BST inorder traversal produces sorted order. Check that."""
    prev = [float('-inf')]

    def inorder(node):
        if not node:
            return True
        if not inorder(node.left):
            return False
        if node.val <= prev[0]:
            return False
        prev[0] = node.val
        return inorder(node.right)

    return inorder(root)


def demonstrate():
    print("=" * 70)
    print("Q2: Validate BST — Why Naive Check Fails")
    print("=" * 70)
    print()

    # --- Why naive fails ---
    print("--- Why Checking Only Immediate Children FAILS ---")
    print()
    print("  This tree passes naive check but is NOT a valid BST:")
    print()
    print("       5")
    print("      / \\")
    print("     1   6")
    print("        / \\")
    print("       3   7")
    print()
    print("  Naive: 1<5? ✓  6>5? ✓  3<6? ✓  7>6? ✓  → 'Valid' ✗ WRONG!")
    print("  But 3 is in the RIGHT subtree of 5, and 3 < 5! → INVALID!")
    print()

    # Build the tricky tree manually
    tricky = TreeNode(5)
    tricky.left = TreeNode(1)
    tricky.right = TreeNode(6)
    tricky.right.left = TreeNode(3)
    tricky.right.right = TreeNode(7)

    print(f"  Naive check: {is_bst_naive(tricky)} (WRONG — says valid)")
    print(f"  Range check: {is_valid_bst(tricky)} (CORRECT — detects violation)")
    print(f"  Inorder check: {is_valid_bst_inorder(tricky)} (CORRECT)")
    print()

    # --- How range check works ---
    print("--- Range-Based Validation ---")
    print()
    print("  Pass (min, max) range down the tree:")
    print("  • Root: (-∞, +∞)")
    print("  • Go left:  range becomes (min, node.val)")
    print("  • Go right: range becomes (node.val, max)")
    print()
    print("  Trace for the tricky tree:")
    print("    Node 5: range(-∞, +∞) → 5 in range? ✓")
    print("    Node 1: range(-∞, 5)  → 1 in range? ✓")
    print("    Node 6: range(5, +∞)  → 6 in range? ✓")
    print("    Node 3: range(5, 6)   → 3 in range? ✗  (3 < 5!) INVALID!")
    print()

    # --- Valid BST ---
    print("--- Valid BST Example ---")
    print()
    print("       5")
    print("      / \\")
    print("     3   7")
    print("    / \\ / \\")
    print("   1  4 6  8")
    valid = build_tree([5, 3, 7, 1, 4, 6, 8])
    print(f"\n  Range check: {is_valid_bst(valid)} ✓")
    print(f"  Inorder check: {is_valid_bst_inorder(valid)} ✓")
    print()

    # --- Test Cases ---
    print("--- Test Cases ---\n")
    tests = [
        ([2, 1, 3], True, "Simple valid"),
        ([5, 1, 4, None, None, 3, 6], False, "4 is right of 5 but < 5"),
        ([1], True, "Single node"),
        ([1, 1], False, "Duplicate (not strictly less)"),
        ([5, 3, 7, 1, 4, 6, 8], True, "Balanced valid BST"),
        ([10, 5, 15, None, None, 6, 20], False, "6 < 10 but in right subtree"),
    ]

    print(f"  {'Description':>30} | {'Range':>5} | {'Inorder':>7} | {'Expected':>8} | {'✓/✗'}")
    print(f"  {'-'*30} | {'-'*5} | {'-'*7} | {'-'*8} | {'-'*3}")
    for vals, expected, desc in tests:
        root = build_tree(vals)
        r1 = is_valid_bst(root)
        r2 = is_valid_bst_inorder(root)
        ok = "✓" if r1 == r2 == expected else "✗"
        print(f"  {desc:>30} | {str(r1):>5} | {str(r2):>7} | {str(expected):>8} | {ok}")

    print()
    print("  Time: O(n) | Space: O(h)")
    print("  ANSWER: Must check entire range constraints, not just immediate children.")


if __name__ == "__main__":
    demonstrate()
