from collections import Counter
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2=len(str1),len(str2)
        def value(i):
            if l1%i or l2%i:
                return False
            n1,n2=l1//i,l2//i
            base=str1[:i]
            return str1==n1*base and str2==n2*base
                
        for i in range(min(l1,l2),0,-1):
            if value(i):
                return str1[:i]
        return ""
        