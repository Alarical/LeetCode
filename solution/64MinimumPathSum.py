#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:20:29 2019

@author: alaric
"""

class Solution(object):
    # 86ms 36.58%
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """ 
        m = len(grid)
        n = len(grid[0])
        dp = [[0]* n for _ in range(m)]
        for j in range(n):
            dp[0][j] = (dp[0][j-1] if j>=1 else 0) + grid[0][j]
        for i in range(m):
            dp[i][0] = (dp[i-1][0] if i>=1 else 0) + grid[i][0]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j] , dp[i][j-1] ) + grid[i][j]
        return dp[-1][-1]