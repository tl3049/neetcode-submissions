# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        second = head
        for i in range(n):
            second = second.next
        dummy = ListNode(0, head)
        l1, l2 = dummy, second
        while l2:
            l1 = l1.next
            l2 = l2.next
        l1.next = l1.next.next
        return dummy.next