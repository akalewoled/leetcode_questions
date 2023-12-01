class Solution:
    # we multiply the number up to n-1 and store at  n
    # then multiply it with the multipication of number  after n 
    # <********************* ->n
    # multiplies with         *n<-*******************
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng=len(nums)
        left=[1]*leng
        right=[1]*leng

        for i in range(1,leng):
            
            left[i]=nums[i-1]*left[i-1]
            
            j=leng-1-i
            right[j]=right[j+1]*nums[j+1]
        for i in range(len(left)):
            left[i]*=right[i]
        return left 



        
        