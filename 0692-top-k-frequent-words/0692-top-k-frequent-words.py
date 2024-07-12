class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        final=collections.Counter(words)
        h=[(-freq, item) for item,freq in final.items()]
        heapq.heapify(h)
        return [ heapq.heappop(h)[1] for _ in range(k)]
    #time klogn
    #space o(n)