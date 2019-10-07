//
// Created by Alaric on 2019-10-06.
//
class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        map<int,int> dp;
        dp.clear();
        int ans = 0;
        for (const auto num:arr){
            int cur_len = max(dp[num] , dp[num-difference]+1);
            ans = max(ans , cur_len);
            dp[num] = cur_len;
        }
        return ans;
    }
};
