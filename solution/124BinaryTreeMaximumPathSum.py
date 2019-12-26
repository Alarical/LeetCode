# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs_max_gain(root):
            nonlocal ans
            if not root:
                return 0
            max_left = max(dfs_max_gain(root.left) , 0)
            max_right = max(dfs_max_gain(root.right) , 0)

            cur_val = root.val + max_left + max_right
            ans = max(ans , cur_val)

            return root.val + max(max_left , max_right)

        ans = float('-inf')
        dfs_max_gain(root)

        return ans