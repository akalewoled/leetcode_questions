class Solution:
    def longestCycle(self, edges: List[int]) -> int:
    
        
        leng=-1
        
        for i in range(len(edges)):
            path=[]
            cur=i
            while edges[cur]>=0:
                path.append(cur)
                next = edges[cur]
                edges[cur] = -1   # mark as visited
                cur=next
            if cur in path:  # cycle found
                leng=max(leng,len(path)-path.index(cur))
        return leng

            

        return leng if leng!=0 else -1
        