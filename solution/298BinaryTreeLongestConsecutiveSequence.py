# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if root == None:
            return 0
        ans = 0
        def dfs(root , parent, pre_len):
            nonlocal ans
            if root == None:
                return
            cur_len = 1
            if root.val == parent + 1:
                cur_len += pre_len
            ans = max(ans , cur_len)
            dfs(root.left , root.val, cur_len)
            dfs(root.right , root.val, cur_len)

        dfs(root, root.val+1 , 0)
        return ans



