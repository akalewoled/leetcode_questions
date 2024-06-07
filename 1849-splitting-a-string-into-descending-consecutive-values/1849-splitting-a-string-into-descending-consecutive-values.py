class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(index,left):
            if index == len(s):
                return True
            
            for j in range(index,len(s)):
                right=int(s[index:j+1])
                
                if right+1== left and dfs(j+1,right):
                    return True
            
            return False
                
            
        
        for i in range(len(s)-1):
            val=int(s[:i+1])
            if dfs(i+1,val):return True
        return False