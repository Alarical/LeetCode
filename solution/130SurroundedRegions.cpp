//
// Created by Alaric on 2019-10-16.
//
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        const int m = board.size();
        if (m==0) return;
        const int n = board[0].size();

        function<void(int,int)> dfs = [&](int x ,int y){
            if (x<0 || x>=m || y < 0 || y>=n || board[x][y] != 'O') return;
            board[x][y] = 'S';
            dfs(x-1,y);
            dfs(x+1,y);
            dfs(x,y-1);
            dfs(x,y+1);
        };
        for (int i = 0;i < m;++i){
            dfs(i,0);
            dfs(i,n-1);
        }
        for (int j = 0; j < n; ++j){
            dfs(0,j);
            dfs(m-1,j);
        }
        map<char,char> v{{'S','O'},{'X','X'},{'O','X'}};
        for(int i = 0 ; i < m ; ++i)
            for (int j = 0 ; j < n ; ++j)
                board[i][j] = v[board[i][j]];
    }
};
