from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:# [a,b,c,a]
        nums1=Counter(nums) #{a:2,b:1,c:3}
        if  len(nums1)<len(nums):
            return True
        return False