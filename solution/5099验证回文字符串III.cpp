//
// Created by Alaric on 2019-10-06.
//
class Solution {
public:
    bool isValidPalindrome(string s, int k) {
        int i, j, n = s.size();
        string a = s;
        reverse(s.begin(),s.end());
        string b = s;
        int dp[n+1][n+1];
        memset(dp, 0x3f, sizeof dp);
        for (i = 0 ; i < n; i++)
            dp[i][0] = dp[0][i] = i;
        for (i = 1; i <= n; i++) {
            int from = max(1, i-k), to = min(i+k, n);
            for (j = from; j <= to; j++) {
                if (a[i-1] == b[j-1])            // same character
                    dp[i][j] = dp[i-1][j-1];
                dp[i][j] = min(dp[i][j], 1 + dp[i][j-1]); // delete character j
                dp[i][j] = min(dp[i][j], 1 + dp[i-1][j]); // insert character i
            }
        }
        cout << dp[n][n];
        return dp[n][n] <= 2*k;
    }
};
