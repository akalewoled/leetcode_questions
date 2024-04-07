class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        i=0
        final=[]
        while i+3<=n:
            row=[]
            j=0
            while j+3<=m  :
                first=max(grid[i][j:j+3])
                second=max(grid[i+1][j:j+3])
                third=max(grid[i+2][j:j+3])
                row.append(max(first,second,third))
                j+=1
            final.append(row)
            i+=1
        return final
                
            
                    
                 
                
            
                
            
            