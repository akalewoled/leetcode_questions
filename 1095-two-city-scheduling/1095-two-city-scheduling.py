class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        costs.sort(key =lambda x: x[0]-x[1])
        a=0
        b=0
        for i in range(n//2):
            a+=costs[i][0]
        for i in range(n//2,n):
            b+=costs[i][1]
        return a+b
