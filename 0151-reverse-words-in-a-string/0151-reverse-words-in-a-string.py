class Solution:
    def reverseWords(self, s: str) -> str:
        ss=[i for i in s.split(" ") if len(i)>0 ]
        
        return " ".join(reversed(ss))
        