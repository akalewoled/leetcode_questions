class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        onepick=numOnes-k
        if onepick >= 0:
            return k
        else:
            zeropick= numZeros +onepick
            if zeropick >= 0 :
                return numOnes 
            else:
                return numOnes +zeropick
        