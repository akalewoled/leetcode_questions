class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        voel=['a','e','i','o','u']
        l,r=0,len(s)-1
        while l<r:
            if s[l].lower() in voel:
                while l<r:
                    if s[r].lower() in voel:
                        
                        s[r],s[l]=s[l],s[r]
                        r-=1
                        break
                    r-=1
            l+=1
        return "".join(s)
            

                
                