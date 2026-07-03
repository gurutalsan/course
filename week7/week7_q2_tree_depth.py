"""
Q2. Write a function to find the maximum depth of a binary tree. Then
    modify it to find the minimum depth (shortest path from root to leaf).

Answer:
    Max Depth: max(left_depth, right_depth) + 1 recursively.
    Min Depth: Careful! A node with one child is NOT a leaf.
               Only count paths that end at actual LEAF nodes (no children).

    Both: Time O(n), Space O(h) where h = height.
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


def max_depth(root):
    """Maximum depth (height) of binary tree. O(n) time."""
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_bfs(root):
    """Iterative max depth using BFS."""
    if not root: return 0
    depth, queue = 0, deque([root])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return depth


def min_depth(root):
    """
    Minimum depth: shortest path from root to NEAREST LEAF.
    A leaf is a node with NO children. A node with one child is NOT a leaf.
    """
    if not root: return 0
    if not root.left: return 1 + min_depth(root.right)
    if not root.right: return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))


def min_depth_bfs(root):
    """BFS min depth — returns as soon as first leaf is found."""
    if not root: return 0
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth  # First leaf found!
        if node.left: queue.append((node.left, depth + 1))
        if node.right: queue.append((node.right, depth + 1))
    return 0


def demonstrate():
    print("=" * 70)
    print("Q2: Maximum Depth & Minimum Depth of Binary Tree")
    print("=" * 70)
    print()

    # Balanced tree
    print("--- Balanced Tree ---")
    print("        1       ")
    print("       / \\      ")
    print("      2   3     depth=1")
    print("     / \\   \\    ")
    print("    4   5   6   depth=2")
    print("   /              ")
    print("  7              depth=3 (max=4)")

    balanced = build_tree([1, 2, 3, 4, 5, None, 6, 7])
    print(f"\n  Max depth: {max_depth(balanced)}")
    print(f"  Min depth: {min_depth(balanced)} (root→3→6 = 3 levels, but root→2→5 is leaf at depth 3)")
    print(f"  Min depth BFS: {min_depth_bfs(balanced)}")
    print()

    # Skewed tree
    print("--- Skewed Tree (why min_depth needs care) ---")
    print("    1")
    print("     \\")
    print("      2")
    print("       \\")
    print("        3  ← only leaf")
    skewed = build_tree([1, None, 2, None, 3])
    print(f"\n  Max depth: {max_depth(skewed)}")
    print(f"  Min depth: {min_depth(skewed)} (must reach leaf at 3, NOT stop at null left child!)")
    print()

    print("--- Why Min Depth Is Tricky ---")
    print("  Node 1 has no left child, but it's NOT a leaf (has right child).")
    print("  Naive min(left=0, right=2)+1 = 1 is WRONG!")
    print("  Correct: if one child is null, only count the other side.")
    print()

    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], "Perfect tree", 3, 3),
        ([1, 2, 3, 4, 5, None, None], "Left-heavy", 3, 2),
        ([1, None, 2, None, 3], "Right-skewed", 3, 3),
        ([1], "Single node", 1, 1),
        ([1, 2, 3], "Simple", 2, 2),
    ]

    print("--- Test Cases ---\n")
    print(f"  {'Description':>20} | {'MaxD':>4} | {'Exp':>3} | {'MinD':>4} | {'Exp':>3} | {'✓/✗'}")
    print(f"  {'-'*20} | {'-'*4} | {'-'*3} | {'-'*4} | {'-'*3} | {'-'*3}")
    for vals, desc, exp_max, exp_min in test_cases:
        root = build_tree(vals)
        mx, mn = max_depth(root), min_depth(root)
        ok = "✓" if mx == exp_max and mn == exp_min else "✗"
        print(f"  {desc:>20} | {mx:>4} | {exp_max:>3} | {mn:>4} | {exp_min:>3} | {ok}")

    print()
    print("  Time: O(n) for both | Space: O(h) recursive, O(w) BFS")
    print("  BFS min_depth is efficient — stops at first leaf found!")


if __name__ == "__main__":
    demonstrate()
