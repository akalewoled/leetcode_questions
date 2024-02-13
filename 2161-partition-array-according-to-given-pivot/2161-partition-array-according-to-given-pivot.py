class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        equal=[]
        greter=[]
        for i in nums:
            if i<pivot:
                less.append(i)
            elif i==pivot:
                equal.append(i)
            elif i> pivot :
                greter.append(i)
        return less+equal+greter    