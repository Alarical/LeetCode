//
// Created by Alaric on 2019-09-20.
//

class Solution {
public:
    int mySqrt(int x) {
        if(x <= 1)
            return x;
        long long left = 0;
        long long right = x/2;
        while (left <= right) {
            long long mid = left + (right-left)/2;
            if (mid * mid > x){
                right = mid-1;
            }
            else{
                left = mid+1;
            }
        }
        return right;
    }
};
