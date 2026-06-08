class Node:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.capacity_so_far = 0
        self.queue = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def insert(self, node):
        last_node = self.right.prev
        last_node.next = node
        node.prev = last_node
        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.queue:
            self.remove(self.queue[key])
            self.insert(self.queue[key])
            return self.queue[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.queue:
           self.queue[key].val = value
           self.remove(self.queue[key])
           self.insert(self.queue[key])
        elif self.capacity_so_far < self.max_capacity:
            self.queue[key] = node
            self.insert(node)
            self.capacity_so_far += 1
        else:
            self.queue[key] = node
            self.queue.pop(self.left.next.key)
            self.remove(self.left.next)
            
            self.insert(node)
        print(self.queue)

        
        

