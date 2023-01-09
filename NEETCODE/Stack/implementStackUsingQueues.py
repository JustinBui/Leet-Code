class MyStack:

    def __init__(self):
        self.queue = []
        
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty() == False:
            for i in range(len(self.queue) - 1):
                element = self.queue.pop(0) # Pop front of the queue
                self.queue.append(element) #  Push the element to the back of the queue
            
            # The first element of the queue now represents the top of our stack
            return self.queue.pop(0)

            

    def top(self) -> int:
        if self.empty() == False:
            for i in range(len(self.queue) - 1):
                element = self.queue.pop(0) # Pop front of the queue
                self.queue.append(element) #  Push the element to the back of the queue
            
            top = self.queue.pop(0)
            self.queue.append(top)
            return top

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()