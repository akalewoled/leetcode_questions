class Solution:
    def tribonacci(self, n: int) -> int:
        final={0:0,1:1,2:1}
        if n<3:
            return final[n]
        num=0
        for i in range(3,n+1):
            num=final[i-3]+final[i-2]+final[i-1]
            final[i]=num

        return num 

        