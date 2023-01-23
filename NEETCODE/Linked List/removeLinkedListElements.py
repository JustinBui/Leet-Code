from SLL import ListNode, SinglyLinkedList
from typing import Optional

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        prev = dummy
        curr = head
        
        while curr:
            post = curr.next
            
            if curr.val == val:
                prev.next = post
            else:
                prev = curr
            
            curr = post

        return dummy.next

if __name__ == "__main__":

    SLL = SinglyLinkedList()
    SLL.append(1)
    SLL.append(2)
    SLL.append(6)
    SLL.append(3)
    SLL.append(4)
    SLL.append(5)
    SLL.append(6)

    print('Before:')
    SLL.traverse()

    obj = Solution()
    obj.removeElements(SLL.head, 6)

    print('After:')
    SLL.traverse()