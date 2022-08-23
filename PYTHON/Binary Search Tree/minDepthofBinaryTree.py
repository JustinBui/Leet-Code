from cmath import inf
from msilib.schema import Binary
from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0  # Edge case where tree is empty
        if (root.left == None and root.right == None):
            return 1

        left = float(inf)
        right = float(inf)

        if (root.left):
            left = self.minDepth(root.left)
        if (root.right):
            right = self.minDepth(root.right)

        return min(left, right) + 1


if __name__ == "__main__":
    testTree = BinarySearchTree()

    # testTree.insert(10)
    # testTree.insert(3)
    # testTree.insert(16)
    # testTree.insert(13)
    # testTree.insert(17)

    # testTree.insert(2)
    # testTree.insert(3)
    # testTree.insert(4)
    # testTree.insert(5)
    # testTree.insert(6)

    testSolution = Solution()
    depth = testSolution.minDepth(testTree.root)

    print(depth)
