class Solution:
    
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        maxSum = lsum = sum(cardPoints[:k])
        r = len(cardPoints) - 1
        rsum = 0
        for l in range(k-1,-1,-1):
            lsum -= cardPoints[l]
            rsum += cardPoints[r]
            r-=1
            maxSum = max(maxSum, rsum+lsum)
        return maxSum

        