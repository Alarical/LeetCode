# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root):
            if root == None:
                return
            if root.left and root.left.left == None and root.left.right == None:
                self.ans += root.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.ans