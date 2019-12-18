# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs(root ,sum):
            if root == None:
                return False
            if root.left == None and root.right == None:
                return root.val == sum

            return dfs(root.left , sum - root.val) or dfs(root.right , sum - root.val)

        return dfs(root,sum)