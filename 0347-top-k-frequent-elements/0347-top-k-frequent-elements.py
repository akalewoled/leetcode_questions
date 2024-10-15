from collections import Counter 
class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        res=[]
        count=Counter(arr)
        bucket=[[] for _ in range(len(arr)+1)]

        for i,j in count.items():
            bucket[j].append(i)
        
        for i in range(len(bucket)-1,-1,-1):
            if len(res)>=k:
                return res[:k]
            res.extend(bucket[i])
        return []
