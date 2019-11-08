class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums , i , temp , ans):
            ans.append(temp)
            if i == len(nums):
                return
            for j in range(i,len(nums)):
                dfs(nums , j+1 , temp + [nums[j]] , ans)

        ans = []
        dfs(nums , 0 , [] , ans)
        return ans