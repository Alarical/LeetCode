class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            temp = []
            if char != ')':
                stack.append(char)
            else:
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                for i in temp:
                    stack.append(i)
        return ''.join(stack)




