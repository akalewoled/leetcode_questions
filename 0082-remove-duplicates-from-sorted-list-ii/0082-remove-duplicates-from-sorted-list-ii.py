# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        empty=ListNode()

        empty.next=head
        curr=empty
        while curr:
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                tempo=curr.next.next
                while tempo and tempo.next and  tempo.val==tempo.next.val:
                    tempo=tempo.next
                curr.next=tempo.next
            else:
                curr=curr.next  
        return empty.next  

