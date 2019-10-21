class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp_0 = 0
        dp_1 = -prices[0]
        dp_last = 0
        for i in range(len(prices)):
            temp = dp_0
            dp_0 = max(dp_0 , dp_1 + prices[i])
            dp_1 = max(dp_1 , dp_last - prices[i])
            dp_last = temp
        return dp_0