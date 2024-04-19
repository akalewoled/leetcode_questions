# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        increment = False
        out = ListNode()
        num_list = []
        while l1 and l2:
            num = l1.val + l2.val
            if increment:
                num += 1
            if num >= 10:
                increment = True
                num = num % 10
            else:
                increment = False
            num_list.append(num)
            l1 = l1.next
            l2 = l2.next

        while l1:
            num = l1.val
            if increment:
                num += 1
            if num >= 10:
                increment = True
                num = num % 10
            else:
                increment = False
            num_list.append(num)
            l1 = l1.next
        
        while l2:
            num = l2.val
            if increment:
                num += 1
            if num >= 10:
                increment = True
                num = num % 10
            else:
                increment = False
            num_list.append(num)
            l2 = l2.next
        if increment:
            num_list.append(1)

        head = out
        head.val = num_list[0]       
        for i in range(1, len(num_list)):
            node = ListNode()
            node.val = num_list[i]
            head.next = node
            head = head.next
        return out
        