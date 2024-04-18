# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return 

        dummy=ListNode(0,head)
        prev=dummy
        curr=prev.next
        while curr and curr.next:
            nextnode=curr.next
            curr.next, nextnode.next, prev.next = nextnode.next, prev.next, nextnode
        
        head=dummy.next
        return head
        