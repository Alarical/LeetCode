class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def dfs(candidates , i , temp):
            if sum(temp) == target:
                ans.append(temp)
                return
            if sum(temp) > target or i == len(candidates):
                return

            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if sum(temp)+candidates[j] > target:
                    break
                dfs(candidates , j+1 , temp+[candidates[j]])

        ans = []
        dfs(candidates , 0 , [])
        return ans