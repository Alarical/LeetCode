class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        stack = [-1]
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i]&1 :
                stack.append(i)
        stack.append(n)
        # [-1,3,6,10]
        print (stack)
        for i in range(k,len(stack)-1):
            left = stack[i-k+1] - stack[i-k]
            right = stack[i+1] - stack[i]
            ans += left*right
        return ans


