class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        final=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==nums[i]:
                    final+=1
        return final
        