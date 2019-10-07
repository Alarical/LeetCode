//
// Created by Alaric on 2019-10-06.
//
class Solution {
public:
    int minCostToMoveChips(vector<int>& chips) {
        int count[2] = {0,0};
        for (auto c:chips) ++count[c&1];
        return min(count[0] , count[1]);
    }
};
