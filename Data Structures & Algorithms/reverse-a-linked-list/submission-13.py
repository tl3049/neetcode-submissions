# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def reverse(h):
            if not h.next:
                return h, h
            else:
                nhead, ntail = reverse(h.next)
                ntail.next = h
                h.next = None
                return nhead, h
        res, tail = reverse(head)
        return res
        
        
        
        
        
        # if not head:
        #     return None
        # pre = None
        # cur = head
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     #move forward
        #     pre = cur
        #     cur = tmp
        # return pre
