class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root):
            if root == None:
                return 0
            return max(dfs(root.left) , dfs(root.right)) + 1
        
        return dfs(root)
    
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        queue = [root] if root else []
        while queue:
            depth += 1
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        return depth