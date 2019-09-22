class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        import bisect
        n = len(nums)
        if k == 0:
            return []
        window = sorted(nums[:k])
        ans = []
        for i in range(k , n+1):
            ans.append( (window[k//2] + window[(k-1)//2])/2.0 )
            if i == n : break
            index = bisect.bisect_left(window , nums[i-k])
            window.pop(index)
            bisect.insort_left(window , nums[i])
        return ans
