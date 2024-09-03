class Solution:  

    def maxProduct(self, words: List[str]) -> int:
        final=0
        words_in_binary=[0 ] * len(words)
        for i  in range(len(words)):
            mask=0
            for j in words[i]:
                index=ord(j)-ord("a")
                mask |= int(2**index)
            words_in_binary[i]=mask
            for k in range(i):
                if words_in_binary[k] & words_in_binary[i] ==0:
                    final=max(final,len(words[k]) * len(words[i]))
        return final
