class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(n+1)}
        for a,b in redEdges :graph[a].append((b,"r"))
        for a,b in blueEdges: graph[a].append((b,"b"))

        ans=[-1]*n
        q=[[0,0,None]]
        visited=set()
        while q:
            curr,dist,prev=q.pop(0)
            visited.add((curr, prev))
            if ans[curr]==-1:
                ans[curr]=dist
            for bro,road in graph[curr]:
                if (bro,road) not in visited and road!=prev:
                    q.append([bro,dist+1,road])
        return ans
