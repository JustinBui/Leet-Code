from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val <= root.val and q.val >= root.val) or (q.val <= root.val and p.val >= root.val):
            # Finding where the split happens
            return root
        # Going toward the direction of the split, depending on whether BOTH p and q are greater OR less than current root
        # value
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
