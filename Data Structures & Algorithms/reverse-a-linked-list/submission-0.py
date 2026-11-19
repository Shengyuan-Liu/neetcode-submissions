# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point = head
        prev = None
        while point:
            next_node = point.next
            point.next = prev
            prev = point
            point = next_node
        return prev