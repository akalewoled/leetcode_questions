class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        buy=sell=profit=0
        n=len(prices)-1
        while i < n:
            while i <n and prices[i]>=prices[i+1]:
                i+=1
            buy=prices[i]
            while i <n and prices[i]<=prices[i+1]:
                i+=1
            sell=prices[i]
            print(buy,sell)
            profit+=sell-buy
        return profit
            
        