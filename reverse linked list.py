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
    
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        
        if head is None:
            return head 
        
        
        
        while head is not None:
            if head.val == val:
                head = head.next 
                
                
                
            else:
                break 
                
        temp = head
                
        while temp is not None and temp.next is not None:
            
            if temp.next.val == val:
                new = temp.next.next 
                
                temp.next = new
                
            else:
                temp = temp.next
            
            
        
        return head
        
        
             
