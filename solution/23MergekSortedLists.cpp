//
// Created by Alaric on 2019-09-26.
//
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;

        auto comp = [](ListNode* a , ListNode* b) {return a->val > b->val;};
        priority_queue<ListNode* , vector<ListNode*>, decltype(comp)> q(comp);

        for(ListNode* list:lists )
            if (list) q.push(list);

        while(!q.empty()){
            tail->next = q.top();
            q.pop();
            tail = tail->next;
            if (tail->next) q.push(tail->next);
        }
        return dummy->next;
    }
};
