//
// Created by Alaric on 2019-10-18.
//
class Solution {
public:
    int rob(vector<int>& nums) {
        int pre = 0,cur = 0;
        int n = nums.size();
        if (n == 0)
            return 0;
        if (n==1)
            return nums[0];
        for (int i = 1 ; i <n ; ++i){
            int temp = cur;
            cur = max(pre + nums[i] , cur);
            pre = temp;
        }

        int ans = cur;
        pre = 0,cur = 0;
        for (int i = 0 ; i <n-1 ; ++i){
            int temp = cur;
            cur = max(pre + nums[i] , cur);
            pre = temp;
        }
        return max(cur,ans);
    }
};

