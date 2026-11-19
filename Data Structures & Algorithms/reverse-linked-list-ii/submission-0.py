# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # 1. Reach node at position `left`
        left_prev, curr = dummy, head
        for _ in range(left - 1):
            left_prev, curr = curr, curr.next
            
        # 2. Reverse from `left` to `right`
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
            
        # 3. Stitch pointers back together
        left_prev.next.next = curr  # old `left` node points to node after `right`
        left_prev.next = prev       # node before `left` points to new `left` (which was `right`)
        
        return dummy.next