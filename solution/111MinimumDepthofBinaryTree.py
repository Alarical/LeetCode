# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        m1 = self.minDepth(root.left)
        m2 = self.minDepth(root.right)
        if root.left == None or root.right == None:
            return m1+m2+1
        return min(m1,m2)+1
