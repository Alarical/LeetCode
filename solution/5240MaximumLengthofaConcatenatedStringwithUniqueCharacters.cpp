//
// Created by Alaric on 2019-10-27.
//
class Solution {
public:
    int ans = 0;
    int cnt[26];
    void dfs(vector<string>& arr , int i ,int n ,int len){
        if (len > ans) ans = len;
        if (i >= n ) return;
        //not
        dfs(arr , i+1 , n ,len);
        //choose
        for (auto c: arr[i])
            ++cnt[c-'a'];
        bool flag = true;
        for (int i = 0; i<26 && flag ; ++i) if (cnt[i] > 1) flag = false;
        if (flag)
            dfs(arr , i+1 , n , len+arr[i].length());
        for (auto c:arr[i])
            --cnt[c-'a'];
    }

    int maxLength(vector<string>& arr) {
        int n = arr.size();
        ans = 0;
        memset(cnt , 0 ,sizeof(cnt));
        dfs(arr , 0 , n , 0);
        return ans;
    }
};
