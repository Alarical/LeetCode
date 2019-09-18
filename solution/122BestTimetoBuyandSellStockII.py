class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        res = 0
        last = prices[0]
        for num in prices:
            last = min(last,num)
            if num > last:
                res += num-last
                last = num
        return res  