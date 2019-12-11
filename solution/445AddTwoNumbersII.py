# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        newhead = dummy
        stack1 = []
        stack2 = []
        ans = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        while stack1 or stack2:
            num1 , num2 = 0 , 0
            if len(stack1) > 0:
                num1 = stack1.pop()
            if len(stack2) > 0:
                num2 = stack2.pop()
            cur = num1 + num2 + carry
            carry = cur // 10
            cur = cur % 10
            #curNode = ListNode(cur)
            ans.append(cur)
        if carry:
            ans.append(1)
        #print (ans)
        for num in ans[::-1]:
            #print (num)
            dummy.next = ListNode(num)
            dummy = dummy.next
        return newhead.next