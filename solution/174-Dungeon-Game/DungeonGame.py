class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        #dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[m][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                # temp 表示要往 右或下 走，最少需要的生命值 
                temp = min( (dp[i+1][j]) , (dp[i][j+1]))-dungeon[i][j]
                # 如果temp > 1,则为temp; 如果temp < 1, 因为当前点骑士必须最小具有1点生命值，
                # 所以dp[i][j] = 1
                dp[i][j] = max(temp, 1)
        return dp[0][0]