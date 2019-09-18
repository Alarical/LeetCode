# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, Min ,Max):
            if root == None:
                return True
            if root.val <= Min or root.val >= Max :
                return False
            return dfs(root.left , Min , root.val) and dfs(root.right , root.val , Max)
                
        import sys
        Max = sys.maxsize
        Min = -sys.maxsize-1
    
        return dfs(root,Min,Max)

 
