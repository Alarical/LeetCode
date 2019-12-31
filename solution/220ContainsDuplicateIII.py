class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        visited = set()
        for i in range(n):
            if t == 0:
                if nums[i] in visited:
                    return True
            else:
                for j in visited:
                    if abs(j - nums[i]) <= t:
                        return True
            visited.add(nums[i])
            if len(visited) > k :
                visited.remove(nums[i-k])

        return False