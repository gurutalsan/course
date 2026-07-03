"""
Q8. Find the Lowest Common Ancestor (LCA) of two nodes.
    What changes if it's a Binary Search Tree (BST)?

Answer:
    Binary Tree LCA: Recursive — if node is p or q, return it.
        Check left and right. If both return non-null, current is LCA.
        Time O(n), Space O(h).

    BST LCA: Use BST property — if both < node go left, both > go right,
        else current node is the split point = LCA.
        Time O(h), Space O(1) iterative.
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


def find_node(root, val):
    """Find a node by value."""
    if not root: return None
    if root.val == val: return root
    return find_node(root.left, val) or find_node(root.right, val)


# ============================================================
# General Binary Tree LCA — O(n)
# ============================================================
def lca_binary_tree(root, p, q):
    """
    LCA for a general binary tree.
    If current node is p or q → return it.
    Recurse left and right. If both sides return non-null → this is LCA.
    Time O(n), Space O(h).
    """
    if not root or root == p or root == q:
        return root

    left = lca_binary_tree(root.left, p, q)
    right = lca_binary_tree(root.right, p, q)

    if left and right:
        return root  # p and q are in different subtrees → this is LCA
    return left if left else right


# ============================================================
# BST LCA — O(h), leverages BST ordering
# ============================================================
def lca_bst(root, p, q):
    """
    LCA for a Binary Search Tree.
    Uses BST property: left < root < right.
    Time O(h), Space O(1) iterative.
    """
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left    # Both in left subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right   # Both in right subtree
        else:
            return root         # Split point = LCA!
    return None


def demonstrate():
    print("=" * 70)
    print("Q8: Lowest Common Ancestor (LCA)")
    print("=" * 70)
    print()

    # --- Binary Tree ---
    print("--- Binary Tree LCA ---")
    print()
    print("         3")
    print("        / \\")
    print("       5   1")
    print("      / \\ / \\")
    print("     6  2 0  8")
    print("       / \\")
    print("      7   4")
    print()

    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

    test_pairs = [(5, 1, 3), (5, 4, 5), (6, 4, 5), (7, 8, 3), (6, 2, 5)]

    print(f"  {'p':>4} {'q':>4} | {'LCA':>4} | {'Expected':>8} | {'✓/✗'}")
    print(f"  {'-'*4} {'-'*4} | {'-'*4} | {'-'*8} | {'-'*3}")

    for pv, qv, expected in test_pairs:
        p = find_node(root, pv)
        q = find_node(root, qv)
        result = lca_binary_tree(root, p, q)
        status = "✓" if result and result.val == expected else "✗"
        print(f"  {pv:>4} {qv:>4} | {result.val:>4} | {expected:>8} | {status}")

    print()
    print("  How: LCA(5,1)=3 because 5 is in left, 1 is in right → split at 3")
    print("       LCA(5,4)=5 because 4 is a descendant of 5 → 5 itself is LCA")
    print()

    # --- BST LCA ---
    print("--- BST LCA (uses ordering!) ---")
    print()
    print("         6")
    print("        / \\")
    print("       2   8")
    print("      / \\ / \\")
    print("     0  4 7  9")
    print("       / \\")
    print("      3   5")
    print()

    bst = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

    bst_tests = [(2, 8, 6), (2, 4, 2), (3, 5, 4), (0, 5, 2), (7, 9, 8)]

    print(f"  {'p':>4} {'q':>4} | {'BST LCA':>7} | {'BT LCA':>6} | {'Match':>5}")
    print(f"  {'-'*4} {'-'*4} | {'-'*7} | {'-'*6} | {'-'*5}")

    for pv, qv, expected in bst_tests:
        p = find_node(bst, pv)
        q = find_node(bst, qv)
        bst_result = lca_bst(bst, p, q)
        bt_result = lca_binary_tree(bst, p, q)
        match = bst_result.val == bt_result.val == expected
        print(f"  {pv:>4} {qv:>4} | {bst_result.val:>7} | {bt_result.val:>6} | {'✓' if match else '✗':>5}")

    print()

    # --- Comparison ---
    print("--- BT vs BST LCA Comparison ---")
    print()
    print("  Property         | Binary Tree    | BST")
    print("  -----------------|----------------|------------------")
    print("  Algorithm        | Recursive DFS  | Value comparison")
    print("  Time             | O(n)           | O(h) ★")
    print("  Space            | O(h)           | O(1) iterative ★")
    print("  Uses ordering?   | No             | Yes (left < root < right)")
    print()
    print("  BST advantage: Don't need to search both subtrees!")
    print("  Just compare values to decide: go left, go right, or found LCA.")
    print()

    print("--- How BST LCA Works ---")
    print()
    print("  LCA(3, 5) in BST [6,2,8,0,4,7,9,_,_,3,5]:")
    print("    Node 6: both 3 and 5 < 6 → go LEFT")
    print("    Node 2: both 3 and 5 > 2 → go RIGHT")
    print("    Node 4: 3 < 4 and 5 > 4 → SPLIT! LCA = 4 ✓")
    print()
    print("ANSWER: BT LCA uses recursive DFS checking both sides O(n).")
    print("BST LCA leverages ordering to decide direction O(h).")


if __name__ == "__main__":
    demonstrate()
