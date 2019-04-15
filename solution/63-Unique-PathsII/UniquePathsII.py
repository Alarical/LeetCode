class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [ [0] * n for i in range(m) ]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = -1

        dp[0][0] = 1
        for i in range(1,m):
            if dp[i][0] != -1:
                dp[i][0] = dp[i-1][0]
            else:
                break
        for i in range(1,n):
            if dp[0][i] != -1:
                dp[0][i] = dp[0][i-1] 
            else:
                break

        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j] != -1:
                    dp[i][j] = (dp[i-1][j] if dp[i-1][j] != -1 else 0) + (dp[i][j-1] if dp[i][j-1] != -1 else 0)

        return dp[m-1][n-1] if dp[m-1][n-1] != -1 else 0