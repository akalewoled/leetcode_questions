class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def factors(nums):
            factors=set()
            for i in range(1,nums+1):
                if nums%i ==0:
                    factors.add(i)
            return factors
        set1=factors(min(nums))
        set2=factors(max(nums))
        return max(set1.intersection(set2))
