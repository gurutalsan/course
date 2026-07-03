"""
Q1. Implement a BST with insert, search, delete, and inorder traversal.
    Delete handles all three cases: leaf, one child, two children.

Answer:
    BST Property: left < node < right (for all nodes).

    Delete cases:
    1. LEAF: just remove it.
    2. ONE CHILD: replace node with its child.
    3. TWO CHILDREN: replace with inorder successor (smallest in right subtree),
       then delete the successor from its original position.

    Insert/Search/Delete: O(h) where h = height. Balanced: O(log n), Skewed: O(n).
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Insert a value maintaining BST property. O(h)."""
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node  # Duplicate values ignored

    def search(self, val):
        """Search for a value. Returns True/False. O(h)."""
        return self._search(self.root, val)

    def _search(self, node, val):
        if not node:
            return False
        if val == node.val:
            return True
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def delete(self, val):
        """Delete a value handling all 3 cases. O(h)."""
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None

        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Found the node to delete
            # Case 1: Leaf node (no children)
            if not node.left and not node.right:
                return None

            # Case 2: One child
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Case 3: Two children
            # Find inorder successor (smallest in right subtree)
            successor = self._find_min(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)

        return node

    def _find_min(self, node):
        """Find the minimum node (leftmost) in a subtree."""
        while node.left:
            node = node.left
        return node

    def inorder(self):
        """Inorder traversal → sorted order. O(n)."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None and level == 0:
            node = self.root
        if node:
            print("    " + " " * (level * 4) + prefix + str(node.val))
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L── ")
                else:
                    print("    " + " " * ((level + 1) * 4) + "L── ∅")
                if node.right:
                    self.print_tree(node.right, level + 1, "R── ")
                else:
                    print("    " + " " * ((level + 1) * 4) + "R── ∅")


def demonstrate():
    print("=" * 70)
    print("Q1: BST — Insert, Search, Delete, Inorder")
    print("=" * 70)
    print()

    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]

    print("--- Building BST ---")
    print(f"  Inserting: {values}")
    for v in values:
        bst.insert(v)

    print()
    print("  Tree structure:")
    bst.print_tree()
    print(f"\n  Inorder (sorted): {bst.inorder()}")
    print()

    # Search
    print("--- Search ---")
    for v in [40, 25, 99, 50]:
        print(f"  search({v}): {bst.search(v)}")
    print()

    # Delete Case 1: Leaf
    print("--- Delete Case 1: LEAF (10) ---")
    print("  10 has no children → just remove it")
    bst.delete(10)
    print(f"  Inorder: {bst.inorder()}")
    print()

    # Delete Case 2: One child
    print("--- Delete Case 2: ONE CHILD (20) ---")
    print("  20 has one child (25) → replace 20 with 25")
    bst.delete(20)
    print(f"  Inorder: {bst.inorder()}")
    print()

    # Delete Case 3: Two children
    print("--- Delete Case 3: TWO CHILDREN (30) ---")
    print("  30 has children (25, 40)")
    print("  Find inorder successor: smallest in right subtree = 35")
    print("  Replace 30's value with 35, delete 35 from right subtree")
    bst.delete(30)
    print(f"  Inorder: {bst.inorder()}")
    print()

    # Delete root
    print("--- Delete Root (50) ---")
    bst.delete(50)
    print(f"  Inorder: {bst.inorder()}")
    print("  Tree after deleting root:")
    bst.print_tree()
    print()

    # Visual explanation
    print("--- Delete Cases Visual ---")
    print()
    print("  Case 1 (Leaf):        Case 2 (One child):    Case 3 (Two children):")
    print("      P                     P                       P")
    print("     /                     /                       /")
    print("    X  ← delete          X  ← delete             X  ← delete")
    print("   (no kids)            /                        / \\")
    print("                       C  ← replaces X         L   R")
    print("                                                   /")
    print("                                                  S ← successor")
    print("                                               (replace X val with S val,")
    print("                                                delete S from R subtree)")
    print()

    print("  Time: O(h) for insert/search/delete, where h = height")
    print("  Balanced BST: h = log n → O(log n)")
    print("  Worst case (skewed): h = n → O(n)")


if __name__ == "__main__":
    demonstrate()
