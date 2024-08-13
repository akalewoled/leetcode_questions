class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        left=0
        final=0
        summ=1
        while summ <= n:
            if left <len(nums) and nums[left] <= summ:
                summ+=nums[left]
                left+=1
            else :
                summ*=2
                final+=1
        return final

            