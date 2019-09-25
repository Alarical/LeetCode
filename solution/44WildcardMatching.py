class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        #pi = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue
                if j == 0:
                    dp[i][j] = False
                    continue
                dp[i][j] = False
                if p[j-1] == '*':
                    dp[i][j] |= dp[i][j-1]
                    if dp[i][j-1] == True:
                        #pi[i][j] = 2
                    if i > 0:
                        dp[i][j] |= dp[i-1][j]
                        if dp[i-1][j] == True:
                            #pi[i][j] = 3
                else:
                    if i > 0 and (s[i-1] == p[j-1] or p[j-1] == '?'):
                        dp[i][j] |= dp[i-1][j-1]
                        #pi[i][j] = 1

        # res = [0 for _ in range(m)]
        # i = m
        # j = n
        # while True:
        #     if j == 0: break
        #     if pi[i][j] == 1:
        #         res[i-1] = j-1
        #         i-=1
        #         j-=1
        #     else:
        #         if pi[i][j] == 2:
        #             j-=1
        #         else:
        #             res[i-1] = j-1
        #             i-=1
        # print (res)

        return dp[m][n]