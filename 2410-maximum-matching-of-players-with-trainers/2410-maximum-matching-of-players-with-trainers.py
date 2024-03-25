class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        p.sort()
        t.sort()
        i=j=0 
        match=0

        while i<len(p) and j <len(t):
            if p[i]>t[j]:
                j+=1
            else:
                match+=1
                i+=1
                j+=1
        return match


