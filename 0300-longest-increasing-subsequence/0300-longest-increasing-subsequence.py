class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n= len(nums)
        memo=[1] *(n)
        for i in range(n):
            for j in range(i):
                if  nums[j] <  nums[i]:
                    memo[i]=max(memo[i],memo[j]+1)
        return max(memo)