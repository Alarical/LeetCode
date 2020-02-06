# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        inorder = []
        def dfs(root):
            if root == None:
                return []
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        dfs(root)

        n = len(inorder)
        left = 0
        right = n - k

        while left < right:
            mid = left + (right - left) // 2
            if target - inorder[mid] > inorder[mid+k] - target:
                left = mid+1
            else:
                right = mid
        return inorder[left:left+k]



            