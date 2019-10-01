//
// Created by Alaric on 2019-10-02.
//
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size();
        int left = 0,right = n;
        int mid = 0;
        while(left + 1 <= right){
            mid = left + (right - left)/2;
            int count = 0;
            for (auto val:nums){
                if (val <= mid)
                    count++;
            }
            if (count<=mid)
                left = mid+1;
            else
                right = mid;
        }
        int count = 0;
        for (auto val:nums){
            if (val <= left)
                count++;
        }
        if(count <= left)
            return right;
        else
            return left;
    }
};
