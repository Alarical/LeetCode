#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:16:04 2019

@author: alaric
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        if len(nums) == 0:
            return 0
        cursum = 0
        res = -sys.maxsize-1
        for num in nums:
            cursum = max(cursum+num ,num)    
            res = max(res,cursum)
        return res