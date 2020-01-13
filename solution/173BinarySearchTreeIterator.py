# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.head = root
        self.stack = deque()

        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        cur = self.stack.pop()
        root = cur.right
        while root:   # 使用了循环，复杂度不应该为O(1)?
            self.stack.append(root)
            root = root.left

        return cur.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()