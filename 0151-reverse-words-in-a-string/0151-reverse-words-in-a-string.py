class Solution:
    def reverseWords(self, s: str) -> str:
        
        s=list(s.split(" "))
        ss=[]
        for i in s:
            if len(i)>=1:
                ss.append(i)
        
        return " ".join(reversed(ss))
        