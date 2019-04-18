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
