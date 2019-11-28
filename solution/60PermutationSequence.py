class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def fact(n):
            ret = 1
            while n:
                ret *= n
                n -= 1
            return ret

        def dfs(nums ,  ans , k):
            if not nums:
                return ans
            l = len(nums)
            count = fact(l-1)
            for i in range(l):
                print (k, count)
                if k > count: # 此处如果k大于该分支排列数量，那么减去该分支
                    k -= count
                else:
                    return dfs(nums[:i]+nums[i+1:], ans+nums[i], k)
        return dfs( [ str(i) for i in range(1 , n+1)] , '' , k)