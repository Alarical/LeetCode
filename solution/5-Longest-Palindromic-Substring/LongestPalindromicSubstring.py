class Solution:
    # Expand Around Center
    def longestPalindrome(self, s): 
        """
        :type s: str
        :rtype: str
        """
        begin = 0 
        res = 0  # longest length
        for i in range(len(s)):
            gap = 0
            while i - gap >= 0 and i + gap < len(s):
                if s[i - gap] == s[i + gap]:
                    if gap*2+1 > res:
                        res = gap*2+1
                        begin = i-gap
                    gap += 1
                else:
                    break
            gap = 1
            while i-gap+1 >=0 and i+gap < len(s):
                if s[i - gap+1] == s[i + gap]:
                    if gap*2 > res:
                        res = gap*2
                        begin = i-gap+1
                    gap += 1
                else:
                    break
        return s[begin : begin+res]
        
    # dp solution
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0] * len(s) for _ in range(len(s))]
        begin = 0
        res = 0
        for i in range(len(s)):
            for j in range(i+1):
                dp[j][i] = s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1] == 1)
                if dp[j][i]:
                    if i-j+1 > res:
                        res = i-j+1
                        begin = j
        return s[begin:begin+res]
                