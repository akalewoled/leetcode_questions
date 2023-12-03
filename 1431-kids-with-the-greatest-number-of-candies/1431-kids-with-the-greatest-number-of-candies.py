class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        final=[]
        maxi = max(candies)
        for i in candies:
            final.append(i + extraCandies>=maxi)
        return final