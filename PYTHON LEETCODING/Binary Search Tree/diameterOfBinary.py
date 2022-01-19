from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree

# Solution: https://www.youtube.com/watch?v=bkxqA8Rfv04


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def traverseDFS(root: Optional[TreeNode]):
            # Finding the greatest diameter by going bottom up
            # for every node in the tree
            if (root == None):
                return -1

            left = traverseDFS(root.left) + 1
            right = traverseDFS(root.right) + 1

            candidate = left + right
            if (candidate > self.max_diameter):
                self.max_diameter = candidate

            return max(left, right)

        traverseDFS(root)

        # Returning the value of the MAX HEIGHT of an individual node during this recursive travsersal
        return self.max_diameter


if __name__ == '__main__':
    testTree = BinarySearchTree()

    testTree.insert(5)
    testTree.insert(3)
    testTree.insert(4)
    testTree.insert(1)
    testTree.insert(7)

    testSolution = Solution()
    diameter = testSolution.diameterOfBinaryTree(testTree.root)

    print(diameter)
