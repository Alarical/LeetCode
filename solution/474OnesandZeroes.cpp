//
// Created by Alaric on 2019-10-16.
//
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int t = strs.size();
        int count0,count1;
        vector<vector<vector<int>>> dp(t + 1, vector<vector<int>>
                                                               (m + 1 , vector<int>(n + 1 , 0)));
        for (int i = 0 ; i <= m ; ++i)
            for(int j = 0 ; j <= n ;++j)
                dp[0][i][j] = 0;

        for(int i = 1 ; i <= t ; ++i ){
            count0 = count1 = 0;
            for (const auto& ch : strs[i-1]){
                if(ch == '0') count0++;
                else count1++;
            }

            for(int j = 0 ; j <=m ; ++j )
                for(int k = 0 ; k<=n ; ++k )
                {
                    dp[i][j][k] = dp[i-1][j][k];
                    if (j >= count0 && k >= count1)
                        dp[i][j][k] = max(dp[i][j][k] , dp[i-1][j-count0][k-count1]+1);
                }
        }
        return dp[t][m][n];

    }
};
