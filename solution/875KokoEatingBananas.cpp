//
// Created by Alaric on 2019-10-10.
//
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int H) {
        int l = 1;
        int r = pow(10,9);
        int mid ;
        while (l+1<r){
            mid = l + (r-l)/2;
            if (canEating(piles , H , mid))
                r = mid;
            else
                l = mid;
        }
        if (canEating(piles , H , l))
            return l;
        else
            return r;
    }

private:
    bool canEating(vector<int>& piles , int H , int mid){
        int t = 0;
        for (const auto& p : piles){
            if (p%mid != 0)
                t++;
            t += p/mid;
        }
        return t<=H;
    }
};
