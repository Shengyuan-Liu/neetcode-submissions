# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        nex = 0
        while l1 or l2:
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()
            s = l1.val + l2.val + nex
            digit = s % 10
            nex = s // 10
            node.next = ListNode(val=digit, next=None)
            node = node.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            node.next = l1
        if l2:
            node.next = l2
        if not l1 and not l2 and nex > 0:
            node.next = ListNode(nex)
        return dummy.next