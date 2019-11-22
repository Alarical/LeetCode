# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def dfs(root):
            if root == None:
                return 0
            return dfs(root.left) + dfs(root.right) + 1
        return dfs(root)