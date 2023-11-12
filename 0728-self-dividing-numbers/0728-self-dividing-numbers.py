class Solution:
    def selfDividingNumbers(self, l: int, r: int) -> List[int]:
        final=[]
        for i in range(l,r+1):
            booli=True
            z=list(str(i).strip())
            for j in z:
                j=int(j)
                if j==0:
                    booli=False
                    break
                if i%j!=0:
                    booli=False
                    break
            if booli:
                final.append(i)
        return final

        