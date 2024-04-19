# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or  not head.next:
            return head
        
        seen=[head.val]
        curr=head
        nxt=head.next
        while nxt:
            if nxt.val in seen:
                curr.next=nxt.next
                nxt=nxt.next
            else:
                seen.append(nxt.val)
                curr=curr.next
                nxt=nxt.next
        return head
        
        