class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices = [7,1,5,3,6,4]
        if len(prices) == 0:
            return 0
        res = 0
        Min = prices[0]
        for num in prices:
            Min = min(num,Min)
            res = max(res , num-Min)
        return res