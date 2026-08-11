# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

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
            cur.next = t1 if t1 else t2
            return dummy.next

        def mergelists(st, end):
            if end - st + 1 <= 1:
                return lists[st]
            mid = (end + st) // 2
            p1 = mergelists(st, mid)
            p2 = mergelists(mid + 1, end)
            return merge(p1, p2)

        return mergelists(0, len(lists) - 1)