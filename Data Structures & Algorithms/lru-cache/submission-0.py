class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # map key to node
        
        # Dummy head and tail to avoid edge cases when removing/adding nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Remove node from the doubly linked list
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert node right before the right boundary (most recently used)
    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move to most recently used by removing and re-inserting
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            # Remove the least recently used node (node right after self.left)
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]