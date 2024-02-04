class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        final=0                          #counts the number of good pairs 
        for i in range(len(nums)):          #trverse through each  number 
            for j in range(i+1,len(nums)):       # check the equality of the numbers  on the right side and add 1 to thecounter 
                if nums[j]==nums[i]:
                    final+=1
        return final
        