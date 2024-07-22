class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        maxheap=[]
        for i ,s in enumerate(score):
            heappush(maxheap, (-s,i))
        final=[0] * len(score)
        place = 1
        while maxheap:
            pos=heappop(maxheap)[1]
            if place > 3:
                rank=str(place)
            elif place == 1:
                rank = "Gold Medal"
            elif place == 2:
                rank = "Silver Medal"
            elif place == 3:
                rank = "Bronze Medal"
            final[pos] = rank
            place +=1
        return final
            