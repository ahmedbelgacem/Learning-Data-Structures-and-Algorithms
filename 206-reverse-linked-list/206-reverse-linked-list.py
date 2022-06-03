# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        else:
            current=head
            tmp2=current
            while current.next.next:
                tmp=current.next.next
                current.next.next=tmp2
                tmp2=current.next
                current.next=tmp
            tmp=current.next
            tmp.next=tmp2
            current.next=None
            return tmp