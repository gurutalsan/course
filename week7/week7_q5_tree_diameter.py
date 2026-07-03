"""
Q5. Find the diameter of a binary tree (longest path between any two nodes).
    Explain why left_height + right_height at every node works.

Answer:
    The diameter is the longest path between ANY two nodes. It may or may
    not pass through the root.

    At each node, the longest path THROUGH that node = left_height + right_height.
    Track the global maximum across all nodes while computing heights.

    Time O(n) — single DFS pass. Space O(h).
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


def diameter_of_tree(root):
    """
    Find diameter in O(n) — single pass DFS.
    At each node: diameter through it = left_height + right_height.
    Track global max.
    """
    diameter = [0]  # Use list to allow mutation in nested function

    def height(node):
        if not node:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)
        # Update diameter: path through this node
        diameter[0] = max(diameter[0], left_h + right_h)
        return 1 + max(left_h, right_h)

    height(root)
    return diameter[0]


def demonstrate():
    print("=" * 70)
    print("Q5: Diameter of a Binary Tree")
    print("=" * 70)
    print()

    print("--- What is Diameter? ---")
    print("  Longest path between ANY two nodes (counted in edges).")
    print("  May or may not pass through the root!")
    print()

    # Example 1: diameter passes through root
    print("--- Example 1: Diameter through root ---")
    print()
    print("         1           ")
    print("        / \\          ")
    print("       2   3         ")
    print("      / \\            ")
    print("     4   5           ")
    print()
    print("  Diameter = 3 (path: 4→2→1→3 or 5→2→1→3)")

    t1 = build_tree([1, 2, 3, 4, 5])
    print(f"  Computed: {diameter_of_tree(t1)}")
    print()

    # Example 2: diameter NOT through root
    print("--- Example 2: Diameter NOT through root ---")
    print()
    print("         1           ")
    print("        /            ")
    print("       2             ")
    print("      / \\            ")
    print("     4   5           ")
    print("    /     \\          ")
    print("   8       9         ")
    print()
    print("  Diameter = 4 (path: 8→4→2→5→9) — doesn't pass through root 1!")

    t2 = build_tree([1, 2, None, 4, 5, 8, None, None, 9])
    print(f"  Computed: {diameter_of_tree(t2)}")
    print()

    # --- Why it works ---
    print("--- Why left_height + right_height Works ---")
    print()
    print("  The longest path through any node N is:")
    print("    depth_of_left_subtree + depth_of_right_subtree")
    print()
    print("  This is because the path goes:")
    print("    deepest left leaf → ... → N → ... → deepest right leaf")
    print()
    print("  By checking EVERY node and keeping the maximum,")
    print("  we find the global diameter even if it doesn't pass through root.")
    print()
    print("  Key: height() returns the height, but as a SIDE EFFECT")
    print("  updates the diameter. This avoids O(n²) recomputation.")
    print()

    # Trace
    print("--- Trace for [1,2,3,4,5] ---")
    print()
    trace_diameter = [0]
    def height_trace(node, depth=0):
        if not node: return 0
        indent = "    " * depth
        lh = height_trace(node.left, depth + 1)
        rh = height_trace(node.right, depth + 1)
        through = lh + rh
        trace_diameter[0] = max(trace_diameter[0], through)
        h = 1 + max(lh, rh)
        print(f"  {indent}Node {node.val}: L_h={lh}, R_h={rh}, "
              f"through={through}, height={h}, max_dia={trace_diameter[0]}")
        return h

    t3 = build_tree([1, 2, 3, 4, 5])
    height_trace(t3)
    print(f"\n  Final diameter: {trace_diameter[0]}")
    print()

    # Test cases
    tests = [
        ([1, 2, 3, 4, 5], 3), ([1], 0), ([1, 2], 1),
        ([1, 2, 3, 4, 5, 6, 7], 4), ([1, 2, None, 3, None, 4], 3),
    ]
    print("--- Test Cases ---\n")
    for vals, expected in tests:
        got = diameter_of_tree(build_tree(vals))
        print(f"  {str(vals):>25} → diameter={got} (expected {expected}) {'✓' if got==expected else '✗'}")

    print("\n  Time: O(n) single pass | Space: O(h)")


if __name__ == "__main__":
    demonstrate()
