class Solution(object):
    def findDiagonalOrder(self, matrix):
        final=[]
        i=j=dir=0
        for _ in range(len(matrix)*len(matrix[0])):
            print(i,j)
            final.append(matrix[i][j])
            if dir==0:
                if j==len(matrix[0])-1:
                    dir=1
                    i+=1
                elif i==0:
                    j+=1
                    dir=1
                else:
                    i-=1
                    j+=1
            else:
                if i==len(matrix)-1:
                    dir=0
                    j+=1
                elif j==0:
                    i+=1
                    dir=0
                else:
                    j-=1
                    i+=1
        return final

