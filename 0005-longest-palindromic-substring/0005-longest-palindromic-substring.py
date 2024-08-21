class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<=1:
            return s

        longest=""
        leng=0
        
        for i in range(0,n):
            # for odd
            l=i
            r=i
            while l>=0 and r <n and s[l]==s[r]:
                print(l,r)
                if r-l+1>leng:
                    longest=s[l:r+1]
                    leng=r-l+1
                r+=1
                l-=1
            #for even
            l=i
            r=i+1
            while l>=0 and r <n and s[l]==s[r]:
                if r-l+1>leng:
                    longest=s[l:r+1]
                    leng=r-l+1
                r+=1
                l-=1
        return longest