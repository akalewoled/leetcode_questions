class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        final = [[ None for i in range(n)] for j in range(m)]
        

        directions=((0,1),(1,0),(0,-1),(-1,0))

        seen=set()
        q=[]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i,j,0])
                    seen.add((i,j)) 
        
        while q:
            
            
            for _ in range(len(q)):

                i,j,dist=q.pop(0)
                if not final[i][j]:
                    final[i][j]=dist

                
                for  x,y in directions:
                    a,b =i+x,j+y
                    if (a,b) not in seen and 0<=a<m and 0<= b< n:
                        q.append([a,b,dist+1])
                        seen.add((i,j))
                
        return final
