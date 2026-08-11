# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(t1, t2):
            dummy = ListNode()
            cur = dummy
            while t1 and t2:
                if t1.val <= t2.val:
                    cur.next = t1
                    t1 = t1.next
                else:
                    cur.next = t2
                    t2 = t2.next
                cur = cur.next
            if t1:
                cur.next = t1
            if t2:
                cur.next = t2
            return dummy.next

        def mergelists(lists, st, end):
            if not lists:
                return None
            if end - st + 1 <= 1:
                return lists[st]
            mid = (end + st) // 2
            p1 = mergelists(lists, st, mid)
            p2 = mergelists(lists, mid + 1, end)
            p = merge(p1, p2)
            return p

        res = mergelists(lists, 0, len(lists) - 1)
        return res