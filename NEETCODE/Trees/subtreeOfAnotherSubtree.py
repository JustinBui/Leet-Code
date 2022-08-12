from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val:
            return self.isSameTree(root, subRoot)

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(6)

    tree2 = BinarySearchTree()
    tree2.insert(5)
    tree2.insert(2)
    tree2.insert(3)
    tree2.insert(6)

    obj = Solution()
    print(obj.isSubtree(tree.root, tree2.root))
