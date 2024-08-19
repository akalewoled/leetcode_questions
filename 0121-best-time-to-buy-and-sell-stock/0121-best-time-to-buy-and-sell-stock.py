class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        minn=float("inf")
        for i in range(len(prices)):
            minn=min(minn,prices[i])
            if prices[i]-minn>0:
                max_profit=max(max_profit,prices[i]-minn)
            
        return max_profit
