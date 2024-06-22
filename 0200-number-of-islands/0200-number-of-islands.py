class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visted=set()
        islands=0
        rows,cols=len(grid),len(grid[0])

        def bfs(row,col):
            
            deque=collections.deque()
            visted.add((row,col))
            deque.append((row,col))
            
            while deque:
                x,y=deque.popleft()
                directions=[  [1,0], [-1,0], [0,1], [0,-1]  ]
                for r,c in directions:
                    xx=x+r
                    yy=y+c
                    if (xx in range(rows) and yy in range(cols) and grid[xx][yy]=="1" and (xx,yy) not in visted):
                        deque.append((xx,yy))
                        visted.add((xx,yy))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visted:
                    bfs(r,c)
                    islands+=1
        return islands
        