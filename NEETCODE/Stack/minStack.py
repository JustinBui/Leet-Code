class MinStack:

    def __init__(self):
        self.smallest_value = float('inf')
        self.stack = list()
        # List containing the smallest values at the certain index when pushed or popped
        self.smallest_values_tracker = list()

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Keeping track of the min values in accordance to where we are in the stack
        if val < self.smallest_value:
            self.smallest_value = val
        self.smallest_values_tracker.append(self.smallest_value)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.smallest_values_tracker.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.smallest_values_tracker) > 0:
            return self.smallest_values_tracker[-1]
        else:
            return None


if __name__ == '__main__':
    # ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
    # [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(2147483646)
    obj.push(2147483646)
    obj.push(5)
    print(obj.getMin())
    obj.pop()
    obj.push(500)
    print(obj.getMin())
