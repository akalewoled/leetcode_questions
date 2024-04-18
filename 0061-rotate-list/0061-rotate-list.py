# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if  not head or k==0:
            return head
        curr=head
        count=1
        while curr.next:
            curr=curr.next
            count+=1
        curr.next=head
        ptr=head
        k%=count
        for i in range(count-k-1):
            ptr=ptr.next
            
        head=ptr.next
        ptr.next=None
        return head
        
        