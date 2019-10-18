# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root , ans, temp):
            temp += root.val
            if root.left == None and root.right == None:
                self.ans += temp
                return
            if root.left !=None:
                dfs(root.left , self.ans , temp*10)
            if root.right != None:
                dfs(root.right , self.ans , temp*10)
            return

        self.ans = 0
        if root == None:
            return 0
        dfs(root , self.ans ,0)
        return self.ans
