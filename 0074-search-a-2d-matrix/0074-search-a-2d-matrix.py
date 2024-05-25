class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1 and len(matrix[0])==1 :
            if matrix[0][0]==target:return True
            else:return False
        if len(matrix)>1:
            l=0
            r=len(matrix)-1
            while l<=r:
                
                mid=l+(r-l)//2
                if matrix[mid][0]<=target:
                    l=mid+1
                else:
                    r=mid-1
        else:
            r=0


        targetrow=matrix[r]
        left=0
        right=len(targetrow)-1
        print(targetrow)
        
        while left<=right:
            mid=left+(right-left)//2
            if targetrow[mid]==target:
                return True
            elif targetrow[mid]<target:
                left=mid+1
                
            elif targetrow[mid]>target :
                right=mid-1
                
        return False
           