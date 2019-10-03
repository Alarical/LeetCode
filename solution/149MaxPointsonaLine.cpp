//
// Created by Alaric on 2019-10-04.
//
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int n = points.size();
        int ans = 0;
        for(int i = 0 ; i < n ; ++i){
            map<pair<int,int> , int> count;
            auto p1 = points[i];
            int samp_points = 1;
            int max_points = 0;
            for(int j = i+1; j < n;++j){
                auto p2 = points[j];
                if (p1[0] == p2[0] && p1[1] == p2[1])
                    ++samp_points;
                else
                    max_points = max(max_points,++count[getslope(p1,p2)]);
            }
            cout << max_points <<" "<< samp_points << " "<< i << " ";
            ans = max(ans , max_points+samp_points);
        }
        return ans;
    }

private:
    pair<int,int> getslope(vector<int>& p1 , vector<int>& p2){
        const int dx = p2[0] - p1[0];
        const int dy = p2[1] - p1[1];
        //vertical
        if (dx == 0) return {p1[0] , 0};
        //horizontal
        if (dy == 0) return {0 , p1[1]};
        const int k = gcd(dx,dy);
        return {dy/k,dx/k};
    }
    int gcd(int m , int n){
        return n == 0? m :gcd(n,m % n);
    }
};s
