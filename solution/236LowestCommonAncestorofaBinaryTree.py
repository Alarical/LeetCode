# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root == None:
                return False
            cur = False
            if root == p or root == q:
                cur = True

            left = dfs(root.left)
            right = dfs(root.right)

            if cur + left + right >= 2:
                self.res = root

            return cur or left or right

        dfs(root)
        return self.res