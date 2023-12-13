class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for i in s:
            count[i]=1+count.get(i,0)
        
        ans=""
        for i in count:
            if count[i]==1:
                ans=i
                break
        return s.index(ans) if len(ans)>=1 else -1
        