class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        answer=[amount+1] * (amount +1 ) 
        answer[0]=0

        for i in range(1,amount+1):
            for j in coins:
                if i -j >= 0:
                    answer[i]=min(answer[i],1+answer[i-j])
        return answer[-1] if answer[-1] != amount+1 else -1