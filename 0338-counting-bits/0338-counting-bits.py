class Solution:
    def countBits(self, n: int) -> List[int]:
        def convertToBit(a):
            final=0
            while a>0:
                final+=a%2
                a=a//2
            return final
        res=[]
        for i in range(n+1):
            res.append(convertToBit (i))
        return res