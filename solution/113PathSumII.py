# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root ,sum , temp , ans):
            if not root:
                return
            if root.left == None and root.right == None and root.val == sum:
                temp.append(root.val)
                ans.append(temp)

            dfs(root.left , sum - root.val , temp + [root.val], ans)
            dfs(root.right , sum - root.val , temp + [root.val] , ans)
        ans = []
        dfs(root, sum , [] , ans)
        return ans

    # 非递归
    # def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
    #     if not root: return []
    #     stack = [([root.val], root)]
    #     res = []
    #     while stack:
    #         tmp, node = stack.pop()
    #         if not node.right and not node.left and sum(tmp) == sum_:
    #             res.append(tmp)
    #         if node.right:
    #             stack.append((tmp + [node.right.val], node.right))
    #         if node.left:
    #             stack.append((tmp + [node.left.val], node.left))
    #     return res
