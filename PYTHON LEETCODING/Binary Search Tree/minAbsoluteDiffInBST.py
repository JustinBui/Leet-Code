from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree
from cmath import inf


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.least = float(inf)

        def BFS(root: Optional[TreeNode]):
            if (root == None):
                return

            # Recursively finding least difference going bottom up
            BFS(root.left)
            BFS(root.right)

            if (root.left):
                if (root.val - root.left.val < self.least):
                    self.least = root.val - root.left.val

                # To check if there are values between root.val and root.left.val
                it = root.left.right
                while (it):
                    if (root.val - it.val < self.least):
                        self.least = root.val - it.val
                    it = it.right

            if (root.right):
                if (root.right.val - root.val < self.least):
                    self.least = root.right.val - root.val

                # To check if there are values between root.val and root.right.val
                it = root.right.left
                while (it):
                    if (it.val - root.val < self.least):
                        self.least = it.val - root.val
                    it = it.left

        BFS(root)
        return self.least


if __name__ == "__main__":
    testTree = BinarySearchTree()

    testTree.insert(1)
    testTree.insert(6)
    testTree.insert(48)
    testTree.insert(12)
    testTree.insert(49)

    testSolution = Solution()
    diff = testSolution.getMinimumDifference(testTree.root)

    print(diff)
