class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        ans = []
        nums.sort()
        def helper(num , idx, tmp , ans):
            ans.append(tmp)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                helper(nums , i+1, tmp + [nums[i]] , ans)
        helper(nums , 0, [] , ans)
        #print (ans)
        return ans