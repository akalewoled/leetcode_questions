class Solution:

    def __init__(self, w: List[int]):
        self.array=w
        
        presum=[0]
        for i in range(len(w)):
            presum.append(presum[-1]+w[i])
        presum.pop(0)
        self.searcharray=presum
        self.n=presum[-1]

    def pickIndex(self) -> int:
        randomnumber=random.uniform(0,self.n)

        left=0
        right=len(self.array)-1

        while left<right:
            mid=left+(right-left)//2
            if randomnumber>self.searcharray[mid]:
                left=mid+1
            else:
                right=mid

        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()