# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            temp = curr
            while temp.next:
                if temp.val > temp.next.val:
                    temp.val, temp.next.val = temp.next.val,temp.val
                temp = temp.next
            curr = nxt
        
        return prev
        