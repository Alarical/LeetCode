//
// Created by Alaric on 2019-10-08.
//
class Solution {
    const int MOD =1000000007;
    long long dp[20001][5];
public:
    int countVowelPermutation(int n) {
        int i,j;
        for (i = 0; i <5 ; ++i)
            dp[1][i] = 1;
        for (i = 1 ; i < n; ++i){
            dp[i+1][0] = (dp[i][1] + dp[i][2] + dp[i][4])%MOD;
            dp[i+1][1] = (dp[i][0] + dp[i][2])%MOD;
            dp[i+1][2] = (dp[i][1] + dp[i][3])%MOD;
            dp[i+1][3] = (dp[i][2])%MOD;
            dp[i+1][4] = (dp[i][2] + dp[i][3])%MOD;
        }
        return (dp[n][0] + dp[n][1] + dp[n][2] + dp[n][3] + dp[n][4])%MOD;
    }
};
