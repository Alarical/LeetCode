class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height)-1
        ans = 0
        while left < right:
            low = min(height[left] , height[right])
            ans = max(ans , low * (right-left))
            if low == height[left]:
                left += 1
            else:
                right -=1
        return ans
