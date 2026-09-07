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
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        stop = slow
        print(stop.val)
        #Reverse link from head to slow
        prev = None
        cur = head
        while cur != slow:
            print(cur.val)
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        res = 0
        while cur:
            res = max(res, cur.val + prev.val)
            cur = cur.next
            prev = prev.next
        return res
        