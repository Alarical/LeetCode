//
// Created by Alaric on 2019-10-10.
//
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (root == NULL)
            return ans;
        bool flag = true;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()){
            int n = q.size();
            vector<int> cur_level;
            for(int i = 0 ; i < n ; ++i){
                TreeNode* cur_node = q.front();
                q.pop();
                if (cur_node -> left != NULL)
                    q.push(cur_node->left);
                if (cur_node -> right != NULL)
                    q.push(cur_node->right);
                cur_level.push_back(cur_node->val);
            }
            if(!flag)
                reverse(cur_level.begin() , cur_level.end());
            flag = !flag;
            ans.push_back(cur_level);
        }
        return ans;
    }
};

