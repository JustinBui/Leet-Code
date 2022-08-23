from SLL import SinglyLinkedList
from SLL import ListNode
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        ptr1 = l1
        ptr2 = l2

        carry = False
        # This will loop until ptr1 and ptr2 are both NULL
        # OR if we don't have to carry anymore terms
        while ((ptr1 != None or ptr2 != None) or carry == True):
            # Finding the 2 operands
            first, second = 0, 0
            if (ptr1 != None):
                first = ptr1.val
            if (ptr2 != None):
                second = ptr2.val

            # Finding the sum
            summation = first + second
            if (carry == True):
                summation += 1
            summationModed = summation % 10

            # Appending new node onto list
            newNode = ListNode(summationModed)
            if (head == None):
                head = newNode
                it = head
            else:
                it.next = newNode
                it = it.next

            # Determining if we have to carry the 1 for the next node
            if (summation >= 10):
                carry = True
            else:
                carry = False

            # Advancing both pointers forward
            if (ptr1 != None):
                ptr1 = ptr1.next
            if (ptr2 != None):
                ptr2 = ptr2.next

        return head


if (__name__ == "__main__"):
    entity = Solution()

    # First List
    l1_terms = [0]
    l1 = SinglyLinkedList()
    for i in l1_terms:
        l1.append(i)

    # Second List
    l2_terms = [7, 3]
    l2 = SinglyLinkedList()
    for i in l2_terms:
        l2.append(i)

    # Adding
    result = entity.addTwoNumbers(l1.head, l2.head)
    it = result
    while(it != None):
        print(it.val)
        it = it.next
