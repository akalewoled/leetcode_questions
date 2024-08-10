
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m=len(s1)
        n=len(s2)
        memo=memo = [[0 for _ in range(n +1 )] for _ in range(m+1 )]

        for i in range (1,m+1):
            for j in range(1, n+1):
                if s1[i-1]==s2[j-1]:
                    last=memo[i-1][j-1]
                    memo[i][j]=last+1
                else:
                    lastx=memo[i][j-1]
                    lasty=memo[i-1][j]
                    memo[i][j]=max(lastx,lasty)
        return memo[m][n]
