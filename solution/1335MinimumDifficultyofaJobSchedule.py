class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = [ [ float('inf') ] * (d+1)  for _ in range(n+1) ]
        dp[0][0] = 0
        for i in range(1 , n+1):
            for k in range(1 , d+1):
                md = 0
                for j in range(i-1 , k-2 , -1):
                    md = max(md , jobDifficulty[j])
                    dp[i][k] = min(dp[i][k] , dp[j][k-1] + md)

        return -1 if dp[n][d] == float('inf') else dp[n][d]
                    