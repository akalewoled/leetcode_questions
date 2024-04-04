class Solution:
    def maxConsecutiveAnswers(self, ak: str, k: int) -> int:
        
        maxi=l=0
        rangee={'T':0,'F':0}
        for r in range(len(ak)):
            rangee[ak[r]]+=1
            maxi=max(rangee[ak[r]],maxi)
            if r+1-l > maxi+k:
                #we have a list of an array which have two diffrent item that we can't make them consquitve using k operations
                rangee[ak[l]]-=1
                l+=1
        return len(ak)-l

