# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.res = 0
        self.num = float('inf')

        def dfs(root):
            if root == None:
                return self.res
            else:
                if abs(root.val - target) < self.num:
                    self.num = abs(root.val - target)
                    self.res = root.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.res


