class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=second=float('inf')
        for n in nums:
            if n<first:
                first=n
            elif n<second and n>first:
                second=n
            elif first<second<n:
                return True
        print(first ,second)
        return False
                

        