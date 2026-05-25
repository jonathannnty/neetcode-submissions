# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # input: the head of a linkedlist
        # we need to account for a possible edge case where head is null
        # output: cycle? --> True, otherwise false

        if not head or not head.next:
            return False

        # slow and fast pointer
        slow, fast = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            if slow == fast:
                return True
            slow = slow.next
        return False