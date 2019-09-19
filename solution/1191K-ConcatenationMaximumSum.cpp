//
// Created by Alaric on 2019-09-19.
//

class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        constexpr int MOD = 1e9+7;
        auto maxSum = [&arr](int r){
            long sum = 0;
            long ans = 0;
            for(int i = 0 ; i < r ; ++i){
                for(long a: arr){
                    sum = max(0L , sum+=a);
                    ans = max(ans , sum);
                }
            }
            return ans;
        };
        if (k < 3)
            return maxSum(k) % MOD;
        long sum = accumulate(begin(arr) , end(arr) , 0L);
        long ans1 = maxSum(1);
        long ans2 = maxSum(2);
        return max({ans1 , ans2 , ans2 + sum*(k-2)}) % MOD;
    }
};