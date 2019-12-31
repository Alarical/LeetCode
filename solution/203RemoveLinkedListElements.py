# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        last = dummy.next

        while last:
            if last.val == val:
                pre.next = last.next
                last = pre.next
            else:
                pre = pre.next
                last = last.next
        return dummy.next
                