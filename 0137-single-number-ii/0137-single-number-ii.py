class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        final=0
        for i in range(32):
            tempo=0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                tempo += num>> i & 1
            tempo = tempo % 3 
            final |=  tempo << i
        
        if final >= 2**31:
            final -= 2**32
        return final
        