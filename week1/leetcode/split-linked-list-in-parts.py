# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        h = head
        curr = head

        count = 0
        while curr:
            curr = curr.next
            count += 1
        
        extra = count % k
        ele = count // k

        curr = h
        ans = []
        for i in range(k):
            new = ListNode()
            new_h = new

            for i in range(ele):
                new.next = ListNode(curr.val)
                curr = curr.next
                new = new.next
                    
            if extra:
                new.next = ListNode(curr.val)
                curr = curr.next
                new = new.next
                extra -= 1
            ans.append(new_h.next)

        return ans
            



