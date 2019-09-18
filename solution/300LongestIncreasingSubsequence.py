#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 00:29:30 2019

@author: alaric
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            temp = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    temp = max(temp , dp[j])
            dp[i] = temp+1
            res = max(res,dp[i])
        return res
                
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarysearch( s , num):
            l , r = 0 , len(s)-1
            while l <= r:
                m = int((l+r)/2)
                if s[m] == num:
                    return m
                elif s[m] > num:
                    r = m-1
                else:
                    l = m+1
            return l
            
        if len(nums) == 0 :
            return 0
        solution = [nums[0]]
        
        for i in range(len(nums)):
            if nums[i] > solution[-1]:
                solution.append(nums[i])
            else:
                index = binarysearch(solution , nums[i])
                solution[index] = nums[i]
        return len(solution)
                