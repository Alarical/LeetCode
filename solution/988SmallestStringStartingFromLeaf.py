# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.ans = "~"
        def dfs(root , temp ):
            if root:
                temp.append( chr(root.val + ord('a')) )
                if root.left == None and root.right == None:
                    self.ans = min(self.ans , ''.join(reversed(temp)) )
                dfs(root.left , temp )
                dfs(root.right , temp )
                temp.pop()
        dfs(root , [] )
        return self.ans
