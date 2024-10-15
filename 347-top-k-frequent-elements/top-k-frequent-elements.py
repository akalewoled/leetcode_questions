from collections import Counter 
class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        res=[]
        count=Counter(arr)
        l= list(count.values())
        l.sort()
        l=l[-k:]
        for j in l:
            for i in count:
                if count[i]==j and i not in res:
                    res.append(i)
        return res