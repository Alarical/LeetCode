#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:53:55 2019

@author: alaric
"""

# 279. Perfect Squares            
class Solution:
    def numSquares1(self, n: int) -> int:
        # TLE
        import math
        n = 12
        dp = [ float('inf') for _ in range(n+1)]
        m = int(math.sqrt(n))
        for i in range(1,m+1):
            dp[i*i] = 1
        for i in range(1,m+1):
            for j in range(i*i , n+1):
                dp[j] = min(dp[j] , dp[j-i*i]+1)
        return dp[-1]
    
    def numSquares2(self, n: int) -> int: 
        import math
        squ_list = [ i*i for i in range(1,int(math.sqrt(n))+1)]
        count = 0
        cur_visited = [n]
        while cur_visited:
            count += 1
            next_visited = set()
            for cur in cur_visited:
                for num in squ_list:
                    if cur == num:
                        return count
                    if cur < num:
                        break
                    next_visited.add(cur - num)
            cur_visited = next_visited
        return count

  
    def numSquares3(self, n: int) -> int:
        queue = [[n,0]]
        visited = [False for _ in range(n+1)]
        visited[n] = True
        
        while any(queue):
            num,step = queue.pop(0)
            i = 1
            temp_num = num-i**2
            while temp_num>=0:
                if temp_num == 0:
                    return step+1
                if not visited[temp_num]:
                    queue.append([temp_num , step+1])
                    visited[temp_num] = True
                i+=1
                temp_num = num-i**2
        