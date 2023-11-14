class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r=0,0
        final=[]
        while l<len(word1) and r<len(word2):
            final.append(word1[l])
            final.append(word2[r])
            l+=1
            r+=1
        if l<len(word1):
            final.append(word1[l:])
        elif r<len(word2):
            final.append(word2[r:])
        return "".join(final)