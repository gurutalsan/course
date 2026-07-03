"""
Q7. Convert a sorted array to a height-balanced BST.
    Why does choosing the middle element as root guarantee balance?

Answer:
    Recursively pick the MIDDLE element as root.
    Left half → left subtree, right half → right subtree.

    Why balanced? Choosing the middle splits elements equally.
    Left subtree has ⌊n/2⌋ nodes, right has ⌈n/2⌉ - 1 nodes.
    Heights differ by at most 1 at every level → balanced!

    Time O(n), Space O(log n) recursion stack.
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right


def sorted_array_to_bst(nums: list):
    """
    Convert sorted array to height-balanced BST.
    Pick middle as root → left half = left subtree, right half = right subtree.
    Time O(n), Space O(log n).
    """
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])
    return root


def get_height(root):
    if not root: return 0
    return 1 + max(get_height(root.left), get_height(root.right))


def is_balanced(root):
    if not root: return True
    lh = get_height(root.left)
    rh = get_height(root.right)
    return abs(lh - rh) <= 1 and is_balanced(root.left) and is_balanced(root.right)


def inorder(root):
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def level_order(root):
    if not root: return []
    result, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result


def print_tree(node, level=0, prefix="Root: "):
    if node:
        print("    " + " " * (level * 4) + prefix + str(node.val))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L── ") if node.left else None
            print_tree(node.right, level + 1, "R── ") if node.right else None


def demonstrate():
    print("=" * 70)
    print("Q7: Sorted Array → Height-Balanced BST")
    print("=" * 70)
    print()

    nums = [-10, -3, 0, 5, 9]
    print(f"  Sorted array: {nums}")
    print()

    root = sorted_array_to_bst(nums)

    print("  Result BST:")
    print("        0")
    print("       / \\")
    print("     -10   5")
    print("       \\    \\")
    print("       -3    9")
    print()

    print("  Tree structure:")
    print_tree(root)
    print()

    print(f"  Inorder (should be sorted): {inorder(root)}")
    print(f"  Level-order: {level_order(root)}")
    print(f"  Height: {get_height(root)}")
    print(f"  Balanced: {is_balanced(root)} ✓")
    print()

    # --- Step-by-step ---
    print("--- Step-by-Step: How Middle Element Splits ---")
    print()
    print(f"  Array: {nums}")
    print(f"  mid = {len(nums)//2} → root = {nums[len(nums)//2]}")
    print(f"  Left half:  {nums[:len(nums)//2]} → left subtree")
    print(f"  Right half: {nums[len(nums)//2+1:]} → right subtree")
    print()
    print("  Recurse on left half [-10, -3]:")
    print("    mid=1 → root=-3, left=[-10], right=[]")
    print()
    print("  Recurse on right half [5, 9]:")
    print("    mid=1 → root=9, left=[5], right=[]")
    print()

    # --- Why balanced? ---
    print("--- Why Middle Element Guarantees Balance ---")
    print()
    print("  If we pick the middle element as root:")
    print("    Left half:  ⌊n/2⌋ elements")
    print("    Right half: ⌈n/2⌉ - 1 elements")
    print("    Difference: at most 1 element")
    print()
    print("  This applies recursively at EVERY level!")
    print("  So heights of left and right subtrees differ by at most 1")
    print("  → HEIGHT-BALANCED (AVL-like property) ✓")
    print()
    print("  Height of resulting tree = O(log n)")
    print()

    # --- Larger example ---
    print("--- Larger Example ---")
    nums2 = list(range(1, 16))
    root2 = sorted_array_to_bst(nums2)
    print(f"  Array: {nums2}")
    print(f"  Level-order: {level_order(root2)}")
    print(f"  Height: {get_height(root2)}, Balanced: {is_balanced(root2)}")
    print(f"  Inorder matches: {inorder(root2) == nums2} ✓")
    print()

    # --- Test cases ---
    print("--- Test Cases ---\n")
    tests = [
        ([-10, -3, 0, 5, 9], True),
        ([1, 2, 3], True),
        ([1], True),
        ([], True),
        (list(range(1, 8)), True),
        (list(range(1, 32)), True),
    ]

    for nums, exp_balanced in tests:
        root = sorted_array_to_bst(nums)
        bal = is_balanced(root) if root else True
        sorted_ok = inorder(root) == nums if root else not nums
        ok = bal == exp_balanced and sorted_ok
        print(f"  {str(nums):>30} → balanced={bal}, sorted={sorted_ok}  {'✓' if ok else '✗'}")

    print()
    print("  Time: O(n) — visit each element once")
    print("  Space: O(log n) recursion stack for balanced tree")


if __name__ == "__main__":
    demonstrate()
