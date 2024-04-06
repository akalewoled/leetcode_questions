class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        presum=[0]
        check={0:1}
        for i in nums:
            tempo=i+presum[-1]
            presum.append(tempo)
            rem=tempo%k
            check[rem]=1+check.get(rem,0)
        final=0
        for i in check:
            if check[i]>1:
                temporary=check[i]*(check[i]-1)//2
                final+=temporary
        return final
    #time  O(n)*O(m)
       
    