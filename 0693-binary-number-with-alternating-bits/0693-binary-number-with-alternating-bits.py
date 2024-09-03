class Solution:
        def hasAlternatingBits(self, n):
            s = bin(n)
            return '00' not in s and '11' not in s