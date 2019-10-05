//
// Created by Alaric on 2019-10-05.
//
//top-down
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
    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* slow = head;
        ListNode* fast = head->next;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* mid = slow->next;
        slow->next = nullptr;
        return merge(sortList(head) , sortList(mid));
    }
private:
    ListNode* merge(ListNode* l1 , ListNode* l2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        while (l1 && l2){
            if (l1->val > l2->val) swap(l1,l2);
            tail->next = l1;
            l1 = l1->next;
            tail = tail->next;
        }
        if (l1) tail->next = l1;
        if (l2) tail->next = l2;
        return dummy.next;
    }
};
