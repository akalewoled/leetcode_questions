
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index ,item in enumerate( tasks):
            item.append(index)
        tasks.sort(key= lambda t: t[0])
       
        final,h=[],[]
        i,time=0,tasks[0][0]

        while h or i< len(tasks):
            while  i < len(tasks) and time >= tasks[i][0] :
                heapq.heappush(h,[tasks[i][1],tasks[i][2]])
                i+=1
            if not h :
                time=tasks[i][0]
            else:
                times,index=heapq.heappop(h)
                time+=times
                final.append(index)
        return final
        

