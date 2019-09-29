//
// Created by Alaric on 2019-09-30.
//
class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        vector<vector<int>> g(s.length());
        for (const auto& e : pairs) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }

        unordered_set<int> seen;
        vector<int> idx;
        string tmp;
        function<void(int)> dfs = [&](int cur) {
            if (seen.count(cur)) return;
            seen.insert(cur);
            idx.push_back(cur);
            tmp += s[cur];
            for (int nxt : g[cur]) dfs(nxt);
        };

        for (int i = 0; i < s.length(); ++i) {
            if (seen.count(i)) continue;
            idx.clear();
            tmp.clear();
            dfs(i);
            sort(begin(tmp), end(tmp));
            sort(begin(idx), end(idx));
            for (int k = 0; k < idx.size(); ++k)
                s[idx[k]] = tmp[k];
        }
        return s;
    }
};
