# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = []
        flag = False
        while queue:
            flag = bool(1-flag)
            cur_level = []
            n = len(queue)
            for i in range(n):
                temp = queue.pop(0)
                if temp.left : queue.append(temp.left)
                if temp.right : queue.append(temp.right)
                cur_level.append(temp.val)
            if flag :
                ans.append(cur_level)
            else:
                ans.append(cur_level[::-1])
        return ans