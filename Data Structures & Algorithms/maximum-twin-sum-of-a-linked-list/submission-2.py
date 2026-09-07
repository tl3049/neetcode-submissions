# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # dummy = ListNode(-1)
        # slow, fast = dummy, dummy
        # dummy.next = head
        # while fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        
        # stop = slow.next
        # #Reverse link from head to slow
        # prev = dummy
        # cur = head
        # while cur != stop:
        #     tmp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = tmp
        
        # res = 0
        # while cur:
        #     res = max(res, cur.val + prev.val)
        #     cur = cur.next
        #     prev = prev.next
        # return res
        slow = head
        fast = head

        # Find the beginning of the second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        cur = slow

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # Compare first half and reversed second half
        res = 0
        left = head
        right = prev

        while right:
            res = max(res, left.val + right.val)
            left = left.next
            right = right.next

        return res
        