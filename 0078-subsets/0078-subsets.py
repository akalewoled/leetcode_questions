class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final=[]
        
        subset=[]
        def  find_sub_sets(i):
            #base case 
            
            if i >= len(nums):
                final.append(subset.copy())
                return
            #left dfs
            subset.append(nums[i])
            find_sub_sets(i+1)
            
            subset.pop()
            find_sub_sets(i+1)
            
        find_sub_sets(0)
        return final
            
            
            
    
        