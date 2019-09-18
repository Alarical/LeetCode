class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # dp[i][j] =
        # dp[i-1][j-1] 如果 i > 0 , 并且 p[j-1] == '.' or s[i-1] == p[j-1]  或
        # (dp[i][j-2] (表示不用 *x ) or ( dp[i-1][j] 在 (s[i-1] == p[j-1] or p[j-2] == '.') )
        # if p[j-1] == '*')
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue
                if j == 0:
                    dp[i][j] = False
                    continue
                # j > 0
                dp[i][j] = False
                if p[j - 1] != '*':
                    if i > 0 and (p[j - 1] == '.' or s[i - 1] == p[j - 1]):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    if j > 1:
                        dp[i][j] |= dp[i][j - 2]
                    if i > 0 and j > 1:
                        if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                            dp[i][j] |= dp[i - 1][j]
        return dp[m][n]
