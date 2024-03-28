class Solution:
    def totalFruit(self, array: List[int]) -> int:
        l=maxlen=0
        basket={}
        for r in range(len(array)):
         
            basket[array[r]]=1+basket.get(array[r],0)

            while l<=r and len(basket)>2:
                basket[array[l]]-=1
                if basket[array[l]]==0:
                    basket.pop(array[l])
                l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen