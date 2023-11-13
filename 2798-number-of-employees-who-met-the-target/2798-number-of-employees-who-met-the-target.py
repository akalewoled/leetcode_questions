class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        k=0
        for i in hours :
            if i>= target:
                k+=1
        return k