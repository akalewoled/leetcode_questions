class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            count[i]=1+count.get(i,0) 
            
        for i in count:
            if count[i]>len(nums)//2:
                return i
            

        