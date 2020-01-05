"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(root):
            if root == None:
                return
            for child in root.children:
                dfs(child)
            res.append(root.val)
        dfs(root)
        return res


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        queue = [root]
        res = []
        while queue:
            cur = queue.pop()
            res.append(cur.val)
            for child in cur.children:
                queue.append(child)
        return res[::-1]
