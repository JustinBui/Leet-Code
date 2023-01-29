class ListNode:
    def __init__(self, pre=None, value='', next=None):
        self.pre = pre
        self.value = value
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(value=homepage)
        self.curr = self.head
        self.tail = self.head    

    def visit(self, url: str) -> None:
        newPage = ListNode(pre=self.curr, value=url)
        self.tail = newPage
        self.curr.next = newPage
        self.curr = newPage

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr == self.head:
                break
            self.curr = self.curr.pre

        return self.curr.value    

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr == self.tail:
                break
            self.curr = self.curr.next

        return self.curr.value
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)