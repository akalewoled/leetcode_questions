# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        num1=[]
        while curr1:
            num1.append(curr1.val)
            curr1=curr1.next
        curr2=l2
        num2=[]
        while curr2:
            num2.append(curr2.val)
            curr2=curr2.next
        num1="".join(map(str,num1))
        num2="".join(map(str,num2))
        final=str(int(num1)+int(num2))
     
        head=ListNode(0,None)
        prev=head
        for i in range(len(final)):
            tempo=ListNode(int(final[i]),None)
            prev.next=tempo
            prev=tempo
        return head.next


     
