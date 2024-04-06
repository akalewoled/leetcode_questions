class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumi=sum(nums)
        cnt=0
        for i in range(len(nums)): 
            cnt+=nums[i]
            current=cnt-nums[i]
            if  current==sumi-cnt:
                return i
        return -1