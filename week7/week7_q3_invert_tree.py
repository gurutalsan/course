"""
Q3. Implement invert (mirror) a binary tree. Draw before/after for [4,2,7,1,3,6,9].

Answer:
    Swap left and right children at EVERY node recursively.
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


def level_order(root):
    if not root: return []
    result, q = [], deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return result


def invert_recursive(root):
    """Invert binary tree recursively. O(n) time, O(h) space."""
    if not root: return None
    root.left, root.right = root.right, root.left
    invert_recursive(root.left)
    invert_recursive(root.right)
    return root


def invert_iterative(root):
    """Invert using BFS queue. O(n) time, O(n) space."""
    if not root: return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return root


def demonstrate():
    print("=" * 70)
    print("Q3: Invert (Mirror) a Binary Tree")
    print("=" * 70)
    print()

    print("--- BEFORE Inversion ---")
    print()
    print("         4            ")
    print("       /   \\          ")
    print("      2     7         ")
    print("     / \\   / \\        ")
    print("    1   3 6   9       ")
    print()

    root = build_tree([4, 2, 7, 1, 3, 6, 9])
    print(f"  Level-order before: {level_order(root)}")
    print()

    # Trace the swaps
    print("--- Step-by-Step Recursive Swaps ---")
    print()
    def invert_trace(node, depth=0):
        if not node: return
        indent = "    " * depth
        old_l = node.left.val if node.left else "∅"
        old_r = node.right.val if node.right else "∅"
        node.left, node.right = node.right, node.left
        new_l = node.left.val if node.left else "∅"
        new_r = node.right.val if node.right else "∅"
        print(f"  {indent}Node {node.val}: swap L={old_l}, R={old_r} → L={new_l}, R={new_r}")
        invert_trace(node.left, depth + 1)
        invert_trace(node.right, depth + 1)

    root2 = build_tree([4, 2, 7, 1, 3, 6, 9])
    invert_trace(root2)
    print()

    print("--- AFTER Inversion ---")
    print()
    print("         4            ")
    print("       /   \\          ")
    print("      7     2         ")
    print("     / \\   / \\        ")
    print("    9   6 3   1       ")
    print()
    print(f"  Level-order after: {level_order(root2)}")
    print()

    # Verify
    root3 = build_tree([4, 2, 7, 1, 3, 6, 9])
    invert_recursive(root3)
    root4 = build_tree([4, 2, 7, 1, 3, 6, 9])
    invert_iterative(root4)
    print(f"  Recursive result: {level_order(root3)}")
    print(f"  Iterative result: {level_order(root4)}")
    print(f"  Match: {'✓' if level_order(root3) == level_order(root4) else '✗'}")
    print()

    # Inverting twice = original
    invert_recursive(root3)
    print(f"  Double invert (back to original): {level_order(root3)}")
    print()
    print("  Time: O(n) | Space: O(h) recursive, O(n) iterative")
    print("  Every node visited once; left and right swapped at each.")


if __name__ == "__main__":
    demonstrate()
