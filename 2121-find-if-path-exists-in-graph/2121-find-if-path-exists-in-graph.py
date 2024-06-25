class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, final: int) -> bool:

        graph={i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def checkpath(node,visited):
            if node ==final:
                return True
            visited.add(node)
            for item in graph[node]:
                if item not in visited:
                    if checkpath(item,visited):
                        return True
            return False

        
        return checkpath(source,set())