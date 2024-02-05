# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy 
        count = 0
        while curr.next:
            curr = curr.next
            count += 1
        
        curr = dummy
        for _ in range(count-n):
            curr= curr.next
        curr.next = curr.next.next

        return dummy.next

      