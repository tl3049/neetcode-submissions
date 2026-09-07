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
        # while cur != stop:#过程中slow指针已经被改变所有slow.next要提前保存
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
        
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        #Reverse link from head to slow
        res = 0
        cur = slow
        while cur:
            res = max(res, cur.val + prev.val)
            cur = cur.next
            prev = prev.next
        return res

        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # #Reverse link from slow to end
        # prev = None
        # cur = slow
        # while cur:
        #     tmp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = tmp
        # res = 0
        # cur = head
        # while prev:
        #     res = max(res, cur.val + prev.val)
        #     cur = cur.next
        #     prev = prev.next
        # return res
        