import SLL
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[SLL.ListNode]) -> Optional[SLL.ListNode]:
        it = head
        while (it != None):
            current_value = it.val
            while (it.next != None and it.next.val == current_value):
                it.next = it.next.next
            it = it.next
        
        return head


if (__name__ == "__main__"):
    myList = SLL.SinglyLinkedList()
