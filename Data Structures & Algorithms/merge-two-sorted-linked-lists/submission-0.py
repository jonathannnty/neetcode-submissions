# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # base cases handled
        if not list1:
            return list2
        if not list2:
            return list1
        
        # past this point we know list1 and list2 have a size of at least 1
        if list1.val < list2.val:
            first = list1
            list1 = list1.next
        else:
            first = list2
            list2 = list2.next
        
        head = first
        
        while list1 or list2:
            # case where we've exhausted either one of the lists
            if list1 and not list2:
                first.next = list1
                return head
            if list2 and not list1:
                first.next = list2
                return head

            # past this point we know there is valid list1 and list2
            # such that a value can be extracted
            # current list1 has a smaller value than list2
            if list1.val < list2.val:
                first.next = list1
                first = first.next
                list1 = list1.next
            # current list2 has a smaller value than list2
            else:
                first.next = list2
                first = first.next
                list2 = list2.next
        return head
