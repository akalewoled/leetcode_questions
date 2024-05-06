
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mezegeb={None:None}

        curr=head
        while curr:
            copy=Node(curr.val)
            mezegeb[curr]=copy

            curr=curr.next
        curr=head
        while curr:
            mezegeb[curr].next=mezegeb[curr.next]
            mezegeb[curr].random=mezegeb[curr.random]
            curr=curr.next

        return mezegeb[head]