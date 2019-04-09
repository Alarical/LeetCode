#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:04:34 2019

@author: alaric
"""

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left , right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return dfs(left.left , right.right) or dfs(left.right, right.left)
        
        if root == None:
            return True
        return dfs(root.left ,root.right)
        
       
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root , root]
        while any(queue):
            t1 = queue.pop()
            t2 = queue.pop()
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True