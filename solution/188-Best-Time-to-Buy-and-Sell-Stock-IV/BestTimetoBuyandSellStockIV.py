class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        prices = [3,2,6,5,0,3]
        k = 2       
        n = len(prices)
        res = 0
        if k >= n//2:
            for i in range(1,n):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res
        
        mustSell = [[0]* (k+1) for _ in range(n+1) ]
        globalBest = [[0]* (k+1) for _ in range(n+1) ]

        for i in range(1,n):
            profit = prices[i] - prices[i-1]
            for j in range(1,k+1):
                mustSell[i][j] = max( globalBest[i-1][j-1] + max(profit , 0) , mustSell[i-1][j]+profit )
                globalBest[i][j] = max(mustSell[i][j] , globalBest[i-1][j]) 
        
        return globalBest[n-1][k]