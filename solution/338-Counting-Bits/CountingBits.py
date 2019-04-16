#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:42:27 2019

@author: alaric
"""

class Solution(object):
    
    # 164 ms 17.34% Brute Force O(n*sizeof(integer))
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            temp = 0
            while i:
                temp += i&1
                i >>= 1
            res.append(temp)
            
    # 72ms 96% dp O(n)     
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0,1,1]
        if num <= 2:
            return res[:num+1]
        cur_2 = 2
        for i in range(3,num+1):
            if i < cur_2*2:
                res.append(res[cur_2] + res[i-cur_2])
            elif i > cur_2*2:
                cur_2 *= 2
                res.append(res[cur_2] + res[i-cur_2])
            else:
                res.append(1)
        return res