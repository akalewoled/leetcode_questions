class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        @cache
        def dfs(i,summ):
           
            if summ==amount:
                return 1
            if summ > amount :
                return 0
            
            cur=0
            for j in range(i,n):
                cur += dfs(j,summ+coins[j])
            return cur
        return dfs(0,0)