class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0 :
            return -1
        left , right  = 0 , len(nums) - 1
        while left + 1 < right :
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]: #左升序
                if target < nums[mid] and target >= nums[left] :
                    right = mid - 1
                else:
                    left = mid + 1
            else: #右升序
                if target <= nums[right] and target > nums[mid] :
                    left = mid + 1
                else:
                    right = mid -1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1


