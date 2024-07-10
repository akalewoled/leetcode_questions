class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[]
        for  p in piles:
            heapq.heappush(heap,-p)
        for _ in range(k):
            current= -heapq.heappop(heap)
            
            current -= current //2
            heapq.heappush(heap,-current)
        return -sum(heap)