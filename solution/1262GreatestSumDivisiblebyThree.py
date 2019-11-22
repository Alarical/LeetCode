class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        left1 = []
        left2 = []
        ans = 0
        for num in nums:
            if num % 3 == 1:
                left1.append(num)
            if num % 3 == 2:
                left2.append(num)
            ans += num
        if ans % 3 == 0:
            return ans
        left1.sort()
        left2.sort()
        if ans % 3 == 1:
            if len(left1) > 0 and len(left2) > 1:
                temp = min(left1[0] , left2[0] + left2[1])
                return ans - temp
            elif len(left1) > 0:
                return ans - left1[0]
            elif len(left2) > 1:
                return ans - (left2[0] + left2[1])
            else:
                return 0
        if ans % 3 == 2:
            if len(left1) > 1 and len(left2) > 0:
                temp = min(left1[0] + left1[1] , left2[0] )
                return ans - temp
            elif len(left2) > 0:
                return ans - left2[0]
            elif len(left1) > 1:
                return ans - (left1[0] + left1[1])
            else:
                return 0

                