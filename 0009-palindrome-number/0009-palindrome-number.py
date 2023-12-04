class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=list(str(x).strip())
        
        
        return  y==list(reversed(y))