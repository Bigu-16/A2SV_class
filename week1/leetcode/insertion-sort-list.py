# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        dummy.next = head
        curr = head.next
        tail = head

        while curr:
            if curr.val >= tail.val:
                tail = curr
                curr = curr.next
            else:
                tail.next = curr.next
                prev = dummy
                while prev.next.val < curr.val:
                    prev = prev.next
                curr.next = prev.next
                prev.next = curr
                curr = tail.next

        return dummy.next