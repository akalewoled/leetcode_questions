class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        #intiate two arrayes 
        left=[]
        right=[]

        i,j= 0 , len(costs)-1
        ans=0
        while k:
            while len(left)<candidates and i <=j:
                heappush(left,costs[i])
                i+=1
            while len(right) < candidates and i <= j:
                heappush(right,costs[j])
                j-=1
            a=left[0] if left else float ('inf')
            b=right[0] if right else float('inf')

            if a<=b:
                ans+=heappop(left)
            else:
                ans+=heappop(right)
            k-=1
        return ans
