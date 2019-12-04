class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]
        head = 1
        for i in range(n):
            l = len(ans)
            for j in range(l-1,-1,-1):
                ans.append(head+ans[j])
            head <<= 1
        return ans