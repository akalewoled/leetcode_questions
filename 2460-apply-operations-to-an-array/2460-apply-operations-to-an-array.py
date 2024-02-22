class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        num=[]
        zeros=[]
        for i in nums:
            if i==0:
                zeros.append(i)
            else:
                num.append(i)
        return num+zeros