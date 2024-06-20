class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph={i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited={source}
        stack=[source]
        while stack:
            n=stack.pop()
            if n== destination: return True
            for edge in graph.get(n,[]):
                if edge not in visited:
                    visited.add(edge)
                    stack.append(edge)
        return False