from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def preorderComparison(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root == None and subRoot == None):
            return True
        elif ((root == None and subRoot != None) or (root != None and subRoot == None)):
            return False
        elif (root.val != subRoot.val):
            return False

        left = self.preorderComparison(root.left, subRoot.left)
        right = self.preorderComparison(root.right, subRoot.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root == None):
            return False
        elif (root.val == subRoot.val):
            if (self.preorderComparison(root, subRoot) == True):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if (__name__ == "__main__"):
    mySolution = Solution()

    # MAIN TREE
    testTree = BinarySearchTree()
    inputs = [3, 4, 5, 1, 2, 0]
    for i in inputs:
        testTree.insert(i)

    # SUBROOT TREE
    subTree = BinarySearchTree()
    inputs2 = [4, 1, 2]
    for i in inputs:
        subTree.insert(i)

    result = mySolution.isSubtree(testTree.root, subTree.root)
    print(result)
