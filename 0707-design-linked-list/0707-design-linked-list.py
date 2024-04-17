class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        
        self.head = None
        self.size = 0

    def get(self, index):
        
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        ptr =0
        
        while ptr <index:
            curr = curr.next
            ptr+=1
        return curr.val

    def addAtHead(self, val):
        
        node = Node(val)
        node.next = self.head
        self.head = node

        self.size += 1

    def addAtTail(self, val):
      
        curr = self.head
        if curr is None:
            self.head = Node(val)
            self.size += 1
            return
        
        while curr.next != None:
            curr = curr.next
        curr.next = Node(val)
        self.size += 1

        

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return
        
        curr = self.head
        ptr=0
        while ptr < index - 1 :
            curr = curr.next
            ptr+=1
        node = Node(val)
        node.next = curr.next
        curr.next = node
        self.size += 1

    def deleteAtIndex(self, index):
   
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
            return
        ptr=0
        while ptr< index - 1:
            curr = curr.next
            ptr+=1
        curr.next = curr.next.next

        self.size -= 1