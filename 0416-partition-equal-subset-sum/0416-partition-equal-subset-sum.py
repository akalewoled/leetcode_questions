class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summed=sum(nums) / 2
        final=set()
        final.add(0)
        for i in nums:
            newdp=list(final)
            for j in newdp:
                new=i+j
                if new==summed:
                    return True
                final.add(new)
        return False


        