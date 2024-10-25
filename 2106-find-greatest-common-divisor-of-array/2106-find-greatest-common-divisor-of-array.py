class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxx = max(nums)
        minn = min(nums)
        for i in range(maxx, 0, -1):
            if maxx % i == 0 and minn % i == 0:
                return i
        return 1