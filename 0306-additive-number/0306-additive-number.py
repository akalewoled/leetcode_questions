class Solution:
    
    def isAdditiveNumber(self, num: str) -> bool:
        
        for  i in range(1,len(num)):
            for j in range(i+1,len(num)):
                first=num[:i]
                second =num[i:j]
                remaning =num[j:]
                if (first.startswith('0') and first != '0') or (second.startswith('0') and second !='0'):
                    continue
                
                
                while remaning:
                    next1=str(int(first)+int(second))
                    if not remaning.startswith(next1):
                             break
                    first=second
                    second=next1
                    remaning=remaning[len(next1):]
                if not remaning : return True
        return False
    