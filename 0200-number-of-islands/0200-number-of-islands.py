class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visted=set()
        islands=0
        rows,cols=len(grid),len(grid[0])

        def bfs(r,c):
            q=collections.deque()

            visted.add((r,c))
            
            q.append((r,c))
            
            while q:
                row,col=q.popleft()
                directions=[  [1,0], [-1,0], [0,1], [0,-1]  ]
                for dr,dc in directions:
                    r=dr+row
                    c=dc+col
                    if (r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visted):
                        q.append((r,c))
                        visted.add((r,c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visted:
                    bfs(r,c)
                    islands+=1
        return islands
        