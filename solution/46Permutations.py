class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums , temp):
            if len(nums) == 0:
                ans.append(temp)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:] , temp + [nums[i]])

        ans = []
        dfs(nums , [])
        return ans


