class Solution:
    def climbStairs(self, n: int) -> int:
        path={0:1,1:1}
        def dp(n):
            if n in path:
                return path[n]
            val=dp(n-1)+dp(n-2)
            path[n]=val
            return val
        return dp(n)
