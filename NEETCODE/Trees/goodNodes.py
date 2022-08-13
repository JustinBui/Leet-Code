from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def preorder(root, greatest):
            if not root:
                # Obviously, any node that is null doesn't have good nodes
                return 0

            # Result will start off as 1, if the current root's value we are in
            # is NOT less than the current greatest. If it is less than, it is not a good node,
            # therefore assign it 0.
            res = 1 if root.val >= greatest else 0
            greatest = max(greatest, root.val)

            # Recursively traversing down the left and right sides and adding more possible
            # good nodes into res
            res += preorder(root.left, greatest)
            res += preorder(root.right, greatest)

            return res

        # Passing in root itself, including its own value as that will be the first node to be counted as good.
        # All roots of nodes will be considered good as it fits the criteria of having no previous nodes being greater than it
        return preorder(root, root.val)
