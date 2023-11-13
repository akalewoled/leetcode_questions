class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=len(nums)//2
        final=[]
        for k in range(i):
            final.append(nums[k])
            final.append(nums[k+i])
        return final
            
        