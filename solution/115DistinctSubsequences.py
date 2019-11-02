class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                # T是空，S不为空
                if j == 0:
                    dp[i][j] = 1
                    continue
                # j > 0 , S为空，T不为空
                if i == 0 :
                    dp[i][j] = 0
                    continue
                # i>0 j >0
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[m][n]
