import random

class RandomizedSet:
    

    def __init__(self):
        self.wana=set()
        

    def insert(self, val: int) -> bool:
        if val in self.wana:
            return False
        else:
            self.wana.add(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.wana:
            self.wana.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(sorted(self.wana))
    


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()