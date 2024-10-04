class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(source,dest,visited):
            if source not in mapping and dest not in  mapping: return -1
            if dest in mapping[source] : return mapping [source][dest]
            
            visited.append(source)

            for  nxt  in mapping[source]:
                if nxt not in visited:
                    temp=dfs(nxt,dest,visited)
                    if temp ==-1:continue
                    return mapping[source][nxt] * temp
            
            return -1
        #lets make the vector array consisting the number and 
        mapping=collections.defaultdict(dict)
        for i in range(len(equations)):
            source=equations[i][0]
            dest=equations[i][1]
            mapping[source][dest]=values[i]
            mapping[dest][source]=1/values[i]
        print(mapping)
        final=[]
        for s,r in queries :
            final.append(dfs(s,r,[]))
        return final
        

        
        