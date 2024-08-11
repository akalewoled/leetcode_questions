class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={}
        #lets solve it using brute force 
        def dfs(i,summ):
            if i == len(nums):
                if summ == target:
                    return 1 
                return 0
            if (i,summ) in cache:
                return cache[(i,summ)]
            cache[(i,summ)] = dfs(i+1,summ+nums[i])+dfs(i+1,summ-nums[i])
            return cache[(i,summ)]
        
        return dfs(0,0)
