class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def inorder(root , node_list , value_list):
            if root == None:
                return
            inorder(root.left , node_list , value_list )
            node_list.append(root)
            value_list.append(root.val)
            inorder(root.right , node_list , value_list )
            
        node_list = []
        value_list = []
        inorder(root , node_list, value_list)
        value_list.sort()
        for ind,node in enumerate(node_list):
            node.val = value_list[ind]
