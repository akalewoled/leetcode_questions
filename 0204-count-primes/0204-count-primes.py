class Solution:
    def countPrimes(self, n: int) -> int:
        reg=[1] *n
        for i in range(2,int(n**0.5)+1,1):
            if reg[i] ==1:
                for j in range(i*i,n,i):
                    reg[j]=0
        final=0
        for i in range(2,n):
            if reg[i]==1:
                final+=1
        return final

