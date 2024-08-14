class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        relation={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        stack=relation[s[n-1]]
        
        for i in range(n-2,-1,-1):
           
            if relation[s[i]]<relation[s[i+1]]:
                stack-=relation[s[i]]
            else:
                stack+=relation[s[i]]
        return stack