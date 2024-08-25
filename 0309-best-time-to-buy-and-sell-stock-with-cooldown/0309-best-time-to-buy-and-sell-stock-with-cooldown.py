class Solution:
    def maxProfit(self, prices):
        
        cache={}
        def dfs(buy,i):
            
            if i >=len(prices):
                return 0
            if (i,buy) in cache:
                return cache[(i,buy)]
            
            if buy:
                buying=  dfs(not buy,i+1)-prices[i]
                cool=dfs(buy,i+1)
                cache[(i,buy)]=max(buying,cool)
            else:
                selling=prices[i]+dfs(not buy,i+2)#not buy to revese the orginal not buy
                cool=dfs(buy,i+1)
                cache[(i,buy)]=max(selling,cool)
            return cache[(i,buy)]
        return dfs(True,0)
            
           