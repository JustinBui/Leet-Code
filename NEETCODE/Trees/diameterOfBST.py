from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            # Adding 2 with left + right because we are taking into account of BOTH nodes
            res[0] = max(res[0], 2 + left + right)

            # While we are finding the max diameter, we are finding the height of each node in the BST Depth First
            return 1 + max(left, right)

        dfs(root)
        return res[0]


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(6)
    tree.insert(7)
    tree.insert(1)

    obj = Solution()
    print(obj.diameterOfBinaryTree(tree.root))
