from heapq import heappop,heappush
class Solution:
    def kSmallestPairs(self, a: List[int], b: List[int], k: int) -> List[List[int]]:
        m,n=len(a),len(b)
        if not m or not n:return []
        final=[]
        h=[(a[0]+b[0],(0,0))]
        visited=set()
        for _ in range(min(k,m*n)):
            val,(i,j)=heappop(h)
            final.append([a[i],b[j]])

            if i+1 <m and (i+1,j) not in visited:
                heappush(h,(a[i+1]+b[j],(i+1,j)))
                visited.add((i+1,j))
            if j+1 <n and (i,j+1) not in visited:
                heappush(h,(a[i]+b[j+1],(i,j+1)))
                visited.add((i,j+1))
        return final
