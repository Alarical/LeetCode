class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size();
        int n = p.size();
        vector<vector<bool>> dp(m+1 , vector<bool>(n+1 , false));
        for (int i = 0 ; i <= m ; i++){
            for (int j = 0 ; j <= n ; j++){
                if (i == 0 && j == 0){
                    dp[i][j] = true;
                    continue;
                }
                if (j == 0){
                    dp[i][j] = false;
                    continue;
                }
                if (p[j-1] != '*'){
                    if (i>0 && (s[i-1] == p[j-1] || p[j-1] == '?')){
                        dp[i][j] = dp[i][j] || dp[i-1][j-1];
                    }
                }
                else {
                    //选择不要 或者要*
                    dp[i][j] = dp[i][j] || dp[i][j-1];
                    if (i > 0){
                        dp[i][j] = dp[i][j] || dp[i-1][j];
                    }
                }
            }
        }
        return dp[m][n];
    }
};