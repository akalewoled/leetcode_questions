class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def  pow(n):

            if n==1: return True
            if n==0 :return False
            if n%3 !=0:return False
            return pow(n//3)
        return pow(n)

        