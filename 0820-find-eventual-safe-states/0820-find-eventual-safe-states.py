class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
         #revesing the relations and tracking incoming changes
        n=len(graph)
        pathrev=defaultdict(list)
        incoming=[0 for _ in range(n)]
        for source in range(n):
            for dist in graph[source]:
                pathrev[dist].append(source)
                incoming[source]+=1
        #taking naturally safe nodes
        #note that terminal nodes are safe
        safe =deque()

        for i in range(n):
            if incoming[i]==0:
                safe.append(i)
        final=[]
        print(pathrev)
        # do  a Bfs
        while safe:
            cursafe=safe.popleft()
            final.append(cursafe)
            for items in pathrev[cursafe]:
                incoming[items]-=1
                if incoming[items] == 0:
                    safe.append(items)

        return sorted(final)