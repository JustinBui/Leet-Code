class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.count = 0
        self.head = None

    def get(self, index: int) -> int:
        if index >= self.count:
            # Out of bound/invalid index
            return -1
        else:
            it = self.head
            for i in range(index):
                it = it.next            
            return it.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, self.head)
        self.head = newNode
        self.count += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)

        if not self.head: # Empty list
            self.head = newNode
        else:
            it = self.head
            while it.next:
                it = it.next
            it.next = newNode
        
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count: # Invalid
            return

        # Valid
        if index == self.count: # Start of list
            self.addAtTail(val)
        elif index == 0:    # End of list
            self.addAtHead(val)
        else: # Any other indices between the list
            pre = self.head
            for i in range(index - 1):
                pre = pre.next
            newNode = ListNode(val, pre.next)
            pre.next = newNode

            self.count += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count: # Invalid
            return

        # Valid
        if index == 0:
            self.head = self.head.next
        else:
            pre = self.head
            for i in range(index - 1):
                pre = pre.next
            pre.next = pre.next.next
        self.count -= 1


def traverse(head):
    it = head
    while it:
        print(it.val, end='->')
        it = it.next
    print('\n')

if __name__ == '__main__':
    l = MyLinkedList()

    l.addAtHead(5)
    l.addAtIndex(1,2)
    print(l.get(1))
    l.addAtHead(6)
    l.addAtTail(2)
    l.get(3)
    l.addAtTail(1)
    print('Count is', l.count)
    l.get(5) #!!
    l.addAtHead(2)
    l.get(2)
    l.addAtHead(6)

    traverse(l.head)

