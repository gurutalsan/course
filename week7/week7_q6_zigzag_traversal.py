"""
Q6. Implement zigzag (spiral) level-order traversal.
    Level 0: L→R, Level 1: R→L, Level 2: L→R, etc.

Answer:
    BFS with a flag to alternate direction.
    Use deque to reverse alternate levels efficiently.
    Time O(n), Space O(n).
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


def zigzag_traversal(root):
    """
    Zigzag level-order: alternate L→R and R→L at each level.
    Time O(n), Space O(n).
    """
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level = deque()

        for _ in range(level_size):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)  # Prepend for R→L

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level))
        left_to_right = not left_to_right

    return result


def normal_level_order(root):
    """Standard level-order for comparison."""
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result


def demonstrate():
    print("=" * 70)
    print("Q6: Zigzag (Spiral) Level-Order Traversal")
    print("=" * 70)
    print()

    print("--- Example Tree ---")
    print()
    print("         3           Level 0: → [3]")
    print("        / \\")
    print("       9   20        Level 1: ← [20, 9]")
    print("          / \\")
    print("        15   7       Level 2: → [15, 7]")
    print()

    root = build_tree([3, 9, 20, None, None, 15, 7])
    result = zigzag_traversal(root)
    normal = normal_level_order(root)

    print(f"  Normal level-order:  {normal}")
    print(f"  Zigzag level-order:  {result}")
    print()

    # Visual zigzag pattern
    print("--- Zigzag Pattern ---")
    print()
    print("  Level 0 (L→R):  ──→  [3]")
    print("  Level 1 (R→L):  ←──  [20, 9]")
    print("  Level 2 (L→R):  ──→  [15, 7]")
    print()

    # Larger tree
    print("--- Larger Tree [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] ---")
    print()
    print("              1                 Level 0: →  [1]")
    print("           /     \\")
    print("         2         3            Level 1: ←  [3, 2]")
    print("       /   \\     /   \\")
    print("      4     5   6     7         Level 2: →  [4, 5, 6, 7]")
    print("     / \\  / \\ / \\   / \\")
    print("    8  9 10 11 12 13 14 15      Level 3: ←  [15,14,13,12,11,10,9,8]")
    print()

    big = build_tree(list(range(1, 16)))
    big_result = zigzag_traversal(big)
    for i, level in enumerate(big_result):
        direction = "→" if i % 2 == 0 else "←"
        print(f"  Level {i} ({direction}): {level}")

    print()

    # How it works
    print("--- How It Works ---")
    print()
    print("  Use a deque for each level:")
    print("  • left_to_right = True:  level.append(val)     → normal order")
    print("  • left_to_right = False: level.appendleft(val) → reversed!")
    print()
    print("  Toggle the flag after each level.")
    print()

    # Test cases
    tests = [
        ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
        ([1], [[1]]),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [3, 2], [4, 5, 6, 7]]),
    ]
    print("--- Test Cases ---\n")
    for vals, expected in tests:
        got = zigzag_traversal(build_tree(vals))
        print(f"  {str(vals):>30} → {got}  {'✓' if got==expected else '✗'}")

    print("\n  Time: O(n) | Space: O(n)")


if __name__ == "__main__":
    demonstrate()
