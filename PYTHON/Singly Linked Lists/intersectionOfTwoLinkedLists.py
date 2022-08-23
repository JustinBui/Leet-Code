# Solution: https://www.youtube.com/watch?v=D0X0BONOQhI

from SLL import ListNode, SinglyLinkedList
from typing import Optional


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        count_a = 0
        count_b = 0

        # Finding how many nodes are in A
        it = headA
        while (it):
            count_a += 1
            it = it.next

        # Finding how many nodes are in B
        it = headB
        while (it):
            count_b += 1
            it = it.next

        if (count_a > count_b):
            greater = headA
            less = headB
        else:   # If count_a <= count_b... but if count_a == count_b, it doesn't matter which one is 'greater'
            greater = headB
            less = headA

        # Advancing the pointer of the longer list to make it on
        # the same level as the one of the shorter list
        difference = abs(count_a - count_b)
        for i in range(difference):
            greater = greater.next

        while(greater):
            if (greater == less):
                return greater
            greater = greater.next
            less = less.next

        return None


if __name__ == "__main__":

    # Creating linked list A
    listA = SinglyLinkedList()
    for i in range(8, 9):  # 8
        listA.append(i)
    print("LIST A BEFORE: ", end=" ")
    listA.traverse()

    # Creating linked list A
    listB = SinglyLinkedList()
    for i in range(2, 5):   # 2 3 4
        listB.append(i)
    print("LIST B BEFORE: ", end=" ")
    listB.traverse()

    # # Connecting A and B
    # intersection = SinglyLinkedList()
    # for i in range(5, 8):   # 5 6 7
    #     intersection.append(i)

    # listA.tail.next = intersection.head
    # listB.tail.next = intersection.head

    print("LIST A AFTER: ", end=" ")
    listA.traverse()

    print("LIST B AFTER: ", end=" ")
    listB.traverse()

    ##########################################################
    testSolution = Solution()
    final_node = testSolution.getIntersectionNode(listA.head, listB.head)

    if (final_node):
        print(final_node.val)
    else:
        print("None")
