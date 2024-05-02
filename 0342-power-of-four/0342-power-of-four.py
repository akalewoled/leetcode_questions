class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def  pow(n):

            if n==1: return True
            if n==0 :return False
            if n%4 !=0:return False
            return pow(n//4)
        return pow(n)


        