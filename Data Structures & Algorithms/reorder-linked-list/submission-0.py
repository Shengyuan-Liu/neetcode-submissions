# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        point = head
        data = []
        while point:
            data.append(point.val)
            point = point.next

        left, right = 0, len(data) - 1
        result = []
        while left <= right:
            result.append(data[left])
            if left < right:
                result.append(data[right])
            left += 1
            right -= 1
        dummy = node = ListNode(val=0, next=head)
        for num in result:
            node.next.val = num
            node = node.next
        head = dummy.next
        # print(data)
