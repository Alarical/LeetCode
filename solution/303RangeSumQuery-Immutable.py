class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = nums[:]
        n = len(nums)
        for i in range(1, n):
            self.dp[i] += self.dp[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j]-self.dp[i-1] if i > 0 else self.dp[j]
