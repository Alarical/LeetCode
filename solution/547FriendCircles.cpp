//
// Created by Alaric on 2019-10-05.
//
//DFS
class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int n = M.size();
        vector<int> visited(n);
        int ans = 0;
        for (int i = 0 ; i < n ; ++i){
            if (visited[i] == 0){
                ++ans;
                dfs(M,visited,i);
            }
        }
        return ans;
    }

private:
    void dfs(vector<vector<int>>& M , vector<int>& visited , int curRow){
        visited[curRow] = 1;
        for (int j = 0 ; j < M.size(); ++j){
            if (M[curRow][j] == 1 && visited[j] == 0){
                visited[j] = 1;
                dfs(M , visited ,j);
            }
        }
        return;
    }
};

//Union-Find
class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int n = M.size();
        vector<int> p(n);
        iota(begin(p) , end(p) , 0);

        function<int(int)> find = [&](int x){
            return p[x] == x ? x : p[x] = find(p[x]);
        };

        for (int i = 0 ; i < n ; ++i){
            for (int j = i+1 ; j<n ; ++j ){
                if (M[i][j] == 1){
                    int rootx = p[find(i)];
                    int rooty = p[find(j)];
                    if(rootx != rooty)
                        p[rooty] = rootx;
                }
            }
        }
        int ans = 0;
        unordered_set<int> circles;
        for (int i = 0 ; i< n; ++i){
            circles.insert(find(i));
        }

        return circles.size();
    }
};
