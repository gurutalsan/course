"""
Q1. Implement all four tree traversals (preorder, inorder, postorder,
    level-order) both recursively and iteratively. Test with a depth-4 tree.

Answer:
    Preorder  (Root-Left-Right): Visit root first, then left subtree, then right.
    Inorder   (Left-Root-Right): Visit left subtree, root, then right subtree.
    Postorder (Left-Right-Root): Visit left subtree, right subtree, then root.
    Level-order (BFS):           Visit nodes level by level, left to right.

    All traversals: Time O(n), Space O(n) (stack/queue holds up to n nodes).
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# ============================================================
# RECURSIVE Implementations
# ============================================================
def preorder_recursive(root):
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)

def inorder_recursive(root):
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)

def postorder_recursive(root):
    if not root:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]

def levelorder(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# ============================================================
# ITERATIVE Implementations
# ============================================================
def preorder_iterative(root):
    """Stack: push root, pop → visit, push right then left."""
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def inorder_iterative(root):
    """Go left as far as possible, then visit, then go right."""
    result, stack, current = [], [], root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

def postorder_iterative(root):
    """Modified preorder (Root-Right-Left) then reverse."""
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]


def demonstrate():
    print("=" * 70)
    print("Q1: Four Tree Traversals — Recursive & Iterative")
    print("=" * 70)
    print()

    vals = list(range(1, 16))
    root = build_tree(vals)

    print("--- Tree (depth 4, 15 nodes) ---")
    print()
    print("              1")
    print("           /     \\")
    print("         2         3")
    print("       /   \\     /   \\")
    print("      4     5   6     7")
    print("     / \\  / \\ / \\   / \\")
    print("    8  9 10 11 12 13 14 15")
    print()

    traversals = [
        ("Preorder  (Root→L→R)", preorder_recursive, preorder_iterative,
         "Visit root, then left subtree, then right subtree"),
        ("Inorder   (L→Root→R)", inorder_recursive, inorder_iterative,
         "Visit left subtree, then root, then right subtree"),
        ("Postorder (L→R→Root)", postorder_recursive, postorder_iterative,
         "Visit left subtree, right subtree, then root"),
        ("Level-order (BFS)   ", levelorder, levelorder,
         "Visit level by level, left to right"),
    ]

    for name, rec_fn, iter_fn, desc in traversals:
        rec_result = rec_fn(root)
        iter_result = iter_fn(root)
        match = rec_result == iter_result
        print(f"  {name}")
        print(f"    {desc}")
        print(f"    Recursive:  {rec_result}")
        print(f"    Iterative:  {iter_result}")
        print(f"    Match: {'✓' if match else '✗'}")
        print()

    # Iterative stack traces
    print("--- Iterative Preorder Stack Trace (small tree) ---")
    print()
    small = build_tree([1, 2, 3, 4, 5])
    print("    1")
    print("   / \\")
    print("  2   3")
    print(" / \\")
    print("4   5")
    print()

    stack = [small]
    result = []
    step = 0
    print(f"  {'Step':>4} | {'Pop':>4} | {'Push R,L':>12} | {'Stack':>20} | {'Result'}")
    print(f"  {'-'*4} | {'-'*4} | {'-'*12} | {'-'*20} | {'-'*20}")

    while stack:
        step += 1
        node = stack.pop()
        result.append(node.val)
        pushed = []
        if node.right:
            stack.append(node.right)
            pushed.append(str(node.right.val))
        if node.left:
            stack.append(node.left)
            pushed.append(str(node.left.val))
        stack_vals = [str(n.val) for n in stack]
        push_str = ",".join(pushed) if pushed else "—"
        print(f"  {step:>4} | {node.val:>4} | {push_str:>12} | {str(stack_vals):>20} | {result}")

    print()
    print("--- Complexity ---")
    print()
    print("  Traversal   | Time | Space  | Data Structure")
    print("  ------------|------|--------|---------------")
    print("  Preorder    | O(n) | O(h)   | Stack")
    print("  Inorder     | O(n) | O(h)   | Stack")
    print("  Postorder   | O(n) | O(h)   | Stack")
    print("  Level-order | O(n) | O(w)   | Queue")
    print()
    print("  h = height of tree, w = max width of tree")
    print()
    print("  Mnemonic: Pre=Root FIRST, In=Root MIDDLE, Post=Root LAST")


if __name__ == "__main__":
    demonstrate()
