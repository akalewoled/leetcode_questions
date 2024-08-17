class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        final=[[float("inf") for i in range(n) ] for j in range(n) ]
        final[n-1]=matrix[n-1]
        
        for i in range(n-2,-1,-1):
            for j in range(n):

                left=matrix[i][j]+final[i+1][max(0,j-1)]
                middle = matrix[i][j]+final[i+1][max(0,j)]
                right=matrix[i][j]+final[i+1][min(n-1,j+1)]

                final[i][j]=min([left,middle,right])
        
        return min(final[0])