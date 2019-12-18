# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root , sum):
            if root == None:
                return 0
            res = 0
            if root.val == sum:
                res += 1
            res += dfs(root.left , sum - root.val)
            res += dfs(root.right , sum - root.val)
            return res

        if root == None : return 0
        ans = dfs(root , sum) + self.pathSum(root.right , sum) + self.pathSum(root.left , sum)
        return ans