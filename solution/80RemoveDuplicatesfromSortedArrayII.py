# 双指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        pos = 1
        for i in range(2 , len(nums)):
            if nums[i] != nums[pos-1]:
                pos += 1
                nums[pos] = nums[i]
        return pos+1
