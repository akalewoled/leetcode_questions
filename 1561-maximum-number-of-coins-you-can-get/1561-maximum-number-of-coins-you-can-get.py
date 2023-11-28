class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        listed=piles
        listed.sort()
        my=0
        while piles:
            my+=listed[-2]
            piles.pop()
            piles.pop()
            piles.pop(0)
        return my