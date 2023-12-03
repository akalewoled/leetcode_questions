class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                left=  flowerbed[i+1]==0 if i<len(flowerbed)-1 else flowerbed[i]==0  
                right=(i==0) or flowerbed[i-1]==0
                if left and right:
                    flowerbed[i]=1
                    n-=1
        print(flowerbed)
        return n<=0