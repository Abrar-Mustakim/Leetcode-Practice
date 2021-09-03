# Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        first = head
        second = head

        while first != None and second != None and first.next != None:
            first = first.next.next
            second = second.next
            if first == second:
                return True

        return False


# Merge two sorted list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return l1
        elif l1 is None and l2 is not None:
            l1 = l2
            l2 = None
        temp = l1
        while temp.next is not None:
            temp = temp.next
        temp1 = l2
        if temp1 is not None:
            if temp1.next is not None:
                while temp1.next is not None:
                    temp.next = temp1
                    temp = temp.next
                    temp1 = temp1.next
            else:
                temp.next = temp1
        else:
            pass
        head = l1
        while head is not None:
            index_min = head
            j = head.next
            while j is not None:
                if index_min.val > j.val:
                    index_min = j
                j = j.next
            temp = head.val
            head.val = index_min.val
            index_min.val = temp
            head = head.next
        return l1
