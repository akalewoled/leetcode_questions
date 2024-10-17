
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n= len(nums)
        if n < 2 :
            return nums[:]
        else:

            middle=int(n/2)

            left=self.sortArray(nums[: middle])
            right=self.sortArray(nums[middle:])
            return self.merge(left,right)
    def merge(self,left,right):
        final=[]
        i,j=0,0
        while i < len(left) and j< len(right):
            if left[i]<right[j]:
                final.append(left[i])
                i+=1
            else:
                final.append(right[j])
                j+=1
        while i < len(left):
            final.append(left[i])
            i+=1
        while j < len(right):
            final.append(right[j])
            j+=1
        return final

