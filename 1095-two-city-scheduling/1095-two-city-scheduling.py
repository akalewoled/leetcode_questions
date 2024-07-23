class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        a=n/2
        b=n/2
        costs.sort(key=lambda x: abs(x[0]- x[1]),reverse=True)
        final=0
       
        for i in costs:
            if i[0]<=i[1] and a>0 or b==0:
                final+=i[0]
                a-=1
            elif i[1] <i[0] and b>0 or a==0:
                final+=i[1]
                b-=1
        return final