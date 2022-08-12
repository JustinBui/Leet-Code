from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        queue = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            curr_level = []
            curr_lvl_count = len(queue)

            for i in range(curr_lvl_count):
                node = queue.pop(0)
                curr_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(curr_level)

        return res


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(6)
    tree.insert(7)
    tree.insert(1)

    obj = Solution()
    print(obj.levelOrder(tree.root))
