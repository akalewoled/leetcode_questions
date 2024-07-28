class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    grid[i][j]=0
                    q.append((i,j))
                else:
                    grid[i][j]==1
        seen=set(q)
        while q:
            for _  in range(m):
                i,j=q.popleft()
                val=grid[i][j]
                directions=((0,1),(1,0),(-1,0),(0,-1))
                for a,b  in directions:
                    x=i+a
                    y=j+b
                    if 0<=x<m and 0<= y<n and (x,y) not in seen:
                        grid[x][y]=val+1
                        q.append((x,y))
                        seen.add((x,y))
        return grid
