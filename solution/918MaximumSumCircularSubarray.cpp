//
// Created by Alaric on 2019-10-29.
//
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& A) {
        int mn = INT_MAX,mx = INT_MIN;
        int cur_max = 0,cur_min = 0;
        int sum = 0;
        for (auto num : A){
            sum += num;
            cur_max = max(num , cur_max + num);
            cur_min = min(num , cur_min + num);
            mx = max(mx , cur_max);
            mn = min(mn , cur_min);
        }
        if (sum - mn == 0)
            return mx;
        return max(mx , sum-mn);
    }
};
