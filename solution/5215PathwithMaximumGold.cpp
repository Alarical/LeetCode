//
// Created by Alaric on 2019-10-07.
//
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
class Solution {
public:
    int ans;
    vector<vector<int>> g, visited;
    int m,n;

    void dfs(int x,int y,int cur){
        ans = max(ans,cur);
        visited[x][y] = 1;
        for (int d = 0; d < 4 ; ++d){
            int tx = x+dx[d];
            int ty = y+dy[d];
            if (tx >= 0 && tx < m && ty>=0 && ty<n && !visited[tx][ty] && g[tx][ty])
                dfs(tx , ty , cur+g[tx][ty]);
        }
        visited[x][y] = 0;
    }

    int getMaximumGold(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        g = grid;
        ans = 0;
        visited = vector<vector<int>>(m, vector<int>(n));
        for (int i = 0 ; i < m; ++i){
            for(int j = 0; j< n; ++j){
                if (grid[i][j])
                    dfs(i,j,grid[i][j]);
            }
        }
        return ans;
    }
};
