from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # PREORDER TRAVERSAL
        res = [None]
        i = [0]

        def inorder(root: Optional[TreeNode], k: int):
            if not root:
                return

            inorder(root.left, k)
            i[0] += 1
            if i[0] == k:
                res[0] = root.val
                return
            inorder(root.right, k)

        inorder(root, k)
        return res[0]


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(6)
    tree.insert(2)
    tree.insert(4)
    tree.insert(1)

    obj = Solution()
    print(obj.kthSmallest(tree.root, 3))
