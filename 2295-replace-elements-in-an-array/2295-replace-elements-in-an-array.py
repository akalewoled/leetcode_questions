class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        refernce={}
        for x,y in enumerate(nums):
            refernce[y]=x # x= index y = value in num
        for value,replce in operations:
            indexInNums=refernce[value]
            nums[indexInNums]=replce
            del refernce[value]
            refernce[replce]=indexInNums
        return nums