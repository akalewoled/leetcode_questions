class Solution:
    def minProcessingTime(self, p: List[int], t: List[int]) -> int:
        p.sort()
        t.sort()
        final=0
        for i in range(len(p)):
            if len(t)<4:break
            t1=t.pop()
            t2=t.pop()
            t3=t.pop()
            t4=t.pop()
            time=max(t1,t2,t3,t4)
            final=max(time+p[i],final)
        return final
        