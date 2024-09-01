class Solution(object):
    def missingNumber(self, nums):
        lenth = len(nums)
        # Calculate the sum of the first N natural numbers as (1 + lenth) * lenth/2...
        sum = (1 + lenth) * lenth/2
        # Traverse the array from start to end...
        for i in nums:
            # Find the sum of all the array elements...
            sum -= i
        return sum