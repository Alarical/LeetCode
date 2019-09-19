class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        res = []
        length = len(nums)
        last_max = max(nums[:k])
        res.append(last_max)
        for i in range(1, length - k + 1):
            if nums[i + k - 1] >= last_max:
                last_max = nums[i + k - 1]
                res.append(last_max)
                continue
            else:
                if nums[i - 1] == last_max:
                    last_max = max(nums[i:i + k])
                    res.append(last_max)
                else:
                    res.append(last_max)
        return res

