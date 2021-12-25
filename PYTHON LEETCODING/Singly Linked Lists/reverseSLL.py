from SLL import ListNode, SinglyLinkedList
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return None

        pre = None
        current = head
        post = current

        while (current != None):
            post = post.next
            current.next = pre

            # Advancing the iterators
            pre = current
            current = post

        head = pre  # Head now belongs to the end

        return head


def traverse(head: ListNode):
    it = head
    while (it != None):
        print(it.val)
        it = it.next


if (__name__ == "__main__"):
    mySol = Solution()
    myList = SinglyLinkedList()

    # for i in range(1, 3):
    #     myList.append(i)

    print("Before: ")
    myList.traverse()

    print("After:")
    newList = mySol.reverseList(myList.head)
    traverse(newList)
