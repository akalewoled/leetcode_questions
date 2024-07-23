class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        a=0
        b=0
        costs.sort(key=lambda x: x[0]- x[1])
       
        for _ in range(n//2):
            val=costs.pop(0)
            a+=val[0]
        for _ in range(n//2):
            val=costs.pop(0)
            b+=val[1]
        return a+b
