# Node for doubly linked list
# DLL will keep track of which node is MOST or LEAST used
class Node:
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        # Nodes added closest to left are least used
        # Nodes added closest to right are most used
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        pre_node, post_node = node.prev, node.next
        pre_node.next, post_node.prev = post_node, pre_node

    def add_right(self, new_node):
        self.right.prev.next = new_node
        new_node.prev = self.right.prev
        self.right.prev = new_node
        new_node.next = self.right

    def get(self, key: int) -> int:
        # Cache hit: Found in cache
        if key in self.map:
            # Replace current node and put it to right
            self.remove(self.map[key])
            self.add_right(self.map[key])
            return self.map[key].val
        else:  # Cache miss: Not found... return -1
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # If key is already found in map, find that key and change its value
            self.remove(self.map[key])
            self.add_right(self.map[key])
            self.map[key].val = value
        else:
            # If key is not found in map: Create a new key, value pair for map, then create new node for DLL
            if len(self.map) >= self.capacity:
                # If the current capacity is full, then evict the least used item from cache by deleting leftmost
                # node off of DLL, and deleting the key value pair from map
                del self.map[self.left.next.key]
                self.remove(self.left.next)

            # Adding new key value pair onto map, and new node onto right of DLL
            self.map[key] = Node(val=value, key=key)
            self.add_right(self.map[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
