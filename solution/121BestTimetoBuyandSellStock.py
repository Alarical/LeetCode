class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #prices = [7,1,5,3,6,4]
        if len(prices) == 0:
            return 0
        res = 0
        Min = prices[0]
        for num in prices:
            Min = min(num,Min)
            res = max(res , num-Min)
        return res

#dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp_0 = 0
        dp_1 = -prices[0]
        for i in range(len(prices)):
            dp_0 = max(dp_0 , dp_1 + prices[i])
            dp_1 = max(dp_1 , -prices[i])
        return dp_0