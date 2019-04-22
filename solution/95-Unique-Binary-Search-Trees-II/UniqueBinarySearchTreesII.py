# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(left , right):
            if left > right:
                return [None]
            res = []
            for i in range(left, right + 1):
                left_nodes = dfs(left, i - 1)
                right_nodes = dfs(i + 1, right)
                for left_node in left_nodes:
                    for right_node in right_nodes:
                        root = TreeNode(i)
                        root.left = left_node
                        root.right = right_node
                        res.append(root)
            return res
        if n == 0 : return []
        return dfs(1,n)