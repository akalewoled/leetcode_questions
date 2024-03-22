class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        maxi=0
        c=0
        for r in range(len(nums)):
            if nums[r]==0 :
                c+=1
            while c>1:
                if nums[l]==0:
                    c-=1
                l+=1
            maxi=max((r-l),maxi)
           
        return maxi