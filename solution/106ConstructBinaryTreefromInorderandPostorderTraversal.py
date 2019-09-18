class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    
        if len(postorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        # preorder 和 inorder 都减少一个node,即当前root.preorder[0] , inorder[index]
        root.left = self.buildTree( inorder[:index] , postorder[:index] )
        root.right = self.buildTree( inorder[index+1:] , postorder[index:-1] )
        return root