class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        second=score.copy()
        second.sort(reverse=True)
        final=[]
        for i in score:
            k=second.index(i)
            if k==0:
                final.append("Gold Medal",)
            elif k==1:
                final.append("Silver Medal")
            elif k==2:
                final.append("Bronze Medal")
            else:
                final.append(str(k+1))
        return final
