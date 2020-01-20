class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        cur_min = float('-inf')
        for i in range(len(preorder)):
            if preorder[i] < cur_min:
                return False
            while stack and stack[-1] < preorder[i]:
                cur_min = stack.pop()
            stack.append(preorder[i])
        return True