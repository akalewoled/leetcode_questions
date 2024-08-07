class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1: return nums[0]
        maxi=[0] *len(nums)
        maxi[0]=nums[0]
        maxi[1]=max(nums[0],nums[1])

        for i in range(2,len(nums)):
            maxi[i] = max (maxi[i-1],nums[i]+maxi[i-2])

        return maxi[-1]
        