class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n=bin(n)
        for i in range(1,len(n)):
            if n[i] ==n[i-1]:
                return False
        return True
        