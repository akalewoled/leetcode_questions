class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        check={}
        def dfs(i,summ):
           
            if summ==amount:
                return 1
            if summ > amount :
                return 0
            if (summ,i) in check:
                return check[(summ,i)]
            
            cur=0
            for j in range(i,n):
                cur += dfs(j,summ+coins[j])
            check[(summ,i)]=cur
            return cur
        return dfs(0,0)