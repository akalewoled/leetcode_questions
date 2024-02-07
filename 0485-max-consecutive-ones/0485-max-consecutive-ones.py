class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = result = 0
        for n in nums:
            consecutive = consecutive*n+n
            result = max(result, consecutive)
        return result
    '''
    we use two varible to comapre the length 
    the trick is in the consecutive=conscecutive*n+n statement this increases as  the number is 1 and returns to 0 of it is 0
    '''