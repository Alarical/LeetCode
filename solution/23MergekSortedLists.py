# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(0)
        tail = dummy
        queue = []
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(queue , (lists[i].val , i))
                lists[i] = lists[i].next
        while queue:
            val,index = heapq.heappop(queue)
            tail.next = ListNode(val)
            tail = tail.next
            if lists[index]:
                heapq.heappush(queue , (lists[index].val , index))
                lists[index] = lists[index].next
        return dummy.next
