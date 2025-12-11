# TC: O(1)
# SC: O(n)
# Doubly Linked List NODE
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Cache
        # Key -> number
        # Value -> Node
        self.cache = {}

        # Left - LRU
        # Right - MRU
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
            
    def insert(self, node):
        prevNode = self.right.prev
        nextNode = self.right

        prevNode.next = node
        nextNode.prev = node

        node.prev = prevNode
        node.next = nextNode

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Remove the node from the current position
            self.remove(node)

            # Insert  it to the most right positon (MRU)
            self.insert(node)

            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)