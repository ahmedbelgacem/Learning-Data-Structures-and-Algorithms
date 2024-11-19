# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        current = head
        values = []
        maximum = 0
        while current:
            values.append(current.val)
            current = current.next
            n += 1
        for i in range(n // 2):
            maximum = max(maximum, values[i] + values[n - 1 - i])
        return maximum
