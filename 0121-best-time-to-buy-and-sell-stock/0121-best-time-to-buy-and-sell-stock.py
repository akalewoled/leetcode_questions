class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=float('inf')
        y=0
        for p in prices:
            if(p<x):
                x=p
            elif p-x>y:
                y=p-x
        return y
        
        