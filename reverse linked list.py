# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = None 
        
        temp1 = head 
        
        if temp1 is None:
            return head
        
        while temp1 is not None:
            
            new = temp1.next 
            
            temp1.next = temp
            
            temp = temp1 
            temp1 = new 
            
        return temp
