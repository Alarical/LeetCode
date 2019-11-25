class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c,0) + 1
        stack = ['0']
        visited = set()
        for c in s:
            if c not in visited:
                while c < stack[-1] and count[stack[-1]] > 0:
                    visited.remove(stack.pop())
                stack.append(c)
                visited.add(c)
            count[c] -= 1
        return ''.join(stack[1:])