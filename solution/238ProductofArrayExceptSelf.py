class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,6,24]
        #[4,12,24,24]
        n = len(nums)
        res = [0]*n
        k = 1
        for i in range(n):
            res[i] = k
            k = k*nums[i]
        k = 1
        for i in range(n-1,-1,-1):
            res[i] *= k
            k *= nums[i]
        return res
