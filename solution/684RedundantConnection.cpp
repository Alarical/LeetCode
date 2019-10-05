//
// Created by Alaric on 2019-10-05.
//
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        if (edges.empty()) return {};
        int n = edges.size();
        vector<int> p(n);
        iota(begin(p), end(p), 0); // p = {0, 1, 2, ... n - 1}

        function<int(int)> find = [&](int x){
            return p[x] == x ? x : p[x] = find(p[x]);
        };

        for (const auto& e :edges){
            int x1 = p[find(e[0]-1)];
            int x2 = p[find(e[1]-1)];
            if (x1 != x2)
                p[x2] = x1;
            else
                return e;
        }
        return {};
    }
};