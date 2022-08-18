from SLL import ListNode, SinglyLinkedList
from typing import Optional


class Solution:
    # ------------------------------ Approach By Inverting Linked List ------------------------------
    # def invert(self, head):
    #     # Invert Linked List
    #     pre = None
    #     post = head

    #     while head:
    #         post = head.next
    #         head.next = pre
    #         pre = head
    #         head = post
    #     head = pre

    #     return head

    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     head = self.invert(head)

    #     i = 1
    #     it = head
    #     while i < n:
    #         it = it.next
    #         i += 1

    #     # Delete first element of the list
    #     if it == head:
    #         head = head.next
    #     else:  # Deleting any element from list that is not head
    #         pre_it = head
    #         while pre_it.next != it:
    #             pre_it = pre_it.next
    #         pre_it.next = pre_it.next.next
    #     it.next = None

    #     return self.invert(head)

    # ---------------------------- Optimized Using 2 Pointer Approach ----------------------------
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)

        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next


if __name__ == "__main__":

    SLL = SinglyLinkedList()

    for i in range(1, 2):
        SLL.append(i)

    print('Before:')
    SLL.traverse()

    obj = Solution()
    res = obj.removeNthFromEnd(SLL.head, 1)

    it = res
    while it:
        print(it.val, end=' ')
        it = it.next
