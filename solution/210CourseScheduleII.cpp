//
// Created by Alaric on 2019-10-10.
//
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        for (const auto& e: prerequisites)
            graph[e[1]].push_back(e[0]);

        // states: 0 = unkonwn, 1 == visiting, 2 = visited
        vector<int> visited(numCourses , 0);
        vector<int> ans;

        for (int i = 0 ; i < numCourses ; ++i)
            if (dfs(i, graph, visited , ans))
                return {};
        reverse(ans.begin() , ans.end());
        return ans;

    }
private:
    bool dfs(int cur , vector<vector<int>>& graph , vector<int>& v , vector<int>& ans){
        //有没有环
        if (v[cur] == 1) return true;
        if (v[cur] == 2) return false;
        v[cur] = 1;
        for (auto e: graph[cur])
            if (dfs(e , graph , v, ans))
                return true;
        v[cur] = 2;
        ans.push_back(cur);
        return false;
    }
};



