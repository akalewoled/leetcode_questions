class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        left=0
        final=0
        summ=0
        while summ < n:
            if left <len(nums) and nums[left] <= summ+1:
                summ+=nums[left]
                left+=1
            else :
                summ+=summ+1
                final+=1
        return final

            