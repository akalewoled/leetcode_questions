# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:#empty list
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:# reached the end 
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        