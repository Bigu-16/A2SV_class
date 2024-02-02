# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        curr = head
        new_head = None

        for _ in range(left - 1):
            prev = curr
            curr = curr.next

        tail = curr
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = new_head
            new_head = curr
            curr = nxt

        if prev:
            prev.next = new_head
        else:
            head = new_head

        tail.next = curr

        return head