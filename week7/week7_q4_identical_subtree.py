"""
Q4. Check if two trees are identical. Then check if one is a subtree of another.

    Identical: O(n) — compare structure + values recursively.
    Subtree:   O(m*n) — for each node in main tree, check if identical to subtree.
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


def is_identical(p, q):
    """Check if two trees are structurally identical with same values. O(n)."""
    if not p and not q: return True
    if not p or not q: return False
    return (p.val == q.val and
            is_identical(p.left, q.left) and
            is_identical(p.right, q.right))


def is_subtree(root, sub):
    """
    Check if 'sub' is a subtree of 'root'.
    A subtree must include all descendants (not just partial match).
    Time: O(m*n) worst case.
    """
    if not sub: return True
    if not root: return False
    if is_identical(root, sub): return True
    return is_subtree(root.left, sub) or is_subtree(root.right, sub)


def demonstrate():
    print("=" * 70)
    print("Q4: Identical Trees & Subtree Check")
    print("=" * 70)
    print()

    # --- Identical ---
    print("--- Identical Trees ---")
    print()
    print("  Tree A:     Tree B:")
    print("    1           1")
    print("   / \\         / \\")
    print("  2   3       2   3")

    a = build_tree([1, 2, 3])
    b = build_tree([1, 2, 3])
    c = build_tree([1, 2, 4])
    print(f"\n  A == B: {is_identical(a, b)} ✓ (same structure & values)")
    print(f"  A == C (val 4): {is_identical(a, c)} (different value at right)")
    print()

    # Trace
    print("  Trace is_identical([1,2,3], [1,2,3]):")
    print("    Node 1==1? ✓ → check children")
    print("    Node 2==2? ✓ → check children (both None) ✓")
    print("    Node 3==3? ✓ → check children (both None) ✓")
    print("    Result: True")
    print()

    # --- Subtree ---
    print("--- Subtree Check ---")
    print()
    print("  Main tree:        Subtree:")
    print("      3               4")
    print("     / \\             / \\")
    print("    4   5           1   2")
    print("   / \\")
    print("  1   2")

    main = build_tree([3, 4, 5, 1, 2])
    sub = build_tree([4, 1, 2])
    not_sub = build_tree([4, 1, 3])

    print(f"\n  is_subtree(main, [4,1,2]): {is_subtree(main, sub)} ✓")
    print(f"  is_subtree(main, [4,1,3]): {is_subtree(main, not_sub)} ✗ (value mismatch)")
    print()

    # Test cases
    print("--- Test Cases ---\n")
    tests = [
        ([1,2,3], [1,2,3], True, True, "Identical"),
        ([1,2,3], [1,2,4], False, False, "Diff value"),
        ([1,2,3], [1,2], False, False, "Diff structure"),
        ([3,4,5,1,2], [4,1,2], False, True, "Valid subtree"),
        ([3,4,5,1,2], [4,1], False, False, "Partial (not subtree)"),
        ([1,2,3,4,5,6,7], [2,4,5], False, True, "Deep subtree"),
        ([], [], True, True, "Both empty"),
    ]

    print(f"  {'Desc':>18} | {'Identical':>9} | {'Subtree':>7}")
    print(f"  {'-'*18} | {'-'*9} | {'-'*7}")
    for v1, v2, exp_id, exp_sub, desc in tests:
        t1, t2 = build_tree(v1), build_tree(v2)
        id_r = is_identical(t1, t2)
        sub_r = is_subtree(t1, t2)
        ok = "✓" if id_r == exp_id and sub_r == exp_sub else "✗"
        print(f"  {desc:>18} | {str(id_r):>9} | {str(sub_r):>7}  {ok}")

    print()
    print("  Identical: O(min(n,m)) | Subtree: O(m×n) worst case")
    print("  A subtree must match ALL descendants, not just partial structure.")


if __name__ == "__main__":
    demonstrate()
