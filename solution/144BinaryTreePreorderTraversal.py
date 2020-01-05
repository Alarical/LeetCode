# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if root == None:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop().right
        return res