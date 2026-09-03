# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #reverse a list
        def reverse(p):
            pre, cur = None, p
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        if not head:
            return False
        p1, p2 = head, head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        p3 = reverse(p1.next)
        p1 = head
        while p3:
            if p1.val != p3.val:
                return False
            p1 = p1.next
            p3 = p3.next
        return True

