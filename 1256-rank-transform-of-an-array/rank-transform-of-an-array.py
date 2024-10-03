class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank={}
        arrd=sorted(set(arr))
        for i in range(len(arrd)):
            rank[arrd[i]]=i+1

        final=[]
        for i in arr :
            
            final.append(rank[i])      
        return final