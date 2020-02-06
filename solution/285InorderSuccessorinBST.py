# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = []
        cur = root
        while cur:
            if cur.val > p.val:
                stack.append(cur)
                cur = cur.left
            elif cur.val < p.val:
                cur = cur.right
            else:
                if cur.right:
                    temp = cur.right
                    while temp.left:
                        temp = temp.left
                    return temp
                if stack:
                    return stack[-1]
                else:
                    return None
        return None







