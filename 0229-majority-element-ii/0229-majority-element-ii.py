class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        ans=[]
        for i in nums:
            count[i]=1+count.get(i,0)
        for i in count:
            if count[i]>len(nums)//3:
                ans.append(i)
        return ans