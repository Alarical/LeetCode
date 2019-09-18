class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [False *(n+1) for _ in range(m+1)]
        # dp[i][j] =
        # dp[i-1][j-1] 如果 i > 0 , 并且 p[j-1] == '.' or s[i-1] == p[j-1]
        # dp[i][j-2] (表示不用 *x ) or ( dp[i-1][j] and (s[i-1] == p[j-1] or p[j-2] == '.') )
        # if p[j-1] == '*'
        for i in range(m+1):
            for j in range(n+1):
                dp[][]