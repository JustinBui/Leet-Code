from turtle import right
from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def height_dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        return 1 + max(self.height_dfs(root.left), self.height_dfs(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        l_height = self.height_dfs(root.left)
        r_height = self.height_dfs(root.right)

        if abs(l_height - r_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)

    obj = Solution()
    print(obj.isBalanced(tree.root))
