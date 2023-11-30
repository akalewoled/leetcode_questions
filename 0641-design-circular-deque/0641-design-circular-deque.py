class MyCircularDeque:
    

    def __init__(self, k: int):
        self.capacity=k
        self.array = []         

    def insertFront(self, value: int) -> bool:
        if len(self.array)<self.capacity:
            self.array.append(value)
            return True
        else:
            return False


    def insertLast(self, value: int) -> bool:
        if len(self.array)<self.capacity:

            a=[value]
            self.array=a+self.array
            return True
        else:
            return False
            

    def deleteFront(self) -> bool:
        if len(self.array)>=1:
            self.array.pop()
            return True
        else:
            return False
        
        

    def deleteLast(self) -> bool:
        if len(self.array)>=1:
            self.array.pop(0)
            return True
        else:
            return False
        

    def getFront(self) -> int:
        return self.array[-1] if len(self.array)>0 else -1
        

    def getRear(self) -> int:
        return self.array[0] if len(self.array)>0 else -1
        

    def isEmpty(self) -> bool:
        
        return len(self.array)==0
        

    def isFull(self) -> bool:
        
        return len(self.array)==self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()