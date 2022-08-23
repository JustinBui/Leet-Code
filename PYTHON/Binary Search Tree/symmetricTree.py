from typing import collections, Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftContent = []

        # Finding and storing all of root's left subtree values
        def preorder(root):
            if (root == None):
                leftContent.append(None)
                return

            leftContent.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root.left)
        self.index = -1

        def reversePreorder(root) -> bool:
            self.index += 1

            # BASE CASES
            if (root == None):
                if (root != leftContent[self.index]):
                    return False
                else:
                    return
            if (root.val != leftContent[self.index]):
                return False
            else:
                return

            # RECURSIVE CASE
            left = True
            right = True

            left = reversePreorder(root.right)
            right = reversePreorder(root.left)

            return left and right

        return reversePreorder(root.right)


if __name__ == "__main__":
    sample = BinarySearchTree()
    sample.insert(5)
    sample.insert(2)
    sample.insert(15)
    sample.insert(9)
    sample.insert(8)
    sample.insert(7)
    sample.insert(20)
    sample.insert(16)

    test = Solution()
    print(test.isSymmetric(sample.root))
