# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            height = max(left , right)
            if len(ans) == height:
                ans.append([])
            ans[height].append(root.val)
            return height + 1
        dfs(root)
        return ans