# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root , temp):
            if root == None:
                return
            if root.left == None and root.right == None:
                ans.append(temp + str(root.val))
            dfs(root.left , temp + str(root.val) + '->')
            dfs(root.right , temp + str(root.val) + '->')

        ans = []
        dfs(root,'')
        return ans