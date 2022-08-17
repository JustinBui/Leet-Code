class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        it1 = list1
        it2 = list2
        
        # Taking care of edge cases if either of the linked lists
        # are empty
        if not it1:
            return it2
        elif not it2:
            return it1
        
        # For whichever has the smallest first value, that will be the head
        # and we can work from there
        if it1.val <= it2.val:
            head = it1
            it1 = it1.next
        else: # if it2.val > it1.val
            head = it2
            it2 = it2.next
            
        next_largest = head
        
        while it1 and it2:
            if it1.val <= it2.val:
                next_largest.next = it1
                it1 = it1.next
            else:
                next_largest.next = it2
                it2 = it2.next
            
            next_largest = next_largest.next
            
        if it1:
            next_largest.next = it1
        elif it2:
            next_largest.next = it2
            
        return head