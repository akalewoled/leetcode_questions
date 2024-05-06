class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxi = collections.deque()
        mini = collections.deque()
        left = 0
        for r in nums:
            while len(maxi) and r > maxi[-1]: maxi.pop()#decresing
            while len(mini) and r < mini[-1]: mini.pop()#increasing
            maxi.append(r)
            mini.append(r)
            if maxi[0] - mini[0] > limit:#above the limit
                if maxi[0] == nums[left]: maxi.popleft()
                if mini[0] == nums[left]: mini.popleft()
                left += 1
           
        return len(nums) - left