class NumArray(object):
    
    def __init__(self, nums):
        self.pre_sum=[0]
   
        for i in range(len(nums)):
            self.pre_sum.append(self.pre_sum[-1]+nums[i])
        print(self.pre_sum,"/n")
        

    def sumRange(self, l, r):
        
        return self.pre_sum[r+1]-self.pre_sum[l]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)