class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n, final, G = len(bombs), 0, defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if bombs[i][2]**2 >= (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2:
                    G[i] += [j]#bomb i can detonate bombj
        
        def dfs(node, visited):#following the trail of bomb i 
            for child in G[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            final = max(final, len(visited))
        return final
