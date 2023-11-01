# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        res = ListNode()
        current2 = res
        s = 0
        while current.next != None:
            current = current.next
            if current.val == 0:
                current2.val = s
                tmp = ListNode()
                if current.next != None:
                    current2.next = tmp
                    current2 = current2.next
                s = 0
            s+= current.val
        return res