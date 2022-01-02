from typing import Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        # BREADTH FIRST SEARCH
        queue = []
        processed = []

        queue.append(root)
        while (len(queue) != 0):
            # Dequeuing and assigning it to curr
            curr = queue[0]
            queue.pop(0)

            processed.add(curr.val if curr != None else None)

            if (curr != None):
                queue.append(curr.left)
                queue.append(curr.right)

        # Splitting all processed elements into sublists
        levelOrderTraversal = [list[int]]

        p = 0
        power = 0
        while (p < len(processed)):  # Traversing through processed elements
            sublist = []
            for s in range(2**power):
                sublist.append(processed[p])
                p += 1
            power += 1

            levelOrderTraversal.append(sublist)

        return levelOrderTraversal


if (__name__ == "__main__"):
