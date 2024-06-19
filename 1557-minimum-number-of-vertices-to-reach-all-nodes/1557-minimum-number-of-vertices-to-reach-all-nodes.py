class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(n)}
        
        for start,end in edges:
            graph[end].append(start)
            
        final=[]
        for i in graph:
            if graph[i]==[]:
                final.append(i)
        return final