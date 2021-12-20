class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None, tail=None):   # Constructor
        self.head = head
        self.tail = tail
        self.count = 0

    def empty(self) -> bool:
        return self.head == None and self.tail == None

    def append(self, value: int):   # Adding to the end
        newNode = ListNode(value)
        if (self.empty()):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    def delete_end(self):
        if (self.empty() == False):

            # If the only element in the list
            if (self.count == 1):
                self.head = None
                self.tail = None
            else:
                it = self.head
                while(it.next != self.tail):
                    it = it.next
                it.next = None
                self.tail = it
            self.count -= 1

    def traverse(self):
        it = self.head
        while(it != None):
            print(it.val)
            it = it.next


if (__name__ == "__main__"):
    myList = SinglyLinkedList()

    print("Is the list empty?")
    if (myList.empty()):
        print("Yes, it is")
    else:
        print("No, it is not")

    for i in range(0, 6):
        myList.append(i)
    myList.delete_end()

    myList.traverse()
