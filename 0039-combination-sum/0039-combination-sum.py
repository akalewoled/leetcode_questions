class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.final=[]
        def backtrack(index,array,total):
            if total ==target:
                self.final.append(array.copy())
                return
            if index>=len(candidates)  or total >target:
                return
            
            array.append(candidates[index])
            backtrack(index,array,total+candidates[index])
            array.pop()
            
            backtrack( index+1,array,total)
            
        backtrack(0,[],0)
        
        return self.final
         