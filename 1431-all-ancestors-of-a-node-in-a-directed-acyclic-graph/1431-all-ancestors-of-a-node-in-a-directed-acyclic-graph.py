from sortedcontainers import SortedSet

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        #create the relations in a dict
        relations=defaultdict(list)
        incoming=[0 for _ in range(n)]

        for source,dist in edges :
            relations[source].append(dist)
            incoming[dist]+=1
        final=[set() for _ in range(n)]
        # find and start from source nodes 
        q =deque()
        for i in range(n):
            if incoming[i]==0:
                q.append(i)
        #do a bfs byrecoding the path and appending what we have on that field 
        seen=set()
        while q:
            child=q.popleft()
            for dist in relations[child]:
                final[dist]=final[dist] | {child} | final[child]
                incoming[dist]-=1
                if incoming[dist]==0:
                    q.append(dist)
        for i in range(len(final)):
            final[i]=sorted(list(final[i]))
                   
        return final
        
        