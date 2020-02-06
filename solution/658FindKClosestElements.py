class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        remove_nums = len(arr) - k

        while remove_nums:
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1
            remove_nums -= 1

        return arr[left:right+1]