class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #preorder = [3,9,20,15,7]
        #inorder = [9,3,15,20,7]
        
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        # preorder 和 inorder 都减少一个node,即当前root.preorder[0] , inorder[index]
        root.left = self.buildTree(preorder[1:index+1] , inorder[:index] )
        root.right = self.buildTree(preorder[index+1:] , inorder[index+1:] )
        return root
