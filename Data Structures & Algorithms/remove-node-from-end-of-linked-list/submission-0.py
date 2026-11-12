# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # slow=head
        # prev=None
        # for _ in range(n):
        #     if slow is not None:
        #         slow=slow.next
        #         prev=slow
        #     else:
        #         break
        # second=slow.next
        # slow.next=None
        # prev=slow
        # while second:
        #     prev=second
        #     second=second.next
        dummy=ListNode(0,head)
        left=dummy
        right=head

        #move right pointer n steps ahead
        for _ in range(n):
            right=right.next
        
        while right:
            left=left.next
            right=right.next
        
        left.next=left.next.next

        return dummy.next
        
         

        
                                                                          
        
        