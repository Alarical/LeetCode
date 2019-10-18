//
// Created by Alaric on 2019-10-18.
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
    int rob(TreeNode* root) {
        vector<int> res;
        res = helper(root);
        return max(res[0] , res[1]);
    }

    vector<int> helper(TreeNode* r){
        vector<int> left ;
        vector<int> right ;
        vector<int> res = {0,0};
        if (!r)
            return vector<int>{0,0};
        left = helper(r->left);
        right = helper(r->right);
        res[0] = max(left[0] , left[1]) + max(right[0] , right[1]);
        res[1] = r->val + left[0] + right[0];
        return res;
    }
};

