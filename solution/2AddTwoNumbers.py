# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #465    243
        #342    564
        #       708
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            val = sum % 10
            cur.next = ListNode(val)
            cur = cur.next
        if carry > 0 :
            cur.next = ListNode(1)
        return dummy.next


