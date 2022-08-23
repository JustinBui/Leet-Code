from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def identifyLeft(root: Optional[TreeNode], leftOrRight: str):
            # BASE CASES
            if (root == None):
                return
            elif (leftOrRight == 'left'):
                if (root.left == None and root.right == None):
                    self.sum += root.val
                    return

            # RECURSIVE CASE
            identifyLeft(root.left, 'left')
            identifyLeft(root.right, 'right')

        identifyLeft(root, "")

        return self.sum


if __name__ == '__main__':
    testSolution = Solution()

    sample = BinarySearchTree()
    sample.insert(5)
    # sample.insert(2)
    # sample.insert(15)
    # sample.insert(9)
    # sample.insert(8)
    # sample.insert(7)
    # sample.insert(20)
    # sample.insert(16)

    x = testSolution.sumOfLeftLeaves(sample.root)
    print(x)
