class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final=[]
        if len(word2)>len(word1):
            for i in range(len(word1)):
                final.append(word1[i])
                final.append(word2[i])
            final= "".join(final)+"".join(word2[i+1:]) if i<len(word2)-1 else "".join(final)
        else:
            for i in range(len(word2)):
                final.append(word1[i])
                final.append(word2[i])
            final="".join(final)+"".join(word1[i+1:]) if i<len(word1)-1 else "".join(final)
        return final
            
      