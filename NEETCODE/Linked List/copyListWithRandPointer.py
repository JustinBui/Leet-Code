class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hash = dict()  # Key: Nodes from Original List, Value: Newly Created Nodes

        # As we create copies of nodes based on the original list, we can map each new copy
        # to the original nodes in the hash map for reference
        it = head
        while it:
            new_node = Node(x=it.val)
            hash[it] = new_node
            it = it.next

        # For every new node created, we now fill in each of their next and random pointers
        # to point at which new node, as corresponding to the original list
        for h in hash:
            if h.next:
                hash[h].next = hash[h.next]
            if h.random:
                hash[h].random = hash[h.random]
            # NOTE: We need to check if h.next and h.random are not null because some can point to null ptrs

        return hash[head]
