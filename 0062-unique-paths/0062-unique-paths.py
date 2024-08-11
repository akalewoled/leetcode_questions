class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache={}
        def dfs(i,j):
            if i==m -1 and j ==n-1:
                return 1 
            if (i,j) in cache:
                return cache[(i,j)]
            bottom=0
            right=0
            if i+1<m:
                bottom=dfs(i+1,j)
            if j+1<n:
                right=dfs(i,j+1)
            cache[(i,j)]=bottom+right
            return cache[(i,j)]
        return dfs(0,0)


