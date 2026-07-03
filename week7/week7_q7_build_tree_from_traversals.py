"""
Q7. Construct a binary tree from preorder and inorder traversal arrays.

Answer:
    Key Insight:
    - Preorder[0] is always the ROOT.
    - Find root in inorder → everything LEFT is left subtree, RIGHT is right.
    - Recurse on left and right partitions.

    Use a hashmap for O(1) inorder index lookup → O(n) total.
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right


def level_order(root):
    if not root: return []
    result, q = [], deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return result


def preorder_trav(root):
    if not root: return []
    return [root.val] + preorder_trav(root.left) + preorder_trav(root.right)


def inorder_trav(root):
    if not root: return []
    return inorder_trav(root.left) + [root.val] + inorder_trav(root.right)


def build_tree(preorder, inorder):
    """
    Construct binary tree from preorder and inorder arrays.
    Time: O(n) with hashmap. Space: O(n).
    """
    if not preorder or not inorder:
        return None

    # Build index map for O(1) lookup in inorder
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = [0]  # Mutable index into preorder

    def helper(in_left, in_right):
        if in_left > in_right:
            return None

        root_val = preorder[pre_idx[0]]
        pre_idx[0] += 1
        root = TreeNode(root_val)

        in_idx = inorder_map[root_val]

        # Build left subtree first (preorder visits left before right)
        root.left = helper(in_left, in_idx - 1)
        root.right = helper(in_idx + 1, in_right)

        return root

    return helper(0, len(inorder) - 1)


def demonstrate():
    print("=" * 70)
    print("Q7: Construct Tree from Preorder + Inorder")
    print("=" * 70)
    print()

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    print(f"  Preorder: {preorder}")
    print(f"  Inorder:  {inorder}")
    print()

    print("--- Step-by-Step ---")
    print()
    print("  Step 1: preorder[0] = 3 → ROOT is 3")
    print("          Find 3 in inorder at index 1")
    print("          Left subtree inorder:  [9]       (indices 0..0)")
    print("          Right subtree inorder: [15,20,7] (indices 2..4)")
    print()
    print("  Step 2: Next preorder = 9 → left child of 3")
    print("          Find 9 in inorder at index 0")
    print("          No left/right children (empty ranges)")
    print()
    print("  Step 3: Next preorder = 20 → right child of 3")
    print("          Find 20 in inorder at index 3")
    print("          Left: [15] → becomes left child of 20")
    print("          Right: [7] → becomes right child of 20")
    print()
    print("  Result:")
    print("       3")
    print("      / \\")
    print("     9   20")
    print("        / \\")
    print("      15   7")
    print()

    # Build and verify
    root = build_tree(preorder, inorder)
    rebuilt_pre = preorder_trav(root)
    rebuilt_in = inorder_trav(root)

    print(f"  Rebuilt preorder: {rebuilt_pre}  {'✓' if rebuilt_pre == preorder else '✗'}")
    print(f"  Rebuilt inorder:  {rebuilt_in}  {'✓' if rebuilt_in == inorder else '✗'}")
    print(f"  Level-order:      {level_order(root)}")
    print()

    # More test cases
    print("--- Test Cases ---\n")
    tests = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], "Standard"),
        ([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7], "Full tree"),
        ([1], [1], "Single node"),
        ([1, 2], [2, 1], "Left child only"),
        ([1, 2], [1, 2], "Right child only"),
    ]

    for pre, ino, desc in tests:
        root = build_tree(pre, ino)
        ok_pre = preorder_trav(root) == pre
        ok_in = inorder_trav(root) == ino
        status = "✓" if ok_pre and ok_in else "✗"
        print(f"  {desc:>18}: pre={pre}")
        print(f"  {'':>18}  ino={ino}  {status}")

    print()
    print("  Time: O(n) with hashmap | Space: O(n)")
    print("  Key: preorder gives root order; inorder splits left/right subtrees.")


if __name__ == "__main__":
    demonstrate()
