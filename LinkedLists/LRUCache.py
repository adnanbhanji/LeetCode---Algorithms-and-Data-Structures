class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right = ListNode(0,0)
        self.left = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def _remove(self, node):
        _next = node.next
        _prev = node.prev
        node.prev.next = _next
        node.next.prev = _prev

    def _add_to_right(self, node):
        _prev = self.right.prev
        _next = self.right
        
        _prev.next = node
        node.prev = _prev
        
        node.next = _next
        _next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._add_to_right(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self._add_to_right(self.cache[key])

        if len(self.cache) > self.capacity:
            least_recently_used = self.left.next
            self._remove(least_recently_used)
            del self.cache[least_recently_used.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)