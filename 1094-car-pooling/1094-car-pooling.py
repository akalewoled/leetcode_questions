
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        a=[0]*1100
        for i in trips:
            a[i[1]]+=i[0]
            a[i[2]]-=i[0]
        if a[0]>capacity:
            return False
        for i in range(1,len(a)):
            a[i]+=a[i-1]
            if a[i]>capacity:

                return False
        return True
            
