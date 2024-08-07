class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def robbing(i):
            return max(robbing(i+1),nums[i]+robbing(i+2)) if i < len(nums) else 0
        return robbing(0)
        