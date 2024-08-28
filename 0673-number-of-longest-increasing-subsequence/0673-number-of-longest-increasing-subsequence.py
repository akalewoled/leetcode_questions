class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        cache=[1 for i in range(len(nums))]
        howmany=[1 for i in range(len(nums))]
        res={}

        for i in range(len(nums)-1,-1,-1):
            maxlen=1
            times=1
            for j in range(i,len(nums)):
                if nums[j]>nums[i]:
                    templen=cache[j]+1
                    if templen> maxlen:
                        maxlen=templen
                        times=howmany[j]
                    elif templen == maxlen:
                        times+=howmany[j]
                    cache[i]=max(cache[i],cache[j]+1)
                    
            howmany[i]=max(howmany[i],times)
            res[cache[i]]= howmany[i]+res.get(cache[i],0)

        final=max(res)
        return res[final]
