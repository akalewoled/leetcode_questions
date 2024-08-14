class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        final=[0 for i in range(n)]
        last=prices[n-1]
        final[n-1]=prices[n-1]

        for i in range(n-2,-1,-1):
            discount=None
            for j in range(i+1,n):
                if prices[j]<=prices[i]:
                    discount=j
                    break
            if discount:
                final[i]=prices[i]-prices[discount]
            else:
                final[i]=prices[i]
         
        return final
        #time 0n space 0n

        