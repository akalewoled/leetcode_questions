class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        cache={}
        def dfs(i,j):
            if i == m-1 and j ==n-1:
                return grid[i][j]
            if (i,j) in cache:
                return cache[(i,j)]
            bottom=float("inf")
            right=float("inf")
            
            if i+1<m:
                bottom=dfs(i+1,j)
            if j+1<n:
                right=dfs(i,j+1)

            cache[(i,j)]=min(bottom,right)+grid[i][j]
            return cache[(i,j)]
        return dfs(0,0)