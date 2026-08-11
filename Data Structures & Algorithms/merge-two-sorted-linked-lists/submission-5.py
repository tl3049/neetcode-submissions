# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        if not p1 and not p2: return None
        if not p1 and p2: return p2
        if p1 and not p2: return p1
        
        #double pointers
        dummy_node = ListNode(-1)
        if p1.val <= p2.val: 
            head = p1
            p1 = p1.next
        else: 
            head = p2
            p2 = p2.next
        dummy_node.next = head
        while p1 and p2:
            if p1.val < p2.val:
                head.next = p1
                p1 = p1.next
            else:
                head.next = p2
                p2 = p2.next
            head = head.next
        if p1 and not p2:
            head.next = p1
        if not p1 and p2:
            head.next = p2
        return dummy_node.next
           
            
            



