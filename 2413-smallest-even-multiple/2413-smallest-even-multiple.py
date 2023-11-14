class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        k=0
        l=1
        while k==0:
            z=n*l
            if z%2==0:
                return z
            l+=1
        return 0
            