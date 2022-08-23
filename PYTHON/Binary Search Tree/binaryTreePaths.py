from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:

    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        paths = []
        currentPath = ""

        def findPath(root: Optional[TreeNode], currentPath: str):
            if (root.left == None and root.right == None):
                paths.append(currentPath + str(root.val))
                return

            currentPath += str(root.val) + "->"
            if (root.left):
                findPath(root.left, currentPath)
            if (root.right):
                findPath(root.right, currentPath)

        findPath(root, currentPath)
        return paths


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(6)
    tree.insert(10)
    tree.insert(8)
    tree.insert(20)
    tree.insert(15)
    tree.insert(21)

    entity = Solution()
    result = entity.binaryTreePaths(tree.root)

    print(result)
