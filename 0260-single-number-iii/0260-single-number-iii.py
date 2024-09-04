class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        xored=0
        for i in range(len(nums)):
            xored ^= nums[i]

        position = 0
        while (xored >> position) & 1 !=1:
            position += 1

        first=0
        second=0
        for i in range(len(nums)):
            if (nums[i] >> position )& 1==1:
                first ^= nums[i]
            else:
                second^=nums[i]
        return [ first,second]
        