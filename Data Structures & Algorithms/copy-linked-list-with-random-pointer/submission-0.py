class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Edge case: empty list
        if not head:
            return None
            
        # Hash map to store mapping from original node to its deep copy
        old_to_new = {None: None}
        
        # First pass: Copy all the nodes' values without pointers
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Second pass: Assign next and random pointers
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next
            
        return old_to_new[head]
        