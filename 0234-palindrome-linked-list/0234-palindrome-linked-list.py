# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # we use the common stack approach 
        check=0
        stack=[]
        ptr=head
        while ptr :
            stack.append(ptr.val)
            ptr=ptr.next
        curr=head
        while curr:
            if curr.val!=stack.pop():
                return False
            curr=curr.next
        return True
            