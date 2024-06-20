class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph={i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited=[]
        
        
        def dfs(node, end, seen):
            if node == destination:
                return True
            if node in seen:
                return False
            
            seen.add(node)
            for n in graph[node]:
                if dfs(n, destination, seen):
                    return True
                
            return False
        
        seen = set()    
        return dfs(source, destination, seen)
                   