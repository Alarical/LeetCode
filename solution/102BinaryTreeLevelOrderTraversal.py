# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        queue = [root]
        while queue:
            n = len(queue)
            res = []
            for i in range(n):
                temp = queue.pop(0)
                res.append(temp.val)
                if temp.left != None:
                    queue.append(temp.left)
                if temp.right != None:
                    queue.append(temp.right)
            ans.append(res)
        return ans