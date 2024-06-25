class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        
        graph={ i:[] for i in range(n)}
        for course,pre in edges:
            graph[pre].append(course)
        visited = [0 for _ in range(n)]
        pvisited=[0 for _ in range(n)]

        #lets run bfs and check if we can complete all the nodes
        def  checkcircle(node: int) ->bool:
            if pvisited[node] == 1:
                return True
            visited[node]=1
            pvisited[node]=1
            for item in graph[node]:
                
                if visited[item]==0 :
                    if checkcircle(item) == True:
                        return True
                elif pvisited[item]==1:
                    return True
            pvisited[node]=0
            return False
            
            
        for item in graph:
            if  visited[item] ==0 :
                if checkcircle(item):#if there is a loop
                    return False
        return True # if there doesnt exist a loop nomatter the entry 
            
                
            
            