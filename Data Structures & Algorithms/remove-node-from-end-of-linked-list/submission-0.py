# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        count = 0
        node = dummy
        while node.next:
            node = node.next
            count += 1
        left_idx = count - n
        left = dummy
        for i in range(left_idx):
            left = left.next
        left_1 = left.next
        left_2 = left_1.next
        left.next = left_2
        return dummy.next