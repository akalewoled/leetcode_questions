class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.solve(a, b) or self.solve(b, a)
    
    def solve(self, a, b):
        i = 0
        j = len(a) - 1
        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
        
        return self.isPalindrome(a[:i] + b[i:]) or self.isPalindrome(a[:j + 1] + b[j + 1:])
        
    
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True