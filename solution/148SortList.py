# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 会超时
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def quicksort(head,end):
            if head == end or head.next == end:
                return
            p = head.next
            pivot = head.val
            mid = head
            while p != end:
                if p.val <  pivot:
                    mid = mid.next
                    mid.val , p.val = p.val,mid.val
                p = p.next
            head.val = mid.val
            mid.val = pivot
            quicksort(head,mid)
            quicksort(mid.next,end)
            
        quicksort(head,None)
        return head