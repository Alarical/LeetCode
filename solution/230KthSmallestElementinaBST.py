# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        count = 0
        p = root
        while p or stack:
            while p :
                stack.append(p)
                p = p.left
            cur = stack.pop()
            count += 1
            if count == k:
                return cur.val
            p = p.right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = k
        self.res = 0
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.count -= 1
            if self.count == 0:
                self.res = root.val
            inorder(root.right)
        inorder(root)
        return self.res