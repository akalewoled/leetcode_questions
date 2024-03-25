class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=-1
        n=len(nums)
       
        for i in range (n-2,-1,-1):
            if nums[i]<nums[i+1]:
               
                # checking if there is elemnt who  break the declin the range
                # stores the index who break the decline 
                index=i
                minigreterindex=index+1
                for j in range(minigreterindex,n):# finding the element eho is greter than the problmatic index
                    
                    print(nums[j],nums[index])
                    if nums[j] > nums[index]  and nums[j] <= nums[minigreterindex]: #getting the value greter than i bu less than i+1
                        minigreterindex=j
                nums[index],nums[minigreterindex]=nums[minigreterindex],nums[index] # swapping hte elemnt with the greter element 
            
                l=i+1
                r=n-1
                while l<=r:# sorting but since we no it was decending order we reverse it to make it assending 
                    nums[l],nums[r]=nums[r],nums[l]
                    l+=1
                    r-=1
                
                break
                    
        if index==-1:
            l=0
            r=n-1
            while l<=r:# sorting but since we no it was decending order we reverse it to make it assending 
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1

        return nums
                

                
                
                    



        