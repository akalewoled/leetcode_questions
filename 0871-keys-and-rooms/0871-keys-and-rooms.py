class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[0 for _ in range(len(rooms ))]
     
        
        queue=[0]

        checked=[0]

        while queue:
            curr=queue.pop(0)
            visited[curr]=1
            for i in rooms[curr]:
                if i not in checked:
                    checked.append(i)
                    queue.append(i)
        return sum(visited)==len(visited)
