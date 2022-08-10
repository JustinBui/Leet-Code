from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap_pointers(root):
            if root == None:
                return

            temp = root.left
            root.left = root.right
            root.right = temp

            swap_pointers(root.left)
            swap_pointers(root.right)

        swap_pointers(root)
        return root


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(6)
    # tree.insert(10)
    # tree.insert(8)
    # tree.insert(20)
    # tree.insert(15)
    # tree.insert(21)

    print('BEFORE:')
    tree.breadthFirstSearch()

    obj = Solution()
    obj.invertTree(tree.root)

    print('AFTER:')
    tree.breadthFirstSearch()
