class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        n = len(heights)
        if n == 0:
            return 0
        stack.append(-1)
        stack.append(0)
        for i in range(1,n):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                    last_num = stack.pop()
                    area = (i - 1 - stack[-1]) * heights[last_num]
                    ans = max(ans , area)
                stack.append(i)
        while stack[-1] != -1:
            last_num = stack.pop()
            area = (n-1 - stack[-1]) * heights[last_num]
            ans = max(ans , area)
        return ans