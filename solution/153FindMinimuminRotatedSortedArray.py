class Solution:
    def findMin(self, nums: List[int]) -> int:
        #36ms 99%
        if len(nums) == 0:
            return 0
        left , right = 0 ,len(nums)-1
        if nums[left] < nums[right]:
            return nums[left]
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[left]:
                left = mid
            elif nums[mid] <= nums[right]:
                right = mid
            else:
                left+=1
        return nums[left]