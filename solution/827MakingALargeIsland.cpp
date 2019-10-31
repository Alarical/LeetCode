//
// Created by Alaric on 2019-10-30.
//
class Solution {
public:
    int largestIsland(vector<vector<int>>& grid) {
        int m = grid.size() , n = grid[0].size();
        int res = 0;
        bool haszero = false;
        for (int i = 0 ; i < m ; ++i){
            for (int j = 0 ; j < n ; ++j){
                if (grid[i][j] == 1)
                    continue;
                haszero = true;
                grid[i][j] = 1;
                vector<vector<bool>> visited(m, vector<bool>(n));
                res = max(res , dfs(grid , i , j , visited));
                if (res == m*n) return res;
                grid[i][j] = 0 ;
            }
        }
        return haszero ? res:m*n;
    }

    int dfs(vector<vector<int>>& grid , int i , int j , vector<vector<bool>>& visited){
        int m = grid.size() , n = grid[0].size();
        if (i>=m || i < 0 || j>=n || j <0 || grid[i][j] == 0 || visited[i][j])
            return 0;
        visited[i][j] = true;
        return 1 + dfs(grid , i+1 , j ,visited) + dfs(grid , i-1 , j ,visited) + dfs(grid , i , j+1 ,visited) + dfs(grid , i , j-1 ,visited);
    }
};
