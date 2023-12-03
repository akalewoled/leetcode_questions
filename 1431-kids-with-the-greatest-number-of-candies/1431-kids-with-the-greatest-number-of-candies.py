class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        final=[]
        maxi = max(candies)
        for i in candies:
            if i + extraCandies>=maxi:
                final.append(True)
            else:
                final.append(False)
        return final