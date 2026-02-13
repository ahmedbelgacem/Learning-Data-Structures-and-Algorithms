class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if not fast:
                break
        return slow