class Solution:
    def minOperations(self, logs: List[str]) -> int:
       
        stack=[]
        for i in logs:
            print(i,stack)
            if i =="../" and len(stack)>=1:
                
                stack.pop()
            elif i=="./":
                continue
                
            elif i[-2]!="." :
                stack.append(i)
            
       
        return len(stack)