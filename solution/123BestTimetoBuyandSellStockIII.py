class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        front = []
        back = []
        res,temp = 0,0
        Min = prices[0]
        Max = prices[-1]
        for num in prices:
            Min = min(num,Min)
            temp = max(temp , num-Min)
            front.append(temp)

        for num in prices[::-1]:
            Max = max(Max,num)
            back.append(Max-num)
        back = back[::-1]
        for i in range(len(prices)):
             res = max(res , front[i]+back[i] )
        return res

#dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [ [ [0] * 2 for _ in range(3) ] for _ in range(n) ]
        for i in range(n):
            for k in range(1,3):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0] , dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1] , dp[i-1][k-1][0] - prices[i])
        return dp[n-1][2][0]



