class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1=sorted(nums)

        dict1={}
        for i in nums1:
            dict1[i]= 1+dict1.get(i,0)
        sumed=0
        presum={}
        for index,value in dict1.items():
            sumed+=value
            presum[index]=sumed
        print(dict1)
        print(presum)
        final=[]
        for i in nums:
            k=presum[i]-dict1[i]
            final.append(k)
        return final
            