class ListNode:
    def __init__(self, val=0, prev=None,next=None):
        self.val = val
        self.next = next
        self.prev = prev



class BrowserHistory:

    def __init__(self, homepage: str):
        self.head=ListNode(homepage)
        self.curr=self.head
    def visit(self, url: str) -> None:
        tempo=ListNode(url,self.curr,None)
        self.curr.next=tempo
        self.curr=self.curr.next
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev:
                self.curr=self.curr.prev
            else:
                break
        return self.curr.val


    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next:
                self.curr=self.curr.next
            else:
                break
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)