class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count={}
        
        for i in edges:
            count[i[0]]=1+count.get(i[0],0)
            count[i[1]]= 1+ count.get(i[1],0)
    
        return   max(count,key=count.get)