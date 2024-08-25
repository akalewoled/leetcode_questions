class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        substrings=0
        for i in range(0,n):
            # for odd
            left=i
            right=i
            while left >=0 and right <n and s[right] ==s[left]:
                print()
                substrings+=1
                right+=1
                left-=1
            if i < 1:continue#this break
            # for even
            left=i-1
            right=i
            
            while left >=0 and right <n and s[right] ==s[left]:
                substrings+=1
                right+=1
                left-=1
        
        return substrings