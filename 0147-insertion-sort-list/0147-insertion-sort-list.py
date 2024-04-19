# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy=ListNode(-5000,head)
        prev=head
        curr=head.next
        while curr:
            if curr.val >= prev.val:
                prev = prev.next
            else:
                prev1 = dummy
                while prev1.next.val <= curr.val:
                    prev1 = prev1.next
                    
                # Insert
                prev.next = curr.next
                curr.next = prev1.next
                prev1.next = curr
            curr = prev.next
        return dummy.next

            
            