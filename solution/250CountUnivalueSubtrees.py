# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res


    def dfs(self,root):
        if root.left == None and root.right == None:
            self.res += 1
            return True
        is_uni = True
        if root.left:
            is_uni = self.dfs(root.left) and is_uni and root.left.val == root.val
        if root.right:
            is_uni = self.dfs(root.right) and is_uni and root.right.val == root.val
        self.res += is_uni
        return is_uni






