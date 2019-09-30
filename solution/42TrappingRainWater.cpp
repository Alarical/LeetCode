//
// Created by Alaric on 2019-09-30.
//
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int* left = new int[n];
        int* right = new int[n];
        for (int i = 1 ; i < n ; ++i){
            left[i] = max(left[i-1],height[i-1]);
        }
        for (int i = n-2 ; i >=0 ; --i){
            right[i] = max(right[i+1],height[i+1]);
        }
        int res = 0;
        for (int i = 0 ; i < n ; i++){
            int temp = min(left[i] , right[i]);
            if (height[i] <= temp)
                res += temp-height[i];
        }
        return res;
    }
};

//two pointers
//class Solution {
//public:
//    int trap(vector<int>& height) {
//        int left_max = 0 , right_max = 0;
//        int ans = 0;
//        int left = 0,right = height.size()-1;
//        while(left<right){
//            if (height[left] <= height[right]){
//                height[left] >= left_max ? (left_max = height[left]) : ans+=left_max - height[left];
//                left++;
//            }
//            else{
//                height[right] >= right_max ? (right_max = height[right]) : ans+= right_max-height[right];
//                right--;
//            }
//        }
//        return ans;
//    }
//};
