# Solution: https://www.youtube.com/watch?v=6ZnyEApgFYg

from typing import collections, Optional
from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if(root == None):
            return []   # Empty tree = empty list

        # BREADTH FIRST SEARCH
        queue = collections.deque()
        levelOrderTraversal = []

        queue.append(root)
        while (len(queue) != 0):
            # Dequeuing and processing that value
            qLen = len(queue)

            sublist = []
            for i in range(qLen):
                curr = queue.popleft()
                if (curr != None):
                    sublist.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)

            if (len(sublist) > 0):
                levelOrderTraversal.append(sublist)

        return levelOrderTraversal


if (__name__ == "__main__"):
    entityTree = BinarySearchTree()

    # Inserting elements
    entityTree.insert(5)
    # entityTree.insert(3)
    # entityTree.insert(4)
    # entityTree.insert(1)
    # entityTree.insert(11)

    mySol = Solution()
    newList = mySol.levelOrder(entityTree.root)

    print(f"Answer is {newList}")
