# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next


        #reverse second
        prev = None
        slow.next = None#cut down the first squence
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        l1, l2 = head, prev
        # #merge two links
        while l1 and l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2










