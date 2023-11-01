class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        presum=[0]
        for i in nums:
            presum.append(i+presum[-1])
        presum.pop(0)
        check={0:1}
        res=0
        for i in presum:
            comp=i%k
            if comp in check:
                res+=check[comp]
                check[comp]+=1
            else:
                check[comp]=1
        return res