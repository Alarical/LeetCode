class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr , low, high):
            pivot = arr[low]
            while low < high:
                while low < high and arr[high] >= pivot:
                    high -= 1
                arr[low] = arr[high]
                while low < high and arr[low] <= pivot:
                    low += 1
                arr[high] = arr[low]
            arr[high] = pivot
            return high
        target = len(nums) - k
        mid = partition(nums , 0 , len(nums)-1)
        if mid == target:
            return nums[mid]
        while mid != target:
            if mid < target:
                mid = partition(nums , mid+1 , len(nums)-1)
            else:
                mid = partition(nums , 0 , mid-1)
        return nums[mid]
