class Solution:
    def nearestExit(self, maze: List[List[str]], start: List[int]) -> int:
        m=len(maze)
        n=len(maze[0])

        directions={(0,1),(1,0),(-1,0),(0,-1)}

        q=[(start[0],start[1],0),]
        visited=set()
        visited.add((start[0],start[1]))
        ans=-1
        path={}
        final=[]

        while q:
            for _ in range(len(q)):
                
                x,y,dist=q.pop(0)
                
                for xx,yy in directions:
                    a=x+xx
                    b=y+yy
                    if 0<= a<m and 0<=b<n:
                        if  maze[a][b]==".":
                                
                            if (a,b) not in visited:


                                path[(a,b)]=dist+1
                                visited.add((a,b))
                                q.append([a,b,dist+1])
                            else:
                               
                                if (a,b) in path   and dist+1<path[(a,b)]:
                                    path[(a,b)]=dist+1
                                    visited.add((a,b))
                                    q.append([a,b,dist+1])

                    else:
                        if [x,y] !=start:
                            final.append(dist)
        return -1 if not final else min(final)