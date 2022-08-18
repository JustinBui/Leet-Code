from SLL import ListNode, SinglyLinkedList
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Using slow and fast pointers to split the list in half
        slow, fast = head, head.next

        # Traversing slow and fast. Fast reaches either: The last node of the list (For linked lists with count(nodes) as EVEN)
        # OR a null value (For linked lists with count(nodes) as ODD). Once fast reaches the end, slow will end up being the last node
        # of the 'first half' of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now we can split the input list into 2 lists from the cutoff since slow.
        # second is the pointer of the FIRST value of the second half of the list
        second = slow.next
        slow.next = None  # Cutoff last node of first half to result in 2 distinct lists

        # Inverting the second half of list
        prev = None
        while second:
            post = second.next
            second.next = prev
            prev = second
            second = post

        second = prev  # head node of second half
        first = head  # head node of first half

        # Merging first and second halves
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


if __name__ == "__main__":

    SLL = SinglyLinkedList()

    for i in range(1, 6):
        SLL.append(i)

    print('Before:')
    SLL.traverse()

    obj = Solution()
    obj.reorderList(SLL.head)

    print('After:')
    SLL.traverse()
