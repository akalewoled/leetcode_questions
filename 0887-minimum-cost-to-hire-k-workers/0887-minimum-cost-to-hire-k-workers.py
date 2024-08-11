class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs=[]
        for i in range(len(quality)):
            pairs.append((wage[i]/quality[i],quality[i]))
        pairs.sort(key= lambda x :x[0])

        heap=[]
        totalwork=0
        res=float("inf")
        for rate,work in  pairs:
            totalwork+=work
            heappush(heap,-work)

            if len(heap) >k:
                totalwork+=heappop(heap)
            if len(heap)==k:
                res=min(res,totalwork*rate)
        return res

