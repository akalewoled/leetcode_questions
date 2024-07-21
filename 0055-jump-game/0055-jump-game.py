class Solution:
    def canJump(self, nums: List[int]) -> bool:
        capacity=0
        for i in nums:
            if capacity<0:
                return False
            if i> capacity:
                capacity=i
            capacity-=1
        return True