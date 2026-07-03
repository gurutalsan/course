"""
Q3. Find the kth smallest element in a BST without converting to array first.

Answer:
    BST inorder traversal visits nodes in sorted order.
    Do an inorder traversal and stop at the kth node.

    Time:  O(h + k) — traverse to leftmost, then k steps.
    Space: O(h) — recursion stack.

    Alternative: Augmented BST with subtree sizes → O(h) always.
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


def kth_smallest_recursive(root, k):
    """Find kth smallest using inorder traversal with early stopping."""
    count = [0]
    result = [None]

    def inorder(node):
        if not node or result[0] is not None:
            return
        inorder(node.left)
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return
        inorder(node.right)

    inorder(root)
    return result[0]


def kth_smallest_iterative(root, k):
    """Find kth smallest using iterative inorder (stack). O(h + k)."""
    stack = []
    current = root
    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        count += 1
        if count == k:
            return current.val

        current = current.right

    return None


def demonstrate():
    print("=" * 70)
    print("Q3: Kth Smallest Element in BST")
    print("=" * 70)
    print()

    print("       5")
    print("      / \\")
    print("     3   6")
    print("    / \\")
    print("   2   4")
    print("  /")
    print(" 1")
    print()
    print("  Inorder (sorted): [1, 2, 3, 4, 5, 6]")
    print()

    root = build_tree([5, 3, 6, 2, 4, None, None, 1])

    print("--- Finding Kth Smallest ---\n")
    for k in range(1, 7):
        rec = kth_smallest_recursive(root, k)
        itr = kth_smallest_iterative(root, k)
        print(f"  k={k}: recursive={rec}, iterative={itr}  {'✓' if rec == itr else '✗'}")

    print()

    # Trace
    print("--- Trace: k=3 (Iterative Stack) ---\n")
    stack_t = []
    curr = root
    cnt = 0
    step = 0

    print(f"  {'Step':>4} | {'Action':>20} | {'Stack':>15} | {'Count':>5} | {'Node'}")
    print(f"  {'-'*4} | {'-'*20} | {'-'*15} | {'-'*5} | {'-'*5}")

    while stack_t or curr:
        while curr:
            step += 1
            stack_t.append(curr)
            sv = [n.val for n in stack_t]
            print(f"  {step:>4} | {'Push '+str(curr.val):>20} | {str(sv):>15} | {cnt:>5} | —")
            curr = curr.left

        curr = stack_t.pop()
        cnt += 1
        step += 1
        sv = [n.val for n in stack_t]
        found = " ★ FOUND!" if cnt == 3 else ""
        print(f"  {step:>4} | {'Pop & visit '+str(curr.val):>20} | {str(sv):>15} | {cnt:>5} | {curr.val}{found}")

        if cnt == 3:
            print(f"\n  Answer: {curr.val}")
            break
        curr = curr.right

    print()
    print("  Time: O(h + k) — go to leftmost (h), then k inorder steps")
    print("  Space: O(h) — stack depth = height of tree")
    print()
    print("  Why NOT convert to array? That's O(n) time + O(n) space.")
    print("  Iterative inorder stops early at k → O(h + k) which is better when k << n.")


if __name__ == "__main__":
    demonstrate()
