class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [ [0]*2 for _ in range(n+1)]
        for i in range(n+1):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -float('inf')
                continue
            dp[i][0] = max(dp[i-1][0] , dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1] , dp[i-1][0]-prices[i-1]-fee)
        return dp[n][0]
