class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        relations=defaultdict(list)
        incoming =[ 0 for _ in range(numCourses)]

        
        for to,pre in prerequisites:
            relations[pre].append(to)
            incoming[to] += 1
        # fined sorce nodes
        q =deque()

        for i in range(numCourses):
            if incoming[i]==0:
                q.append(i)
        #bfs 
        orderd=[]
        while q:
            child=q.popleft()
            orderd.append(child)
            for dependant in relations[child]:
                incoming[dependant]-=1
                if incoming[dependant] ==0:
                    q.append(dependant)
        return orderd if len(orderd) ==numCourses else []