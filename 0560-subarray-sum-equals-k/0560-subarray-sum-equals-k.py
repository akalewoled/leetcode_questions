class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lastdiff={0:1}
        sum=0
        count=0
        for num in nums:
            sum+=num
            if sum-k in lastdiff:
                count+=lastdiff[sum-k]
            lastdiff[sum]=1+lastdiff.get(sum,0)
        return count