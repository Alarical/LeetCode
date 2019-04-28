#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 17:07:29 2018

@author: alaric
"""

from collections import Counter
# 347. Top K Frequent Elements
l = [1,1,1,1,7,7,3]
res = []
for k,v in Counter(l).most_common(2):
    res.append(k)
    
#46. Permutations
class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        nums = [1,2,3]
        res = []
        length = len(nums)
        def dfs(nums, i):
            if i == length:
                res.append(nums.copy())
            for j in range(i,length):
                nums[i] , nums[j] = nums[j] , nums[i]
                dfs(nums , i+1)
                nums[j] , nums[i] = nums[i] , nums[j]
        
        dfs(nums,0)
        
#47. Permutations II
class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        nums = [1,1,2]
        res = []
        length = len(nums)
        def dfs(nums, i):
            if i == length:
                if nums.copy() not in res:
                    res.append(nums.copy())
            for j in range(i,length):
                nums[i] , nums[j] = nums[j] , nums[i]
                dfs(nums , i+1)
                nums[j] , nums[i] = nums[i] , nums[j]
                
        def dfs(nn, cur, res):
            #print (nn,cur)
            if not nn :
                res.add(cur)
            else:
                for i in range(len(nn)):
                    dfs(nn[:i] + nn[i+1:], cur + (nn[i],), res)
    
        res = set()
        dfs(nums, (), res)
        
        
        dfs(nums,0)

        
#5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0] * len(s) for i in range(len(s))]
        ans = ""
        max_length = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if ans == "" or max_length < j - i + 1:
                        ans = s[i:j+1]
                        max_length = j - i + 1
        return ans


# 17. Letter Combinations of a Phone Number
# 考虑为空的情况
_map  = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
res = ['']
digits = '23'
for num in digits:
    res_length = len(res)
    print (num,len(res))
    for _ in range(res_length):
        temp = res.pop(0)
        for ch in _map[int(num)]:
            res.append(temp+ch)
    print (res)

# 39. Combination Sum
candidates = [2,3,6,7]
target = 7       

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        
        def dfs( res, target, candidates):
            if sum(res) == target:
                ans.append(res)
                return
            if sum(res) > target:
                return
            
            for i,val in enumerate(candidates):
                if sum(res)+val > target:   break
                dfs(res + [val] , target , candidates[i:] )
            
        
        dfs( [] , target, candidates)
        return ans
    
# 39. Combination Sum II
candidates = [10,1,2,7,6,1,5]
target = 8
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        
        def dfs( res, target, candidates):
            if (sum(res) == target) & (res not in ans):
                ans.append(res)
                return
            if sum(res) > target:
                return
            
            for i,val in enumerate(candidates):
                if sum(res)+val > target:   break
                dfs(res + [val] , target , candidates[i+1:] )
            
        
        dfs( [] , target, candidates)
        return ans


#216. Combination Sum III
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates = [i for i in range(1,10)]
        
        def dfs( res, k, n, candidates):
            if (len(res) > k) | (sum(res) > n) :
                return
            if (sum(res) == n) & (len(res) == k) :
                ans.append(res)
                return
            
            
            for i,val in enumerate(candidates):
                if (sum(res)+val > n) | (len(res) > k):   break
            
                dfs(res + [val] , k , n, candidates[i+1:] )
            
        
        dfs( [] , k, n, candidates)
        return ans

# 77. Combinations
n = 4
k = 2

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates = [i for i in range(1,n+1)]
        
        def dfs( res, k, candidates):
            if len(res) > k :
                return
            if len(res) == k :
                ans.append(res)
                return
            
            for i,val in enumerate(candidates):
                if len(res) > k:   break
            
                dfs(res + [val] , k , candidates[i+1:] )
            
        
        dfs( [] , k, candidates)
        return ans

# 55. Jump Game
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 暴力 超时
# =============================================================================
#         nums = [0,2,3]
#         ans = [False]*len(nums)
#         ans[0] = True
#         for i,val in enumerate(nums):
#             if ans[i] == True:
#                 for j in range(1,val+1):
#                     if i+j < len(nums):
#                         ans[i+j] = True
#         return ans[-1]     
# =============================================================================
     
# 49 Group Anagrams

strs = ["aa","ab","ba","abc","cba"]

dic = {}

for i in strs:
    temp = ''
    for j in sorted(i):
        temp += ''.join(j)
    if temp in dic.keys() :
        dic[temp].append(i)
    else:
        dic[temp] = [i]
        
print (list(dic.values()))

# 120ms solution
# =============================================================================
# result = {}
# for i in strs:
#     key = "".join(sorted(i))
#     if result.get(key):
#         result[key].append(i)
#     else:
#         result[key] = [i]
# return list(result.values())
# =============================================================================


#83 Remove Duplicates from Sorted List
# =============================================================================
# Example 1:
# 
# Input: 1->1->2
# Output: 1->2
# Example 2:
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# =============================================================================

m = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]


# 98. Validate Binary Search Tree
# 二叉搜索树 中序遍历一定有序递增 124ms 2.59%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        def inOrder(root):
            if root == None:
                return
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)
        
        if root == None:
            return True
        if (root.left == None) & (root.right == None):
            return True
        inOrder(root)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rty
        """
        def dfs(root,minValue,maxValue):
            if root == None:
                return True
            if ( root.val <= minValue ) | ( root.val >= maxValue ):
                return False
            return dfs(root.left, minValue , root.val) & dfs(root.right , root.val , maxValue)


        Max = sys.maxsize,
        Min = -sys.maxsize - 1
        return dfs(root,Min,Max)
        

#102. Binary Tree Level Order Traversal                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = [] 
        if root == None:
            return result
        
        queue = [root]

        while queue:
            level = []
            l = len(queue)
            for i in range(l):
                n = queue.pop(0)
                level.append(n.val)
    
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)

            result.append(level)

        return result

        def levelOrder(self, root):
                """
                :type root: TreeNode
                :rtype: List[List[int]]
                """
                result , level = [],[root]

                if root == None:
                    return result
                
                while level:
                    result.append([ node.val for node in level ])
                    # 用temp 重新复制level
                    temp = []
                    for node in level:
                        temp.extend([node.left, node.right])
                    level = [ node for node in temp if node ]

                return result


## 103. Binary Tree Zigzag Level Order Traversal
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result , level = [] , [root]
        if root == None:
            return result
        num = 1
        while level:
            if num % 2 == 0:
                result.append( [ node.val for node in level[::-1] ] )
            else:
                result.append( [ node.val for node in level ] )
            temp = []
            for node in level:
                temp.extend([ node.left , node.right ])
            level = [ node for node in temp if node] 
            num += 1
        return result


# 114. Flatten Binary Tree to Linked List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return 
        while root != None:
            if root.left != None:
                current = root.left
                while current.right != None:
                    current = current.right
                current.right = root.right
                root.right = root.left
                root.left = None
            root = root.right


#108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def binary(nums,left,right):
            if left > right:
                return
            mid = (right + left) // 2
            node = TreeNode(nums[mid])
            node.left =  binary(nums,left,mid-1)
            node.right = binary(nums,mid+1,right)

            return node
        root = binary(nums , 0 , len(nums) - 1 )
        return root


#109. Convert Sorted List to Binary Search Tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def binary(nums,left,right):
            if left > right:
                return
            mid = (right + left) // 2
            node = TreeNode(nums[mid])
            node.left =  binary(nums,left,mid-1)
            node.right = binary(nums,mid+1,right)

            return node

        if head == None:
            return    
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        root = binary(nums , 0 , len(nums) - 1 )
        return root

    def sortedListToBST(self, head):
            """
            :type head: ListNode
            :rtype: TreeNode
            """
            def binary(head,end):
                if head == end:
                    return 
                slow = head
                fast = head
                prev = None
                while fast != None & fast.next != None:
                    prev = slow
                    slow = slow.next
                    fast = fast.next.next
                root = TreeNode(slow)
                prev.next = None                   # prev is the node before root, set prev.next to None to cut off the 1st half linked list
                root.left =  binary(head, slow )
                root.right = binary(slow.next, end )

            return root

            if head == None:
                return head
            head = binary(head,None)
            return head



#5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        #  全0矩阵
        dp = [ [0] * len(s) for i in range(len(s)) ]
        maxlen = 0
        res = ''
        for i in range(len(s)):
            for j in range(i+1):
                dp[j][i] = s[j]== s[i] and ( i-j <= 2 or dp[j+1][i-1] )
                if dp[j][i]:
                    if i-j+1 > maxlen:
                        maxlen = i-j+1
                        res = s[j:i+1]
            #dp[i][i] = True
        return res

#53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        import sys
        Max = -sys.maxsize-1
        Sum = 0

        for i in nums:
            Sum = max(Sum+i , i)
            Max = max(Max,Sum)
        return Max

#62. Unique Paths
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        Min = min(m-1,n-1)
        res = 1
        temp = 1
        for i in range(m+n-2 , m+n-2-Min , -1):
            res *= i
        for i in range(1,Min+1):
            temp *= i
        
        res = int(res/temp)
        return res

        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [ [1] * n for i in range(m) ]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
 

#63. Unique Paths II
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


#64. Minimum Path Sum
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for i in range(0,m):
            for j in range(0,n):
                if i == 0 or j == 0:
                    grid[i][j] += grid[i-1][j] if i != 0 else 0  + grid[i][j-1] if j != 0 else 0
                else:
                    grid[i][j] += min( grid[i-1][j], grid[i][j-1] )

        return grid[m-1][n-1]


#72. Edit Distance
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m = len(word1)
        n = len(word2)

        dp = [ [0] * (n+1) for i in range(m+1) ]

        for i in range(m+1):
            dp[i][0] = i 
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min( dp[i-1][j-1] , min(dp[i][j-1],dp[i-1][j]) ) + 1

        return dp[m][n]  #dp[-1][-1]



#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        Min = prices[0]
        res = 0
        for num in prices:
            Min = min(Min , num)
            res = max(num - Min , res)
        return res


#122. Best Time to Buy and Sell Stock II

#120. Triangle
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #triangle = [ [2],[3,4],[6,5,7],[4,1,8,3]]
        for i in range(1,len(triangle)):
            length = len(triangle[i-1])
            for inx in range(len(triangle[i])):
                if (inx >=0 and inx < length) and (inx-1 >=0 and inx-1 < length):
                    triangle[i][inx] += min(triangle[i-1][inx] , triangle[i-1][inx-1])
                else:
                    if inx >= length:
                        triangle[i][inx] += triangle[i-1][inx-1]
                    else: 
                        triangle[i][inx] += triangle[i-1][inx]
                #triangle[i][inx] += min(triangle[i-1][inx] , triangle[i-1][inx-1])
        return min(triangle[-1])

#139. Word Break
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        s = 'leetcode'
        wordDict = ["leet", "code"]
        word = [ False for _ in range(len(s)+1)]
        word[0] = True
        for i in range(1,len(s)+1):
            for j in range(i-1,-1,-1):
                if word[j] and s[j:i] in wordDict:
                    word[i] = True
                    #print (i,j)
                    break
        return word[-1]
            
#152. Maximum Product Subarray
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#Input: [2,3,-2,4]
#Output: 6
        nums = [2,3,-2,-4]
        dp_min = [0 for _ in range(len(nums))]
        dp_max = [0 for _ in range(len(nums))]

        dp_min[0] , dp_max[0] = nums[0] , nums[0]
        Max = nums[0]
        
        for i in range( 1,len(nums) ):
            dp_min[i] = min ( min( dp_min[i-1]*nums[i] , dp_max[i-1]*nums[i]) , nums[i] )
            dp_max[i] = max ( max( dp_min[i-1]*nums[i] , dp_max[i-1]*nums[i]) , nums[i] )
            Max = max( Max, dp_max[i])
            print (Max)

#221. Maximal Square
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        matrix = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
        m = len(matrix)
        
        if m == 0 :
            return 0
        
        n = len(matrix[0])
        result = 0
        dp = [[0] * n for _ in range(m) ]
        for j in range(n):
            dp[0][j] = matrix[0][j]
            result = max(result,matrix[0][j])
        for i in range(m):
            dp[i][0] = matrix[i][0]
            result = max(result,matrix[i][0])
            
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 1:
                    dp[i][j] = 1
                    dp[i][j] = min(dp[i][j-1] , dp[i-1][j-1] , dp[i-1][j]) + 1
                    result = max(result,dp[i][j])
        return result * result

#263. Ugly Number
class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num = 14
        if num <= 0:
            return False
        for i in [2,3,5]:
            while num%i == 0:
                num = num/i
        return num == 1 

#264. Ugly Number II
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = 11
        if n == 1:
            return 1
        dp = [True]
        i = 2
        length = 1
        while n > SUM:
            flag = 0
            print (i)
            for num in [2,3,5]:
                if i % num == 0 :
                    temp = int(i/num)
                    if dp[temp-1] == True:
                        dp.append(True)
                        flag = 1
                        break
            if flag == 0:
                dp.append(False)
            SUM = sum(dp)
            print (length)
            i += 1
            print (i)
            print ('\n')
        print (i-1)
        
     def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        n= 11
        dp = [1]
        n2 ,n3, n5 = 0,0,0
        while n > 1:
            num2 , num3 , num5 = 2*dp[n2] , 3*dp[n3] ,5*dp[n5]
            umin = min(num2,num3,num5)
            dp.append(umin)
            if umin == num2:
                n2 += 1
            if umin == num3:
                n3 += 1
            if umin == num5:
                n5 += 1
            n -= 1
        return dp[-1]
        
        
# 92. Reverse Linked List II
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next
        cur = pre.next
        for i in range(m,n):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp

        return dummy.next      
        
# 54. Spiral Matrix        
class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        res = []
        if matrix == []:
            return res
        m = len(matrix)
        n = len(matrix[0])
        i , j = 0 ,0
        row_beg , row_end = 0 , m-1
        col_beg , col_end = 0 , n-1
        while row_beg <= row_end and col_beg <= col_end:
            for j in range(col_beg,col_end+1):
                res.append(matrix[row_beg][j])
            for i in range(row_beg+1,row_end+1):
                res.append(matrix[i][col_end])
            for j in range(col_end-1,col_beg-1,-1):
                if row_beg < row_end:
                    res.append(matrix[row_end][j])
            for i in range(row_end-1,row_beg,-1):
                if col_beg < col_end:
                    res.append(matrix[i][row_beg])
            row_beg += 1
            row_end -= 1
            col_beg += 1
            col_end -= 1
        return res        
        
#55. Jump Game        
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxreach = 0
        for i in range(len(nums)):
            if i > maxreach:
                return False
            maxreach = max(maxreach, i + nums[i])
            if maxreach >= len(nums)-1:
                return True        
        
#56. Merge Intervals        
class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':        
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        intervals.sort(key = lambda x: x.start)
        res = []
        for i in range(len(intervals)):
            if res == []:
                res.append(intervals[i])
            else:
                length = len(res)
                if res[length-1].start <= intervals[i].start and intervals[i].start <= res[length-1].end:
                    res[length-1].end = max(intervals[i].end,res[length-1].end)
                else:
                    res.append(intervals[i])
        return res       

# 75. Sort Colors
#Input: [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]   
class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = [2,0,2,1,1,0]
        nums = [2,0]
        left , right = 0 , len(nums)-1
        i=0
        while i < right+1 :
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[left]
                nums[left] = temp
                left += 1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[right]
                nums[right] = temp
                right -= 1
                i -= 1
            i+= 1
# =============================================================================
#             if i >= right:
#                 break
# =============================================================================
        
        
        
        
# 989. Add to Array-Form of Integer
A = [1,2] 
K = 3400
b = K//10
i = len(A)-1
res = []
while K != 0:
    flag = 0
    a = K%10
    b = K//10
    temp = A[i]+a
    if temp >= 10:
        flag = 1
        temp -= 10
    K = b + flag
    res.append(temp)
    i -= 1
    if i < 0:
        break
while K != 0:
    a = K%10
    b = K//10
    res.append(a)
    K = b
while i >= 0:
    res.append(A[i])
    i-=1
print (res[::-1])   

#1. Two Sum
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        nums = [3,3]
        save = nums.copy()
        target = 6
        nums.sort()
        i , j = 0 , len(nums)-1
        while i < j:
            if nums[i] + nums[j] == target:
                first = save.index(nums[i])
                last = save.index(nums[j])
                if first != last:
                    print (first , last)
                else:
                    save = save[first+1:]
                    last = save.index(nums[j])
                    print (first , first+1+last)
                break
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        
#15. 3Sum
class Solution:
    # -a = b + c
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        def twosum(nums , i , j , target ,res):
            while i < j :
                if nums[i] + nums[j] == target: 
                    res.append([nums[i] , nums[j] , -target])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1] : i+=1
                    while i < j and nums[j] == nums[j+1] : j-=1

                elif nums[i] + nums[j] < target:
                    i+=1
                else:
                    j-=1
        if len(nums) < 3:
            return []
                    
        nums = [-2, 0, 1, 2, 1, -4]
        nums.sort()
        res = []
        i , j = 0 , len(nums)-1
        for ind in range(len(nums)):
            if ind > 0 and nums[ind] == nums[ind-1]:
                continue
            else:
                twosum(nums , ind+1 , j , -nums[ind] , res)
        
# 考虑 a = b+c 的情况
        def twosum(nums , i , j , ind , target ,res):
            while i < j and i < ind:
                print (i,j,target,ind)
                if nums[i] + nums[j] == target: 
                    res.append([nums[i] , nums[j] , target])
                    i += 1
                    j -= 1
                    while i < j  and nums[i] == nums[i+1] : i-=1
                    while i < j  and nums[j] == nums[j-1] : j+=1
                elif nums[i] + nums[j] < target:
                    i+=1
                else:
                    j-=1
                if j == ind:
                    j -= 1
                    
        nums = [-2, 0, 1, 2, 1, -4]
        nums.sort()
        res = []
        i , j = 0 , len(nums)-1
        for ind in range(len(nums)):
            if ind > 0 and nums[ind] == nums[ind-1]:
                continue
            else:
                twosum(nums , i , j , ind, nums[ind] , res)                
        # 上述只处理了 对某个元素 其 两边相加 = 它的情况

#78. Subsets
class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        nums = [1,2,3]
        res = [[]]
        for i in nums:
            for temp in res.copy():
                x = temp.copy()
                x.append(i)
                res.append(x)
            #break
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        nums = [1,2,3]
        res = []
        temp = []
        dfs(nums, temp , res , 0)
        
        def dfs(nums, temp , res , j):
            res.append(temp.copy())
            for i in range(j,len(nums)):
                temp.append(nums[i])
                dfs(nums, temp , res , i+1)
                temp.remove(nums[i])

        
# 993. Cousins in Binary Tree
class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        def f(n):
            if(n==1):
                return 1
            else:
                return (1+2*f(n-1))

        
        root = [1,2,3,'null',4,'null',5]
        x = 5 
        y = 4
        if len(root) <= 3:
            return False
        ind1 = root.index(x)
        ind2 = root.index(y)
        Min = min(ind1,ind2)+1
        temp = 0
        N = 1
        while 1:
            temp = f(N)
            if temp > Min:
                break
            N += 1
            
        if f(N-1) < ind1+1 and f(N-1) < ind2+1:
            if max(ind1,ind2) - min(ind1,ind2) >= (f(N) - f(N-1))/2:
                return True
        
        input = [1,2,null]
        class TreeNode:
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None
       
        
        temp = TreeNode(0)
        temp.left = None
        temp.right = None
        four = TreeNode(4)
        second.left = None
        second.right = None
        second = TreeNode(2)
        second.left = None
        second.right = four
        thr = TreeNode(3)
        thr.left = None
        thr.right = None
        root = TreeNode(1)
        
        root.left = second
        root.right = thr
        
        result = [] 
        if root == None:
            return result
        
        queue = [root]

        while queue:
            level = []
            l = len(queue)
            for i in range(l):
                n = queue.pop(0)
                level.append(n.val)
                if n.val == 0:
                    continue
                if n.left:
                    queue.append(n.left)
                else:
                    queue.append(temp)
                if n.right:
                    queue.append(n.right)
                else:
                    queue.append(temp)
                    
            result.append(level)
            
        
# 112. Path Sum        
class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        sum = 22
        
        
        def dfs(root ,sum):
            if root == None:
                return False
            if root.left == None and root.right == None:
                return root.val == sum
        
            return dfs(root.left , sum - root.val) or dfs(root.right , sum - root.val)
        
# 113. Path Sum II    
class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        temp  =[]
        res = []
        def dfs(root ,temp , ans):
            if root == None:
                return 
            #print (temp , root.val  , ans)
            if root.left == None and root.right == None:
                if  root.val == ans:
                    res.append(temp + [root.val])
                return 
            if root.left:
                dfs(root.left , temp +[root.val] ,ans-root.val)
            if root.right:
                dfs(root.right , temp +[root.val],ans-root.val)
            
        dfs(root ,temp , sum)
        return res
    
#993. Cousins in Binary Tree          
class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        d = {}
        def dfs(root, depth = 0, parent = None):
            if root and (x not in d or y not in d):
                d[root.val] = (parent , depth+1)
                dfs(root.left , depth+1 , root)
                dfs(root.right , depth+1 , root)
        dfs(root)
        return d[x][0]!=d[y][0] and d[x][1] == d[y][1]        
        
        
#386. Lexicographical Numbers        
class Solution:
    def lexicalOrder(self, n: 'int') -> 'List[int]':
         n = 13
         #return: [1,10,11,12,13,2,3,4,5,6,7,8,9].    
         res = []
         count = 1
         for i in range(n):
             res.append(count)
             if count * 10 <= n:
                 count *= 10
             elif count % 10 != 9 and count+1 <= n:
                 count += 1
             else:
                 while count//10%10 == 9:
                    count = count // 10      
                 count = count//10 + 1
            
#79. Word Search        
class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        board =[
                  ['A','B','C','E'],
                  ['S','F','C','S'],
                  ['A','D','E','E']
               ]
        word = "ABCCED"
        
        def dfs(board,word,i,j,m,n):
            if len(word) == 0:
                return True
            if i<0 or i>=m or j<0 or j>=n:
                return False
            elif word[0] == board[i][j]:
                board[i][j] = None
                res = dfs(board,word[1:],i+1,j,m,n) or dfs(board,word[1:],i-1,j,m,n) or dfs(board,word[1:],i,j+1,m,n) or dfs(board,word[1:],i,j-1,m,n)
                board[i][j] = word[0]
                return res
            return False
            
        
        if len(word) == 0:
            return Ture
        
        m = len(board)
        if m == 0:
            return True
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(board,word,i,j,m,n):
                    print ('ok')
        #print ('ddd')
        
#226. Invert Binary Tree                

class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        temp = root.left
        root.left = invertTree(root.right)
        root.right = invertTree(temp)
        return root
        # 方法二
        from queue import Queue
        q = Queue()
        if root == None:
            return None
        q.put(root)
        while(!q.empty()):
            cur = q.get()
            temp = cur.left
            cur.left = cur.right
            cur.right = temp
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)
        return root
    
#94. Binary Tree Inorder Traversal        
class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        res = []
        inorder(root)
        return res        
        
#91. Decode Ways        
class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        s = '127'
        dp = [ 0 for _ in range(len(s)+1)]
        if s == '' or s[0] == 0:
            return 0
        dp[0] , dp[1] = 1, 1
        for i in range(2,len(s)+1):
            if s[i-1]>='1' and s[i-1]<='9':
                dp[i] += dp[i-1]
            if (s[i-2] == '1') or (s[i-2] == '2' and s[i-1]>='0' and s[i-1]<='6'):
                dp[i] += dp[i-2]
        return dp[-1]
        
#997. Find the Town Judge        
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        N = 4
        trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
        dic = {}
        temp = set()
        for item in trust:
            if item[1] not in dic.keys():
                dic[item[1]] = [item[0]]
                temp.add(item[0])
            else:
                dic[item[1]].append(item[0])
                temp.add(item[0])
        for key in dic.keys():
            if len(dic[key]) == N-1 and key not in temp:
                print (key)
                
#999. Available Captures for Rook           
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    x = i
                    y = j
        count = 0 
        for a in range(y-1,-1,-1):
            if board[x][a] == 'B':
                break
            if board[x][a] == 'p':
                count+=1
                break
        for a in range(y+1,8):
            if board[x][a] == 'B':
                break
            if board[x][a] == 'p':
                count+=1
                break
        for b in range(x-1,-1,-1):
            if board[b][y] == 'B':
                break
            if board[b][y] == 'p':
                count+=1
                break
        for b in range(x+1,8):
            if board[b][y] == 'B':
                break
            if board[b][y] == 'p':
                count+=1
                break


#1001. Grid Illumination
# 还有问题，同时有多个灯可以照射，应该关闭哪个灯
N = 5
lamps = [[0,0],[4,4]]
queries = [[1,1],[1,0]]
N =10
lamps =[[3,4],[6,6],[1,8],[4,5],[8,7],[0,6],[5,2],[1,9]]
queries =[[7,9],[2,8],[8,6],[6,8],[2,8]]
lamps.sort(key=lambda x:x[0])
res = []
for ques in queries:
    flag = 0
    for item in lamps:
        # 一行一列
        
        if item[0] == ques[0] or item[1] == ques[1]:
            res.append(1)
            flag = 1
            lamps.remove(item)
            break
        elif (item[1] - ques[1]) / (item[0] - ques[0]) == 1:
            res.append(1)
            flag = 1
            lamps.remove(item)
            break
    if flag == 0:
        res.append(0)

#131. Palindrome Partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        s = "aab"
        length = len(s)
        res = []
        temp = []
        dfs(s,0,temp,res)
        
        def palindrome(s):
            i = 0
            j = len(s)-1
            while i<=j:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        
        def dfs(s,i,temp,res):            
            if i == length:
                res.append(temp.copy())
                return
            for j in range(i,length):
                if palindrome(s[i:j+1]):
                    temp.append(s[i:j+1])
                    dfs(s,j+1,temp,res)
                    temp.pop()
        
        
#148:Sort List        
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def getMid(head):
            if head == None or head.next == None:
                return
            fast = head
            slow = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            # 截断链表
            fast = slow
            slow = slow.next
            fast.next = None
            return slow
        def merge(left , right):
            dummy = cur = ListNode(0)
            while left != None and right != None:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                    cur = cur.next
                else:
                    cur.next = right
                    right = right.next
                    cur = cur.next
                if left != None:
            if left != None:
                cur.next = left
            if right != None:
                cur.next = right
            return dummy.next
        
        if head == None or head.next == None:
            return head
        mid = getMid(head)
        head = sortList(head)
        mid = sortList(mid)
        head = merge(head,mid)
        
        return head
        
#200. Number of Islands        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
        if not grid:
            return 0
        m,n=len(grid),len(grid[0])
        
        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >=n or  grid[r][c]!="1":
                return 
            else:
                grid[r][c]='0'
                if r+1<m and grid[r+1][c]=='1':
                    dfs(r+1,c)
                if r-1 >=0 and grid[r-1][c]=='1':
                    dfs(r-1,c)
                if c+1<n and grid[r][c+1]=='1':
                    dfs(r,c+1)
                if c-1>=0 and grid[r][c-1]=='1':
                    dfs(r,c-1)
                
        result=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j)
                    result+=1
        return result 
            
            
#611. Valid Triangle Number        
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = [2,2,3,4]
        nums.sort()
        count = 0 
        for i in range(len(nums)-1 , 1 ,-1):
            left = 0
            right = i-1
            while left < right:
                if nums[i] < nums[left] + nums[right]:
                    count += right-left
                    right -= 1
                else:
                    left += 1
                
        
#215. Kth Largest Element in an Array        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #nums.sort(reverse = True)
        #return nums[k-1] 
        
        nums = [3,2,3,1,2,4,5,5,6]
        nums=[3,2,1,5,6,4]
        k = 2
        def partition(arr , low , high):
            pivot = arr[low]
            while low < high:
                while low < high and arr[high] >= pivot:
                    high -= 1
                arr[low] = arr[high]
                while low < high and arr[low] <= pivot:
                    low += 1
                arr[high] = arr[low]

            arr[high] = pivot
            return  high
        
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = partition(nums,low,high)
            print (mid, nums)
            if len(nums)-mid > k:
                low = mid + 1
            elif len(nums)-mid < k:
                high = mid - 1
            else:
                break
        print (nums[-k])
        
        #####（2）
        import heapq
        queue = []
        for i in range(len(nums)):
            # heapq.heappush([] , num) 向 堆 list中插入数字
            heapq.heappush(queue, nums[i])
            #break
            if len(queue) > k:
                # heappop,从堆中 pop 最小值，heap[0] 是堆中最小值
                heapq.heappop(queue)
        return heapq.heappop(queue)
        
        
#494. Target Sum        
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nums = [1, 1, 1, 1, 1]
        S = 3
        
#1002. Find Common Characters
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
        dic = {}
        res = []
        if len(A) == 1:
            return []
        for char in A[1]:
            if char in A[0]:
                res.append(char)
                ind = A[0].index(char)
                A[0] = A[0][:ind]+A[0][ind+1:]
                
        for i in range(2,len(A)):
            if res == []:
                return []
            for char in res:
                if char in A[i]:
                    ind = A[i].index(char)
                    A[i] = A[i][:ind]+A[i][ind+1:]
                else:
                    ind = res.index(char)
                    res = res[:ind]+res[ind+1:]
        return res

#1003. Check If Word Is Valid After Substitutions
class Solution:
    def isValid(self, S: str) -> bool:
        S = "abcabcababcc"
        ans = 'abc'
        while len(S) != 0:
            if ans in S:
                beg = S.index(ans)
                S = S[0:beg] + S[beg+len(ans):]
                print (S)
            else:
                print ('P')
                break
                
#1000. Minimum Cost to Merge Stones  未完
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        
        stones = [4,6,4,7,5]
        K = 2
        al = 0
        import sys
        res = 0
        length = len(stones)
        
        while length >= K:
            length = length - K + 1
        if length != 1:
            print ('no')
            
        dfs(stones,res,al)
        
        def dfs(stones,res,al):  
            while len(stones) >= K:
                Min = sys.maxsize
                beg = []
                for i in range(len(stones) - K+1):
                    if sum(stones[i:i+K]) <= Min:
                        Min = sum(stones[i:i+K])
                        beg.append(i)
                print (stones,Min)
                res += Min
                print (res)
                for an in beg:
                    stones = stones[:an] + [Min] + stones[an+K:]
                    temp = dfs(stones,res,al)
                    al = min(temp,al)
            return res
            
#485. Max Consecutive Ones            
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = [1,1,0,1,1,1]
        res = 0 
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                res = max(res,count)
            else:
                count = 0
        
#487. Max Consecutive Ones II            
class Solution:
    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:            
        nums = [1,0,1,1,0]
        
        res,cur,count = 0,0,0
        for num in nums:
            count += 1
            if num == 0:
                # cur 代表上一次0翻转为1时的最长1子串
                cur = count
                count = 0
            res = max(res , count + cur)
            
#1004. Max Consecutive Ones III            
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        A = [1,1,1,0,0,0,1,1,1,1,0]
        K = 2   #out = 6
        res , count0 = 0,0
        left = 0
        for i in range(len(A)):
            if A[i] == 0:
                count0 += 1
            while count0 > K:
                if A[left] == 0:
                    count0 -= 1
                left += 1
            res = max(res , i-left+1)
            
#670. Maximum Swap            
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = 2736
        num = list(str(num))
        #num = list(map(int, str(num)))
        for i in range(1,len(num)):
            if int(num[i]) > int(num[i-1]):
                temp = num[i]
                num[i] = num[i-1]
                num[i-1] = temp
                break
        return int(''.join(num))
        
        #A = map(int, str(num))
        A = list(map(int, str(num)))
        #A = map(int, str(num))
        last = {x: i for i, x in enumerate(A)}
        #A = list(map(int, str(num)))
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, -1) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    #return int("".join(map(str, A)))
                    print(int("".join(map(str, A))))
                    break
                else:
                    continue
            
# 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [2,7,9,3,1]
        #out = 12
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0],nums[1])
        
        dp = [ 0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+ nums[i] , dp[i-1])
        return dp[-1]

#213. House Robber II
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [2,5,4] # out 3
        
        def dp(nums,beg,end):
            A2,A1 = 0,0
            # 比较A2+nums【i】 和 A1 ，A2代表dp【i-2】
            for i in range(beg,end+1):
                temp = A1
                A1 = max(A2+nums[i] , A1)
                A2 = temp
            return A1
                
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0],nums[1])
        print (dp(nums,0,len(nums)-2))
        print (dp(nums,1,len(nums)-1))
        return max(dp(nums,0,len(nums)-2),dp(nums,1,len(nums)-1))


        
# 5 longest pan substring       
s = 'ac'
res = 0
beg = 0
if len(s)==1:
    return s
for i in range(len(s)):
    j = i
    gap = 0
    while j-gap >= 0 and j+gap < len(s):
        if s[j-gap] == s[j+gap]:
            if gap*2+1 > res:
                res = 2*gap+1
                beg = j-gap
            gap += 1
        else:
            break
    gap = 1
    while j-gap+1 >= 0 and j+gap< len(s):
         if s[j-gap+1] == s[j+gap]:
            if gap*2 > res:
                res = 2*gap
                beg = j-gap+1
            gap += 1
         else:
            break
print (s[beg:beg+res])
       

# 头条 一个升序数组（不是严格的，有相同元素），给一个target，
# 找出比target小的数的最后一个下标，要求最差情况下，时间复杂度logN。
# 找不到比target小的，返回-1
        
nums = [0,1,2,4,5,7,10]
target = 6

left = 0
right = len(nums)
ind = -1

if nums[0] >= target:
    print ('-1')
    
while left<=right:
    mid = (left+right)//2
    print (left,right, mid, nums[mid])
    if nums[mid] < target:
        ind = mid
        left = mid+1
    else:
        right = mid-1
    
print (ind)
        


#96. Unique Binary Search Trees
#遍历n个元素作为root节点
#num(n)=num(0)*num(n-1)+num(1)*num(n-2)+num(2)*num(n-3)+...+num(n-1)*num(0)
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        n = 3
        dp = [0 for _ in range(n+1)]
        dp[0],dp[1] = 1,1
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[-1]

#95. Unique Binary Search Trees II




# 搜狗：一个数组，如何让奇数在前边，偶数在后边
nums = [2,1,3,6,8,9,22,11,13,14]
left = 0 
right = len(nums)-1
while left < right:
    if nums[left] % 2 == 1:
        left += 1
    else:
        temp = nums[right]
        nums[right]= nums[left]
        nums[left] = temp
        right -= 1
        
        
#1020. Partition Array Into Three Parts With Equal Sum        
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        A = [0,2,1,-6,6,-7,9,1,2,0,1]
        if sum(A) % 3 != 0:
            return False
        temp = sum(A)//3
        count = 0
        res = 0
        for num in A:
            res += num
            if res == temp:
                count+=1
                res=0
        
        
# =============================================================================
#         left , right = 0 , len(A)-1
#         while left < right:
#             if sum(A[:left+1]) < sum(A[right:]):
#                 left += 1
#             elif sum(A[:left+1]) > sum(A[right:]):
#                 right -= 1
#             else:
#                 if sum(A[left+1:right]) == sum(A[:left+1]):
#                     print ('ok')
#                     break
# =============================================================================
        
# =============================================================================
#         for i in range(len(A)-1):
#             for j in range(i+1,len(A)):
#                 if sum(A[:i]) == sum(A[i:j]) == sum(A[j:]):
#                     print ('ok')
#                     break
# =============================================================================
        
#1021. Best Sightseeing Pair       
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # max A[i]+i + A[j]-j i < j
        A = [8,1,5,2,6]
        res = 0
        i = 0 
        for j in range(i+1 , len(A)):   
            res = max(res,A[i]+i+A[j]-j)
            print (res , i, j , A[j]-j)
            if A[j]+j > A[i]+i:
                print (j)
                i = j
        
#1023. Binary String With Substrings Representing 1 To N 
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        S = '0110'
        N = 3
        #aa = [bin(i)[2:] in S for i in range(N, N // 2, -1)] 
        return all(bin(i)[2:] in S for i in range(Ns N // 2, -1))        
    
    
    
# json多级字典嵌套 得到list
        
dic = { 'k1' : 'aaa' , 'k2':{'k3':{'k4':'bbb'} , 'k5':111}, 'k6':{'k7':222}}
#return ['k1','k2.k3.k4','k2.k5','k6.k7']

def dfs(dic , key_total):
    if isinstance(dic,dict) == False:
        res.append(str(key_total))
    else:
        for key in dic:
            dfs(dic[key],  str(key_total)+str('.')+str(key)) 
          
res = []
for key in dic.keys():
    dfs(dic[key],  str(key)) 

# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix = [
                  [1,   3,  5,  7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 50]
                 ]
        target = 3
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        row , col = 0,n-1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
            
# 101. Symmetric Tree            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
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
            
#62. Unique Paths            
class Solution:
    def uniquePaths(self, m, n):
        m,n = 7 ,3
        dp = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
                
#63. Unique Paths II
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
                    
#980. Unique Paths III
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(x, y, zerocount):
            direction = [(-1,0),(1,0),(0,1),(0,-1)]
            for i,j in direction:
                nx ,ny = x+i , y+j
                if 0 <= nx < m and 0 <=ny < n:
                    if grid[nx][ny] == 2:
                        if zerocount == 0:
                            self.res += 1
                            return
                        else:
                            continue
                    if grid[nx][ny] == 0: # backtracking
                        grid[nx][ny] = 1
                        dfs(nx, ny , zerocount-1)
                        grid[nx][ny] = 0

       
        m , n  = len(grid),len(grid[0])
        zerocount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx , sy = i,j
                elif grid[i][j] == 2:
                    end = (i,j)
                elif grid[i][j] == 0:
                    zerocount += 1
        self.res = 0       
        dfs(sx , sy , zerocount)
        return self.res
    
A = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]   
print (Solution().uniquePathsIII(A))
        

#5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = 'cbbd'
        begin = 0 
        res = 0  # longest length
        for i in range(len(s)):
            gap = 0
            while i - gap >= 0 and i + gap < len(s):
                if s[i - gap] == s[i + gap]:
                    if gap*2+1 > res:
                        res = gap*2+1
                        begin = i-gap
                    gap += 1
                else:
                    break
            gap = 1
            while i-gap+1 >=0 and i+gap < len(s):
                if s[i - gap+1] == s[i + gap]:
                    if gap*2 > res:
                        res = gap*2
                        begin = i-gap+1
                    gap += 1
                else:
                    break
        return s[begin : begin+res]
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0] * len(s) for _ in range(len(s))]
        begin = 0
        res = 0
        for i in range(len(s)):
            for j in range(i+1):
                dp[j][i] = s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1] == 1)
                if dp[j][i]:
                    if i-j+1 > res:
                        res = i-j+1
                        begin = j
        return s[begin:begin+res]

                
#300. Longest Increasing Subsequence                
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #对于每一个nums中元素，都有是LIS中元素和不是两种选择，
        #暴力递归所有的可能 time O(2^n) space O(n^n)
        #会超时
        import sys
        def recursion(nums , last_value , ind):
            taken , nottaken = 0,0
            if ind == len(nums):
                return 0
            if nums[ind] > last_value:
                taken = 1+recursion(nums,nums[ind],ind+1)
            nottaken = recursion(nums,last_value,ind+1)
            return max(taken,nottaken)
              
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        return recursion(nums , -sys.maxsize - 1 , 0)
        
        
    #dp
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
    #dp with binarysearch
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
                
#53. Maximum Subarray                
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
                
#191. Number of 1 Bits                
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n&1
            n >>= 1
        return count
        
#338. Counting Bits        
class Solution(object):
    
    # 164 ms 17.34% Brute Force O(n*sizeof(integer))
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        num = 5
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
        
#64. Minimum Path Sum        
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
        
#174. Dungeon Game        
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

#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices = [7,1,5,3,6,4]
        if len(prices) == 0:
            return 0
        res = 0
        Min = prices[0]
        for num in prices:
            Min = min(num,Min)
            res = max(res , num-Min)
        return res

#122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        res = 0
        last = prices[0]
        for num in prices:
            last = min(last,num)
            if num > last:
                res += num-last
                last = num
        return res  
        
#123. Best Time to Buy and Sell Stock III        
class Solution:
    # 56ms 84%
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
        # TLE
# =============================================================================
#         if len(prices) == 0:
#             return 0
#         Min = prices[0]
#         Max = prices[-1]
#         front = []
#         back = []
#         for num in prices:
#             Min = min(Min,num)
#             front.append(num-Min)
#             
#         for num in prices[::-1]:
#             Max = max(Max,num)
#             back.append(Max-num)
#         back = back[::-1]
#         res = 0
#         for i in range(len(prices)-1):
#             res = max(res , max( front[:i+1] ) + max( back[i:] ))
#         return res
# =============================================================================
        

#188. Best Time to Buy and Sell Stock IV
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
                   
#96. Unique Binary Search Trees                    
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
# =============================================================================
#         由1,2,3,...,n构建的二叉查找树，以i为根节点，左子树由[1,i-1]构成，其右子树由[i+1,n]构成。
#         定义f(i)为以[1,i]能产生的Unique Binary Search Tree的数目
#         若数组为空，则只有一种BST，即空树，f(0)=1;
#         若数组仅有一个元素1，则只有一种BST，单个节点，f(1)=1;
#         若数组有两个元素1，2，则有两种可能，f(2)=f(0)*f(1)+f(1)*f(0);
#         若数组有三个元素1，2，3，则有f(3)=f(0)*f(2)+f(1)*f(1)+f(2)*f(0)
#         由此可以得到递推公式：f(i)=f(0)*f(i-1)+...+f(k-1)*f(i-k)+...+f(i-1)*f(0)
# =============================================================================
        #对于元素来说，总有排列顺序，所以 1 2 和 6 7的组合数是一样的，都是f(2) = 2
        n = 3
        dp = [0 * _ for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        if n <= 1:
            return 1
        for i in range(2 , n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]
        
#95. Unique Binary Search Trees II                    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
# =============================================================================
#         Input: 3
#         Output:
#         [
#           [1,null,3,2],
#           [3,2,null,1],
#           [3,1,null,null,2],
#           [2,1,3],
#           [1,null,2,null,3]
#         ]                    
# =============================================================================
        
        def dfs(left , right):
            if left > right:
                return [None]
            res = []
            # 包含n可能为根节点,所以right+1
            for i in range(left , right+1):
                # i已经是root节点了，要减掉
                left_list = dfs(left , i-1)
                right_list = dfs(i+1 , right)
                for left in left_list:
                    for right in right_list:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        
        if n == 0 : return []
        return dfs(1,n)
        
        
        def dfs(left , right):
            if left > right:
                return [None]
            res = []
            for i in range(left, right + 1):
                left_nodes = dfs(left, i - 1)
                right_nodes = dfs(i + 1, right)
                for left_node in left_nodes:
                    for right_node in right_nodes:
                        root = TreeNode(i)
                        root.left = left_node
                        root.right = right_node
                        res.append(root)
            return res
        if n == 0 : return []
        return dfs(1,n)

#120. Triangle
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
        for i in range(1,len(triangle)):
            length = len(triangle[i-1])
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == length:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1] , triangle[i-1][j])
        return min(triangle[-1])


#98. Validate Binary Search Tree                        
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """    
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
        
    def isValidBST(self, root):
        def dfs(root, Min ,Max):
            if root == None:
                return True
            if root.val <= Min or root.val >= Max :
                return False
            return dfs(root.left , Min , root.val) and dfs(root.right , root.val , Max)
                
        import sys
        Max = sys.maxsize
        Min = -sys.maxsize-1
    
        return dfs(root,Min,Max)
            
            
# 99. Recover Binary Search Tree           
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def inorder(root , node_list , value_list):
            if root == None:
                return
            inorder(root.left , node_list , value_list )
            node_list.append(root)
            value_list.append(root.val)
            inorder(root.right , node_list , value_list )
            
        node_list = []
        value_list = []
        inorder(root , node_list, value_list)
        value_list.sort()
        for ind,node in enumerate(node_list):
            node.val = value_list[ind]
                    
            
#100. Same Tree
            
#101. Symmetric Tree  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs( p , q ):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False
            return p.val == q.val and dfs(p.left , q.right) and dfs(p.right , q.left)
            
        return dfs(root,root)

    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root,root]
        while len(queue)!= 0:
            p = queue.pop()
            q = queue.pop()
            if p == None and q == None:
                continue
            elif p == None or q == None:
                return False
            elif p.val != q.val:
                return False
            queue.append(p.left)
            queue.append(q.right)
            queue.append(p.right)
            queue.append(q.left)
        return True
  
            
#104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root):
            if root == None:
                return 0
            return max(dfs(root.left) , dfs(root.right)) + 1
        
        return dfs(root)
    
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        queue = [root] if root else []
        while queue:
            depth += 1
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        return depth
    
#105. Construct Binary Tree from Preorder and Inorder Traversal            
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #preorder = [3,9,20,15,7]
        #inorder = [9,3,15,20,7]
        
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        # preorder 和 inorder 都减少一个node,即当前root.preorder[0] , inorder[index]
        root.left = self.buildTree(preorder[1:index+1] , inorder[:index] )
        root.right = self.buildTree(preorder[index+1:] , inorder[index+1:] )
        return root


#106. Construct Binary Tree from Inorder and Postorder Traversal
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        #inorder = [9,3,15,20,7]
        #postorder = [9,15,7,20,3]
        if len(postorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        # preorder 和 inorder 都减少一个node,即当前root.preorder[0] , inorder[index]
        root.right = self.buildTree(postorder[index:-1] , inorder[index+1:] )
        root.left = self.buildTree(postorder[:index] , inorder[:index] )
        return root




#153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #36ms 99%
        if len(nums) == 0:
            return 0
        left , right = 0 ,len(nums)-1
        if nums[left] < nums[right]:
            return nums[left]
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[left]:
                left = mid
            elif nums[mid] <= nums[right]:
                right = mid
            else:
                left+=1
        return nums[left]







            
            
            
            
            
            
            
            
            
            



