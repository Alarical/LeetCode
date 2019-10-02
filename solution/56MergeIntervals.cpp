//
// Created by Alaric on 2019-10-03.
//
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        vector<vector<int>> ans;
        sort(intervals.begin() , intervals.end());
        for(const auto& interval:intervals){
            if (ans.empty() || interval[0] > ans.back()[1])
                ans.push_back(interval);
            else{
                ans.back()[1] = max(ans.back()[1] , interval[1]);
            }
        }
        return ans;
    }
};
