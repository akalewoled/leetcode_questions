class Solution:
    def findIndices(self, nums: List[int], id: int, vd: int) -> List[int]:
        maxi,mini=0,0
        for i in range(id,len(nums)):
            tempo=i-id
            if nums[tempo]<nums[mini]: mini=tempo# just tracking the mini
            if nums[tempo]>nums[maxi]:maxi=tempo# just tracking the maxi
            #checking the validity by comparing the current value with the extreme cases
            if abs(nums[maxi]-nums[i])>= vd:#checking with maximum 
                return [maxi,i]
            if abs(nums[mini]-nums[i])>=vd:#checking with the minimum so far
                return [mini,i]
        return [-1,-1]
        