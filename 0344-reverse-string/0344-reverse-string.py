class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        if len(s)<=1:
            return
        for i in range(0,(n)//2):
            print(i,n-1-i)
            s[i],s[n-1-i]=s[n-1-i],s[i]
            
        
        