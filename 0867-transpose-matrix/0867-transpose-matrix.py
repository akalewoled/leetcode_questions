class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        x=len(matrix)
        y=len(matrix[0])
        final=[[0 for _ in range(x)] for _  in range(y)]
        for i in range(x):
            for j in range(y):
                final[j][i]=matrix[i][j]
        return final
        