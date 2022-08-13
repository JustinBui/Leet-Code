
from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        queue = []
        res = []

        if root:
            queue.append(root)

        while queue:
            res.append(queue[len(queue) - 1].val)
            level_len = len(queue)

            for i in range(level_len):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
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
    print(obj.rightSideView(tree.root))
