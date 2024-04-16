class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ref={'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
        #lets calculate the prefix sum 
        presum=[0]
        for i in range(len(words)):
            curr=0
            if words[i][0] in ref and words[i][-1] in ref:
                curr=1
            presum.append(presum[-1]+curr)
        
        #lets answer for the queries 
      
        final=[]
        for j in queries:
            final.append(presum[j[1]+1]-presum[j[0]])
        return final
