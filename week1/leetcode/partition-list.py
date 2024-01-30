# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head  
        
        less_dummy = ListNode()   
        less_tail = less_dummy         
        
        greater_dummy = ListNode()
        greater_tail = greater_dummy 
       
        while curr:
            if curr.val < x:
                less_tail.next = ListNode(curr.val)
                less_tail = less_tail.next 
            else:
                greater_tail.next = ListNode(curr.val)
                greater_tail = greater_tail.next  
            curr = curr.next  
        
        less_tail.next = greater_dummy.next
        
        return less_dummy.next