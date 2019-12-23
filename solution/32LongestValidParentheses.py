class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(": #(()
                stack.append(i) # -1 0 1
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res,i - stack[-1])
        return res
