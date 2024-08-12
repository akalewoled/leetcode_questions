class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        avalible=[room for room in range(n)]
        taked=[]
        heapify(avalible)
        final=[0] *n

        meetings.sort(key=lambda x :x[0])


        for start,finsh in meetings:
            
            while taked and taked[0][0] <=start:
                lastend ,room = heappop(taked)
                heappush(avalible,room)
            if avalible:
                room=heappop(avalible)
                heappush(taked,[finsh,room])
            else:
                end,room=heappop(taked)
                newend=end+(finsh-start)
                heappush(taked,[newend,room])
            final[room]+=1
            
        maxi=max(final)
        return final.index(maxi)


        